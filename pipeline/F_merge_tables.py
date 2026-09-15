#!/usr/bin/env python3
"""Merge eggNOG / InterProScan / DIAMOND into one gene-centric TSV (best-effort parsers)."""
from __future__ import annotations
import argparse, csv, re, sys
from pathlib import Path
from collections import defaultdict, Counter

def fasta_ids(path: str) -> list[str]:
    ids = []
    for line in open(path):
        if line.startswith(">"):
            ids.append(line[1:].split()[0])
    return ids

def parse_emapper(path: Path) -> dict[str, dict]:
    out = {}
    with open(path) as f:
        header = None
        for line in f:
            if line.startswith("#"):
                if line.startswith("#query") or "query" in line.lower() and "seed" in line.lower():
                    header = line.lstrip("#").strip().split("\t")
                continue
            if not line.strip():
                continue
            cols = line.rstrip("\n").split("\t")
            if header and len(cols) >= len(header):
                row = dict(zip(header, cols))
                q = row.get("query") or row.get("#query") or cols[0]
            else:
                q = cols[0]
                row = {"raw": line.rstrip()}
            # common emapper columns (v2 names; v3 may differ — keep raw too)
            out[q] = {
                "emapper_COG": row.get("COG_category") or row.get("cog_category") or "",
                "emapper_Description": row.get("Description") or row.get("description") or "",
                "emapper_GOs": row.get("GOs") or row.get("go") or "",
                "emapper_KEGG_ko": row.get("KEGG_ko") or row.get("kegg_ko") or "",
                "emapper_KEGG_Pathway": row.get("KEGG_Pathway") or row.get("kegg_pathway") or "",
                "emapper_PFAMs": row.get("PFAMs") or row.get("pfam") or "",
                "emapper_Preferred_name": row.get("Preferred_name") or row.get("preferred_name") or "",
            }
    return out

def parse_ips_tsv(path: Path) -> dict[str, dict]:
    # InterProScan TSV: protein_id ... signature ... go ...
    go = defaultdict(set)
    sig = defaultdict(set)
    ipr = defaultdict(set)
    for line in open(path):
        if not line.strip() or line.startswith("#"):
            continue
        c = line.rstrip("\n").split("\t")
        if len(c) < 12:
            continue
        pid, analysis, sigacc, sigdesc = c[0], c[3], c[4], c[5]
        sig[pid].add(f"{analysis}:{sigacc}")
        if len(c) > 11 and c[11].startswith("IPR"):
            ipr[pid].add(c[11])
        if len(c) > 13 and c[13]:
            for g in re.split(r"[|,]", c[13]):
                if g.startswith("GO:"):
                    go[pid].add(g)
    return {
        k: {
            "ips_signatures": ";".join(sorted(sig[k]))[:2000],
            "ips_InterPro": ";".join(sorted(ipr[k])),
            "ips_GOs": ";".join(sorted(go[k])),
        }
        for k in set(sig) | set(ipr) | set(go)
    }

def parse_diamond(path: Path) -> dict[str, dict]:
    best = {}
    for line in open(path):
        c = line.rstrip("\n").split("\t")
        if len(c) < 12:
            continue
        q, s, pident, evalue, bits = c[0], c[1], c[2], c[10], float(c[11])
        title = c[12] if len(c) > 12 else ""
        if q not in best or bits > best[q]["_bits"]:
            best[q] = {
                "diamond_sseqid": s,
                "diamond_pident": pident,
                "diamond_evalue": evalue,
                "diamond_stitle": title,
                "_bits": bits,
            }
    for v in best.values():
        v.pop("_bits", None)
    return best

def _row_has_annotation(row: dict) -> bool:
    keys = (
        "emapper_GOs", "emapper_KEGG_ko", "emapper_PFAMs", "emapper_Preferred_name",
        "emapper_Description", "emapper_COG", "emapper_KEGG_Pathway",
        "ips_InterPro", "ips_signatures", "ips_GOs",
        "diamond_sseqid",
    )
    for k in keys:
        v = row.get(k) or ""
        if str(v).strip():
            return True
    return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proteins", required=True)
    ap.add_argument("--emapper", action="append", default=[])
    ap.add_argument("--ips", action="append", default=[])
    ap.add_argument("--diamond", action="append", default=[])
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    ids = fasta_ids(args.proteins)
    # Gate-F5 honesty: duplicate gene_id must not fake-pass
    counts = Counter(ids)
    dups = sorted([g for g, n in counts.items() if n > 1])
    if dups:
        sample = ", ".join(dups[:10])
        more = f" (+{len(dups)-10} more)" if len(dups) > 10 else ""
        print(
            f"[ERR] Gate-F5: duplicate gene_id in --proteins ({len(dups)} ids); "
            f"e.g. {sample}{more}. Deduplicate before merge.",
            file=sys.stderr,
        )
        return 1

    em, ip, di = {}, {}, {}
    for p in args.emapper:
        em.update(parse_emapper(Path(p)))
    for p in args.ips:
        ip.update(parse_ips_tsv(Path(p)))
    for p in args.diamond:
        di.update(parse_diamond(Path(p)))

    # Per-source hit counts (coverage visible for Gate-F5 narrative)
    n_em = sum(1 for gid in ids if gid in em)
    n_ip = sum(1 for gid in ids if gid in ip)
    n_di = sum(1 for gid in ids if gid in di)
    print(
        f"[merge] source_hits proteins={len(ids)} "
        f"emapper={n_em} ips={n_ip} diamond={n_di}",
        file=sys.stderr,
    )

    fields = [
        "gene_id",
        "emapper_Preferred_name", "emapper_Description", "emapper_GOs",
        "emapper_KEGG_ko", "emapper_KEGG_Pathway", "emapper_COG", "emapper_PFAMs",
        "ips_InterPro", "ips_signatures", "ips_GOs",
        "diamond_sseqid", "diamond_pident", "diamond_evalue", "diamond_stitle",
    ]
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    annotated = 0
    with open(args.out, "w", newline="") as fo:
        w = csv.DictWriter(fo, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        for gid in ids:
            row = {"gene_id": gid}
            row.update(em.get(gid, {}))
            row.update(ip.get(gid, {}))
            row.update(di.get(gid, {}))
            if _row_has_annotation(row):
                annotated += 1
            w.writerow(row)
    print(
        f"[merge] rows={len(ids)} proteins_in={len(ids)} "
        f"rows_with_any_annotation={annotated}",
        file=sys.stderr,
    )

    if ids and annotated == 0:
        print(
            "[ERR] Gate-F5: all rows look annotation-empty — check emapper/IPS/DIAMOND "
            "paths and DB↔binary versions. Refusing exit 0 (would fake-pass Gate-F5).",
            file=sys.stderr,
        )
        return 1
    print(f"[OK] {len(ids)} genes → {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
