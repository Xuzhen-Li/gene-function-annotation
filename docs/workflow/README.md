# Workflow index

[中文](README.zh.md) · [Home page](../../README.md) · [Knowledge map](../KNOWLEDGE_MAP.md)

This repository is a knowledge base. The workflow is one reference route through it, with small example scripts. This page says which page is authoritative for each workflow question, so that repeated text elsewhere can be read as a copy.

## The route in one line

Protein input QC (F0) → framework F1: DIAMOND against Swiss-Prot, eggNOG-mapper, InterProScan → optional add-ons (F4, F6–F9) → merge into `merged_function_table.tsv` → function QC (F10) → release (route as drawn in the route map and stated in [`docs/ROADMAP.md`](../ROADMAP.md)).

![Route map](../figures/guide/function_route_map_v2.png)

## Which page is authoritative

| Question | Authoritative page | Pages that repeat or teach it |
|---|---|---|
| Step order, frames and add-ons | [`docs/ROADMAP.md`](../ROADMAP.md) | README, Usage; [`catalog/_namespaces.md`](../../catalog/_namespaces.md); book chapter 18 |
| The route chosen for your data | `my_fa_plan.md`, written by [`pipeline/flow_tool/flow.py`](../../pipeline/flow_tool/flow.py) from your answers | README, Usage |
| Inputs and outputs of each stage | [`docs/STAGE_IO.md`](../STAGE_IO.md) | [`pipeline/00_overview.md`](../../pipeline/00_overview.md) |
| Commands for each tool | [`docs/TOOLS.md`](../TOOLS.md) and the scripts in [`pipeline/`](../../pipeline/00_overview.md) | `docs/tools/`, `docs/notes/` |
| When a result is good enough | [`docs/EVALUATION.md`](../EVALUATION.md) | [`docs/EVALUATION_CHECKLIST.md`](../EVALUATION_CHECKLIST.md); knowledge units on criteria |
| Installing tools and databases | [`docs/INSTALL_FUNCTIONAL.md`](../INSTALL_FUNCTIONAL.md) | [`docs/DB_INSTALL_CHECKLIST.md`](../DB_INSTALL_CHECKLIST.md) |
| Hand-off between structure and function | [`docs/HANDOFF_STRUCTURE_TO_FUNCTION.md`](../HANDOFF_STRUCTURE_TO_FUNCTION.md) | README, Usage |
| A first walk through | [`docs/QUICKSTART.md`](../QUICKSTART.md) | [`docs/START_HERE.md`](../START_HERE.md) |

## Older workflow pages

These pages are kept as a record. Where they differ from the authoritative page above, the authoritative page wins.

- [`docs/CLASSROOM_TONIGHT.md`](../CLASSROOM_TONIGHT.md) and the wiki page Start-tonight: an early quick start.
- The dated status sections at the end of [`docs/ROADMAP.md`](../ROADMAP.md): progress notes of their date.
- Step cards in the stage folders of [`catalog/`](../../catalog/README.md): the 2026-11 first pass; see [`docs/kb/NUMBERING.md`](../kb/NUMBERING.md).
- [`docs/STAGE_IO.md`](../STAGE_IO.md) labels `F2_eggnog.sh` and `F3_interproscan.sh` as F1 steps in short form; the full wording is in [`catalog/_namespaces.md`](../../catalog/_namespaces.md).
