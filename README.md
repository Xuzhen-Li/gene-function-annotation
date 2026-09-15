# gene-function-annotation

> **中文教学：** [`docs/zh/`](docs/zh/)（是什么 / 与结构的关系 / 怎么跑 / F线）  
> **English ops:** [`docs/BILINGUAL.md`](docs/BILINGUAL.md)

---

## What this repo is

**Label proteins** — names, GO/KEGG-ish maps, domains — **after** gene models exist.

```text
proteins.faa  (from structure release)
        ↓
 F0 QC → F1 (DIAMOND + eggNOG + InterProScan) → merge
        ↓
  functional_master.tsv  +  release/<TAG>/
```

**Not** gene finding / GFF editing — that is upstream  
[`gene-structure-annotation`](https://github.com/Xuzhen-Li/gene-structure-annotation).

---

## Three steps (start here)

### 1. You already have proteins

If not, finish structure first (its `flow_tool` → GFF + `proteins.faa`).

### 2. Auto-plan the FA frame

```bash
git clone https://github.com/Xuzhen-Li/gene-function-annotation.git
cd gene-function-annotation
cp pipeline/flow_tool/answers.example.yaml my_answers.yaml
# edit: prefer_fast? plant add-ons?
python3 pipeline/flow_tool/flow.py --answers my_answers.yaml -o my_fa_plan.md
```

### 3. Install DBs → run F1 → release

[`docs/INSTALL_FUNCTIONAL.md`](docs/INSTALL_FUNCTIONAL.md) → follow `my_fa_plan.md` →  
tick [`docs/EVALUATION_CHECKLIST.md`](docs/EVALUATION_CHECKLIST.md) (full rules: [`docs/EVALUATION.md`](docs/EVALUATION.md)). Default bar **F-L1**.

```bash
cp config/example.env config/local.env   # PROTEINS_FA, DIAMOND_DB, …
```

---

## Docs (when needed)

| Need | Open |
|------|------|
| Chinese teaching (short path first) | [`docs/zh/`](docs/zh/) |
| Flow tool | [`pipeline/flow_tool/`](pipeline/flow_tool/) |
| Install · **Done?** | [`docs/INSTALL_FUNCTIONAL.md`](docs/INSTALL_FUNCTIONAL.md) · [`docs/EVALUATION_CHECKLIST.md`](docs/EVALUATION_CHECKLIST.md) · [`docs/EVALUATION.md`](docs/EVALUATION.md) |
| QC methods / papers | [`docs/QUALITY_SOURCES.md`](docs/QUALITY_SOURCES.md) |
| Stage I/O · branch map | [`docs/STAGE_IO.md`](docs/STAGE_IO.md) · [`docs/ROADMAP.md`](docs/ROADMAP.md) |
| Walkthrough | [`docs/QUICKSTART.md`](docs/QUICKSTART.md) |

More: [`docs/TUTORIALS_AND_MEETINGS.md`](docs/TUTORIALS_AND_MEETINGS.md) · [`docs/RECENT_HIGH_QUALITY.md`](docs/RECENT_HIGH_QUALITY.md).

Figure: ![overview](docs/figures/functional_overview.png)

**Author:** Xuzhen Li · [ORCID](https://orcid.org/0000-0003-3670-6657)
