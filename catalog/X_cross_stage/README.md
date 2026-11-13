# Cross-stage — whole pipelines, non-protein resources, downstream pointers, ideas

**Collects:** Whole alternative pipelines, ncRNA and expression resources outside the protein spine [待确认 placement], pointers to downstream enrichment, LLM/agent ideas.

**Does not collect:** —

## Entries

- [GFA-X-001 · GOMAP](#gfa-x-001--gomap)
- [GFA-X-002 · ncPlantDB](#gfa-x-002--ncplantdb)
- [GFA-X-003 · PLncDB V2.0](#gfa-x-003--plncdb-v20)
- [GFA-X-004 · GreeNC 2.0](#gfa-x-004--greenc-20)
- [GFA-X-005 · CANTATAdb 3.0](#gfa-x-005--cantatadb-30)
- [GFA-X-006 · PlantCircRNA](#gfa-x-006--plantcircrna)
- [GFA-X-007 · psRNATarget (2017 release)](#gfa-x-007--psrnatarget-2017-release)
- [GFA-X-008 · PmiREN 2.0](#gfa-x-008--pmiren-20)
- [GFA-X-009 · scPlantDB](#gfa-x-009--scplantdb)
- [GFA-X-010 · hdWGCNA](#gfa-x-010--hdwgcna)
- [GFA-X-011 · CoNekT](#gfa-x-011--conekt)
- [GFA-X-012 · DAVID (2025 update)](#gfa-x-012--david-2025-update)
- [GFA-X-013 · g:Profiler (2023)](#gfa-x-013--gprofiler-2023)
- [GFA-X-014 · agriGO v2.0](#gfa-x-014--agrigo-v20)
- [GFA-X-015 · clusterProfiler 4.0](#gfa-x-015--clusterprofiler-40)
- [GFA-X-016 · GeneAgent](#gfa-x-016--geneagent)
- [GFA-X-017 · LLM-assisted Reactome annotation](#gfa-x-017--llm-assisted-reactome-annotation)
- [GFA-X-018 · Agentic AI for gene function across genomes](#gfa-x-018--agentic-ai-for-gene-function-across-genomes)

## Whole alternative pipelines

### GFA-X-001 · GOMAP

| field | value |
|---|---|
| type | tool |
| stage | Cross-stage · whole plant GO pipeline |
| script | none |
| tools_card | none |
| gates | Gate-F3 (framework) |
| what it does | Gene Ontology Meta Annotator for Plants: combines sequence similarity, domains and mixed-method predictors into plant GO sets. |
| url | https://github.com/Dill-PICL/GOMAP |
| doi | [10.1186/s13007-021-00754-1](https://doi.org/10.1186/s13007-021-00754-1) |
| venue / year | Plant Methods 2021 |
| venue_label | Below allowlist |
| latest release (GitHub API) | v1.0.0 (2018-07-20); last push 2023-05-22 |
| license | MIT |
| plant_evidence | Plant-specific (maize origin, applied to many crops). |
| existing_doc | none |
| io | varies (see card) |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

## Non-coding RNA function resources [待确认 placement: this repo starts from proteins]

### GFA-X-002 · ncPlantDB

| field | value |
|---|---|
| type | db |
| stage | Cross-stage · ncRNA resources (outside protein spine) |
| script | none |
| tools_card | none |
| gates | — |
| what it does | Plant ncRNAs with potential ncRNA-encoded peptides and cell-type interactions (43 species). |
| url | https://bis.zju.edu.cn/ncPlantDB |
| doi | [10.1093/nar/gkae1017](https://doi.org/10.1093/nar/gkae1017) |
| venue / year | Nucleic Acids Research 2024 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Plant-specific. |
| existing_doc | none |
| io | ncRNA loci from the structure side → database lookup |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-X-003 · PLncDB V2.0

| field | value |
|---|---|
| type | db |
| stage | Cross-stage · ncRNA resources (outside protein spine) |
| script | none |
| tools_card | none |
| gates | — |
| what it does | Plant lncRNA encyclopedia. |
| url | https://www.tobaccodb.org/plncdb/ |
| doi | [10.1093/nar/gkaa910](https://doi.org/10.1093/nar/gkaa910) |
| venue / year | Nucleic Acids Research 2020 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Plant-specific. |
| existing_doc | none |
| io | ncRNA loci from the structure side → database lookup |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-X-004 · GreeNC 2.0

| field | value |
|---|---|
| type | db |
| stage | Cross-stage · ncRNA resources (outside protein spine) |
| script | none |
| tools_card | none |
| gates | — |
| what it does | Plant lncRNA catalog. |
| url | http://greenc.sequentiabiotech.com |
| doi | [10.1093/nar/gkab1014](https://doi.org/10.1093/nar/gkab1014) |
| venue / year | Nucleic Acids Research 2021 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Includes Vitis. |
| existing_doc | none |
| io | ncRNA loci from the structure side → database lookup |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-X-005 · CANTATAdb 3.0

| field | value |
|---|---|
| type | db |
| stage | Cross-stage · ncRNA resources (outside protein spine) |
| script | none |
| tools_card | none |
| gates | — |
| what it does | Updated plant lncRNA repository. |
| url | http://cantata.amu.edu.pl |
| doi | [10.1093/pcp/pcae081](https://doi.org/10.1093/pcp/pcae081) |
| venue / year | Plant And Cell Physiology 2024 |
| venue_label | Below allowlist |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Plant-specific. |
| existing_doc | none |
| io | ncRNA loci from the structure side → database lookup |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-X-006 · PlantCircRNA

| field | value |
|---|---|
| type | db |
| stage | Cross-stage · ncRNA resources (outside protein spine) |
| script | none |
| tools_card | none |
| gates | — |
| what it does | Plant circular RNA database. |
| url | https://plant.deepbiology.cn/PlantCircRNA/ |
| doi | [10.1093/nar/gkae709](https://doi.org/10.1093/nar/gkae709) |
| venue / year | Nucleic Acids Research 2024 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Plant-specific. |
| existing_doc | none |
| io | ncRNA loci from the structure side → database lookup |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-X-007 · psRNATarget (2017 release)

| field | value |
|---|---|
| type | tool |
| stage | Cross-stage · ncRNA resources (outside protein spine) |
| script | none |
| tools_card | none |
| gates | — |
| what it does | Plant small-RNA target prediction server. |
| url | https://www.zhaolab.org/psRNATarget/ |
| doi | [10.1093/nar/gky316](https://doi.org/10.1093/nar/gky316) |
| venue / year | Nucleic Acids Research 2018 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | miRNA-target function hypotheses. |
| existing_doc | none |
| io | ncRNA loci from the structure side → database lookup |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-X-008 · PmiREN 2.0

| field | value |
|---|---|
| type | db |
| stage | Cross-stage · ncRNA resources (outside protein spine) |
| script | none |
| tools_card | none |
| gates | — |
| what it does | Plant miRNA encyclopedia. |
| url | https://pmiren.com |
| doi | [10.1093/nar/gkab811](https://doi.org/10.1093/nar/gkab811) |
| venue / year | Nucleic Acids Research 2021 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Plant-specific. |
| existing_doc | none |
| io | ncRNA loci from the structure side → database lookup |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

## Expression-supported function (hypotheses, not experimental GO)

### GFA-X-009 · scPlantDB

| field | value |
|---|---|
| type | db |
| stage | Cross-stage · expression-supported function |
| script | none |
| tools_card | none |
| gates | — |
| what it does | Plant single-cell atlas: cell types and markers. |
| url | https://biobigdata.nju.edu.cn/scplantdb/ |
| doi | [10.1093/nar/gkad706](https://doi.org/10.1093/nar/gkad706) |
| venue / year | Nucleic Acids Research 2023 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Cell-type context for candidate genes. |
| existing_doc | none |
| io | expression data + gene IDs → modules / cell-type context |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-X-010 · hdWGCNA

| field | value |
|---|---|
| type | tool |
| stage | Cross-stage · expression-supported function |
| script | none |
| tools_card | none |
| gates | — |
| what it does | Co-expression networks in single-cell/spatial data. |
| url | https://github.com/smorabit/hdWGCNA |
| doi | [10.1016/j.crmeth.2023.100498](https://doi.org/10.1016/j.crmeth.2023.100498) |
| venue / year | Cell Reports Methods 2023 |
| venue_label | Allowlisted |
| latest release (GitHub API) | v0.4.12 (2026-06-16); last push 2026-06-16 |
| license | custom/other (see repo) |
| plant_evidence | Module membership as function evidence (non-IEA labels only with experiments). |
| existing_doc | none |
| io | expression data + gene IDs → modules / cell-type context |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-X-011 · CoNekT

| field | value |
|---|---|
| type | tool + db |
| stage | Cross-stage · expression-supported function |
| script | none |
| tools_card | none |
| gates | — |
| what it does | Co-expression network toolkit/framework for plants. |
| url | https://conekt.sbs.ntu.edu.sg |
| doi | [10.1101/255075](https://doi.org/10.1101/255075) |
| venue / year | preprint 2018 |
| venue_label | Preprint |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Comparative co-expression [待确认 journal DOI]. |
| existing_doc | none |
| io | expression data + gene IDs → modules / cell-type context |
| db_version_field | — |
| verdict | needs evidence |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

## Downstream enrichment — pointers only (FUNCTIONAL_MAIN calls this Downstream)

### GFA-X-012 · DAVID (2025 update)

| field | value |
|---|---|
| type | tool |
| stage | Cross-stage · downstream enrichment (pointer) |
| script | none |
| tools_card | none |
| gates | — |
| what it does | Enrichment server; adds DAVID Ortholog for cross-species analysis. |
| url | https://davidbioinformatics.nih.gov |
| doi | [10.1093/nar/gkag470](https://doi.org/10.1093/nar/gkag470) |
| venue / year | Nucleic Acids Research 2026 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Model-organism heavy; map plant genes via orthologs. |
| existing_doc | none |
| io | `merged_function_table.tsv` as background → enrichment table |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-X-013 · g:Profiler (2023)

| field | value |
|---|---|
| type | tool |
| stage | Cross-stage · downstream enrichment (pointer) |
| script | none |
| tools_card | none |
| gates | — |
| what it does | Enrichment and ID conversion. |
| url | https://biit.cs.ut.ee/gprofiler |
| doi | [10.1093/nar/gkad347](https://doi.org/10.1093/nar/gkad347) |
| venue / year | Nucleic Acids Research 2023 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Supports Ensembl Plants species. |
| existing_doc | none |
| io | `merged_function_table.tsv` as background → enrichment table |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-X-014 · agriGO v2.0

| field | value |
|---|---|
| type | tool |
| stage | Cross-stage · downstream enrichment (pointer) |
| script | none |
| tools_card | none |
| gates | — |
| what it does | GO enrichment for agricultural species. |
| url | http://systemsbiology.cau.edu.cn/agriGOv2/ |
| doi | [10.1093/nar/gkx382](https://doi.org/10.1093/nar/gkx382) |
| venue / year | Nucleic Acids Research 2017 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Plant-focused. |
| existing_doc | none |
| io | `merged_function_table.tsv` as background → enrichment table |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-X-015 · clusterProfiler 4.0

| field | value |
|---|---|
| type | tool |
| stage | Cross-stage · downstream enrichment (pointer) |
| script | none |
| tools_card | none |
| gates | — |
| what it does | R enrichment with custom TERM2GENE from merged_function_table.tsv. |
| url | https://github.com/YuLab-SMU/clusterProfiler |
| doi | [10.1016/j.xinn.2021.100141](https://doi.org/10.1016/j.xinn.2021.100141) |
| venue / year | The Innovation 2021 |
| venue_label | Allowlisted |
| latest release (GitHub API) | —; last push 2026-11-11 |
| license | no licence file |
| plant_evidence | Any species with your own GO table. |
| existing_doc | none |
| io | `merged_function_table.tsv` as background → enrichment table |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

## Ideas — LLMs and agents in curation (human sign-off required)

### GFA-X-016 · GeneAgent

| field | value |
|---|---|
| type | idea |
| stage | Cross-stage · ideas (LLMs and agents) |
| script | none |
| tools_card | none |
| gates | — |
| what it does | Self-verifying LLM agent for gene-set analysis using domain databases. |
| url | — |
| doi | [10.1038/s41592-025-02748-6](https://doi.org/10.1038/s41592-025-02748-6) |
| venue / year | Nature Methods 2025 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Idea for checking enrichment summaries; human review. |
| existing_doc | none |
| io | — |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-X-017 · LLM-assisted Reactome annotation

| field | value |
|---|---|
| type | idea |
| stage | Cross-stage · ideas (LLMs and agents) |
| script | none |
| tools_card | none |
| gates | — |
| what it does | LLM/RAG proposals of pathway annotations for curator review (preprint). |
| url | — |
| doi | [10.64898/2025.12.20.695723](https://doi.org/10.64898/2025.12.20.695723) |
| venue / year | preprint 2025 |
| venue_label | Preprint |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Idea for plant pathway curation. |
| existing_doc | none |
| io | — |
| db_version_field | — |
| verdict | needs evidence |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-X-018 · Agentic AI for gene function across genomes

| field | value |
|---|---|
| type | idea |
| stage | Cross-stage · ideas (LLMs and agents) |
| script | none |
| tools_card | none |
| gates | — |
| what it does | GO curators' agent workflow with constrained schemas and validators (Zenodo record). |
| url | — |
| doi | [10.5281/zenodo.18904049](https://doi.org/10.5281/zenodo.18904049) |
| venue / year | Zenodo 2026 |
| venue_label | Below allowlist |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Idea only. |
| existing_doc | none |
| io | — |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

[Back to catalog index](../README.md)
