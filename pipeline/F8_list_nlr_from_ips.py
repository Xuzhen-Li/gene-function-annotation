#!/usr/bin/env python3
"""List NLR candidates from an InterProScan 5 TSV and classify them.

Rule (domain architecture, not keywords):
  * An NLR candidate MUST carry the NB-ARC domain (Pfam PF00931 or InterPro IPR002182).
    LRR-only proteins (PF00560, PF13516, IPR001611 ...) are receptor-like kinases or
    receptor-like proteins (RLK/RLP), not NLRs, and are never listed. TIR-only or
    RPW8-only proteins are not listed either.
  * N-terminal class, first match wins: TIR -> T, RPW8 -> R, coiled coil -> C, else none.
  * LRR present -> 'L' suffix.

nlr_class values: CNL, TNL, RNL (N-terminal domain + NB-ARC + LRR);
                  CN, TN, RN (no LRR detected); NL (NB-ARC + LRR, no N-terminal domain);
                  N (NB-ARC only).
Partial classes (CN, TN, RN, NL, N) are often truncated or atypical models; check them.
Coiled-coil calls from the IPS 'Coils' analysis are permissive. For publication, compare
with a dedicated NLR tool (NLRtracker, Resistify or NLR-Annotator).
Stdlib only.
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict

NBARC = {"PF00931", "IPR002182"}
TIR = {"PF01582", "PF13676", "IPR000157", "IPR035897", "SM00255", "PS50104"}
RPW8 = {"PF05659", "IPR008808", "PS51153"}
CC = {"PF18052", "IPR041118", "IPR038005"}       # Rx-type N-terminal coiled coil
CC_ANALYSES = {"Coils"}                           # IPS coiled-coil predictor
LRR = {"PF00560", "PF07723", "PF07725", "PF12799", "PF13516", "PF13855",
       "IPR001611", "IPR003591", "IPR032675", "IPR011713",
       "SM00369", "PS51450"}

COLUMNS = ["gene_id", "nlr_class", "n_terminal", "has_lrr", "nlr_signatures"]


def classify(accs: set[str], analyses: set[str]) -> tuple[str, str, bool] | None:
    """Return (nlr_class, n_terminal, has_lrr), or None if not an NLR (no NB-ARC)."""
    if not accs & NBARC:
        return None
    if accs & TIR:
        nterm = "TIR"
    elif accs & RPW8:
        nterm = "RPW8"
    elif accs & CC or analyses & CC_ANALYSES:
        nterm = "CC"
    else:
        nterm = ""
    lrr = bool(accs & LRR)
    prefix = {"TIR": "T", "RPW8": "R", "CC": "C", "": ""}[nterm]
    cls = prefix + "N" + ("L" if lrr else "")
    return cls, nterm, lrr


def read_ips(path: str) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    """protein -> accessions (member signature + InterPro entry), protein -> analyses."""
    accs: dict[str, set[str]] = defaultdict(set)
    analyses: dict[str, set[str]] = defaultdict(set)
    with open(path) as f:
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue
            c = line.rstrip("\n").split("\t")
            if len(c) < 5:
                continue
            pid = c[0]
            analyses[pid].add(c[3])
            accs[pid].add(c[4])
            if len(c) > 11 and c[11].startswith("IPR"):
                accs[pid].add(c[11])
    return accs, analyses


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument("--ips", required=True, help="InterProScan TSV (-f tsv, run with -iprlookup)")
    ap.add_argument("--out", required=True, help="output nlr_candidates.tsv")
    a = ap.parse_args(argv)
    try:
        accs, analyses = read_ips(a.ips)
    except FileNotFoundError:
        print(f"[ERR] InterProScan TSV not found: {a.ips} (run pipeline/F3_interproscan.sh first)",
              file=sys.stderr)
        return 1
    rows = []
    for pid in sorted(accs):
        res = classify(accs[pid], analyses[pid])
        if res is None:
            continue
        cls, nterm, lrr = res
        keep = accs[pid] & (NBARC | TIR | RPW8 | CC | LRR)
        if nterm == "CC" and not accs[pid] & CC:
            keep = keep | {"Coils"}
        rows.append([pid, cls, nterm or "-", "yes" if lrr else "no", ";".join(sorted(keep))])
    with open(a.out, "w", newline="") as fo:
        w = csv.writer(fo, delimiter="\t", lineterminator="\n")
        w.writerow(COLUMNS)
        w.writerows(rows)
    counts = defaultdict(int)
    for r in rows:
        counts[r[1]] += 1
    summary = " ".join(f"{k}={counts[k]}" for k in sorted(counts)) or "none"
    print(f"[OK] {len(rows)} NB-ARC proteins ({summary}) -> {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
