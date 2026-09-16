#!/usr/bin/env python3
"""flow.py — Step-1 flow tool for gene-function-annotation."""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

try:
    import yaml
except ImportError:
    yaml = None


def load_answers(path: Path) -> dict:
    text = path.read_text()
    if yaml is not None:
        data = yaml.safe_load(text)
    else:
        data = {}
        for line in text.splitlines():
            s = line.split("#", 1)[0].strip()
            if not s or ":" not in s:
                continue
            k, v = s.split(":", 1)
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if v.lower() in ("true", "yes"):
                v = True
            elif v.lower() in ("false", "no"):
                v = False
            data[k] = v
    return data


def choose_frame(a: dict) -> dict:
    if not a.get("proteins_ready", True):
        return {
            "frame": None,
            "grade": "blocked",
            "reason": "Proteins not ready — finish gene-structure-annotation first.",
            "addons": [],
        }
    structure_l0 = str(a.get("structure_grade", "L1")).upper() == "L0"
    if structure_l0:
        grade = "F-L0"
    else:
        grade = "F-L1"

    if a.get("transcriptome_only"):
        frame, reason = "F5", "Transcriptome CDS → Trinotate (± F1 on peptides)."
    elif a.get("use_entap"):
        frame, reason = "F3", "EnTAP-centric lab frame."
    elif a.get("prefer_fast"):
        frame, reason = "F2", "Fast emapper (± optional Kofam F1+); IPS deferred; grade capped at F-L0."
        grade = "F-L0"
    else:
        frame, reason = "F1", "Default paper frame: DIAMOND + eggNOG + InterProScan."

    if structure_l0 and "grade capped" not in reason:
        reason = reason.rstrip(".") + "; grade capped at F-L0 (structure L0)."

    addons = []
    if a.get("want_ahrd"):
        addons.append("F4")
    if a.get("want_mercator"):
        addons.append("F6")
    if a.get("want_orthofinder"):
        addons.append("F7")
    if a.get("want_nlr"):
        addons.append("F8")
    if a.get("want_itak"):
        addons.append("F9")

    return {"frame": frame, "grade": grade, "reason": reason, "addons": addons}


def stages_for(choice: dict, a: dict) -> list[dict]:
    if choice["frame"] is None:
        return [
            {
                "id": "blocked",
                "title": "Upstream structure required",
                "inputs": "None yet",
                "software": "gene-structure-annotation flow tool",
                "process": "Run structure plan to L1/L2; export proteins.faa.",
                "outputs": "PROTEINS_FA with RELEASE_TAG",
                "helper": "https://github.com/Xuzhen-Li/gene-structure-annotation",
            }
        ]
    stages = []

    def add(sid, title, inputs, software, process, outputs, helper="", note="", emit=""):
        # helper = one path; note = extra docs; emit = optional full command for --emit-commands
        stages.append(dict(id=sid, title=title, inputs=inputs, software=software, process=process, outputs=outputs, helper=helper, note=note, emit=emit))

    add(
        "F0",
        "Protein-set sanity (BUSCO)",
        "PROTEINS_FA from structure release",
        "BUSCO protein mode — sanity brake before expensive IPS.",
        "Record Completeness + lineage; if catastrophic, return to structure.",
        "qc/ BUSCO summary",
        "docs/FUNCTIONAL_GUIDE.md",
    )

    fr = choice["frame"]
    if fr == "F1":
        add("F1a", "DIAMOND Swiss-Prot", "PROTEINS_FA + DIAMOND_DB", "DIAMOND blastp vs Swiss-Prot — curated homology names/hits.", "Sensitive search; keep TSV.", "function/diamond/", "pipeline/F1_diamond.sh")
        add("F1b", "eggNOG-mapper", "PROTEINS_FA", "emapper — orthology-aware GO/KEGG/COG transfer (match DB↔mapper version).", "Run with EGGNOG_TAX_SCOPE for your clade.", "function/emapper/", "pipeline/F2_eggnog.sh", "Script name F2_* = frame F1 step 2; not fast-frame F2")
        add("F1c", "InterProScan", "PROTEINS_FA", "InterProScan — domains, sites, member-DB signatures.", "CPU-heavy; batch if needed.", "function/interpro/", "pipeline/F3_interproscan.sh")
    elif fr == "F2":
        add("F2", "Fast emapper frame", "PROTEINS_FA", "eggNOG-mapper (± optional Kofam F1+)", "Skip or defer IPS; grade capped at F-L0.", "function/emapper/", "pipeline/F2_eggnog.sh")
    elif fr == "F3":
        add("F3", "EnTAP frame", "PROTEINS_FA / transcriptome", "EnTAP (DIAMOND + emapper ± IPS inside EnTAP)", "Follow EnTAP docs; copy tables into merge layout.", "EnTAP out → merge/", "docs/tools/entap.md")
    elif fr == "F5":
        add("F5", "Trinotate transcriptome frame", "Trinity CDS/peptides", "Trinotate", "Transcriptome FA; optional still run F1 on peptides.", "Trinotate report", "docs/tools/trinotate.md")

    add(
        "merge",
        "Merge → master TSV",
        "Per-tool F1 tables (DIAMOND / eggNOG / IPS)",
        "F_merge_tables.py — gene-centric join.",
        "Require row count ≈ proteins; document drops. Run this before Mercator ingest / AHRD join.",
        "function/merge/functional_master.tsv",
        "pipeline/F_merge_tables.py",
    )

    # Add-ons AFTER merge when they join/ingest onto master (F4/F6) or consume F1 outputs
    for ad in choice["addons"]:
        if ad == "F4":
            add(
                "F4",
                "AHRD readable names",
                "functional_master.tsv + DIAMOND/blast tables",
                "AHRD — human-readable gene names for papers.",
                "Join into master via F4_join_ahrd.py (after merge).",
                "AHRD-enriched table",
                "pipeline/F4_run_ahrd.md",
            )
        elif ad == "F6":
            add(
                "F6",
                "Mercator4 MapMan BINs (ingest)",
                "functional_master.tsv + Mercator result dir",
                "Mercator4 web job can run in parallel with F1; ingest must be AFTER merge.",
                "Unpack results under $FUNCTION_DIR/mercator/; then "
                "python3 pipeline/F6_ingest_mercator.py --mercator-dir $FUNCTION_DIR/mercator "
                "--master $FUNCTION_DIR/merge/functional_master.tsv --out …",
                "master + mapman_bin (or with_mapman table)",
                "pipeline/F6_ingest_mercator.py",
                "docs/tools/mercator.md · docs/FUNCTIONAL_GUIDE.md F6",
                'python3 pipeline/F6_ingest_mercator.py --mercator-dir "$FUNCTION_DIR/mercator" '
                '--master "$FUNCTION_DIR/merge/functional_master.tsv" '
                '--out "$FUNCTION_DIR/merge/functional_master.with_mapman.tsv"',
            )
        elif ad == "F7":
            add("F7", "OrthoFinder then FA on reps", "Multi-genome proteins", "OrthoFinder", "Pick representatives; re-enter F1 on reps.", "orthogroups + reps", "pipeline/F7_orthofinder.sh")
        elif ad == "F8":
            add("F8", "NLR census", "IPS TSV", "IPS filter ± HRP", "Plant resistance-gene list (can run after IPS; often after merge for release).", "NLR list", "pipeline/F8_run.sh")
        elif ad == "F9":
            add("F9", "iTAK TF/kinase", "PROTEINS_FA", "iTAK", "Plant TF/kinase classification.", "iTAK table", "pipeline/F9_itak.sh")

    add(
        "release",
        "Package FA release",
        "master TSV (± MapMan/AHRD) + proteins + METHODS",
        "F_release.sh",
        "Tick docs/EVALUATION.md F-L0/F-L1 gates. If Mercator ran, prefer the with_mapman master for release.",
        "function/release/<TAG>/",
        "pipeline/F_release.sh",
    )
    return stages


def render(a, choice, stages, emit_commands: bool) -> str:
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        f"# Function flow plan — {a.get('species_label', 'run')}",
        "",
        f"Generated: {now}",
        "",
        "## Chooser decision",
        "",
        "> **Numbering legend:** **Frame** F1/F2/… = annotation strategy; script names like `F2_eggnog.sh` = historical step files inside frame F1; checklist **Gate-*** = release pass/fail (see `docs/zh/FAQ_入门.md`).",
        "",
        f"- **Frame:** `{choice['frame']}`",
        f"- **Add-ons:** {', '.join(choice['addons']) if choice['addons'] else '(none)'}"
        + (" — optional modules, NOT F-L1 hard gates" if choice.get("addons") else ""),
        f"- **Target grade:** `{choice['grade']}`",
        f"- **Reason:** {choice['reason']}",
        f"- **Protein provenance:** {a.get('proteins_provenance', '(set me)')}",
        f"- **structure_grade (self-declared):** {a.get('structure_grade', '(unset)')}",
        "",
        "---",
        "",
        "## Narrated stages",
        "",
    ]

    # Placeholder / grade warnings for learners
    try:
        dash = lines.index("---")
    except ValueError:
        dash = None
    if dash is not None:
        prov = str(a.get("proteins_provenance", ""))
        warns = []
        if ("or path/hash" in prov) or ("RELEASE_TAG or" in prov) or ("(set me)" in prov) or (not prov.strip()):
            warns.append(
                "> **Warning:** `proteins_provenance` still looks like a placeholder — "
                "replace with a real structure RELEASE_TAG or path/sha256 before claiming F-L1."
            )
        if str(a.get("structure_grade", "")).upper() == "L0" and choice.get("grade") == "F-L1":
            warns.append(
                "> **Warning:** structure_grade is L0 but target is F-L1 — keep FA provisional / F-L0 until structure is L1."
            )
        for w in reversed(warns):
            lines.insert(dash, "")
            lines.insert(dash, w)

    for i, st in enumerate(stages, 1):
        lines += [
            f"### {i}. {st['id']} — {st['title']}",
            "",
            f"**Input:** {st['inputs']}",
            "",
            f"**Software & purpose:** {st['software']}",
            "",
            f"**Process:** {st['process']}",
            "",
            f"**Output:** {st['outputs']}",
            "",
        ]
        h = str(st.get("helper") or "").strip()
        note = str(st.get("note") or "").strip()
        if h:
            lines.append(f"**Helper:** `{h}`")
            lines.append("")
        if note:
            lines.append(f"**Also see:** {note}")
            lines.append("")
        emit_cmd = str(st.get("emit") or "").strip()
        if emit_commands and emit_cmd:
            lines += [
                "```bash",
                "# Print-first: review before running on cluster.",
                emit_cmd,
                "```",
                "",
            ]
        elif emit_commands and h.endswith(".sh"):
            hp = REPO / h
            if hp.is_file():
                lines += [
                    "```bash",
                    "# Print-first: DRY-run first; set RUN=1 only after review (see script header).",
                    f"bash {h}",
                    "```",
                    "",
                ]
            else:
                lines += [f"> **emit skipped:** `{h}` not found under repo root.", ""]
    lines += [
        "---",
        "",
        "## After this plan",
        "",
        "1. Copy `config/example.env` → `config/local.env` (PROTEINS_FA, DIAMOND_DB, EGGNOG_*, INTERPROSCAN_HOME).",
        "2. Tick `docs/EVALUATION_CHECKLIST.md` (Chinese: `docs/zh/验收勾选表.md`).",
        "3. Optional: `python3 pipeline/print_qc_commands.py`.",
        "4. Print-first helpers: `F1_diamond.sh` → `F2_eggnog.sh` (= F1 eggNOG step) → `F3_interproscan.sh` → merge.",
        "5. Add-ons (AHRD/F4, …) appear **only** when the matching `want_*` flag is true (default `want_ahrd: false` → Add-ons:(none)). F1 spine alone can still be F-L1; METHODS: say which add-ons you skipped.",
        "",
        "See docs/ROADMAP.md · docs/zh/FAQ_入门.md. Step-1 tool = plan + explain only.",
        "",
    ]
    return "\n".join(lines)


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--answers", type=Path, required=True)
    p.add_argument("-o", "--output", type=Path)
    p.add_argument("--emit-commands", action="store_true")
    args = p.parse_args(argv)
    a = load_answers(args.answers)
    choice = choose_frame(a)
    stages = stages_for(choice, a)
    md = render(a, choice, stages, args.emit_commands)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(md)
        print(f"Wrote {args.output}", file=sys.stderr)
    print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
