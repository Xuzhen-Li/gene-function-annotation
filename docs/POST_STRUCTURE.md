# After structure — function one-pager

You already have a **structure release** (`proteins.faa` + `RELEASE_TAG` or hash). This repo only labels proteins.

```text
proteins in → DB checklist → F1 → merge → release
```

| Step | Done when | Open |
|------|-----------|------|
| **1. Proteins in** | Stable `PROTEINS_FA` from structure `release/<TAG>/` (one rep/gene); provenance recorded | [`HANDOFF_STRUCTURE_TO_FUNCTION.md`](HANDOFF_STRUCTURE_TO_FUNCTION.md) · Upstream [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation) · [`START_HERE.md`](START_HERE.md) |
| **2. DB checklist** | Swiss-Prot DIAMOND + eggNOG data + InterProScan paths real; disk budget OK | [`DB_INSTALL_CHECKLIST.md`](DB_INSTALL_CHECKLIST.md) · [`INSTALL_FUNCTIONAL.md`](INSTALL_FUNCTIONAL.md) |
| **3. F0 → F1** | Protein BUSCO sanity → DIAMOND + eggNOG + InterProScan (framework **F1**) | [`ROADMAP.md`](ROADMAP.md) · [`QUICKSTART.md`](QUICKSTART.md) · `pipeline/flow_tool/` |
| **4. Merge → release** | `functional_master.tsv` + `function/release/<TAG>/` + METHODS; tick F-L* | [`EVALUATION_CHECKLIST.md`](EVALUATION_CHECKLIST.md) · [`EVALUATION.md`](EVALUATION.md) · [`METHODS_FUNCTIONAL.md`](METHODS_FUNCTIONAL.md) |

**Classroom / print-first:** `flow.py` → `my_fa_plan.md` (± DB path list) is enough tonight. Full IPS is not the classroom deliverable.

**Hard stops:** empty / placeholder `PROTEINS_FA` → fix structure first. Unmatched eggNOG data vs emapper major → no F-L1 claim. `print_qc` `[STOP]` → no cluster.

Wiki: [Spine-F1](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Spine-F1) · [Evaluate-release](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Evaluate-release)
