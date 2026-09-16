#!/usr/bin/env python3
"""Convert FA F8 nlr_candidates.tsv → structure-style families.tsv (gene_id\tNLR).

Timing:
  - Structure S7a can build families.tsv *before* FA (HRP / curated IDs) for G9 boost.
  - FA F8 runs *after* InterProScan and writes nlr_candidates.tsv for the FA release.
  - To feed a *later* structure re-priority pass, convert F8 → families and re-run
    02_priority_loci.py --families (not the same step as first-pass S7a).

Usage:
  python3 pipeline/F8b_nlr_to_families.py \
    --nlr function/nlr/nlr_candidates.tsv \
    --out curate/families_from_f8.tsv \
    --family NLR
"""
from __future__ import annotations
import argparse, csv
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--nlr", type=Path, required=True, help="F8 nlr_candidates.tsv")
    ap.add_argument("--out", type=Path, required=True, help="families.tsv for 02_priority_loci --families")
    ap.add_argument("--family", default="NLR", help="family label written in column 2 (default NLR)")
    args = ap.parse_args()
    rows = []
    with args.nlr.open() as f:
        r = csv.DictReader(f, delimiter="\t")
        if not r.fieldnames or "gene_id" not in r.fieldnames:
            raise SystemExit(f"need gene_id column in {args.nlr}")
        for row in r:
            gid = (row.get("gene_id") or "").strip()
            if gid:
                rows.append((gid, args.family))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w") as f:
        f.write("gene_id\tfamily\n")
        for gid, fam in rows:
            f.write(f"{gid}\t{fam}\n")
    print(f"[OK] {len(rows)} genes → {args.out} (family={args.family})")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
