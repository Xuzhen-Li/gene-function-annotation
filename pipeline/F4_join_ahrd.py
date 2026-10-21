#!/usr/bin/env python3
"""Join AHRD CSV/TSV descriptions onto merged_function_table.tsv."""
from __future__ import annotations
import argparse, csv
from pathlib import Path

def load_ahrd(path: Path) -> dict[str, str]:
    text = path.read_text().splitlines()
    # detect delimiter
    delim = "\t" if "\t" in text[0] else ","
    r = csv.DictReader(text, delimiter=delim)
    out = {}
    for row in r:
        # common AHRD column names
        gid = row.get("Protein-Accession") or row.get("accession") or row.get("query") or row.get("Gene-ID")
        desc = row.get("Human-Readable-Description") or row.get("description") or row.get("HRD") or ""
        if gid:
            out[gid.strip()] = desc.strip()
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--master", required=True)
    ap.add_argument("--ahrd", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    ahrd = load_ahrd(Path(args.ahrd))
    with open(args.master) as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
        fields = list(rows[0].keys()) if rows else ["gene_id"]
    if "ahrd_description" not in fields:
        fields.append("ahrd_description")
    with open(args.out, "w", newline="") as fo:
        w = csv.DictWriter(fo, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        for row in rows:
            gid = row.get("gene_id", "")
            row["ahrd_description"] = ahrd.get(gid, "")
            w.writerow(row)
    print(f"[OK] joined {sum(1 for v in ahrd.values() if v)} descriptions → {args.out}")

if __name__ == "__main__":
    main()
