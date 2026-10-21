#!/usr/bin/env python3
"""Preflight check before RUN=1 (standard library only; runs nothing).

For one pipeline step it checks that:
  - required input files / folders exist (pipeline products of LATER steps are not required),
  - no value is still a placeholder (/path/to, YOUR_*, $(...), unset $VAR),
  - output paths can be created,
  - required tools are on PATH (shutil.which), or the container image is present,
  - values with a known fixed set (e.g. EGGNOG_PFAM_REALIGN) are valid.
Prints [PASS] / [STOP] / [WARN] lines and a next-step hint.
Exit 0 = PASS, 1 = STOP, 2 = usage error.

Usage:
  python3 pipeline/preflight.py --list
  python3 pipeline/preflight.py --env config/local.env --step diamond
  python3 pipeline/preflight.py --step eggnog --step interproscan     # default env: config/local.env

The env file is read directly, so `source` without `set -a` cannot hide values.
print_qc_commands.py stays a command printer; this script is the check before RUN=1.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENV = REPO_ROOT / "config" / "local.env"

# --------------------------------------------------------------------------
# env file
# --------------------------------------------------------------------------

_VAR_RE = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)(?::-([^}]*))?\}|\$([A-Za-z_][A-Za-z0-9_]*)")


def _strip_comment(value: str) -> str:
    out, quote = [], None
    for i, ch in enumerate(value):
        if quote:
            if ch == quote:
                quote = None
            out.append(ch)
        elif ch in "\"'":
            quote = ch
            out.append(ch)
        elif ch == "#" and (i == 0 or value[i - 1].isspace()):
            break
        else:
            out.append(ch)
    return "".join(out).strip()


def _unquote(v: str) -> tuple[str, bool]:
    """Return (value, single_quoted)."""
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1], v[0] == "'"
    return v, False


def load_env(path: Path | None, base: dict[str, str] | None = None) -> dict[str, str]:
    """Read KEY=VALUE lines like `set -a; source FILE` would, without running anything.

    ${VAR}, ${VAR:-default} and $VAR are expanded. $(...) is NOT run; it is left in the
    value so the check can report it.
    """
    env = dict(os.environ if base is None else base)
    if path is None:
        return env
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export "):].strip()
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)=(.*)$", line)
        if not m:
            continue
        key, value = m.group(1), _strip_comment(m.group(2))
        value, literal = _unquote(value)
        if not literal:
            def repl(mm: re.Match[str]) -> str:
                name = mm.group(1) or mm.group(3)
                if name in env and env[name] != "":
                    return env[name]
                if mm.group(2) is not None:
                    return mm.group(2)
                return mm.group(0)
            value = _VAR_RE.sub(repl, value)
        env[key] = value
    return env


def placeholder_reason(value: str) -> str | None:
    if value is None or value.strip() == "":
        return "empty"
    if "/path/to" in value or value.startswith("/path/"):
        return "still a /path/to placeholder"
    if "YOUR_" in value or "your_" in value.lower():
        return "still a YOUR_* placeholder"
    if "$(" in value or "`" in value:
        return "contains $(...); it is not evaluated here, write the real absolute path"
    if re.search(r"\$\{?[A-Za-z_]", value):
        return "contains an unset variable ($...)"
    if "\u2026" in value or value.strip() == "...":
        return "contains '...'"
    return None


# --------------------------------------------------------------------------
# step model
# --------------------------------------------------------------------------


@dataclass
class Tool:
    label: str
    any_of: list[str] = field(default_factory=list)      # names looked up on PATH
    path_keys: list[tuple[str, str]] = field(default_factory=list)  # (KEY, relative file)
    container_key: str = ""                               # KEY of a .sif image
    optional: bool = False


@dataclass
class Step:
    name: str
    script: str
    files: list[str] = field(default_factory=list)          # must exist as files
    dirs: list[str] = field(default_factory=list)           # must exist as folders
    outputs: list[str] = field(default_factory=list)        # set, not placeholder; may not exist yet
    optional_files: list[str] = field(default_factory=list)  # checked only when set
    optional_dirs: list[str] = field(default_factory=list)
    any_file: list[list[str]] = field(default_factory=list)  # at least one of these keys exists
    tools: list[Tool] = field(default_factory=list)
    extra: list = field(default_factory=list)              # callables(env, report)
    run: str = ""                                           # command to print on PASS


class Report:
    def __init__(self):
        self.lines: list[tuple[str, str]] = []

    def ok(self, msg):
        self.lines.append(("PASS", msg))

    def stop(self, msg):
        self.lines.append(("STOP", msg))

    def warn(self, msg):
        self.lines.append(("WARN", msg))

    @property
    def n_stop(self):
        return sum(k == "STOP" for k, _ in self.lines)


def _producer_hint(key: str) -> str:
    step = PRODUCED_BY.get(key)
    if not step:
        return ""
    if step not in STEPS:
        return f" ({step})"
    return f" (made by step '{step}': preflight --step {step}, then RUN=1 bash pipeline/{STEPS[step].script})"


def _value(env, key, report, required=True):
    val = env.get(key, "")
    why = placeholder_reason(val)
    if why:
        if required:
            report.stop(f"{key}: {why} -> edit config/local.env")
        return None
    return val


def check_step(step: Step, env: dict[str, str]) -> Report:
    r = Report()
    for key in step.files:
        val = _value(env, key, r)
        if val is None:
            continue
        p = Path(val)
        if p.is_file():
            r.ok(f"{key} exists: {val}")
        elif p.is_dir():
            r.stop(f"{key} is a folder, expected a file: {val}")
        else:
            r.stop(f"{key} not found: {val}{_producer_hint(key)}")
    for key in step.dirs:
        val = _value(env, key, r)
        if val is None:
            continue
        if Path(val).is_dir():
            r.ok(f"{key} folder exists: {val}")
        else:
            r.stop(f"{key} folder not found: {val}")
    for key in step.optional_files + step.optional_dirs:
        val = env.get(key, "")
        if val.strip() in ("", "none"):
            r.ok(f"{key} not set (optional)")
            continue
        why = placeholder_reason(val)
        want_dir = key in step.optional_dirs
        if why:
            r.stop(f"{key}: {why} -> set a real path or leave it empty")
        elif (Path(val).is_dir() if want_dir else Path(val).is_file()):
            r.ok(f"{key} exists: {val}")
        else:
            r.stop(f"{key} is set but not found: {val}")
    for keys in step.any_file:
        found = None
        for key in keys:
            val = env.get(key, "")
            if not placeholder_reason(val) and Path(val).is_file():
                found = (key, val)
                break
        if found:
            r.ok(f"input {found[0]} exists: {found[1]}")
        else:
            hints = "".join(_producer_hint(k) for k in keys[:1])
            r.stop(f"none of {', '.join(keys)} points to an existing file{hints}")
    for key in step.outputs:
        val = _value(env, key, r)
        if val is None:
            continue
        p = Path(val)
        parent = next((q for q in [p, *p.parents] if q.exists()), None)
        if parent is None or not os.access(parent, os.W_OK):
            r.stop(f"{key}: cannot create {val} (no writable parent folder)")
        else:
            r.ok(f"{key} can be written: {val}")
    for tool in step.tools:
        _check_tool(tool, env, r)
    for fn in step.extra:
        fn(env, r)
    return r


def _check_tool(tool: Tool, env, r: Report):
    for name in tool.any_of:
        hit = shutil.which(name)
        if hit:
            r.ok(f"tool {tool.label}: {hit}")
            return
    for key, rel in tool.path_keys:
        base = env.get(key, "")
        if base and not placeholder_reason(base):
            p = Path(base) / rel
            if p.is_file() and os.access(p, os.X_OK):
                r.ok(f"tool {tool.label}: {p}")
                return
    if tool.container_key:
        sif = env.get(tool.container_key, "")
        runner = shutil.which("apptainer") or shutil.which("singularity")
        if sif and not placeholder_reason(sif) and Path(sif).is_file() and runner:
            r.ok(f"tool {tool.label}: container {sif} via {runner}")
            return
    where = " or ".join(
        [f"'{n}' on PATH" for n in tool.any_of]
        + [f"{k}/{rel}" for k, rel in tool.path_keys]
        + ([f"{tool.container_key} (.sif) + apptainer/singularity"] if tool.container_key else []))
    msg = f"tool {tool.label} not found: need {where}"
    if tool.optional:
        r.warn(msg + " (optional)")
    else:
        r.stop(msg + " -> load the module / activate the env")


# --------------------------------------------------------------------------
# lineage checks
# --------------------------------------------------------------------------

KNOWN_BAD_LINEAGES = {
    "eudicots_odb12": "no such dataset; odb12 name is eudicotyledons_odb12 (odb10: eudicots_odb10)",
}


def busco_lineage_check(key: str):
    def fn(env, r: Report):
        val = env.get(key, "")
        why = placeholder_reason(val)
        if why:
            r.stop(f"{key}: {why} -> pick a clade lineage (check: busco --list-datasets)")
        elif val in KNOWN_BAD_LINEAGES:
            r.stop(f"{key}={val}: {KNOWN_BAD_LINEAGES[val]}")
        elif val.lower().startswith("eukaryota"):
            r.stop(f"{key}={val}: too broad -> set a clade lineage (busco --list-datasets)")
        elif not re.fullmatch(r"[a-z0-9_]+_odb\d+", val):
            if Path(val).is_dir():
                r.ok(f"{key} is a local lineage folder: {val}")
            else:
                r.stop(f"{key}={val}: expected a BUSCO name like embryophyta_odb12")
        else:
            r.ok(f"{key}={val} (confirm it is listed by: busco --list-datasets)")
    return fn


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Check inputs, paths and tools for one pipeline step before RUN=1.",
        epilog="Exit 0 = PASS, 1 = STOP, 2 = usage error. Steps: " + ", ".join(STEPS),
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--env", type=Path, default=None,
                    help="env file (default config/local.env when it exists)")
    ap.add_argument("--step", action="append", choices=list(STEPS), metavar="STEP",
                    help="step to check (repeatable): " + ", ".join(STEPS))
    ap.add_argument("--list", action="store_true", help="list steps and exit")
    a = ap.parse_args(argv)
    if a.list:
        for s in STEPS.values():
            print(f"{s.name:14s} pipeline/{s.script}")
        return 0
    if not a.step:
        ap.print_usage(sys.stderr)
        print("preflight: give --step (see --list)", file=sys.stderr)
        return 2
    env_path = a.env
    if env_path is None and DEFAULT_ENV.is_file():
        env_path = DEFAULT_ENV
    if env_path is not None and not env_path.is_file():
        print(f"[STOP] env file not found: {env_path} -> cp config/example.env config/local.env")
        return 1
    env = load_env(env_path)
    src = str(env_path) if env_path else "environment only (no config/local.env)"
    total_stop = 0
    for name in a.step:
        step = STEPS[name]
        print(f"== preflight step={name}  script=pipeline/{step.script}  env={src}")
        rep = check_step(step, env)
        for kind, msg in rep.lines:
            print(f"[{kind}] {msg}")
        total_stop += rep.n_stop
        if rep.n_stop:
            print(f"RESULT {name}: STOP ({rep.n_stop} to fix). Do not use RUN=1 yet.")
            print(f"  Fix the items above, then re-run: python3 pipeline/preflight.py"
                  f"{' --env ' + str(env_path) if env_path else ''} --step {name}")
        else:
            print(f"RESULT {name}: PASS. Next:")
            env_arg = str(env_path) if env_path else "config/local.env"
            print(f"  set -a && source {env_arg} && set +a")
            print(f"  {step.run or 'RUN=1 bash pipeline/' + step.script}")
        print()
    return 1 if total_stop else 0


# --------------------------------------------------------------------------
# steps of this repo
# --------------------------------------------------------------------------


def _fdir(env) -> str:
    f = env.get("FUNCTION_DIR", "")
    if f and not placeholder_reason(f):
        return f
    w = env.get("WORK_DIR", "")
    return f"{w}/function" if w and not placeholder_reason(w) else ""


def _prefix(env) -> str:
    return env.get("FUN_PREFIX", "").strip() or "ann"


def _proteins_from_release(env, r: Report):
    val = env.get("PROTEINS_FA", "")
    if val and not placeholder_reason(val) and "/release/" not in val:
        r.warn("PROTEINS_FA is not under a structure release/<TAG>/ folder; "
               "record its source and sha256 in METHODS (Gate-F1)")


def _pfam_realign(env, r: Report):
    val = env.get("EGGNOG_PFAM_REALIGN", "").strip()
    allowed = ("none", "realign", "denovo")
    if val in allowed:
        r.ok(f"EGGNOG_PFAM_REALIGN={val}")
    elif not val:
        r.stop("EGGNOG_PFAM_REALIGN not set: the script default 'realtime' is not accepted by "
               "emapper -> set EGGNOG_PFAM_REALIGN=none | realign | denovo in config/local.env")
    else:
        r.stop(f"EGGNOG_PFAM_REALIGN={val}: emapper accepts none | realign | denovo")


def _merge_inputs(env, r: Report):
    fd, pre = _fdir(env), _prefix(env)
    if not fd:
        r.stop("WORK_DIR / FUNCTION_DIR not set -> edit config/local.env")
        return
    paths = {
        "eggNOG": Path(fd) / "emapper" / f"{pre}_fun.emapper.annotations",
        "InterProScan": Path(fd) / "interpro" / f"{pre}_ips.tsv",
        "DIAMOND": Path(fd) / "diamond" / "swissprot.tsv",
    }
    found = 0
    for label, p in paths.items():
        if p.is_file():
            found += 1
            r.ok(f"{label} result exists: {p}")
        else:
            r.warn(f"{label} result not found: {p} (leave its flag out of the merge command)")
    if not found:
        r.stop("no eggNOG / InterProScan / DIAMOND result found -> run F1_diamond.sh, "
               "F2_eggnog.sh or F3_interproscan.sh first")


def _master_table(env, r: Report):
    fd = _fdir(env)
    tag = env.get("RELEASE_TAG", "")
    if placeholder_reason(tag):
        r.stop(f"RELEASE_TAG: {placeholder_reason(tag)} -> edit config/local.env")
    if not fd:
        r.stop("WORK_DIR / FUNCTION_DIR not set -> edit config/local.env")
        return
    hits = sorted((Path(fd) / "merge").glob("merged_function_table*.tsv"))
    if hits:
        r.ok(f"master table exists: {hits[0]}")
    else:
        r.stop(f"no merged_function_table*.tsv under {fd}/merge -> run step 'merge' first")


def _ips_tsv(env, r: Report):
    fd = _fdir(env)
    p = Path(fd) / "interpro" / f"{_prefix(env)}_ips.tsv" if fd else None
    if p and p.is_file():
        r.ok(f"InterProScan TSV exists: {p}")
    else:
        r.stop(f"InterProScan TSV not found: {p or '(FUNCTION_DIR unset)'} -> run F3_interproscan.sh first")


def _orthofinder_input(env, r: Report):
    fd = _fdir(env)
    d = Path(fd) / "orthofinder" / "input" if fd else None
    n = 0
    if d and d.is_dir():
        n = sum(1 for p in d.iterdir() if p.suffix in (".faa", ".fa", ".fasta"))
    if n >= 2:
        r.ok(f"{n} proteomes in {d}")
    else:
        r.stop(f"need at least 2 proteomes (*.faa) in {d or '$FUNCTION_DIR/orthofinder/input'}")


_MERGE_RUN = ('python3 pipeline/F_merge_tables.py --proteins "$PROTEINS_FA" '
              '--emapper "$FUNCTION_DIR/emapper/${FUN_PREFIX}_fun.emapper.annotations" '
              '--ips "$FUNCTION_DIR/interpro/${FUN_PREFIX}_ips.tsv" '
              '--diamond "$FUNCTION_DIR/diamond/swissprot.tsv" '
              '--out "$FUNCTION_DIR/merge/merged_function_table.tsv"')

STEPS: dict[str, Step] = {s.name: s for s in [
    Step("diamond", "F1_diamond.sh", files=["PROTEINS_FA", "DIAMOND_DB"], outputs=["WORK_DIR"],
         tools=[Tool("DIAMOND", ["diamond"])], extra=[_proteins_from_release]),
    Step("eggnog", "F2_eggnog.sh", files=["PROTEINS_FA"], optional_dirs=["EGGNOG_DATA_DIR"],
         outputs=["WORK_DIR"],
         tools=[Tool("eggNOG-mapper", ["emapper.py"], container_key="EGGNOG_SIF")],
         extra=[_proteins_from_release, _pfam_realign]),
    Step("interproscan", "F3_interproscan.sh", files=["PROTEINS_FA"], dirs=["INTERPROSCAN_HOME"],
         outputs=["WORK_DIR"],
         tools=[Tool("InterProScan", path_keys=[("INTERPROSCAN_HOME", "interproscan.sh")]),
                Tool("java", ["java"])],
         extra=[_proteins_from_release]),
    Step("kofam", "F1b_kofam.sh", files=["PROTEINS_FA", "KOFAM_KO_LIST"], dirs=["KOFAM_PROFILE_DIR"],
         outputs=["WORK_DIR"], tools=[Tool("KofamScan", ["exec_annotation"])]),
    Step("merge", "F_merge_tables.py", files=["PROTEINS_FA"], outputs=["WORK_DIR"],
         extra=[_merge_inputs], run=_MERGE_RUN + "   # drop flags whose result is missing"),
    Step("nlr", "F8_run.sh", dirs=["REPO_ROOT"], outputs=["WORK_DIR"], extra=[_ips_tsv],
         run="bash pipeline/F8_run.sh"),
    Step("orthofinder", "F7_orthofinder.sh", outputs=["WORK_DIR"],
         tools=[Tool("OrthoFinder", ["orthofinder"])], extra=[_orthofinder_input]),
    Step("itak", "F9_itak.sh", files=["PROTEINS_FA"], outputs=["WORK_DIR"],
         tools=[Tool("iTAK", ["iTAK", "itak"])]),
    Step("release", "F_release.sh", files=["PROTEINS_FA"], outputs=["WORK_DIR"],
         extra=[_master_table, _proteins_from_release],
         run="bash pipeline/F_release.sh   # no dry mode"),
]}

PRODUCED_BY = {"PROTEINS_FA": "made in gene-structure-annotation: release/<TAG>/proteins.faa"}


if __name__ == "__main__":
    sys.exit(main())
