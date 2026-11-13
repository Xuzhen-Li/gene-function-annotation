# F8 · NLR protein classification (IPS filter ± HRP)

**Collects:** Plant NLR classifiers and reference sets. Results can be handed to structure scenario S7 to mark windows for gene-model review.

**Does not collect:** Merging re-annotated loci into the release GFF (structure side). Placement of genome-level NLR locus finders (NLR-Annotator) between F8 and structure S7 is [待确认].

## Entries

- [GFA-F8-001 · Resistify](#gfa-f8-001--resistify)
- [GFA-F8-002 · NLRtracker + RefPlantNLR](#gfa-f8-002--nlrtracker--refplantnlr)
- [GFA-F8-003 · NLR-Annotator](#gfa-f8-003--nlr-annotator)
- [GFA-F8-004 · NLRexpress](#gfa-f8-004--nlrexpress)
- [GFA-F8-005 · NLRSeek](#gfa-f8-005--nlrseek)

### GFA-F8-001 · Resistify

| field | value |
|---|---|
| type | tool |
| stage | F8 · NLR protein classification |
| script | `F8_run.sh`, `F8_list_nlr_from_ips.py`, `F8b_nlr_to_families.py` |
| tools_card | F8 |
| gates | Gate-F4 (versions) |
| what it does | Fast NLR identification/classification from proteins using NLRexpress motifs. |
| url | https://github.com/SwiftSeal/resistify |
| doi | [10.1177/11779322241308944](https://doi.org/10.1177/11779322241308944) |
| venue / year | Bioinformatics and Biology Insights 2025 |
| venue_label | Below allowlist |
| latest release (GitHub API) | v2.4.0 (2026-07-22); last push 2026-07-22 |
| license | GPL-3.0 |
| plant_evidence | Plant NLRs (frame F8 peer to HRP). |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F8-002 · NLRtracker + RefPlantNLR

| field | value |
|---|---|
| type | tool + db |
| stage | F8 · NLR protein classification |
| script | `F8_run.sh`, `F8_list_nlr_from_ips.py`, `F8b_nlr_to_families.py` |
| tools_card | F8 |
| gates | Gate-F4 (versions) |
| what it does | Extracts and classifies NLRs from proteomes/transcripts using features of RefPlantNLR. |
| url | https://github.com/slt666666/NLRtracker |
| doi | [10.1371/journal.pbio.3001124](https://doi.org/10.1371/journal.pbio.3001124) |
| venue / year | PLOS Biology 2021 |
| venue_label | Below allowlist |
| latest release (GitHub API) | —; last push 2024-03-06 |
| license | MIT |
| plant_evidence | Plant NLRs. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F8-003 · NLR-Annotator

| field | value |
|---|---|
| type | tool |
| stage | F8 · NLR protein classification |
| script | `F8_run.sh`, `F8_list_nlr_from_ips.py`, `F8b_nlr_to_families.py` |
| tools_card | F8 |
| gates | Gate-F4 (versions) |
| what it does | Annotation-independent NLR locus finder on genomic sequence. |
| url | https://github.com/steuernb/NLR-Annotator |
| doi | [10.1104/pp.19.01273](https://doi.org/10.1104/pp.19.01273) |
| venue / year | Plant Physiology 2020 |
| venue_label | Below allowlist |
| latest release (GitHub API) | tag v0.7-beta; last push 2023-07-19 |
| license | GPL-3.0 |
| plant_evidence | Window list can be handed to structure scenario S7 for model review. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F8-004 · NLRexpress

| field | value |
|---|---|
| type | tool |
| stage | F8 · NLR protein classification |
| script | `F8_run.sh`, `F8_list_nlr_from_ips.py`, `F8b_nlr_to_families.py` |
| tools_card | F8 |
| gates | Gate-F4 (versions) |
| what it does | ML motif predictors for CC/TIR/NB-ARC/LRR motifs. |
| url | https://github.com/eliza-m/NLRexpress |
| doi | [10.3389/fpls.2022.975888](https://doi.org/10.3389/fpls.2022.975888) |
| venue / year | Frontiers in Plant Science 2022 |
| venue_label | Below allowlist |
| latest release (GitHub API) | —; last push 2022-08-22 |
| license | GPL-3.0 |
| plant_evidence | Plant NLRs. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F8-005 · NLRSeek

| field | value |
|---|---|
| type | tool |
| stage | F8 · NLR protein classification |
| script | `F8_run.sh`, `F8_list_nlr_from_ips.py`, `F8b_nlr_to_families.py` |
| tools_card | F8 |
| gates | Gate-F4 (versions) |
| what it does | Combines NLR-Annotator loci, targeted re-annotation and NLRtracker to recover NLRs missing from proteomes. |
| url | https://github.com/Wang-Mengda/NLRSeek |
| doi | [10.1016/j.abiote.2025.100001](https://doi.org/10.1016/j.abiote.2025.100001) |
| venue / year | aBIOTECH 2026 |
| venue_label | Below allowlist |
| latest release (GitHub API) | —; last push 2026-02-02 |
| license | GPL-3.0 |
| plant_evidence | Its re-annotation output is a structure-side hint: send recovered loci to S7, do not merge them into the release GFF from here. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

[Back to catalog index](../README.md)
