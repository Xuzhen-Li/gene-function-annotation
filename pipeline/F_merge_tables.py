#!/usr/bin/env python3
"""DEPRECATED thin wrapper around pipeline/F_aggregate.py (the primary merge step).

Kept so that older command lines still work:
  python3 pipeline/F_merge_tables.py --proteins P.faa [--emapper E] [--ips I] \
      [--diamond SWISSPROT.tsv] --out merged_function_table.tsv
Option mapping: --diamond -> --diamond-swissprot; --proteins, --emapper, --ips, --out
unchanged. Any other option (e.g. --db-version, --kofam, --diamond-trembl) is passed
through to F_aggregate.py unchanged. Output columns are the F_aggregate.py columns.
Every input is optional except --proteins and --out; a path that is given but missing
stops with a one-line [ERR] (no traceback).
New commands should call F_aggregate.py directly (docs/steps/functional/F_AGGREGATE.md).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import F_aggregate  # noqa: E402

LEGACY = (
    ("proteins", "--proteins", None),
    ("emapper", "--emapper", "eggNOG-mapper"),
    ("ips", "--ips", "InterProScan"),
    ("diamond", "--diamond", "DIAMOND"),
)


def build_argv(argv: list[str] | None = None) -> tuple[list[str] | None, list[str]]:
    """Translate legacy options. Returns (F_aggregate argv or None, error lines)."""
    ap = argparse.ArgumentParser(
        description="DEPRECATED: use pipeline/F_aggregate.py. Legacy options are translated; "
                    "unknown options are passed through to F_aggregate.py.")
    ap.add_argument("--proteins", required=True)
    ap.add_argument("--emapper", action="append", default=[])
    ap.add_argument("--ips", action="append", default=[])
    ap.add_argument("--diamond", action="append", default=[],
                    help="DIAMOND outfmt 6 vs Swiss-Prot (-> --diamond-swissprot)")
    ap.add_argument("--out", required=True)
    a, rest = ap.parse_known_args(argv)
    errs = F_aggregate.missing_inputs(a, LEGACY)
    if errs:
        return None, errs
    out = ["--proteins", a.proteins, "--out", a.out]
    for p in a.emapper:
        out += ["--emapper", p]
    for p in a.ips:
        out += ["--ips", p]
    for p in a.diamond:
        out += ["--diamond-swissprot", p]
    return out + rest, []


def main(argv: list[str] | None = None) -> int:
    print("[DEPRECATED] F_merge_tables.py now calls F_aggregate.py; "
          "switch to: python3 pipeline/F_aggregate.py ...", file=sys.stderr)
    new, errs = build_argv(argv)
    if errs:
        print("\n".join(errs), file=sys.stderr)
        return 1
    return F_aggregate.main(new)


if __name__ == "__main__":
    raise SystemExit(main())
