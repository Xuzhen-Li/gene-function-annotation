# F4 · readable names (AHRD, PANNZER2)

**Collects:** Name sources and naming rules.

**Does not collect:** —

## Entries

- [GFA-F4-001 · Grapedia Grapevine Reference Gene Catalogue](#gfa-f4-001--grapedia-grapevine-reference-gene-catalogue)
- [GFA-F4-002 · Grape Gene Reference Catalogue (paper)](#gfa-f4-002--grape-gene-reference-catalogue-paper)
- [GFA-F4-003 · ProtNLM (UniProt names)](#gfa-f4-003--protnlm-uniprot-names)

### GFA-F4-001 · Grapedia Grapevine Reference Gene Catalogue

| field | value |
|---|---|
| type | db |
| stage | F4 · readable names |
| script | `F4_join_ahrd.py` / `F4b_join_pannzer.py` |
| tools_card | F4 |
| gates | Gate-F4 (versions) |
| what it does | Curated V. vinifera gene ID/symbol pairs with function, literature and confidence; v3.1 (Nov 2025) aligned to T2T v5.1 annotation. |
| url | https://grapedia.org/genes/ |
| doi | none found |
| venue / year | — |
| venue_label | — (no paper) |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Grapevine-specific naming source. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F4-002 · Grape Gene Reference Catalogue (paper)

| field | value |
|---|---|
| type | db |
| stage | F4 · readable names |
| script | `F4_join_ahrd.py` / `F4b_join_pannzer.py` |
| tools_card | F4 |
| gates | Gate-F4 (versions) |
| what it does | Describes the catalogue as a standard for gene selection. |
| url | — |
| doi | [10.3389/fpls.2021.803977](https://doi.org/10.3389/fpls.2021.803977) |
| venue / year | Frontiers in Plant Science 2022 |
| venue_label | Below allowlist |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Grapevine. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F4-003 · ProtNLM (UniProt names)

| field | value |
|---|---|
| type | idea |
| stage | F4 · readable names |
| script | `F4_join_ahrd.py` / `F4b_join_pannzer.py` |
| tools_card | F4 |
| gates | Gate-F4 (versions) |
| what it does | UniProt uses a Google protein-naming model to propose names for unreviewed entries; names carry an automatic evidence tag. |
| url | https://www.uniprot.org/help/ProtNLM |
| doi | none found |
| venue / year | — |
| venue_label | — (no paper) |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Explains machine names arriving via TrEMBL hits. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

[Back to catalog index](../README.md)
