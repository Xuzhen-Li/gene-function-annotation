#!/usr/bin/env python3
"""Join PANNZER2 tabular output onto merged_function_table.tsv (best-effort columns)."""
from __future__ import annotations
import argparse, csv
from pathlib import Path

def load_pannzer(path: Path) -> dict[str, dict]:
    out = {}
    lines = path.read_text(errors="replace").splitlines()
    if not lines:
        return out
    delim = "\t" if "\t" in lines[0] else ","
    # skip comment lines
    start = 0
    while start < len(lines) and lines[start].startswith("#"):
        start += 1
    reader = csv.DictReader(lines[start:], delimiter=delim)
    for row in reader:
        gid = (
            row.get("qpid")
            or row.get("query")
            or row.get("Query")
            or row.get("gene_id")
            or row.get("Protein id")
            or next(iter(row.values()), "")
        )
        if not gid:
            continue
        out[gid.strip()] = {
            "pannzer_DE": row.get("DE") or row.get("description") or row.get("desc") or row.get("Annotation") or "",
            "pannzer_GO": row.get("GO ids") or row.get("GO") or row.get("goids") or "",
        }
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--master", required=True)
    ap.add_argument("--pannzer", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    pz = load_pannzer(Path(args.pannzer))
    with open(args.master) as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
        fields = list(rows[0].keys()) if rows else ["gene_id"]
    for c in ("pannzer_DE", "pannzer_GO"):
        if c not in fields:
            fields.append(c)
    with open(args.out, "w", newline="") as fo:
        w = csv.DictWriter(fo, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        for row in rows:
            extra = pz.get(row.get("gene_id", ""), {})
            row.update(extra)
            w.writerow(row)
    print(f"[OK] PANNZER joined for {len(pz)} ids → {args.out}")

if __name__ == "__main__":
    main()
