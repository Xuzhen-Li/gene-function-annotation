# Structural main process — moved

The **structural** annotation spine (S1–S14: soft-mask → draft → merge → QC → curation → release GFF) lives in the sibling repo:

**[gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation)**

| Need | On structure repo |
|------|-------------------|
| Main spine | [`docs/steps/MAIN.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/steps/MAIN.md) |
| Quickstart | [`docs/QUICKSTART.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/QUICKSTART.md) |
| Playbook / checklist | [`docs/PLAYBOOK.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/PLAYBOOK.md) |
| Scenarios | [`docs/SCENARIOS.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/SCENARIOS.md) |

This repo (`gene-function-annotation`) is the **function layer only**. After a qualified `proteins.faa` (and optional GFF) exists upstream, set `PROTEINS_FA` and follow [`FUNCTIONAL_MAIN.md`](FUNCTIONAL_MAIN.md).
