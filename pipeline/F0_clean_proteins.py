#!/usr/bin/env python3
"""F0 protein clean-up before F1: strip terminal stop symbols, report internal stops.

gffread -y writes a stop codon as '.', other tools write '*'. InterProScan and some
other tools reject or mis-handle these symbols, so:
  * trailing '*' or '.' (one or more) at the end of each protein is removed;
  * a '*' or '.' anywhere else is an INTERNAL stop (pseudogene, frameshift or a broken
    model). It is reported in --report; the protein is kept as-is unless
    --drop-internal is given. Internal stops are a structure problem: fix them upstream
    (gene-structure-annotation) rather than here.

Usage:
  python3 pipeline/F0_clean_proteins.py --in proteins.faa --out proteins.clean.faa \
      --report internal_stops.tsv [--drop-internal]
Exit 0 on success (also when internal stops were found; read the [WARN] line), 1 on bad input.
Stdlib only.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

STOPS = "*."
WRAP = 60


def read_fasta(path: Path):
    """Yield (header_line_without_>, sequence)."""
    head, seq = None, []
    with open(path) as f:
        for line in f:
            line = line.rstrip("\r\n")
            if line.startswith(">"):
                if head is not None:
                    yield head, "".join(seq)
                head, seq = line[1:], []
            elif head is not None:
                seq.append(line.strip())
            elif line.strip():
                raise ValueError(f"{path}: sequence data before the first '>' header")
    if head is not None:
        yield head, "".join(seq)


def clean(seq: str) -> tuple[str, int, list[int]]:
    """Return (cleaned sequence, n terminal stops removed, 1-based internal stop positions)."""
    core = seq.rstrip(STOPS)
    n_term = len(seq) - len(core)
    internal = [i + 1 for i, aa in enumerate(core) if aa in STOPS]
    return core, n_term, internal


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Strip terminal stops ('*' or '.') and report internal stops.")
    ap.add_argument("--in", dest="inp", required=True, help="protein FASTA (e.g. the structure release proteins.faa)")
    ap.add_argument("--out", required=True, help="cleaned protein FASTA")
    ap.add_argument("--report", required=True, help="TSV of proteins with internal stops")
    ap.add_argument("--drop-internal", action="store_true",
                    help="leave proteins with internal stops out of --out (default: keep them)")
    a = ap.parse_args(argv)
    inp = Path(a.inp)
    if not inp.is_file():
        print(f"[ERR] protein FASTA not found: {inp}", file=sys.stderr)
        return 1
    if Path(a.out).resolve() == inp.resolve():
        print("[ERR] --out must differ from --in (the input is never overwritten)", file=sys.stderr)
        return 1
    n = n_trim = n_bad = n_drop = 0
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.report).parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(a.out, "w") as fo, open(a.report, "w") as fr:
            fr.write("gene_id\tlength\tn_internal_stops\tpositions\taction\n")
            for head, seq in read_fasta(inp):
                n += 1
                core, n_term, internal = clean(seq)
                n_trim += n_term > 0
                gid = head.split()[0] if head.split() else ""
                if internal:
                    n_bad += 1
                    pos = ",".join(map(str, internal[:20])) + (",..." if len(internal) > 20 else "")
                    action = "dropped" if a.drop_internal else "kept"
                    fr.write(f"{gid}\t{len(core)}\t{len(internal)}\t{pos}\t{action}\n")
                    if a.drop_internal:
                        n_drop += 1
                        continue
                fo.write(f">{head}\n")
                for i in range(0, len(core), WRAP):
                    fo.write(core[i:i + WRAP] + "\n")
    except ValueError as e:
        print(f"[ERR] {e}", file=sys.stderr)
        return 1
    if n == 0:
        print(f"[ERR] no FASTA records in {inp}", file=sys.stderr)
        return 1
    print(f"[F0] proteins={n} terminal_stop_stripped={n_trim} internal_stop={n_bad} "
          f"dropped={n_drop}", file=sys.stderr)
    if n_bad:
        print(f"[WARN] {n_bad} protein(s) with internal stops -> {a.report}; "
              f"fix these models upstream", file=sys.stderr)
    print(f"[OK] {n - n_drop} proteins -> {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
