# F10 · function-table QC

**Collects:** Checks and cautions on functional claims in `merged_function_table.tsv`.

**Does not collect:** —

## Entries

- [GFA-F10-001 · GO specificity balance (Genome Res 2026)](#gfa-f10-001--go-specificity-balance-genome-res-2026)
- [GFA-F10-002 · CAFA lessons (idea)](#gfa-f10-002--cafa-lessons-idea)

### GFA-F10-001 · GO specificity balance (Genome Res 2026)

| field | value |
|---|---|
| type | idea |
| stage | F10 · function-table QC |
| script | `F10_function_qc.py` |
| tools_card | none |
| gates | Gate-F5 (row counts) |
| what it does | Balancing GO term specificity in sequence-language-model predictions. |
| url | — |
| doi | [10.1101/gr.280816.125](https://doi.org/10.1101/gr.280816.125) |
| venue / year | Genome Research 2026 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Avoids over-specific electronic GO on plant genes [待确认 details]. |
| existing_doc | none |
| io | `merged_function_table.tsv` → QC notes |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F10-002 · CAFA lessons (idea)

| field | value |
|---|---|
| type | idea |
| stage | F10 · function-table QC |
| script | `F10_function_qc.py` |
| tools_card | none |
| gates | Gate-F5 (row counts) |
| what it does | Community assessments keep showing GO prediction is hard for proteins with partial knowledge; publish ML GO as electronic evidence (IEA) only. |
| url | https://biofunctionprediction.org/cafa/ |
| doi | none found |
| venue / year | — |
| venue_label | — (no paper) |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | All frames. |
| existing_doc | none |
| io | `merged_function_table.tsv` → QC notes |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

[Back to catalog index](../README.md)
