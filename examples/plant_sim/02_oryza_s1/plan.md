# Function flow plan — Oryza_sativa_sim

Generated: 2026-09-16 01:30 UTC

## Chooser decision

> **Numbering legend:** **Frame** F1/F2/… = annotation strategy; script names like `F2_eggnog.sh` = historical step files inside frame F1; checklist **Gate-*** = release pass/fail (see `docs/zh/FAQ_入门.md`).

- **Frame:** `F1`
- **Add-ons:** (none)
- **Target grade:** `F-L1`
- **Reason:** Default paper frame: DIAMOND + eggNOG + InterProScan.
- **Protein provenance:** Oryza_sim.v0.1
- **structure_grade (self-declared):** L1

---

## Narrated stages

### 1. F0 — Protein-set sanity (BUSCO)

**Input:** PROTEINS_FA from structure release

**Software & purpose:** BUSCO protein mode — sanity brake before expensive IPS.

**Process:** Record Completeness + lineage; if catastrophic, return to structure.

**Output:** qc/ BUSCO summary

**Helper:** `docs/FUNCTIONAL_GUIDE.md`

### 2. F1a — DIAMOND Swiss-Prot

**Input:** PROTEINS_FA + DIAMOND_DB

**Software & purpose:** DIAMOND blastp vs Swiss-Prot — curated homology names/hits.

**Process:** Sensitive search; keep TSV.

**Output:** function/diamond/

**Helper:** `pipeline/F1_diamond.sh`

```bash
# Print-first: DRY-run first; set RUN=1 only after review (see script header).
bash pipeline/F1_diamond.sh
```

### 3. F1b — eggNOG-mapper

**Input:** PROTEINS_FA

**Software & purpose:** emapper — orthology-aware GO/KEGG/COG transfer (match DB↔mapper version).

**Process:** Run with EGGNOG_TAX_SCOPE for your clade.

**Output:** function/emapper/

**Helper:** `pipeline/F2_eggnog.sh`

**Also see:** Script name F2_* = frame F1 step 2; not fast-frame F2

```bash
# Print-first: DRY-run first; set RUN=1 only after review (see script header).
bash pipeline/F2_eggnog.sh
```

### 4. F1c — InterProScan

**Input:** PROTEINS_FA

**Software & purpose:** InterProScan — domains, sites, member-DB signatures.

**Process:** CPU-heavy; batch if needed.

**Output:** function/interpro/

**Helper:** `pipeline/F3_interproscan.sh`

```bash
# Print-first: DRY-run first; set RUN=1 only after review (see script header).
bash pipeline/F3_interproscan.sh
```

### 5. merge — Merge → master TSV

**Input:** Per-tool tables

**Software & purpose:** F_merge_tables.py — gene-centric join.

**Process:** Require row count ≈ proteins; document drops.

**Output:** function/merge/functional_master.tsv

**Helper:** `pipeline/F_merge_tables.py`

### 6. release — Package FA release

**Input:** master TSV + proteins + METHODS

**Software & purpose:** F_release.sh

**Process:** Tick docs/EVALUATION.md F-L0/F-L1 gates.

**Output:** function/release/<TAG>/

**Helper:** `pipeline/F_release.sh`

```bash
# Print-first: DRY-run first; set RUN=1 only after review (see script header).
bash pipeline/F_release.sh
```

---

## After this plan

1. Copy `config/example.env` → `config/local.env` (PROTEINS_FA, DIAMOND_DB, EGGNOG_*, INTERPROSCAN_HOME).
2. Tick `docs/EVALUATION_CHECKLIST.md` (Chinese: `docs/zh/验收勾选表.md`).
3. Optional: `python3 pipeline/print_qc_commands.py`.
4. Print-first helpers: `F1_diamond.sh` → `F2_eggnog.sh` (= F1 eggNOG step) → `F3_interproscan.sh` → merge.
5. Add-ons (AHRD/F4, …) appear **only** when the matching `want_*` flag is true (default `want_ahrd: false` → Add-ons:(none)). F1 spine alone can still be F-L1; METHODS: say which add-ons you skipped.

See docs/ROADMAP.md · docs/zh/FAQ_入门.md. Step-1 tool = plan + explain only.
