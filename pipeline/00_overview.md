# Pipeline overview — function layer only

This directory holds **F-line** runners for functional annotation. Structural soft-mask / draft / merge / GFF release scripts live in the sibling repo, not here.

## Docs (this repo)

1. **Functional main:** [`../docs/steps/FUNCTIONAL_MAIN.md`](../docs/steps/FUNCTIONAL_MAIN.md)
2. **Functional guide:** [`../docs/FUNCTIONAL_GUIDE.md`](../docs/FUNCTIONAL_GUIDE.md)
3. **F1–F9 situations:** [`../docs/SCENARIOS_FUNCTIONAL.md`](../docs/SCENARIOS_FUNCTIONAL.md)
4. **Quickstart / stage I/O:** [`../docs/QUICKSTART.md`](../docs/QUICKSTART.md) · [`../docs/STAGE_IO.md`](../docs/STAGE_IO.md)
5. **Install:** [`../docs/INSTALL_FUNCTIONAL.md`](../docs/INSTALL_FUNCTIONAL.md)
6. **AI co-pilot:** [`../docs/AI_ASSIST.md`](../docs/AI_ASSIST.md)

## Upstream structure

Finish a qualified GFF + `proteins.faa` in  
[gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation)  
([MAIN](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/steps/MAIN.md) · [QUICKSTART](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/QUICKSTART.md) · [PLAYBOOK](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/PLAYBOOK.md)),  
**or** bring your own release. Then set `PROTEINS_FA` and run **F1**.

## F-line scripts here

`F1_diamond.sh` · `F1b_kofam.sh` (F1+ optional KO) · `F2_eggnog.sh` · `F3_interproscan.sh` · `F4_*` · `F4b_*` · `F6_*` · `F7_*` · `F8_*` · `F9_*` · `F_merge_tables.py` · `F_release.sh`
