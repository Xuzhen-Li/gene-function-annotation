# F6 · MapMan BINs (Mercator4) and plant pathway views

**Collects:** Plant pathway/BIN resources.

**Does not collect:** —

## Entries

- [GFA-F6-001 · Plant Reactome (2024)](#gfa-f6-001--plant-reactome-2024)
- [GFA-F6-002 · Plant Metabolic Network / E2P2](#gfa-f6-002--plant-metabolic-network--e2p2)

### GFA-F6-001 · Plant Reactome (2024)

| field | value |
|---|---|
| type | db |
| stage | F6 · plant pathway views |
| script | `F6_ingest_mercator.py` (Mercator only) |
| tools_card | F6 |
| gates | Gate-F4 (versions) |
| what it does | Curated plant pathways (rice reference, projected to other plants). |
| url | https://plantreactome.gramene.org |
| doi | [10.1093/nar/gkad1052](https://doi.org/10.1093/nar/gkad1052) |
| venue / year | Nucleic Acids Research 2023 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Projections include grapevine [待确认 species list]. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F6-002 · Plant Metabolic Network / E2P2

| field | value |
|---|---|
| type | db + tool |
| stage | F6 · plant pathway views |
| script | `F6_ingest_mercator.py` (Mercator only) |
| tools_card | F6 |
| gates | Gate-F4 (versions) |
| what it does | PlantCyc and species pathway DBs built with the E2P2 enzyme predictor. |
| url | https://plantcyc.org |
| doi | none found |
| venue / year | — |
| venue_label | — (no paper) |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Plant-specific metabolism; DOI of current release [待确认]. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | needs evidence |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

[Back to catalog index](../README.md)
