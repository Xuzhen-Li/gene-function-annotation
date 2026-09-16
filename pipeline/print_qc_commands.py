#!/usr/bin/env python3
"""Print recommended function QC / F0–F1 commands (print-first)."""
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


def g(env: dict[str, str], key: str, default: str = "") -> str:
    v = env.get(key, "").strip()
    return v if v else default


def is_placeholder(v: str) -> bool:
    if not v:
        return True
    low = v.lower()
    if "/path/to" in low or v.startswith("/path/"):
        return True
    if "your_" in low or "YOUR_" in v:
        return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--env", type=Path, default=None)
    ap.add_argument("--grade", choices=["F-L0", "F-L1"], default="F-L1")
    args = ap.parse_args()
    env = load_env(args.env)

    work = g(env, "WORK_DIR", "$WORK_DIR")
    proteins = g(env, "PROTEINS_FA", "$PROTEINS_FA")
    fun = g(env, "FUNCTION_DIR", f"{work}/function" if work and not work.startswith("$") else "$FUNCTION_DIR")
    lineage = g(env, "BUSCO_LINEAGE_PROTEIN", "")
    busco_out = g(env, "BUSCO_OUT", f"{fun}/qc/busco_prot")
    threads = g(env, "THREADS", "16")
    tag = g(env, "RELEASE_TAG", "fun_tag")
    release = f"{fun}/release/{tag}"
    diamond = g(env, "DIAMOND_DB", "$DIAMOND_DB")

    bad = []
    for label, val in [
        ("WORK_DIR", work),
        ("PROTEINS_FA", proteins),
        ("FUNCTION_DIR", fun),
        ("BUSCO_LINEAGE_PROTEIN", lineage),
        ("DIAMOND_DB", diamond),
    ]:
        if is_placeholder(val) or val.startswith("$"):
            bad.append(f"{label}={val or '(empty)'}")
    if lineage and re.search(r"(?i)^eukaryota", lineage):
        bad.append(f"BUSCO_LINEAGE_PROTEIN={lineage} (bare eukaryota anti-pattern)")

    print("# Function QC — print-first")
    print(f"# Target: {args.grade}  ·  docs/EVALUATION_CHECKLIST.md")
    print("# Bare bash pipeline/F*.sh without RUN=1 is DRY (may still refuse placeholders).")
    print()

    if bad:
        print("# [STOP] Placeholders / unset — do NOT paste mkdir/busco/F* RUN=1 yet:")
        for b in bad:
            print(f"#   - {b}")
        print("# Edit config/local.env to real paths + clade lineage, then re-run this printer.")
        print("# Gate-F1 reminder: PROTEINS_FA must be structure release/<TAG>/proteins.faa (or hash in METHODS)")
        print("# exit 1: fix local.env before treating this as a runnable QC plan")
        return 1

    print("## Pack smoke")
    print(f"python3 pipeline/check_release_pack.py {release}")
    print()
    print("## Gate-F1 — protein provenance")
    print(f"# PROTEINS_FA={proteins}")
    print()
    print("## Gate-F2 — F0 protein BUSCO")
    print(f"mkdir -p {busco_out}")
    print(f"busco -i {proteins} -l {lineage} -o $(basename {busco_out}) \\")
    print(f"  --out_path $(dirname {busco_out}) -m proteins -c {threads}")
    print()
    print("## Gate-F3 — framework F1 scripts")
    print(f"# DIAMOND_DB={diamond}")
    print("RUN=1 bash pipeline/F1_diamond.sh")
    print("RUN=1 bash pipeline/F2_eggnog.sh   # F1 inner step, not fast-frame F2")
    print("RUN=1 bash pipeline/F3_interproscan.sh")
    print('python3 pipeline/F_merge_tables.py \\')
    print(f'  --proteins "{proteins}" \\')
    print(f'  --emapper "{fun}/emapper/${{FUN_PREFIX:-ann}}_fun.emapper.annotations" \\')
    print(f'  --ips "{fun}/interpro/${{FUN_PREFIX:-ann}}_ips.tsv" \\')
    print(f'  --diamond "{fun}/diamond/swissprot.tsv" \\')
    print(f'  --out "{fun}/merge/functional_master.tsv"')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
