#!/usr/bin/env python3
"""F-aggregate: merge InterProScan / eggNOG-mapper / DIAMOND (Swiss-Prot, TrEMBL) /
KofamScan outputs into one gene-level table (one row per protein = one gene).

Name rule:   Swiss-Prot hit passing DIAMOND filters -> its name;
             else "similar to <X>" with X from InterPro -> eggNOG -> TrEMBL (passing);
             else "uncharacterized protein".
KEGG KO:     final KO is kofam_ko only (KofamScan rows marked '*' or score >= threshold).
GO:          union of InterProScan + eggNOG GO, deduplicated and sorted; evidence code IEA.
Columns:     exactly pipeline/schema/merged_function_table.tsv (checked when that file exists).
Stdlib only.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_SCHEMA = HERE / "schema" / "merged_function_table.tsv"
DEFAULT_THRESHOLDS = HERE.parent / "config" / "function_qc_thresholds.tsv"

COLUMNS = [
    "gene_id",
    "ips_domains", "ips_domain_desc", "ips_ipr", "ips_go",
    "eggnog_og", "eggnog_name", "eggnog_description", "eggnog_go", "eggnog_ko",
    "diamond_db", "diamond_hit", "diamond_name", "diamond_evalue",
    "diamond_pident", "diamond_qcov", "diamond_scov",
    "kofam_ko",
    "final_name", "final_name_source",
    "go_terms", "go_evidence",
    "db_versions",
]

# Fallback DIAMOND filters if the thresholds file is absent (same values as
# config/function_qc_thresholds.tsv param_* keys).
FALLBACK_PARAMS = {
    "param_max_evalue": 1e-5,
    "param_min_pident": 30.0,
    "param_min_qcov": 50.0,
    "param_min_scov": 50.0,
}

# Repo default DIAMOND outfmt 6 (pipeline/F1_diamond.sh); qlen/slen optional extras.
DEFAULT_DIAMOND_COLS = ("qseqid sseqid pident length mismatch gapopen qstart qend "
                        "sstart send evalue bitscore stitle qlen slen").split()

GO_EVIDENCE = "IEA"
UNCHARACTERIZED = "uncharacterized protein"
UNINFORMATIVE_RE = re.compile(
    r"^\s*(-|uncharacteri[sz]ed protein.*|hypothetical protein.*|predicted protein.*|"
    r"unknown( protein)?|protein of unknown function.*)?\s*$", re.I)
DB_VER_RE = re.compile(r"^[A-Za-z0-9_.-]+=[^@;=]+@\d{4}-\d{2}-\d{2}$")
GO_RE = re.compile(r"GO:\d{7}")


# ---------------------------------------------------------------- helpers
def empty(v: str | None) -> bool:
    return v is None or v.strip() in ("", "-")


def join(items) -> str:
    return ";".join(items)


def fmt_num(x: float | None, nd: int = 1) -> str:
    return "" if x is None else f"{x:.{nd}f}"


def fasta_lengths(path: Path) -> tuple[list[str], dict[str, int]]:
    ids: list[str] = []
    lens: dict[str, int] = {}
    cur = None
    with open(path) as f:
        for line in f:
            if line.startswith(">"):
                cur = line[1:].split()[0]
                ids.append(cur)
                lens.setdefault(cur, 0)
            elif cur is not None:
                lens[cur] += len(line.strip().rstrip("*"))
    return ids, lens


def load_params(path: Path | None) -> dict[str, float]:
    params = dict(FALLBACK_PARAMS)
    if path is not None and path.is_file():
        with open(path, newline="") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                if r.get("direction") == "param" and r.get("key") in params:
                    params[r["key"]] = float(r["value"])
    else:
        print(f"[aggregate] thresholds file not found ({path}); using built-in "
              f"DIAMOND filters {params}", file=sys.stderr)
    return params


def check_schema(path: Path) -> None:
    if not path.is_file():
        return
    with open(path, newline="") as f:
        cols = [r["column"] for r in csv.DictReader(f, delimiter="\t")]
    if cols != COLUMNS:
        raise SystemExit(f"[ERR] output columns differ from schema {path}:\n"
                         f"  schema: {cols}\n  script: {COLUMNS}")


def parse_db_versions(entries: list[str], files: list[str]) -> list[str]:
    out: dict[str, str] = {}
    raw: list[str] = []          # file entries first, so --db-version wins on the same tool
    for p in files:
        with open(p, newline="") as f:
            for r in csv.reader(f, delimiter="\t"):
                if not r or r[0].startswith("#") or r[0] == "tool":
                    continue
                if len(r) < 3:
                    raise SystemExit(f"[ERR] {p}: need tool<TAB>version<TAB>YYYY-MM-DD, got {r}")
                raw.append(f"{r[0].strip()}={r[1].strip()}@{r[2].strip()}")
    raw += entries
    for e in raw:
        e = e.strip()
        if not DB_VER_RE.match(e):
            raise SystemExit(f"[ERR] --db-version must look like tool=version@YYYY-MM-DD, got {e!r}")
        out[e.split("=", 1)[0]] = e
    return list(out.values())


# ---------------------------------------------------------------- parsers
def parse_interproscan(path: Path) -> dict[str, dict]:
    """InterProScan TSV (-f tsv): 0 protein, 3 analysis, 4 sig_acc, 5 sig_desc,
    8 evalue, 9 status, 11 IPR acc, 12 IPR desc, 13 GO (optional, may carry '(InterPro)')."""
    out: dict[str, dict] = {}
    with open(path) as f:
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue
            c = line.rstrip("\n").split("\t")
            if len(c) < 11:
                continue
            if len(c) > 9 and c[9] not in ("T", ""):
                continue
            g = out.setdefault(c[0], {"domains": {}, "ipr": {}, "go": set()})
            dom = f"{c[3]}:{c[4]}"
            g["domains"].setdefault(dom, c[5] if not empty(c[5]) else "")
            try:
                ev = float(c[8])
            except ValueError:
                ev = float("inf")
            if len(c) > 11 and c[11].startswith("IPR"):
                desc = c[12] if len(c) > 12 and not empty(c[12]) else ""
                prev = g["ipr"].get(c[11])
                if prev is None or ev < prev[1]:
                    g["ipr"][c[11]] = (desc, ev)
            if len(c) > 13:
                g["go"].update(GO_RE.findall(c[13]))
    return out


def parse_emapper(path: Path) -> dict[str, dict]:
    """eggNOG-mapper v2 *.emapper.annotations (header line '#query ...')."""
    out: dict[str, dict] = {}
    header = None
    with open(path) as f:
        for line in f:
            if line.startswith("##") or not line.strip():
                continue
            if line.startswith("#"):
                header = line[1:].rstrip("\n").split("\t")
                continue
            if header is None:
                continue
            r = dict(zip(header, line.rstrip("\n").split("\t")))
            q = r.get("query") or r.get("query_name")
            if not q:
                continue
            og = _pick_og(r.get("eggNOG_OGs", ""), r.get("max_annot_lvl", ""))
            gos = set(GO_RE.findall(r.get("GOs", "") or ""))
            kos = sorted({k.strip().removeprefix("ko:") for k in (r.get("KEGG_ko") or "").split(",")
                          if not empty(k)})
            out[q] = {
                "og": og,
                "name": "" if empty(r.get("Preferred_name")) else r["Preferred_name"].strip(),
                "desc": "" if empty(r.get("Description")) else r["Description"].strip(),
                "go": gos,
                "ko": kos,
            }
    return out


def _pick_og(ogs: str, max_lvl: str) -> str:
    """Orthologous group at the annotation level emapper used (orthology, not seed best-hit)."""
    if empty(ogs):
        return ""
    parts = [p.strip() for p in ogs.split(",") if p.strip()]
    lvl = max_lvl.split("|")[0].strip() if not empty(max_lvl) else ""
    if lvl:
        for p in parts:
            if p.split("@", 1)[-1].split("|")[0] == lvl:
                return p
    return parts[-1]


def parse_uniprot_title(stitle: str, sseqid: str) -> str:
    """UniProt FASTA header: '<id> <name> OS=... OX=... GN=... PE=... SV=...' -> name."""
    t = stitle.strip()
    if t.split(" ", 1)[0] == sseqid or "|" in t.split(" ", 1)[0]:
        t = t.split(" ", 1)[1] if " " in t else ""
    return re.split(r"\s(?:OS|OX|GN|PE|SV)=", t, maxsplit=1)[0].strip()


def parse_diamond(path: Path, cols: list[str], qlens: dict[str, int], db: str,
                  params: dict[str, float]) -> dict[str, dict]:
    """Best hit per query: best passing hit (bitscore), else best failing hit (kept for QC)."""
    best: dict[str, dict] = {}
    warned = False
    with open(path) as f:
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue
            c = line.rstrip("\n").split("\t")
            r = dict(zip(cols, c))
            try:
                q, s = r["qseqid"], r["sseqid"]
                pident, evalue, bits = float(r["pident"]), float(r["evalue"]), float(r["bitscore"])
                qs, qe, ss, se = (int(r[k]) for k in ("qstart", "qend", "sstart", "send"))
            except (KeyError, ValueError):
                continue
            qlen = _int(r.get("qlen")) or qlens.get(q)
            slen = _int(r.get("slen"))
            qcov = 100.0 * (abs(qe - qs) + 1) / qlen if qlen else None
            scov = 100.0 * (abs(se - ss) + 1) / slen if slen else None
            if scov is None and not warned:
                print(f"[aggregate] {path}: no slen column -> subject coverage unknown, "
                      f"hits fail the scov filter (add 'qlen slen' to --outfmt 6)", file=sys.stderr)
                warned = True
            passed = (evalue <= params["param_max_evalue"] and pident >= params["param_min_pident"]
                      and qcov is not None and qcov >= params["param_min_qcov"]
                      and scov is not None and scov >= params["param_min_scov"])
            hit = {
                "db": db, "hit": s, "name": parse_uniprot_title(r.get("stitle", ""), s),
                "evalue": evalue, "pident": pident, "qcov": qcov, "scov": scov,
                "bits": bits, "passed": passed,
            }
            cur = best.get(q)
            if cur is None or (hit["passed"], hit["bits"], -hit["evalue"]) > \
                    (cur["passed"], cur["bits"], -cur["evalue"]):
                best[q] = hit
    return best


def _int(v: str | None) -> int | None:
    try:
        return int(v) if v not in (None, "") else None
    except ValueError:
        return None


def parse_kofam(path: Path) -> dict[str, list[tuple[str, float]]]:
    """KofamScan output: detail (default), detail-tsv, or mapper.
    Keep a row if it is marked '*' or score >= threshold (numeric threshold only)."""
    out: dict[str, dict[str, float]] = {}
    with open(path) as f:
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue
            s = line.rstrip("\n")
            if "\t" in s:
                c = s.split("\t")
                if len(c) <= 2:                     # mapper: gene<TAB>KO (only significant)
                    if len(c) == 2 and re.fullmatch(r"K\d{5}", c[1].strip()):
                        out.setdefault(c[0].strip(), {})[c[1].strip()] = float("inf")
                    continue
                star, gene, ko, thr, score = (x.strip() for x in c[:5])
            else:                                   # detail: whitespace-aligned
                star = "*" if s.startswith("*") else ""
                c = s.lstrip("*").split(None, 5)
                if len(c) < 4:
                    continue
                gene, ko, thr, score = c[:4]
            if not re.fullmatch(r"K\d{5}", ko):
                continue
            try:
                sc = float(score)
            except ValueError:
                continue
            try:
                t = float(thr)
            except ValueError:
                t = None
            if star == "*" or (t is not None and sc >= t):
                d = out.setdefault(gene, {})
                d[ko] = max(sc, d.get(ko, float("-inf")))
    return {g: sorted(d.items(), key=lambda kv: (-kv[1], kv[0])) for g, d in out.items()}


# ---------------------------------------------------------------- merge
def informative(name: str) -> bool:
    return not UNINFORMATIVE_RE.match(name or "")


def ips_best_desc(ips: dict) -> str:
    ranked = sorted(((ev, acc, d) for acc, (d, ev) in ips["ipr"].items() if informative(d)))
    if ranked:
        return ranked[0][2]
    for d in ips["domains"].values():
        if informative(d):
            return d
    return ""


def build_row(gid: str, ips: dict | None, em: dict | None, sp: dict | None,
              tr: dict | None, ko: list | None, db_versions: str) -> dict:
    row = {c: "" for c in COLUMNS}
    row["gene_id"] = gid
    go_all: set[str] = set()
    if ips:
        doms = sorted(ips["domains"])
        row["ips_domains"] = join(doms)
        row["ips_domain_desc"] = join(ips["domains"][d] or "-" for d in doms)
        row["ips_ipr"] = join(sorted(ips["ipr"]))
        row["ips_go"] = join(sorted(ips["go"]))
        go_all |= ips["go"]
    if em:
        row["eggnog_og"] = em["og"]
        row["eggnog_name"] = em["name"]
        row["eggnog_description"] = em["desc"]
        row["eggnog_go"] = join(sorted(em["go"]))
        row["eggnog_ko"] = join(em["ko"])      # reported only; final KO = kofam_ko
        go_all |= em["go"]
    # DIAMOND: Swiss-Prot passing > TrEMBL passing > best failing (SP first) for QC
    hit = None
    for cand in (sp, tr):
        if cand and cand["passed"]:
            hit = cand
            break
    if hit is None:
        hit = sp or tr
    if hit:
        row.update({
            "diamond_db": hit["db"], "diamond_hit": hit["hit"], "diamond_name": hit["name"],
            "diamond_evalue": f"{hit['evalue']:.3g}", "diamond_pident": fmt_num(hit["pident"]),
            "diamond_qcov": fmt_num(hit["qcov"]), "diamond_scov": fmt_num(hit["scov"]),
        })
    if ko:
        row["kofam_ko"] = join(k for k, _ in ko)
    # name: Swiss-Prot > similar to (InterPro > eggNOG > TrEMBL) > uncharacterized
    name, src = UNCHARACTERIZED, "none"
    if sp and sp["passed"] and informative(sp["name"]):
        name, src = sp["name"], "swissprot"
    else:
        for s, cand in (("interproscan", ips_best_desc(ips) if ips else ""),
                        ("eggnog", em["desc"] if em else ""),
                        ("trembl", tr["name"] if tr and tr["passed"] else "")):
            if informative(cand):
                name, src = f"similar to {cand}", s
                break
    row["final_name"], row["final_name_source"] = name, src
    if go_all:
        row["go_terms"] = join(sorted(go_all))
        row["go_evidence"] = GO_EVIDENCE
    row["db_versions"] = db_versions
    return row


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="F-aggregate: one gene-level table from InterProScan, eggNOG-mapper, "
                    "DIAMOND (Swiss-Prot/TrEMBL) and KofamScan outputs.")
    ap.add_argument("--proteins", help="proteins FASTA (row order, duplicate check, qlen fallback)")
    ap.add_argument("--ips", action="append", default=[], help="InterProScan TSV (repeatable)")
    ap.add_argument("--emapper", action="append", default=[], help="*.emapper.annotations (repeatable)")
    ap.add_argument("--diamond-swissprot", action="append", default=[], help="DIAMOND outfmt 6 vs Swiss-Prot")
    ap.add_argument("--diamond-trembl", action="append", default=[], help="DIAMOND outfmt 6 vs TrEMBL")
    ap.add_argument("--diamond-columns", default=" ".join(DEFAULT_DIAMOND_COLS),
                    help="space-separated outfmt 6 field names in file order (default: %(default)s)")
    ap.add_argument("--kofam", action="append", default=[], help="KofamScan detail/detail-tsv/mapper output")
    ap.add_argument("--thresholds", default=str(DEFAULT_THRESHOLDS),
                    help="TSV with param_max_evalue/param_min_pident/param_min_qcov/param_min_scov")
    ap.add_argument("--max-evalue", type=float, help="override param_max_evalue")
    ap.add_argument("--min-pident", type=float, help="override param_min_pident (percent)")
    ap.add_argument("--min-qcov", type=float, help="override param_min_qcov (percent)")
    ap.add_argument("--min-scov", type=float, help="override param_min_scov (percent)")
    ap.add_argument("--db-version", action="append", default=[],
                    help="tool=version@YYYY-MM-DD, e.g. swissprot=2026_03@2026-06-18 (repeatable)")
    ap.add_argument("--db-versions-file", action="append", default=[],
                    help="TSV: tool<TAB>version<TAB>YYYY-MM-DD")
    ap.add_argument("--schema", default=str(DEFAULT_SCHEMA), help="column schema to check against if present")
    ap.add_argument("--out", required=True, help="output gene-level TSV")
    a = ap.parse_args(argv)

    check_schema(Path(a.schema))
    params = load_params(Path(a.thresholds) if a.thresholds else None)
    for key, val in (("param_max_evalue", a.max_evalue), ("param_min_pident", a.min_pident),
                     ("param_min_qcov", a.min_qcov), ("param_min_scov", a.min_scov)):
        if val is not None:
            params[key] = val
    dbv = parse_db_versions(a.db_version, a.db_versions_file)
    dbv_names = {e.split("=", 1)[0].lower() for e in dbv}

    ids: list[str] = []
    qlens: dict[str, int] = {}
    if a.proteins:
        ids, qlens = fasta_lengths(Path(a.proteins))
        dups = sorted(g for g, n in Counter(ids).items() if n > 1)
        if dups:
            print(f"[ERR] Gate-F5: duplicate gene_id in --proteins ({len(dups)}): "
                  f"{', '.join(dups[:10])}", file=sys.stderr)
            return 1

    ips: dict = {}
    em: dict = {}
    sp: dict = {}
    tr: dict = {}
    ko: dict = {}
    cols = a.diamond_columns.split()
    for p in a.ips:
        ips.update(parse_interproscan(Path(p)))
    for p in a.emapper:
        em.update(parse_emapper(Path(p)))
    for p in a.diamond_swissprot:
        sp.update(parse_diamond(Path(p), cols, qlens, "swissprot", params))
    for p in a.diamond_trembl:
        tr.update(parse_diamond(Path(p), cols, qlens, "trembl", params))
    for p in a.kofam:
        ko.update(parse_kofam(Path(p)))

    used = {"interproscan": bool(a.ips), "eggnog": bool(a.emapper),
            "diamond": bool(a.diamond_swissprot or a.diamond_trembl), "kofam": bool(a.kofam),
            "swissprot": bool(a.diamond_swissprot), "trembl": bool(a.diamond_trembl)}
    missing = [t for t, u in used.items() if u and t not in dbv_names]
    if missing:
        print(f"[WARN] no --db-version for: {', '.join(missing)} (F10 QC will flag db_versions)",
              file=sys.stderr)

    if not ids:
        ids = sorted(set(ips) | set(em) | set(sp) | set(tr) | set(ko))
    dbs = join(dbv)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    annotated = 0
    with open(out, "w", newline="") as fo:
        w = csv.DictWriter(fo, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        for gid in ids:
            row = build_row(gid, ips.get(gid), em.get(gid), sp.get(gid), tr.get(gid), ko.get(gid), dbs)
            annotated += row["final_name_source"] != "none" or bool(row["go_terms"] or row["kofam_ko"])
            w.writerow(row)
    print(f"[aggregate] genes={len(ids)} ips={sum(g in ips for g in ids)} eggnog={sum(g in em for g in ids)} "
          f"swissprot={sum(g in sp for g in ids)} trembl={sum(g in tr for g in ids)} "
          f"kofam={sum(g in ko for g in ids)} annotated={annotated} filters={params}", file=sys.stderr)
    if ids and annotated == 0:
        print("[ERR] Gate-F5: every row is annotation-empty; check input paths.", file=sys.stderr)
        return 1
    print(f"[OK] {len(ids)} genes -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
