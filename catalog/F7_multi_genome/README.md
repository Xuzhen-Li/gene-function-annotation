# F7 · multi-genome orthogroups (OrthoFinder)

**Collects:** Orthology tools and databases. F7 annotates orthogroup **representatives**, not each released gene; a single genome does not need F7 first. vitis-pangenome also uses OrthoFinder for a different purpose.

**Does not collect:** —

## Entries

- [GFA-F7-001 · OrthoFinder 3](#gfa-f7-001--orthofinder-3)
- [GFA-F7-002 · FastOMA](#gfa-f7-002--fastoma)
- [GFA-F7-003 · SonicParanoid2](#gfa-f7-003--sonicparanoid2)
- [GFA-F7-004 · OrthoDB v12](#gfa-f7-004--orthodb-v12)
- [GFA-F7-005 · OMA browser 2024](#gfa-f7-005--oma-browser-2024)
- [GFA-F7-006 · Ensembl Plants](#gfa-f7-006--ensembl-plants)

### GFA-F7-001 · OrthoFinder 3

| field | value |
|---|---|
| type | tool |
| stage | F7 · multi-genome orthogroups |
| script | `F7_orthofinder.sh` |
| tools_card | none |
| gates | Gate-F3 (framework), Gate-F4 |
| what it does | Scalable phylogenetic orthology (v3.x, FAMSA alignment). |
| url | https://github.com/OrthoFinder/OrthoFinder |
| doi | [10.1101/2025.07.15.664860](https://doi.org/10.1101/2025.07.15.664860) |
| venue / year | preprint 2025 |
| venue_label | Preprint |
| latest release (GitHub API) | v3.2 (2026-10-23); last push 2026-10-23 |
| license | GPL-3.0 |
| plant_evidence | Grapevine pangenome/clade comparisons; annotates orthogroup representatives, not each gene. |
| existing_doc | none |
| io | several proteomes → orthogroups; representatives → frame F1 |
| db_version_field | — |
| verdict | needs evidence |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F7-002 · FastOMA

| field | value |
|---|---|
| type | tool |
| stage | F7 · multi-genome orthogroups |
| script | `F7_orthofinder.sh` |
| tools_card | none |
| gates | Gate-F3 (framework), Gate-F4 |
| what it does | Linear-scaling orthology inference (OMAmer placement). |
| url | https://github.com/DessimozLab/FastOMA |
| doi | [10.1038/s41592-024-02552-8](https://doi.org/10.1038/s41592-024-02552-8) |
| venue / year | Nature Methods 2025 |
| venue_label | Allowlisted |
| latest release (GitHub API) | v0.5.1 (2025-12-19); last push 2026-11-12 |
| license | MPL-2.0 |
| plant_evidence | Thousands of proteomes. |
| existing_doc | none |
| io | several proteomes → orthogroups; representatives → frame F1 |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F7-003 · SonicParanoid2

| field | value |
|---|---|
| type | tool |
| stage | F7 · multi-genome orthogroups |
| script | `F7_orthofinder.sh` |
| tools_card | none |
| gates | Gate-F3 (framework), Gate-F4 |
| what it does | Fast orthology with ML and language models. |
| url | https://gitlab.com/salvo981/sonicparanoid2 |
| doi | [10.1186/s13059-024-03298-4](https://doi.org/10.1186/s13059-024-03298-4) |
| venue / year | Genome Biology 2024 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Generic. |
| existing_doc | none |
| io | several proteomes → orthogroups; representatives → frame F1 |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F7-004 · OrthoDB v12

| field | value |
|---|---|
| type | db |
| stage | F7 · multi-genome orthogroups |
| script | `F7_orthofinder.sh` |
| tools_card | none |
| gates | Gate-F3 (framework), Gate-F4 |
| what it does | Hierarchical orthologs with functional descriptors (OrthoDB + BUSCO update paper). |
| url | https://www.orthodb.org |
| doi | [10.1093/nar/gkae987](https://doi.org/10.1093/nar/gkae987) |
| venue / year | Nucleic Acids Research 2024 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Includes many plants. |
| existing_doc | none |
| io | several proteomes → orthogroups; representatives → frame F1 |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F7-005 · OMA browser 2024

| field | value |
|---|---|
| type | db |
| stage | F7 · multi-genome orthogroups |
| script | `F7_orthofinder.sh` |
| tools_card | none |
| gates | Gate-F3 (framework), Gate-F4 |
| what it does | OMA orthology resource update. |
| url | https://omabrowser.org |
| doi | [10.1093/nar/gkad1020](https://doi.org/10.1093/nar/gkad1020) |
| venue / year | Nucleic Acids Research 2023 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Plants included. |
| existing_doc | none |
| io | several proteomes → orthogroups; representatives → frame F1 |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F7-006 · Ensembl Plants

| field | value |
|---|---|
| type | db |
| stage | F7 · multi-genome orthogroups |
| script | `F7_orthofinder.sh` |
| tools_card | none |
| gates | Gate-F3 (framework), Gate-F4 |
| what it does | Plant genomes with gene trees and projected annotation. |
| url | https://plants.ensembl.org |
| doi | none found |
| venue / year | — |
| venue_label | — (no paper) |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Vitis vinifera present. |
| existing_doc | none |
| io | several proteomes → orthogroups; representatives → frame F1 |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

[Back to catalog index](../README.md)
