#!/usr/bin/env python3
"""Print recommended function QC / F0–F1 commands (print-first).

Maps to docs/EVALUATION_CHECKLIST.md / docs/QUALITY_SOURCES.md.

Usage:
  set -a && source config/local.env && set +a
  python3 pipeline/print_qc_commands.py
  python3 pipeline/print_qc_commands.py --env config/example.env
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


def load_env(path: Path | None) -> dict[str, str]:
    env = dict(os.environ)
    if path is None:
        return env
    if not path.is_file():
        print(f"[WARN] env file not found: {path}", file=sys.stderr)
        return env
    for line in path.read_text().splitlines():
        s = line.split("#", 1)[0].strip()
        if not s or "=" not in s:
            continue
        k, v = s.split("=", 1)
        k = k.strip()
        v = v.strip().strip('"').strip("'")

        def repl(m: re.Match[str]) -> str:
            name = m.group(1) or m.group(2)
            return env.get(name, os.environ.get(name, m.group(0)))

        v = re.sub(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}|\$([A-Za-z_][A-Za-z0-9_]*)", repl, v)
        env[k] = v
    return env


def g(env: dict[str, str], key: str, default: str = "/path/to/…") -> str:
    v = env.get(key, "").strip()
    return v if v else default


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--env", type=Path, default=None)
    ap.add_argument("--grade", choices=["F-L0", "F-L1"], default="F-L1")
    args = ap.parse_args()
    env = load_env(args.env)

    work = g(env, "WORK_DIR", "$WORK_DIR")
    proteins = g(env, "PROTEINS_FA", "$PROTEINS_FA")
    fun = g(env, "FUNCTION_DIR", f"{work}/function")
    lineage = g(env, "BUSCO_LINEAGE_PROTEIN", "eukaryota_odb10")  # PLACEHOLDER — set YOUR lineage
    busco_out = g(env, "BUSCO_OUT", f"{fun}/qc/busco_prot")
    threads = g(env, "THREADS", "16")
    tag = g(env, "RELEASE_TAG", "fun_tag")
    release = f"{fun}/release/{tag}"
    diamond = g(env, "DIAMOND_DB", "$DIAMOND_DB")

    print("# Function QC — print-first")
    print(f"# Target: {args.grade}  ·  docs/EVALUATION_CHECKLIST.md")
    print("# Does not run DIAMOND/eggNOG/IPS for you — prints the spine.")
    print("# !!! MUST set YOUR BUSCO_LINEAGE_PROTEIN in local.env — default eukaryota_odb10 is a placeholder.")
    print()

    print("## Pack smoke")
    print(f"python3 pipeline/check_release_pack.py {release}")
    print()

    print("## Gate-F1 — protein provenance (hard)")
    print(f"# PROTEINS_FA={proteins}")
    print("# Confirm structure RELEASE_TAG or hash is in METHODS")
    print()

    print("## Gate-F2 — F0 protein BUSCO (hard)")
    print(f"mkdir -p {busco_out}")
    print(f"busco -i {proteins} -l {lineage} -o $(basename {busco_out}) \\")
    print(f"  --out_path $(dirname {busco_out}) -m proteins -c {threads}")
    print("# Record Completeness + lineage name; catastrophic → fix structure first")
    print()

    print("## Gate-F3 — F1 frame (hard) or waiver")
    print(f"# DIAMOND vs Swiss-Prot: DIAMOND_DB={diamond}")
    print("bash pipeline/F1_diamond.sh      # after sourcing local.env")
    print("bash pipeline/F2_eggnog.sh        # writes $FUNCTION_DIR/emapper/  (F1 step, not fast-frame F2)")
    print("# needs INTERPROSCAN_HOME=.../interproscan  (dir with interproscan.sh)")
    print("bash pipeline/F3_interproscan.sh")
    print('python3 pipeline/F_merge_tables.py \\')
    print(f'  --proteins "{proteins}" \\')
    print(f'  --emapper "{fun}/emapper/${{FUN_PREFIX:-ann}}_fun.emapper.annotations" \\')
    print(f'  --ips "{fun}/interpro/${{FUN_PREFIX:-ann}}_ips.tsv" \\')
    print(f'  --diamond "{fun}/diamond/swissprot.tsv" \\')
    print(f'  --out "{fun}/merge/functional_master.tsv"')
    print("# Or written waiver naming alternate frames F2/F3/F5")
    print()

    print("## Gate-F4–Gate-F6 — versions, master count, release")
    print("bash pipeline/F_release.sh")
    print("# METHODS: tool + DB versions (Gate-F4); master rows ≈ proteins (Gate-F5); release/<TAG>/ (Gate-F6)")
    print()

    print("## Gate-F7 — hygiene (hard, checklist)")
    print("# No private BAM/FASTQ / multi-GB DBs in release")
    print()
    print("## Soft")
    print("# Hit / domain coverage narrative (clade-aware)")
    print("# Domain-only vs GO-empty if relevant")
    print("# Shelf: docs/QUALITY_SOURCES.md")
    print()

    print("## Finish — tick docs/zh/验收勾选表.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
