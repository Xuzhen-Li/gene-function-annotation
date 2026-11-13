# F1 · default framework (DIAMOND, eggNOG-mapper, InterProScan, optional KofamScan and add-ons)

**Collects:** Tools and databases for the three F1 steps, the optional KofamScan step, and optional add-ons run after F1 (localization, CAZy, enzyme/EC, machine-learning GO, protein 3D-structure routes). "Structure" in these cards means protein 3D structure.

**Does not collect:** Gene finding, soft-masking, GFF editing (gene-structure-annotation).

## Entries

- [GFA-F1-001 · MMseqs2-GPU](#gfa-f1-001--mmseqs2-gpu)
- [GFA-F1-002 · TM-Vec 2s](#gfa-f1-002--tm-vec-2s)
- [GFA-F1-003 · UniProt 2025](#gfa-f1-003--uniprot-2025)
- [GFA-F1-004 · Carbon Annotation Database (CADB)](#gfa-f1-004--carbon-annotation-database-cadb)
- [GFA-F1-005 · Foldseek](#gfa-f1-005--foldseek)
- [GFA-F1-006 · ProstT5](#gfa-f1-006--prostt5)
- [GFA-F1-007 · AlphaFold Protein Structure Database (2024)](#gfa-f1-007--alphafold-protein-structure-database-2024)
- [GFA-F1-008 · AlphaFind v2](#gfa-f1-008--alphafind-v2)
- [GFA-F1-009 · DPFunc](#gfa-f1-009--dpfunc)
- [GFA-F1-010 · WASP](#gfa-f1-010--wasp)
- [GFA-F1-011 · PARSE](#gfa-f1-011--parse)
- [GFA-F1-012 · metagenomic-DeepFRI](#gfa-f1-012--metagenomic-deepfri)
- [GFA-F1-013 · SMART (2021 update)](#gfa-f1-013--smart-2021-update)
- [GFA-F1-014 · CDD / CD-Search (2023)](#gfa-f1-014--cdd--cd-search-2023)
- [GFA-F1-015 · Merizo](#gfa-f1-015--merizo)
- [GFA-F1-016 · PLAZA 5.0](#gfa-f1-016--plaza-50)
- [GFA-F1-017 · DeepGO-SE](#gfa-f1-017--deepgo-se)
- [GFA-F1-018 · ProtGO](#gfa-f1-018--protgo)
- [GFA-F1-019 · AltereGO](#gfa-f1-019--alterego)
- [GFA-F1-020 · KEGG (2025 NAR)](#gfa-f1-020--kegg-2025-nar)
- [GFA-F1-021 · CLEAN](#gfa-f1-021--clean)
- [GFA-F1-022 · EZpred](#gfa-f1-022--ezpred)
- [GFA-F1-023 · ProteEC-CLA](#gfa-f1-023--proteec-cla)
- [GFA-F1-024 · plantiSMASH 2.0](#gfa-f1-024--plantismash-20)
- [GFA-F1-025 · dbCAN3](#gfa-f1-025--dbcan3)
- [GFA-F1-026 · DeepLoc 2.1](#gfa-f1-026--deeploc-21)
- [GFA-F1-027 · TargetP 2.0](#gfa-f1-027--targetp-20)
- [GFA-F1-028 · DeepTMHMM](#gfa-f1-028--deeptmhmm)

## F1 · DIAMOND step — search engines and reference databases

### GFA-F1-001 · MMseqs2-GPU

| field | value |
|---|---|
| type | tool |
| stage | F1 · DIAMOND (homology search) |
| script | `F1_diamond.sh` |
| tools_card | F1a |
| gates | Gate-F4 (versions) |
| what it does | GPU-accelerated MMseqs2 sequence search (also speeds ColabFold MSAs). |
| url | https://github.com/soedinglab/MMseqs2 |
| doi | [10.1038/s41592-025-02819-8](https://doi.org/10.1038/s41592-025-02819-8) |
| venue / year | Nature Methods 2025 |
| venue_label | Allowlisted |
| latest release (GitHub API) | 18-8cc5c (2025-07-27); last push 2026-11-11 |
| license | MIT |
| plant_evidence | Fast proteome-vs-UniRef search for large plant proteomes. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-002 · TM-Vec 2s

| field | value |
|---|---|
| type | tool |
| stage | F1 · DIAMOND (homology search) |
| script | `F1_diamond.sh` |
| tools_card | F1a |
| gates | Gate-F4 (versions) |
| what it does | Embedding-based remote homology / TM-score prediction (preprint 2026). |
| url | — |
| doi | [10.64898/2026.02.05.704073](https://doi.org/10.64898/2026.02.05.704073) |
| venue / year | preprint 2026 |
| venue_label | Preprint |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Idea-level for unannotated plant proteins. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | needs evidence |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-003 · UniProt 2025

| field | value |
|---|---|
| type | db |
| stage | F1 · DIAMOND (homology search) |
| script | `F1_diamond.sh` |
| tools_card | F1a |
| gates | Gate-F4 (versions) |
| what it does | Swiss-Prot/TrEMBL reference; cite the current NAR update for METHODS. |
| url | https://www.uniprot.org |
| doi | [10.1093/nar/gkae1010](https://doi.org/10.1093/nar/gkae1010) |
| venue / year | Nucleic Acids Research 2024 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Core DB for every frame. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-004 · Carbon Annotation Database (CADB)

| field | value |
|---|---|
| type | db |
| stage | F1 · DIAMOND (homology search) |
| script | `F1_diamond.sh` |
| tools_card | F1a |
| gates | Gate-F4 (versions) |
| what it does | Predicted protein-coding loci and proteins for ~48k GenBank eukaryote assemblies (Carbon-A). |
| url | https://huggingface.co/blog/HuggingFaceBio/carbon-annotator-genbank-genome-annotation |
| doi | [10.64898/2026.10.20.760448](https://doi.org/10.64898/2026.10.20.760448) |
| venue / year | preprint 2026 |
| venue_label | Preprint |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Extra homolog source for under-sampled plant lineages; predictions, not curated (preprint). |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | needs evidence |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

## F1 · optional add-ons — protein 3D-structure routes

### GFA-F1-005 · Foldseek

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (protein 3D structure) |
| script | none |
| tools_card | F1+ [待确认: no card yet] |
| gates | Gate-F4 (versions) |
| what it does | Protein 3D-structure search via 3Di alphabet; finds remote homologs missed by sequence search. |
| url | https://github.com/steineggerlab/foldseek |
| doi | [10.1038/s41587-023-01773-0](https://doi.org/10.1038/s41587-023-01773-0) |
| venue / year | Nature Biotechnology 2023 |
| venue_label | Allowlisted |
| latest release (GitHub API) | 10-941cd33 (2025-01-19); last push 2026-11-11 |
| license | GPL-3.0 |
| plant_evidence | Structure here = protein 3D structure (AlphaFold/ESMFold models), not gene structure. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-006 · ProstT5

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (protein 3D structure) |
| script | none |
| tools_card | F1+ [待确认: no card yet] |
| gates | Gate-F4 (versions) |
| what it does | Protein language model translating sequence to 3Di tokens so Foldseek can run without predicted structures. |
| url | https://github.com/mheinzinger/ProstT5 |
| doi | [10.1093/nargab/lqae150](https://doi.org/10.1093/nargab/lqae150) |
| venue / year | NAR Genomics and Bioinformatics 2024 |
| venue_label | Below allowlist |
| latest release (GitHub API) | 0.0.1 (2024-10-15); last push 2026-03-06 |
| license | MIT |
| plant_evidence | Plant proteomes without AlphaFold models. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-007 · AlphaFold Protein Structure Database (2024)

| field | value |
|---|---|
| type | db |
| stage | F1 · optional add-on (protein 3D structure) |
| script | none |
| tools_card | F1+ [待确认: no card yet] |
| gates | Gate-F4 (versions) |
| what it does | Predicted protein 3D structures for UniProt; target for Foldseek searches. |
| url | https://alphafold.ebi.ac.uk |
| doi | [10.1093/nar/gkad1011](https://doi.org/10.1093/nar/gkad1011) |
| venue / year | Nucleic Acids Research 2023 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Arabidopsis/rice/maize proteomes plus UniProt-wide models. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-008 · AlphaFind v2

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (protein 3D structure) |
| script | none |
| tools_card | F1+ [待确认: no card yet] |
| gates | Gate-F4 (versions) |
| what it does | Similarity search over AlphaFold DB and TED domains. |
| url | https://alphafind.fi.muni.cz |
| doi | [10.1093/nar/gkag372](https://doi.org/10.1093/nar/gkag372) |
| venue / year | Nucleic Acids Research 2026 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Web lookup for single plant proteins. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-009 · DPFunc

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (protein 3D structure) |
| script | none |
| tools_card | F1+ [待确认: no card yet] |
| gates | Gate-F4 (versions) |
| what it does | Deep learning GO prediction guided by domain + 3D-structure information. |
| url | https://github.com/CSUBioGroup/DPFunc |
| doi | [10.1038/s41467-024-54816-8](https://doi.org/10.1038/s41467-024-54816-8) |
| venue / year | Nature Communications 2025 |
| venue_label | Allowlisted |
| latest release (GitHub API) | —; last push 2026-03-18 |
| license | MIT |
| plant_evidence | Generic proteins; 3D = protein structure. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-010 · WASP

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (protein 3D structure) |
| script | none |
| tools_card | F1+ [待确认: no card yet] |
| gates | Gate-F4 (versions) |
| what it does | Whole-proteome annotation via Foldseek against AlphaFold DB (GO, Pfam, PANTHER, CATH, Rhea, EC). |
| url | https://github.com/gioodm/wasp-proteins-annotation |
| doi | none found |
| venue / year | — |
| venue_label | — (no paper) |
| latest release (GitHub API) | v3.0 (2026-09-26); last push 2026-10-10 |
| license | MIT |
| plant_evidence | 3D-structure route for plant proteins without sequence hits. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-011 · PARSE

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (protein 3D structure) |
| script | none |
| tools_card | F1+ [待确认: no card yet] |
| gates | Gate-F4 (versions) |
| what it does | Functional site annotation from local 3D-structure embeddings. |
| url | — |
| doi | [10.1073/pnas.2513219122](https://doi.org/10.1073/pnas.2513219122) |
| venue / year | Proceedings of the National Academy of Sciences 2025 |
| venue_label | Below allowlist |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Generic. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-012 · metagenomic-DeepFRI

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (protein 3D structure) |
| script | none |
| tools_card | F1+ [待确认: no card yet] |
| gates | Gate-F4 (versions) |
| what it does | Scaled DeepFRI (GO from protein 3D-structure graphs) (preprint 2026). |
| url | — |
| doi | [10.64898/2026.04.27.720983](https://doi.org/10.64898/2026.04.27.720983) |
| venue / year | preprint 2026 |
| venue_label | Preprint |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Here 'structure' is protein 3D structure. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | needs evidence |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

## F1 · InterProScan step — domain resources

### GFA-F1-013 · SMART (2021 update)

| field | value |
|---|---|
| type | db |
| stage | F1 · InterProScan (domains) |
| script | `F3_interproscan.sh` |
| tools_card | F1c |
| gates | Gate-F4 (versions) |
| what it does | Signalling/extracellular domain resource (member DB of InterPro). |
| url | https://smart.embl.de |
| doi | [10.1093/nar/gkaa937](https://doi.org/10.1093/nar/gkaa937) |
| venue / year | Nucleic Acids Research 2020 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Receptor-like kinase / LRR domains in plants. |
| existing_doc | [`docs/steps/functional/F_AGGREGATE.md`](../../docs/steps/functional/F_AGGREGATE.md) |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | include — update to something already mentioned (not a new tool) |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-014 · CDD / CD-Search (2023)

| field | value |
|---|---|
| type | db |
| stage | F1 · InterProScan (domains) |
| script | `F3_interproscan.sh` |
| tools_card | F1c |
| gates | Gate-F4 (versions) |
| what it does | NCBI conserved-domain models and SPARCLE architectures. |
| url | https://www.ncbi.nlm.nih.gov/Structure/cdd/cdd.shtml |
| doi | [10.1093/nar/gkac1096](https://doi.org/10.1093/nar/gkac1096) |
| venue / year | Nucleic Acids Research 2022 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Second opinion on domain architecture. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-015 · Merizo

| field | value |
|---|---|
| type | tool |
| stage | F1 · InterProScan (domains) |
| script | `F3_interproscan.sh` |
| tools_card | F1c |
| gates | Gate-F4 (versions) |
| what it does | Domain segmentation of predicted 3D structures. |
| url | https://github.com/psipred/Merizo |
| doi | [10.1038/s41467-023-43934-4](https://doi.org/10.1038/s41467-023-43934-4) |
| venue / year | Nature Communications 2023 |
| venue_label | Allowlisted |
| latest release (GitHub API) | v1.0.0 (2023-10-13); last push 2025-05-22 |
| license | GPL-3.0 |
| plant_evidence | Split multi-domain plant proteins before structure search. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

## F1 · eggNOG-mapper step — cross-checks for transferred GO

### GFA-F1-016 · PLAZA 5.0

| field | value |
|---|---|
| type | db |
| stage | F1 · eggNOG-mapper (orthology-based GO/KEGG) |
| script | `F2_eggnog.sh` (a step inside framework F1) |
| tools_card | F1b |
| gates | Gate-F4 (versions) |
| what it does | Plant comparative genomics: gene families, orthologs, GO/InterPro projections. |
| url | https://bioinformatics.psb.ugent.be/plaza/ |
| doi | [10.1093/nar/gkab1024](https://doi.org/10.1093/nar/gkab1024) |
| venue / year | Nucleic Acids Research 2021 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Includes Vitis vinifera; good cross-check for transferred GO. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

## F1 · optional add-ons — machine-learning GO (electronic evidence only)

### GFA-F1-017 · DeepGO-SE

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (machine-learning GO) |
| script | none |
| tools_card | F1+ [待确认: no card yet] |
| gates | Gate-F4 (versions) |
| what it does | GO prediction as approximate semantic entailment over ESM2 embeddings and GO axioms. |
| url | https://github.com/bio-ontology-research-group/deepgo2 |
| doi | [10.1038/s42256-024-00795-w](https://doi.org/10.1038/s42256-024-00795-w) |
| venue / year | Nature Machine Intelligence 2024 |
| venue_label | Allowlisted |
| latest release (GitHub API) | v1.0.0 (2023-12-13); last push 2026-10-27 |
| license | BSD-3-Clause |
| plant_evidence | Generic; electronic evidence - keep as hypothesis. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-018 · ProtGO

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (machine-learning GO) |
| script | none |
| tools_card | F1+ [待确认: no card yet] |
| gates | Gate-F4 (versions) |
| what it does | Multi-modal GO prediction (PLM + text + taxonomy + GO graph). |
| url | https://github.com/sunyatawang/ProtGO |
| doi | [10.1093/bioinformatics/btaf390](https://doi.org/10.1093/bioinformatics/btaf390) |
| venue / year | Bioinformatics 2025 |
| venue_label | Below allowlist |
| latest release (GitHub API) | —; last push 2024-07-25 |
| license | no licence file |
| plant_evidence | Generic. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-019 · AltereGO

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (machine-learning GO) |
| script | none |
| tools_card | F1+ [待确认: no card yet] |
| gates | Gate-F4 (versions) |
| what it does | Score-level fusion of ESM2, ProtT5, Ankh and ProstT5-3Di predictors for GO molecular function (preprint 2026). |
| url | — |
| doi | [10.64898/2026.10.23.761425](https://doi.org/10.64898/2026.10.23.761425) |
| venue / year | preprint 2026 |
| venue_label | Preprint |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Low-homology proteins. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | needs evidence |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

## F1 · KofamScan step (optional)

### GFA-F1-020 · KEGG (2025 NAR)

| field | value |
|---|---|
| type | db |
| stage | F1 · KofamScan (optional) |
| script | `F1b_kofam.sh` (Kofam step, not card F1b) |
| tools_card | F1+ |
| gates | Gate-F4 (versions) |
| what it does | Current KEGG citation for KO/pathway mapping. |
| url | https://www.kegg.jp |
| doi | [10.1093/nar/gkae909](https://doi.org/10.1093/nar/gkae909) |
| venue / year | Nucleic Acids Research 2024 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Used via KofamScan (F1+) or eggNOG. |
| existing_doc | [`CONTRIBUTING.md`](../../CONTRIBUTING.md), [`README.md`](../../README.md), [`README.zh.md`](../../README.zh.md) |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | include — update to something already mentioned (not a new tool) |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

## F1 · optional add-ons — enzymes, CAZy and plant metabolic gene clusters

### GFA-F1-021 · CLEAN

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (enzymes, CAZy, plant BGC) |
| script | none |
| tools_card | F1+ [待确认: no card yet] |
| gates | Gate-F4 (versions) |
| what it does | Contrastive-learning EC number prediction. |
| url | https://github.com/tttianhao/CLEAN |
| doi | [10.1126/science.adf2465](https://doi.org/10.1126/science.adf2465) |
| venue / year | Science 2023 |
| venue_label | Allowlisted |
| latest release (GitHub API) | v1.0.1 (2023-03-31); last push 2025-04-06 |
| license | MIT |
| plant_evidence | Enzyme hypotheses for plant specialised metabolism. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-022 · EZpred

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (enzymes, CAZy, plant BGC) |
| script | none |
| tools_card | F1+ [待确认: no card yet] |
| gates | Gate-F4 (versions) |
| what it does | EC prediction using unlabeled sequence homologs (Advanced Science 2026). |
| url | — |
| doi | [10.1002/advs.78703](https://doi.org/10.1002/advs.78703) |
| venue / year | Advanced Science 2026 |
| venue_label | Below allowlist |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Generic enzymes.DOI looks unusual [待确认] |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | needs evidence |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-023 · ProteEC-CLA

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (enzymes, CAZy, plant BGC) |
| script | none |
| tools_card | F1+ [待确认: no card yet] |
| gates | Gate-F4 (versions) |
| what it does | EC prediction with contrastive learning + agent attention on ESM2. |
| url | — |
| doi | [10.1002/prot.26822](https://doi.org/10.1002/prot.26822) |
| venue / year | Proteins: Structure, Function, and Bioinformatics 2025 |
| venue_label | Below allowlist |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Generic enzymes. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-024 · plantiSMASH 2.0

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (enzymes, CAZy, plant BGC) |
| script | none |
| tools_card | F1+ [待确认: no card yet] |
| gates | Gate-F4 (versions) |
| what it does | Plant biosynthetic gene cluster detection, substrate prediction for some enzyme families, promoter TF sites; DB of ~30k BGCs over 430 genomes. |
| url | https://github.com/plantismash/plantismash |
| doi | [10.1016/j.jmb.2026.169798](https://doi.org/10.1016/j.jmb.2026.169798) |
| venue / year | Journal of Molecular Biology 2026 |
| venue_label | Below allowlist |
| latest release (GitHub API) | plantismash-2.0.4 (2025-10-25); last push 2026-02-26 |
| license | AGPL-3.0 |
| plant_evidence | Grapevine terpene/stilbene clusters. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-025 · dbCAN3

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (enzymes, CAZy, plant BGC) |
| script | none |
| tools_card | F1+ [待确认: no card yet] |
| gates | Gate-F4 (versions) |
| what it does | CAZyme and substrate annotation. |
| url | https://github.com/linnabrown/run_dbcan |
| doi | [10.1093/nar/gkad328](https://doi.org/10.1093/nar/gkad328) |
| venue / year | Nucleic Acids Research 2023 |
| venue_label | Allowlisted |
| latest release (GitHub API) | 4.1.4 (2024-01-23); last push 2025-04-23 |
| license | GPL-3.0 |
| plant_evidence | Cell-wall enzymes; already noted in this repo - cite NAR 2023. |
| existing_doc | [`docs/CITATIONS.md`](../../docs/CITATIONS.md), [`docs/RELATED_SOFTWARE.md`](../../docs/RELATED_SOFTWARE.md), [`docs/SCENARIOS_FUNCTIONAL.md`](../../docs/SCENARIOS_FUNCTIONAL.md) |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | release / version date recorded in METHODS (Gate-F4) |
| verdict | include — update to something already mentioned (not a new tool) |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

## F1 · optional add-ons — localization and topology

### GFA-F1-026 · DeepLoc 2.1

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (localization / topology) |
| script | none |
| tools_card | F1+ (Phobius/SignalP card exists) |
| gates | Gate-F4 (versions) |
| what it does | Subcellular localization + membrane protein type from PLMs. |
| url | https://services.healthtech.dtu.dk/services/DeepLoc-2.1/ |
| doi | [10.1093/nar/gkae237](https://doi.org/10.1093/nar/gkae237) |
| venue / year | Nucleic Acids Research 2024 |
| venue_label | Allowlisted |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Includes plastid class. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-027 · TargetP 2.0

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (localization / topology) |
| script | none |
| tools_card | F1+ (Phobius/SignalP card exists) |
| gates | Gate-F4 (versions) |
| what it does | N-terminal targeting peptides (signal, mitochondrial, chloroplast, thylakoid). |
| url | https://services.healthtech.dtu.dk/services/TargetP-2.0/ |
| doi | [10.26508/lsa.201900429](https://doi.org/10.26508/lsa.201900429) |
| venue / year | Life Science Alliance 2019 |
| venue_label | Below allowlist |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Plant organelle targeting. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | include |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

### GFA-F1-028 · DeepTMHMM

| field | value |
|---|---|
| type | tool |
| stage | F1 · optional add-on (localization / topology) |
| script | none |
| tools_card | F1+ (Phobius/SignalP card exists) |
| gates | Gate-F4 (versions) |
| what it does | Transmembrane topology prediction (preprint). |
| url | https://dtu.biolib.com/DeepTMHMM |
| doi | [10.1101/2022.04.08.487609](https://doi.org/10.1101/2022.04.08.487609) |
| venue / year | preprint 2022 |
| venue_label | Preprint |
| latest release (GitHub API) | — |
| license | — |
| plant_evidence | Generic. |
| existing_doc | none |
| io | `PROTEINS_FA` → per-protein hits table; join into `merged_function_table.tsv` via `F_aggregate.py` [待确认: no join written yet] |
| db_version_field | — |
| verdict | needs evidence |
| checked_at_CST | 2026-11-12 |
| checked_by | overnight survey (DOI via Crossref/DataCite, repo via GitHub API) |

[Back to catalog index](../README.md)
