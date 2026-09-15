# KofamScan — KEGG KO on proteins

**Role:** **F1+** optional KO / complements eggNOG KEGG columns (TOOLS table F1+).

Do **not** call this TOOLS **F1b** — F1b is eggNOG-mapper inside frame F1.

## Get it
KEGG KofamKOALA downloads: profiles + `ko_list` + `exec_annotation`.

## Run
`pipeline/F1b_kofam.sh` (historical filename; narrative = **F1+**) with `KOFAM_PROFILE_DIR`, `KOFAM_KO_LIST`, `RUN=1`.
