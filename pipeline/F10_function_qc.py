#!/usr/bin/env python3
"""F10: quality assessment of the gene-level merged function table. [[TODO-TEXT]]"""
from __future__ import annotations

import argparse
import csv
import math
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_SCHEMA = HERE / "schema" / "merged_function_table.tsv"
DEFAULT_THRESHOLDS = HERE.parent / "config" / "function_qc_thresholds.tsv"
TOOLS = ("interproscan", "eggnog", "diamond", "kofam")
TOOL_COLS = {
    "interproscan": ("ips_domains", "ips_ipr", "ips_go"),
    "eggnog": ("eggnog_og", "eggnog_name", "eggnog_ko", "eggnog_go"),
    "diamond": ("diamond_hit",),
    "kofam": ("kofam_ko",),
}
HYPO_RE = re.compile(r"hypothetical|uncharacteri[sz]ed|unknown|predicted protein|^\s*$", re.I)
STOP = {"protein", "domain", "family", "putative", "probable", "like", "containing",
        "subunit", "type", "with", "from", "related", "superfamily", "repeat"}
DB_VER_RE = re.compile(r"^[A-Za-z0-9_.-]+=[^@;]+@\d{4}-\d{2}-\d{2}$")


def split_list(v: str) -> set[str]:
    return {x.strip() for x in (v or "").split(";") if x.strip() and x.strip() != "-"}


def tokens(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]+", (text or "").lower())
            if len(t) >= 4 and t not in STOP}


def read_tsv(path: Path) -> list[dict]:
    with open(path, newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def load_schema(path: Path) -> list[str]:
    return [r["column"] for r in read_tsv(path) if r.get("required") == "yes"]


def load_thresholds(path: Path) -> dict[str, tuple[str, float, str]]:
    return {r["key"]: (r["direction"], float(r["value"]), r.get("label", ""))
            for r in read_tsv(path)}


def check_columns(rows: list[dict], required: list[str], what: str) -> None:
    if not rows:
        sys.exit(f"ERROR: {what} has no rows")
    missing = [c for c in required if c not in rows[0]]
    if missing:
        sys.exit(f"ERROR: {what} missing columns: {', '.join(missing)}")


def has_tool(r: dict, tool: str) -> bool:
    return any(split_list(r.get(c, "")) for c in TOOL_COLS[tool])


def fnum(v: str) -> float | None:
    try:
        x = float(v)
        return None if math.isnan(x) else x
    except (TypeError, ValueError):
        return None


def frac(n: int, d: int) -> float | None:
    return None if d == 0 else n / d


def quantile(xs: list[float], q: float) -> float | None:
    if not xs:
        return None
    s = sorted(xs)
    k = (len(s) - 1) * q
    lo, hi = math.floor(k), math.ceil(k)
    return s[lo] + (s[hi] - s[lo]) * (k - lo)


def pair_agreements(r: dict) -> dict[str, bool | None]:
    """None = pair not comparable (one side empty)."""
    out: dict[str, bool | None] = {}
    a, b = split_list(r["eggnog_ko"]), split_list(r["kofam_ko"])
    out["ko_eggnog_vs_kofam"] = bool(a & b) if a and b else None
    a, b = split_list(r["ips_go"]), split_list(r["eggnog_go"])
    out["go_ips_vs_eggnog"] = bool(a & b) if a and b else None
    a, b = tokens(r["eggnog_name"] + " " + r["eggnog_description"]), tokens(r["diamond_name"])
    out["name_eggnog_vs_diamond"] = bool(a & b) if a and b else None
    return out


def conflicts(r: dict) -> list[tuple[str, str, str]]:
    found = []
    e = tokens(r["eggnog_name"] + " " + r["eggnog_description"])
    p = tokens(r["ips_domain_desc"])
    if e and p and not (e & p):
        found.append(("eggnog_name_vs_pfam_domain",
                      f"{r['eggnog_name']}|{r['eggnog_description']}", r["ips_domain_desc"]))
    a, b = split_list(r["eggnog_ko"]), split_list(r["kofam_ko"])
    if a and b and not (a & b):
        found.append(("eggnog_ko_vs_kofam_ko", ";".join(sorted(a)), ";".join(sorted(b))))
    return found


def diamond_pass(r: dict, p: dict) -> bool | None:
    if not split_list(r["diamond_hit"]):
        return None
    ev, pi, qc, sc = (fnum(r[k]) for k in ("diamond_evalue", "diamond_pident",
                                            "diamond_qcov", "diamond_scov"))
    if None in (ev, pi, qc, sc):
        return False
    return ev <= p["param_max_evalue"] and pi >= p["param_min_pident"] \
        and qc >= p["param_min_qcov"] and sc >= p["param_min_scov"]


NAME_SOURCES = ("swissprot", "eggnog", "interproscan_domain", "none")
# The next two constants mirror pipeline/F_aggregate.py (UNINFORMATIVE_RE, DOMAIN_ANALYSES);
# keep them in sync so this check and the merge step apply the same naming rule.
UNINFORMATIVE_RE = re.compile(
    r"^\s*(-|uncharacteri[sz]ed protein.*|hypothetical protein.*|predicted protein.*|"
    r"unknown( protein)?|protein of unknown function.*)?\s*$", re.I)
DOMAIN_ANALYSES = ("Pfam", "SMART", "ProSiteProfiles", "CDD")


def informative(name: str) -> bool:
    return not UNINFORMATIVE_RE.match(name or "")


def domain_tier(r: dict) -> set[str]:
    """Accepted sources at the InterProScan tier.
    {"interproscan_domain"}: a Pfam/SMART/ProSiteProfiles/CDD signature with an informative
    description (F_aggregate names such genes from it).
    {"interproscan_domain", "none"}: only InterPro IDs (ips_ipr) without such a signature, or
    ips_domains / ips_domain_desc counts differ on ';' -- F_aggregate's choice there depends on
    InterPro entry descriptions, which this table does not carry, so both are accepted.
    {"none"}: no domain evidence, e.g. rows only from MobiDBLite / PANTHER / Coils."""
    doms = (r.get("ips_domains") or "").split(";")
    descs = (r.get("ips_domain_desc") or "").split(";")
    if len(doms) != len(descs):
        return {"interproscan_domain", "none"}
    for dom, desc in zip(doms, descs):
        if dom.split(":", 1)[0].strip() in DOMAIN_ANALYSES and informative(desc.strip()):
            return {"interproscan_domain"}
    if split_list(r.get("ips_ipr", "")):
        return {"interproscan_domain", "none"}
    return {"none"}


def expected_name_sources(r: dict, p: dict) -> set[str]:
    """Accepted final_name_source values. Naming rule (word lists mirror F_aggregate):
    Swiss-Prot hit passing all filters with an informative name > informative eggNOG
    preferred name > InterProScan domain > none. TrEMBL never names. At the InterProScan
    tier IPR-only / count-mismatch rows accept both interproscan_domain and none."""
    if r["diamond_db"].strip().lower() == "swissprot" and diamond_pass(r, p) \
            and informative(r["diamond_name"]):
        return {"swissprot"}
    if informative(r["eggnog_name"].strip()):
        return {"eggnog"}
    return domain_tier(r)


def db_versions_ok(r: dict) -> bool:
    entries = split_list(r["db_versions"])
    if not entries or not all(DB_VER_RE.match(e) for e in entries):
        return False
    names = {e.split("=")[0].lower() for e in entries}
    return all(t in names for t in TOOLS if has_tool(r, t))


def table_basic(rows: list[dict]) -> dict[str, float | None]:
    n = len(rows)
    kos: set[str] = set()
    for r in rows:
        kos |= split_list(r.get("kofam_ko", "")) | split_list(r.get("eggnog_ko", ""))
    return {
        "coverage_any": frac(sum(any(has_tool(r, t) for t in TOOLS) for r in rows), n),
        "share_hypothetical": frac(sum(bool(HYPO_RE.search(r.get("final_name", ""))) for r in rows), n),
        "_kos": kos,
    }


def compute(rows: list[dict], thr: dict, relative: list[dict] | None):
    n = len(rows)
    params = {k: v[1] for k, v in thr.items() if v[0] == "param"}
    m: dict[str, float | None] = {"n_genes": n}
    for t in TOOLS:
        m[f"coverage_{t}"] = frac(sum(has_tool(r, t) for r in rows), n)
    base = table_basic(rows)
    m["coverage_any"] = base["coverage_any"]
    m["share_hypothetical"] = base["share_hypothetical"]

    pair_hits = {k: [0, 0] for k in ("ko_eggnog_vs_kofam", "go_ips_vs_eggnog", "name_eggnog_vs_diamond")}
    ge2 = 0
    conflict_rows = []
    for r in rows:
        ag = pair_agreements(r)
        for k, v in ag.items():
            if v is not None:
                pair_hits[k][1] += 1
                pair_hits[k][0] += int(v)
        if any(ag.values()):
            ge2 += 1
        for kind, a, b in conflicts(r):
            conflict_rows.append({"gene_id": r["gene_id"], "conflict": kind, "side_a": a, "side_b": b})
    for k, (hit, tot) in pair_hits.items():
        m[f"agree_{k}"] = frac(hit, tot)
    m["share_ge2_tools_agree"] = frac(ge2, n)
    m["share_conflict"] = frac(len({c["gene_id"] for c in conflict_rows}), n)

    dp = [diamond_pass(r, params) for r in rows]
    dp = [x for x in dp if x is not None]
    m["share_diamond_hits_pass_filters"] = frac(sum(dp), len(dp))
    dist = {}
    for col in ("diamond_evalue", "diamond_pident", "diamond_qcov", "diamond_scov"):
        vals = [fnum(r[col]) for r in rows if split_list(r["diamond_hit"])]
        vals = [v for v in vals if v is not None]
        if col == "diamond_evalue":
            vals = [-math.log10(max(v, 1e-300)) for v in vals]
            col = "diamond_neglog10_evalue"
        for q, lab in ((0.1, "p10"), (0.5, "median"), (0.9, "p90")):
            dist[f"{col}_{lab}"] = quantile(vals, q)
    m.update(dist)

    m["share_name_source_consistent"] = frac(
        sum(r["final_name_source"].strip() in expected_name_sources(r, params) for r in rows), n)
    for src in NAME_SOURCES:
        m[f"share_name_source_{src}"] = frac(sum(r["final_name_source"].strip() == src for r in rows), n)

    with_go = [r for r in rows if split_list(r["go_terms"])]
    m["share_go_evidence_iea"] = frac(sum(r["go_evidence"].strip().upper() == "IEA" for r in with_go), len(with_go))
    m["share_go_with_source"] = frac(sum(bool(split_list(r["go_source"])) for r in with_go), len(with_go))
    m["share_genes_db_versions_complete"] = frac(sum(db_versions_ok(r) for r in rows), n)

    if relative is not None:
        rb = table_basic(relative)
        m["relative_n_genes"] = len(relative)
        m["relative_coverage_any"] = rb["coverage_any"]
        m["relative_share_hypothetical"] = rb["share_hypothetical"]
        m["delta_coverage_any_vs_relative"] = None if None in (m["coverage_any"], rb["coverage_any"]) \
            else m["coverage_any"] - rb["coverage_any"]
        m["delta_hypothetical_vs_relative"] = None if None in (m["share_hypothetical"], rb["share_hypothetical"]) \
            else m["share_hypothetical"] - rb["share_hypothetical"]
        u = base["_kos"] | rb["_kos"]
        m["ko_jaccard_vs_relative"] = frac(len(base["_kos"] & rb["_kos"]), len(u))
    return m, conflict_rows


def status(key: str, value, thr: dict) -> tuple[str, str, str]:
    if key not in thr or thr[key][0] == "param":
        return "info", "", ""
    d, t, label = thr[key]
    if value is None:
        return "na", f"{d} {t:g}", label
    # Compare the rounded value as written in the table (fmt), so the status always
    # agrees with the printed number (e.g. 0.99996 prints as 1 and passes min 1).
    value = float(fmt(value))
    ok = {"min": value >= t, "max": value <= t, "maxabs": abs(value) <= t}[d]
    return ("pass" if ok else "warn"), f"{d} {t:g}", label


def fmt(v) -> str:
    if v is None:
        return "NA"
    if isinstance(v, int):
        return str(v)
    return f"{v:.4g}"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="F10 function QC")
    ap.add_argument("--merged", required=True, help="gene-level merged table from F-merge")
    ap.add_argument("--relative", help="close relative species annotation table (same schema)")
    ap.add_argument("--schema", default=str(DEFAULT_SCHEMA))
    ap.add_argument("--thresholds", default=str(DEFAULT_THRESHOLDS))
    ap.add_argument("--out", required=True, help="QC summary TSV")
    ap.add_argument("--conflicts", help="conflict table TSV (default: <out>.conflicts.tsv)")
    a = ap.parse_args(argv)

    required = load_schema(Path(a.schema))
    thr = load_thresholds(Path(a.thresholds))
    rows = read_tsv(Path(a.merged))
    check_columns(rows, required, "merged table")
    rel = None
    if a.relative:
        rel = read_tsv(Path(a.relative))
        check_columns(rel, ["gene_id", "final_name", "kofam_ko", "eggnog_ko"], "relative table")

    m, conf = compute(rows, thr, rel)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["metric", "value", "threshold", "status", "threshold_label"])
        for k, v in m.items():
            st, th, lab = status(k, v, thr)
            w.writerow([k, fmt(v), th, st, lab])
    cpath = Path(a.conflicts) if a.conflicts else out.with_suffix(".conflicts.tsv")
    with open(cpath, "w", newline="") as f:
        w = csv.DictWriter(f, ["gene_id", "conflict", "side_a", "side_b"], delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(conf)
    print(f"wrote {out} and {cpath}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
