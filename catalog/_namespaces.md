# Four numbering systems

From the README "Namespace details". Catalog folders and stage labels use **framework / stage number + step name** only.

| Namespace | Content | How the catalog uses it |
|---|---|---|
| Framework | F1 (default: DIAMOND + eggNOG-mapper + InterProScan), F2 (fast: eggNOG-mapper alone ± Kofam), F3 (EnTAP), F5 (Trinotate); add-on stages F0, F4, F6–F10 keep their numbers | Stage label and folder (`frame_F1/` …) |
| Script file | `F1_diamond.sh`, `F2_eggnog.sh`, `F3_interproscan.sh` are the **three steps of framework F1**; `F1b_kofam.sh` is the **Kofam step of framework F1** (TOOLS: optional F1+), **not card F1b**; framework F2 also calls `F2_eggnog.sh` | `script` field only — never a stage name |
| TOOLS card | F1a DIAMOND, F1b eggNOG-mapper, F1c InterProScan; F1+ KofamScan, Phobius/SignalP; F2+ KEGGaNOG | `tools_card` field only |
| Gate | Gate-F1 protein source, Gate-F2 F0 BUSCO lineage, Gate-F3 framework, Gate-F4 versions, Gate-F5 table rows, Gate-F6 release pack, Gate-F7 hygiene (`docs/EVALUATION.md`) | `gates` field only; no folders |

Known wording issue (not changed here): `docs/STAGE_IO.md` lines 20–21 label `F2_eggnog.sh` / `F3_interproscan.sh` as "F1 eggNOG" / "F1 InterPro" without saying they are steps of framework F1. Suggested wording for a later PR: "framework F1 · eggNOG-mapper (script `F2_eggnog.sh`)".

[Back to catalog index](README.md)
