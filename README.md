# gene-function-annotation

[![Stars](https://img.shields.io/github/stars/Xuzhen-Li/gene-function-annotation?style=flat-square)](https://github.com/Xuzhen-Li/gene-function-annotation/stargazers)
[![Forks](https://img.shields.io/github/forks/Xuzhen-Li/gene-function-annotation?style=flat-square)](https://github.com/Xuzhen-Li/gene-function-annotation/network/members)
[![Last commit](https://img.shields.io/github/last-commit/Xuzhen-Li/gene-function-annotation?style=flat-square)](https://github.com/Xuzhen-Li/gene-function-annotation/commits/main)
[![Issues](https://img.shields.io/github/issues/Xuzhen-Li/gene-function-annotation?style=flat-square)](https://github.com/Xuzhen-Li/gene-function-annotation/issues)
[![Sibling: structure](https://img.shields.io/badge/sibling-gene--structure--annotation-1565C0?style=flat-square)](https://github.com/Xuzhen-Li/gene-structure-annotation)
[![Project](https://img.shields.io/badge/Project-structure→function-informational?style=flat-square)](https://github.com/users/Xuzhen-Li/projects/2)

> **中文教学：** [`docs/zh/`](docs/zh/)（是什么 / 与结构的关系 / 怎么跑 / F线）  
> **English ops:** [`docs/BILINGUAL.md`](docs/BILINGUAL.md)  
> **Plant sims (3):** [`examples/plant_sim/`](examples/plant_sim/) — paired with structure (Vitis+NLR / Oryza plain F1 / Solanum+Mercator).


---

## What this repo is

**Label proteins** — names, GO/KEGG-ish maps, domains — **after** a structure release exists.

This repo **starts after** structure ships `proteins.faa`.  
**No** BRAKER / soft-mask / GFF editing / gene finding here.

```text
proteins.faa  (from structure release)
        ↓
 F0 QC → F1 (DIAMOND + eggNOG + InterProScan) → merge
        ↓
  functional_master.tsv  +  release/<TAG>/
```

Upstream gene models: [`gene-structure-annotation`](https://github.com/Xuzhen-Li/gene-structure-annotation)  
(three-layer boundary: [structure `docs/BOUNDARY.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/BOUNDARY.md)).  
TE soft-mask and TE library build are **not** under function.

![Beginner spine](docs/figures/functional_spine.png)

Naming note: `pipeline/F2_eggnog.sh` is the **eggNOG step inside default F1**, not the fast-frame branch F2.

**One-glance tonight:** [Wiki Start-tonight](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Start-tonight) (GitHub Wiki — **not** in the clone) · offline [`docs/CLASSROOM_TONIGHT.md`](docs/CLASSROOM_TONIGHT.md).

**Track work:** [Annotation board (Project #2)](https://github.com/users/Xuzhen-Li/projects/2).

## F cheat (sticky — do not mix namespaces)

1. **Framework** F1 / F2 / F3 / F5 = which *whole* annotation frame you claim (default **F1** = DIAMOND+eggNOG+IPS).
2. **Script** `F2_eggnog.sh` = eggNOG *step inside* framework F1 — **not** frame F2.
3. **TOOLS** F1a / F1b / F1c = literacy cards for those three F1 steps.
4. **Gates** (`Gate-F1` …) = release hard checks — not a frame choice. Deep dive: [`docs/zh/FAQ_入门.md`](docs/zh/FAQ_入门.md).

## Three steps (start here)

### 1. You already have proteins

If not, finish structure first (its `flow_tool` → GFF + `proteins.faa`). Card: [`docs/HANDOFF_STRUCTURE_TO_FUNCTION.md`](docs/HANDOFF_STRUCTURE_TO_FUNCTION.md).

### 2. Auto-plan the FA frame

```bash
git clone https://github.com/Xuzhen-Li/gene-function-annotation.git
cd gene-function-annotation
cp pipeline/flow_tool/answers.example.yaml my_answers.yaml
# edit: prefer_fast? plant add-ons?
python3 pipeline/flow_tool/flow.py --answers my_answers.yaml -o my_fa_plan.md
```

### 3. Plan tonight; run when you have DBs + compute

| | |
|--|--|
| **Tonight (classroom)** | Finish `my_fa_plan.md` (± list DB disk paths). No InterProScan required. Oral check: [Wiki Concepts](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Concepts) **or** offline [`docs/zh/02_和结构注释的关系.md`](docs/zh/02_和结构注释的关系.md). Write `grade=` and `status=` separately — do **not** write `status=F-L1`. |
| **Later (cluster)** | Only after [Done when](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Start-tonight#done-when) is ticked **and** `python3 pipeline/print_qc_commands.py` exits 0 with **no** `[STOP]`. Otherwise **no** `RUN=1`. Browsing with `--env config/example.env` **will** show `[STOP]` — **expected**. METHODS required fields must be draftable ([Wiki Evaluate-release](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Evaluate-release)). |

Then [`docs/INSTALL_FUNCTIONAL.md`](docs/INSTALL_FUNCTIONAL.md) / [`docs/DB_INSTALL_CHECKLIST.md`](docs/DB_INSTALL_CHECKLIST.md) → `RUN=1` framework F1 → tick [`docs/EVALUATION_CHECKLIST.md`](docs/EVALUATION_CHECKLIST.md). **F-L1** is the acceptance *bar*, not “must finish IPS tonight.”

```bash
cp config/example.env config/local.env
# set PROTEINS_FA to your structure release proteins (one representative per gene)
# set DIAMOND_DB, EGGNOG_*, INTERPROSCAN_HOME, BUSCO_LINEAGE_PROTEIN, …
```

<details>
<summary>F numbering (one glance) — expand if namespaces collide</summary>

Four namespaces — do not mix them in speech or METHODS:

| Namespace | Examples | Means |
|-----------|----------|--------|
| **Framework** | F1 / F2 / F3 / F5 | Which whole annotation *frame* you claim (default **F1** = DIAMOND+eggNOG+IPS) |
| **Script filenames** | `F1_diamond.sh`, `F2_eggnog.sh`, `F3_interproscan.sh` | Steps *inside* framework F1 (historical names; **F2_eggnog ≠ framework F2**) |
| **TOOLS cards** | F1a / F1b / F1c | Same three steps as literacy pages (F1b = eggNOG) |
| **Gates** | Gate-F1 … Gate-F7 | Release hard checks (provenance, BUSCO, versions, row counts, …) |

Full Chinese cheat sheet: [`docs/zh/FAQ_入门.md`](docs/zh/FAQ_入门.md). Script renames to semantic names are backlog (②); until then, use this table.

</details>

---

## Docs (when needed)

Chinese teaching + start door: [`docs/zh/`](docs/zh/) · [`docs/START_HERE.md`](docs/START_HERE.md)

<details>
<summary>More docs</summary>

| Need | Open |
|------|------|
| Flow tool | [`pipeline/flow_tool/`](pipeline/flow_tool/) |
| Install · **Done?** | [`docs/INSTALL_FUNCTIONAL.md`](docs/INSTALL_FUNCTIONAL.md) · tick list [`docs/DB_INSTALL_CHECKLIST.md`](docs/DB_INSTALL_CHECKLIST.md) · [`docs/EVALUATION_CHECKLIST.md`](docs/EVALUATION_CHECKLIST.md) |
| **After structure (one-pager)** | [`docs/POST_STRUCTURE.md`](docs/POST_STRUCTURE.md) |
| Stage I/O · branch map | [`docs/STAGE_IO.md`](docs/STAGE_IO.md) · [`docs/ROADMAP.md`](docs/ROADMAP.md) |
| Tool how-tos | [`docs/TOOLS.md`](docs/TOOLS.md) · [`docs/tools/`](docs/tools/) |
| Full evaluation rules | [`docs/EVALUATION.md`](docs/EVALUATION.md) |
| QC methods / papers | [`docs/QUALITY_SOURCES.md`](docs/QUALITY_SOURCES.md) |
| Walkthrough | [`docs/QUICKSTART.md`](docs/QUICKSTART.md) |
| Mercator4 web — when (F6) | [`docs/MERCATOR_WHEN.md`](docs/MERCATOR_WHEN.md) |
| Tutorials · recent high-quality | [`docs/TUTORIALS_AND_MEETINGS.md`](docs/TUTORIALS_AND_MEETINGS.md) · [`docs/RECENT_HIGH_QUALITY.md`](docs/RECENT_HIGH_QUALITY.md) |

</details>

<details>
<summary>Advanced overview figure (optional)</summary>

![overview](docs/figures/functional_overview.png)

</details>

**Author:** Xuzhen Li · [ORCID](https://orcid.org/0000-0003-3670-6657)
