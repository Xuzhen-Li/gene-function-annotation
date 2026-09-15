#!/usr/bin/env python3
"""Smoke-check a function release folder (not a full F-L1 judge).

Usage:
  python3 pipeline/check_release_pack.py path/to/function/release/TAG
Exit 0 if master TSV + proteins + METHODS-like file found; else 1.
Full pass/fail: docs/EVALUATION_CHECKLIST.md
"""
from __future__ import annotations
import sys
from pathlib import Path

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_release_pack.py function/release/<TAG>", file=sys.stderr)
        return 2
    root = Path(sys.argv[1])
    if not root.is_dir():
        print(f"FAIL: not a directory: {root}")
        return 1
    names = {p.name.lower() for p in root.iterdir() if p.is_file()}
    master = any("master" in n and n.endswith((".tsv", ".txt", ".csv")) for n in names) or any(
        n.endswith(".tsv") for n in names
    )
    faa = any(n.endswith(".faa") for n in names) or any(
        "prot" in n and n.endswith((".fa", ".fasta")) for n in names
    )
    methods = any("method" in n or n.endswith(".md") or "readme" in n for n in names)
    print(f"release_dir={root}")
    print(f"  master table: {'OK' if master else 'MISSING (*master*.tsv or *.tsv)'}")
    print(f"  proteins copy: {'OK' if faa else 'MISSING'}")
    print(f"  METHODS/README: {'OK' if methods else 'MISSING'}")
    print("Note: pack smoke only. Tick docs/EVALUATION_CHECKLIST.md for F-L0/F-L1.")
    return 0 if (master and faa and methods) else 1

if __name__ == "__main__":
    raise SystemExit(main())
