# Branch roadmap — gene function

One page: **mandatory trunk**, **alternate frames**, **optional plant add-ons**.  
Process map: [`steps/FUNCTIONAL_MAIN.md`](steps/FUNCTIONAL_MAIN.md) · recipes: [`SCENARIOS_FUNCTIONAL.md`](SCENARIOS_FUNCTIONAL.md).

Upstream structure roadmap: [gene-structure-annotation `ROADMAP`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/ROADMAP.md).

---

## Big picture (second layer only)

```text
qualified proteins.faa  (+ optional curated GFF)
        │
        ▼
┌───────────────────────────────┐
│  gene-function-annotation     │  ← this repo
│  F0 → F1 (default)            │
│  → optional add-ons           │
│  → functional_master.tsv      │
│  → release/<TAG>/             │
└───────────────────────────────┘
```

No genome assembly, BRAKER, or EVM here. If you still need gene models, finish [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation) first.

---

## Trunk (default paper path)

```text
PROTEINS_FA
  │
F0    protein BUSCO (sanity; fix structure upstream if catastrophic)
  │
F1    DIAMOND Swiss-Prot  +  eggNOG-mapper  +  InterProScan
  │         (runners: F1_diamond.sh · F2_eggnog.sh · F3_interproscan.sh)
  │
      optional add-ons (F4 / F6 / F7 / F8 / F9) — see below
  │
merge F_merge_tables.py  →  function/merge/functional_master.tsv
  │
pack  F_release.sh       →  function/release/<TAG>/
```

**Always:** F0 → F1 → merge → release.  
**Default if unsure:** F1 only (skip plant add-ons).

---

## A. Alternate frames — pick **instead of** full F1 (or as a slim path)

These change *how* the main homology/domain tables are produced. Still rejoin at merge/release.

| ID | When | Core | Notes |
|----|------|------|-------|
| **F1** | Default / paper | DIAMOND + eggNOG + InterProScan | Preferred METHODS spine |
| **F2** | Fast / lightweight | eggNOG (± optional Kofam **F1+**) | Skip or defer InterProScan |
| **F3** | EnTAP-centric lab | EnTAP → copy TSVs into merge | Docs-driven; not a full runner rewrite |
| **F5** | Transcriptome CDS (no genome GFF) | Trinotate (± still run F1 on peptides) | Not a plant-genome default |

```text
Chooser:
  Normal genome proteins, publication  → F1
  Need answers today, IPS too slow     → F2 now, IPS later into merge
  Lab standardized on EnTAP            → F3
  Trinity/transcriptome only           → F5
```

---

## B. Optional add-ons — **after** F1 (or after an alternate frame)

Never replace F1 as the gene-centric master without a documented reason.

| ID | When | Product | Runner |
|----|------|---------|--------|
| **F4** | Readable gene names | AHRD names joined | `F4_run_ahrd.md` · `F4_join_ahrd.py` (± PANNZER `F4b`) |
| **F6** | Plant MapMan BINs | Mercator4 ingest | `F6_ingest_mercator.py` |
| **F7** | Multi-genome orthologs first | OrthoFinder reps → then F1 | `F7_orthofinder.sh` |
| **F8** | Plant NLR candidates / screen | IPS filter ± HRP | `F8_run.sh` |
| **F9** | Plant TF / kinase | iTAK | `F9_itak.sh` |

```text
Default (any clade):   F0 → frame F1 → merge → release
Plant paper (pick):    F1 required; then F4 / F6 / F8 / F9 only if that figure or species needs them
  — F8 = NLR candidates/screen, not a curated NLR set; skip if no disease/NLR story
  — F4/F6/F9 likewise optional — not a higher F-L grade by themselves
Multi-genome panel:    F7 → F1 on representatives → merge
```

Do **not** treat AHRD+Mercator+NLR+iTAK as a plant-genome checklist. `cases/` and grape examples are illustrations, not the only L2/F-L1 template.

---

## C. What is **not** an F-branch

| Need | Where |
|------|--------|
| Soft-mask / BRAKER / liftover / GSAman | [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation) |
| TE curatedlib | structure `TE_LIBRARY` · [vitis-te](https://github.com/Xuzhen-Li/vitis-te) |
| Writing GO into GFF column 9 | Not claimed yet — master TSV is source of truth |

---

## ID cheat sheet

| Kind | IDs |
|------|-----|
| Trunk | F0, F1, merge, release |
| Alternate frame | F2, F3, F5 |
| Optional add-on | F4, F6, F7, F8, F9 |

Naming quirk (historical): script `F2_eggnog.sh` is the **eggNOG step inside F1**, and also the core of the **F2** fast frame. Same binary, two roles — see [`FUNCTIONAL_GUIDE.md`](FUNCTIONAL_GUIDE.md).

---

## Quick links

| Doc | Use |
|-----|-----|
| [`QUICKSTART.md`](QUICKSTART.md) | Run F1 once |
| [`STAGE_IO.md`](STAGE_IO.md) | Inputs → products |
| [`EVALUATION.md`](EVALUATION.md) | **Final** F-L0/F-L1 criteria |
| [`PLAYBOOK.md`](PLAYBOOK.md) | Short FA checklist |
| [`SCENARIOS_FUNCTIONAL.md`](SCENARIOS_FUNCTIONAL.md) | Situation recipes |
| [`INSTALL_FUNCTIONAL.md`](INSTALL_FUNCTIONAL.md) | DBs / tools |
| [`DB_INSTALL_CHECKLIST.md`](DB_INSTALL_CHECKLIST.md) | F1 DB tick list + disk / METHODS fields |
| [`POST_STRUCTURE.md`](POST_STRUCTURE.md) | One-page proteins → DB → F1 → release |
| [`SELF_AUDIT.md`](SELF_AUDIT.md) | 2026-09-14 lit/peer gap table |
| [`RECENT_HIGH_QUALITY.md`](RECENT_HIGH_QUALITY.md) | Allowlisted FA standards |
