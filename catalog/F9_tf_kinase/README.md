# F9 · transcription factors / kinases (iTAK)

**Collects:** Plant TF/kinase family resources.

**Does not collect:** —

## Entries

- [GFA-F9-001 · PlantTFDB / PlantRegMap](#gfa-f9-001--planttfdb--plantregmap)
- [GFA-F9-002 · PlantPAN (latest)](#gfa-f9-002--plantpan-latest)

### GFA-F9-001 · PlantTFDB / PlantRegMap

| field | value |
|---|---|
| type | db |
| stage | F9 · TF / kinase families |
| script | `F9_itak.sh` |
| tools_card | F9 |
| gates | Gate-F4 (versions) |
| what it does | Plant TF families, binding motifs and regulatory map. |
| url | http://planttfdb.gao-lab.org |
| doi | [10.1093/nar/gkz1020](https://doi.org/10.1093/nar/gkz1020) |
| venue / year | Nucleic Acids Research 2019 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | TF family calls beside iTAK (frame F9). |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F9-002 · PlantPAN (latest)

| field | value |
|---|---|
| type | db |
| stage | F9 · TF / kinase families |
| script | `F9_itak.sh` |
| tools_card | F9 |
| gates | Gate-F4 (versions) |
| what it does | Plant promoter / TF-binding analysis navigator. |
| url | https://plantpan.itps.ncku.edu.tw |
| doi | [10.1093/nar/gkad945](https://doi.org/10.1093/nar/gkad945) |
| venue / year | Nucleic Acids Research 2023 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Promoter/CNS context for TF families (115 species). |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

[Back to catalog index](../README.md)
