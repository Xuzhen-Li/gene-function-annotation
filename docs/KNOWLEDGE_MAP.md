# Knowledge map

[中文](KNOWLEDGE_MAP.zh.md)

This page indexes every part of this repository, by topic and by kind of page. The repository is a knowledge base on functional annotation of plant proteins: the book explains each step, the catalogue compares software and databases, the reference workflow shows one way to run the steps, and the example code shows what a step looks like on small data. The layout follows [TE-Lib](https://github.com/Xuzhen-Li/TE-Lib).

TE-Lib was formerly named vitis-te. Older pages still use that name; GitHub redirects the old links.

- [Knowledge units and workflow index](#knowledge-units)
- [Topics](#topics)
- [Learn](#learn)
- [Reference workflow](#reference-workflow)
- [Software lists and sources](#software-lists-and-sources)
- [Example code and test data](#example-code)
- [Figures](#figures)
- [Older pages and corrections](#older-pages)
- [Other repository files](#other-files)

<a id="knowledge-units"></a>
## Knowledge units and workflow index

- [Functional gene annotation: an overview](kb/field-overview.md)
- [Functional labels and the four numbering schemes](kb/function-concepts.md)
- [Transferring function by homology and orthology](kb/homology-transfer.md)
- [How far to trust a function table (criteria)](kb/credibility-criteria.md)
- Numbering schemes: [`kb/NUMBERING.md`](kb/NUMBERING.md)
- Workflow index: [`workflow/README.md`](workflow/README.md)
- Full methods catalogue: [`catalog/METHODS_CATALOG.md`](../catalog/METHODS_CATALOG.md); [`catalog/README.by-type.md`](../catalog/README.by-type.md); [`catalog/COUNTS.md`](../catalog/COUNTS.md)
- Overlap of docs/tools and docs/notes: [`TOOLS_NOTES_OVERLAP.md`](TOOLS_NOTES_OVERLAP.md)

<a id="topics"></a>
## Topics

Each topic lists the book chapter that explains it, the catalogue section that compares the tools, and, where they exist, notes on single tools, tool cards with commands, first-pass step cards, other pages and the example code.

### Concepts and principles

- Book: [Chapter 1. Concepts and principles](../book/chapters/01-concepts.md)

### Input protein QC (F0)

- Catalogue: [Data needed alongside the input, in the Methods catalog](../catalog/METHODS_CATALOG.md#data-needs)
- Tool cards: [BUSCO — protein completeness (F0)](../docs/tools/busco.md)
- First-pass step cards: [F0 · protein input QC (BUSCO protein mode)](../catalog/F0_protein_qc/README.md)
- Example code and data: [`F0_clean_proteins.py`](../pipeline/F0_clean_proteins.py)

### 1. Homology search

- Book: [Chapter 2. Homology search](../book/chapters/02-homology-search.md)
- Catalogue: [section 1 of the Methods catalog](../catalog/METHODS_CATALOG.md#section-1)
- Tool cards: [DIAMOND — SwissProt hits for names / AHRD](../docs/tools/diamond_func.md)
- Example code and data: [`F1_diamond.sh`](../pipeline/F1_diamond.sh)

### 2. Reference sequence and ontology databases

- Book: [Chapter 3. Reference sequence and ontology databases](../book/chapters/03-reference-sequence-and-ontology-databases.md)
- Catalogue: [section 2 of the Methods catalog](../catalog/METHODS_CATALOG.md#section-2)
- First-pass step cards: [Database index](../catalog/_databases.md)

### 3. Domain and family annotation

- Book: [Chapter 4. Domain and family annotation](../book/chapters/04-domain-and-family-annotation.md)
- Catalogue: [section 3 of the Methods catalog](../catalog/METHODS_CATALOG.md#section-3)
- Tool cards: [InterProScan — domains and GO](../docs/tools/interproscan.md)
- Example code and data: [`F3_interproscan.sh`](../pipeline/F3_interproscan.sh)

### 4. Orthology-based names, GO and KEGG

- Book: [Chapter 5. Orthology-based names, GO and KEGG](../book/chapters/05-orthology-based-names-go-and-kegg.md)
- Catalogue: [section 4 of the Methods catalog](../catalog/METHODS_CATALOG.md#section-4)
- Notes on single tools: [AHRD + eifunannot](../docs/notes/ahrd_eifunannot.md); [eggnogdb/eggnog-mapper](../docs/notes/eggnog.md); [EnTAP (PlantGenomicsLab)](../docs/notes/entap.md); [funannotate2-addons (FA peer)](../docs/notes/funannotate2_addons_fa.md); [Trinotate](../docs/notes/trinotate.md)
- Tool cards: [AHRD — human-readable descriptions](../docs/tools/ahrd.md); [Blast2GO-style path without a commercial licence](../docs/tools/blast2go_style.md); [eggNOG-mapper — orthology-aware transfer (F1 step / optional fast frame)](../docs/tools/eggnog_mapper.md); [EnTAP](../docs/tools/entap.md); [PANNZER2 — GO + descriptions (Camellia T2T FA stack)](../docs/tools/pannzer2.md); [Trinotate](../docs/tools/trinotate.md)
- First-pass step cards: [F4 · readable names (AHRD, PANNZER2)](../catalog/F4_readable_names/README.md)
- Example code and data: [`F2_eggnog.sh`](../pipeline/F2_eggnog.sh); [`F4_join_ahrd.py`](../pipeline/F4_join_ahrd.py); [F4 — run AHRD then join](../pipeline/F4_run_ahrd.md); [`F4b_join_pannzer.py`](../pipeline/F4b_join_pannzer.py)

### 5. Machine-learning GO prediction

- Book: [Chapter 6. Machine-learning GO prediction](../book/chapters/06-machine-learning-go-prediction.md)
- Catalogue: [section 5 of the Methods catalog](../catalog/METHODS_CATALOG.md#section-5)
- Notes on single tools: [DeepFRI](../docs/notes/deepfri.md); [DeepGOPlus (and DeepGO family)](../docs/notes/deepgoplus.md); [NetGO 3.0](../docs/notes/netgo3.md); [ProteInfer](../docs/notes/proteinfer.md)

### 6. Pathways, KO and EC

- Book: [Chapter 7. Pathways, KO and EC](../book/chapters/07-pathways-ko-and-ec.md)
- Catalogue: [section 6 of the Methods catalog](../catalog/METHODS_CATALOG.md#section-6)
- Notes on single tools: [DeepKOALA (+ BlastKOALA / GhostKOALA)](../docs/notes/deepkoala.md); [BlastKOALA / GhostKOALA](../docs/notes/ghostkoala.md)
- Tool cards: [KEGGaNOG — pathway heatmaps from eggNOG](../docs/tools/kegganog.md); [KofamScan — KEGG KO on proteins](../docs/tools/kofamscan.md); [Mercator4 / MapMan4](../docs/tools/mercator.md)
- First-pass step cards: [F6 · MapMan BINs (Mercator4) and plant pathway views](../catalog/F6_mapman/README.md)
- Other pages: [Mercator4 — when to use the web (F6)](../docs/MERCATOR_WHEN.md)
- Example code and data: [`F1b_kofam.sh`](../pipeline/F1b_kofam.sh); [`F6_ingest_mercator.py`](../pipeline/F6_ingest_mercator.py)

### 7. Multi-genome orthology

- Book: [Chapter 8. Multi-genome orthology](../book/chapters/08-multi-genome-orthology.md)
- Catalogue: [section 7 of the Methods catalog](../catalog/METHODS_CATALOG.md#section-7)
- First-pass step cards: [F7 · multi-genome orthogroups (OrthoFinder)](../catalog/F7_multi_genome/README.md)
- Example code and data: [`F7_orthofinder.sh`](../pipeline/F7_orthofinder.sh)

### 8. Localization and topology

- Book: [Chapter 9. Localization and topology](../book/chapters/09-localization-and-topology.md)
- Catalogue: [section 8 of the Methods catalog](../catalog/METHODS_CATALOG.md#section-8)
- Notes on single tools: [dbCAN3 · DeepLoc 2.0 · SignalP 6.0](../docs/notes/dbcan_deeploc_signalp.md)
- Tool cards: [Phobius / SignalP — secreted & TM (GeneForge-style)](../docs/tools/phobius_signalp.md)

### 9. Plant gene families

- Book: [Chapter 10. Plant gene families](../book/chapters/10-plant-gene-families.md)
- Catalogue: [section 9 of the Methods catalog](../catalog/METHODS_CATALOG.md#section-9)
- Tool cards: [HRP — NB-LRR / NLR helpers](../docs/tools/hrp.md); [iTAK — plant TF / TR / kinases](../docs/tools/itak.md)
- First-pass step cards: [F8 · NLR protein classification (IPS filter ± HRP)](../catalog/F8_nlr/README.md); [F9 · transcription factors / kinases (iTAK)](../catalog/F9_tf_kinase/README.md)
- Example code and data: [`F8_list_nlr_from_ips.py`](../pipeline/F8_list_nlr_from_ips.py); [`F8_run.sh`](../pipeline/F8_run.sh); [`F8b_nlr_to_families.py`](../pipeline/F8b_nlr_to_families.py); [`F9_itak.sh`](../pipeline/F9_itak.sh)

### 10. Non-coding RNA function resources

- Book: [Chapter 11. Non-coding RNA function resources](../book/chapters/11-non-coding-rna-function-resources.md)
- Catalogue: [section 10 of the Methods catalog](../catalog/METHODS_CATALOG.md#section-10)

### 11. Expression-supported function

- Book: [Chapter 12. Expression-supported function](../book/chapters/12-expression-supported-function.md)
- Catalogue: [section 11 of the Methods catalog](../catalog/METHODS_CATALOG.md#section-11)

### 12. Community catalogues and naming

- Book: [Chapter 13. Community catalogues and naming](../book/chapters/13-community-catalogues-and-naming.md)
- Catalogue: [section 12 of the Methods catalog](../catalog/METHODS_CATALOG.md#section-12)
- First-pass step cards: [Cross-stage: whole pipelines, non-protein resources and downstream pointers](../catalog/X_cross_stage/README.md)

### 13. Protein 3D structure

- Book: [Chapter 14. Protein 3D structure](../book/chapters/14-protein-3d-structure.md)
- Catalogue: [section 13 of the Methods catalog](../catalog/METHODS_CATALOG.md#section-13)

### 14. Downstream enrichment

- Book: [Chapter 15. Downstream enrichment](../book/chapters/15-downstream-enrichment.md)
- Catalogue: [section 14 of the Methods catalog](../catalog/METHODS_CATALOG.md#section-14)

### 15. Ideas, formats and merge rules

- Book: [Chapter 16. Ideas, formats and merge rules](../book/chapters/16-ideas-formats-and-merge-rules.md)
- Catalogue: [section 15 of the Methods catalog](../catalog/METHODS_CATALOG.md#section-15)
- First-pass step cards: [Merge / aggregate (`F_merge_tables.py`, `F_aggregate.py`)](../catalog/Fmerge_aggregate/README.md); [Release (`F_release.sh`, Gate-F1–F7)](../catalog/Frelease/README.md); [Four numbering systems](../catalog/_namespaces.md)
- Example code and data: [`F_aggregate.py`](../pipeline/F_aggregate.py); [`F_merge_tables.py`](../pipeline/F_merge_tables.py); [`F_release.sh`](../pipeline/F_release.sh); [pipeline/schema/ (`pipeline/schema/`)](../pipeline/schema/)

### Visualization tools

- Book: [Chapter 17. Visualization tools](../book/chapters/17-visualization-tools.md)
- Catalogue: [Visualization tools in the Methods catalog](../catalog/METHODS_CATALOG.md#visualization)

### Choosing a frame and add-ons

- Book: [Chapter 18. Choosing a frame and add-ons](../book/chapters/18-choosing-tools.md)
- First-pass step cards: [F1](../catalog/frame_F1/README.md); [F2 · fast framework (eggNOG-mapper alone ± Kofam; KEGGaNOG plots)](../catalog/frame_F2/README.md); [F3 · EnTAP framework](../catalog/frame_F3/README.md); [F5 · Trinotate framework (transcriptome CDS)](../catalog/frame_F5/README.md)

### Pitfalls and quality control

- Book: [Chapter 19. Pitfalls and quality control](../book/chapters/19-pitfalls-and-qc.md)
- First-pass step cards: [F10 · function-table QC](../catalog/F10_function_qc/README.md)
- Example code and data: [`F10_function_qc.py`](../pipeline/F10_function_qc.py)

### Worked example: grapevine proteins through frame F1 and add-on F8

- Book: [Chapter 20. Worked example: grapevine proteins through frame F1 and add-on F8](../book/chapters/20-worked-example.md)
- Example code and data: [Plant simulation trio (`examples/plant_sim/`)](../examples/plant_sim/README.md)

### Glossary

- Book: [Appendix A. Glossary](../book/chapters/appendix-a-glossary.md)

<a id="learn"></a>
## Learn

- Book: [Plant gene function annotation: a study guide with grapevine as the example](../book/README.md); [Plant gene function annotation: a study guide with grapevine as the example](../book/BOOK_full.md); [Book file index · 全书文件索引](../book/INDEX.md); [Preface](../book/chapters/00-preface.md)
- Bilingual pages: [Bilingual teaching track](../docs/BILINGUAL.md)
- Chinese teaching pages (26):
  - [为什么要做功能注释？](zh/00_为什么要做功能注释.md)
  - [什么是基因功能注释？](zh/01_什么是功能注释.md)
  - [和结构注释的关系](zh/02_和结构注释的关系.md)
  - [怎么开始跑（功能注释）](zh/03_怎么开始跑.md)
  - [F 线怎么选](zh/04_F线怎么选.md)
  - [F0：蛋白 BUSCO（开工前的急刹车）](zh/05_F0蛋白BUSCO.md)
  - [F1 精讲：DIAMOND + eggNOG + InterProScan](zh/06_F1精讲_DIAMOND_eggNOG_IPS.md)
  - [替代框架：F2 / F3 / F5](zh/07_替代框架_F2F3F5.md)
  - [植物加件：F4 / F6 / F8 / F9（+ F7 简述）](zh/08_植物加件_F4F6F8F9.md)
  - [合并与放行](zh/09_合并与放行.md)
  - [验收：F-L0 / F-L1](zh/10_验收_FL0_FL1.md)
  - [flow 工具怎么用（功能）](zh/11_flow工具怎么用.md)
  - [常见翻车（功能注释）](zh/12_常见翻车.md)
  - [为什么 F1 是「三件套」？](zh/13_为什么F1是三件套.md)
  - [为什么先结构后功能？](zh/14_为什么先结构后功能.md)
  - [为什么版本和谱系必须写清？](zh/15_为什么版本和谱系必须写清.md)
  - [外部软件流程教程与会议（功能）](zh/17_外部教程与会议.md)
  - [术语表（功能注释教学）](zh/99_术语表.md)
  - [中文指针](zh/DB_INSTALL_CHECKLIST.md)
  - [入门 FAQ（功能仓）](zh/FAQ_入门.md)
  - [中文指针](zh/MERCATOR_WHEN.md)
  - [中文教学入口](zh/README.md)
  - [中文指针](zh/golden_pack.md)
  - [交接指针](zh/交接_结构到功能.md)
  - [读 plan 时看什么（英文 plan 指针）](zh/读plan.md)
  - [功能注释](zh/验收勾选表.md)

<a id="reference-workflow"></a>
## Reference workflow

These pages give one reference route, how to choose a branch and how to check the result. They are part of the knowledge base, not a maintained software package.

- [Start here — gene function](../docs/START_HERE.md)
- [Quickstart — functional annotation (second layer)](../docs/QUICKSTART.md)
- [Branch roadmap — gene function](../docs/ROADMAP.md)
- [Gene function playbook — proteins to master TSV](../docs/PLAYBOOK.md)
- [Detailed guide — structural copy removed](../docs/DETAILED_GUIDE.md)
- [Full pipeline index — structural half moved](../docs/FULL_PIPELINE.md)
- [Functional annotation — complete copy-paste guide](../docs/FUNCTIONAL_GUIDE.md)
- [METHODS template — functional annotation](../docs/METHODS_FUNCTIONAL.md)
- [Main process — functional annotation](../docs/steps/FUNCTIONAL_MAIN.md)
- [Functional steps (F0–F9) (`docs/steps/functional/`)](../docs/steps/functional/README.md)
- [Stage I/O — functional annotation](../docs/STAGE_IO.md)
- [Structural scenarios — moved](../docs/SCENARIOS.md)
- [Functional scenarios F1–F8 (every command in-repo)](../docs/SCENARIOS_FUNCTIONAL.md)
- [After structure — function one-pager](../docs/POST_STRUCTURE.md)
- [Boundary — one-liner](../docs/BOUNDARY.md)
- [Handoff card — structure → function](../docs/HANDOFF_STRUCTURE_TO_FUNCTION.md)
- [Install everything for functional annotation (copy this)](../docs/INSTALL_FUNCTIONAL.md)
- [F1 database install checklist](../docs/DB_INSTALL_CHECKLIST.md)
- [Preflight check before RUN=1 / 运行前检查](../docs/PREFLIGHT.md)
- [Flow tool — progressive automation (FA)](../docs/FLOW_TOOL.md)
- [Final evaluation criteria — gene function](../docs/EVALUATION.md)
- [Function release checklist (pass / fail)](../docs/EVALUATION_CHECKLIST.md)
- [AI-assisted functional annotation — prompts, data, order, checks](../docs/AI_ASSIST.md)

<a id="software-lists-and-sources"></a>
## Software lists and sources

- [Software guide by analysis step](../docs/software/README.md)
- [`SOFTWARE_AUTHORITY.tsv`](../catalog/SOFTWARE_AUTHORITY.tsv)
- [Catalog — new functional tools, databases and ideas by stage (2026-11)](../catalog/README.md)
- [Tools — functional annotation](../docs/TOOLS.md)
- [Related software](../docs/RELATED_SOFTWARE.md)
- [Functional annotation quality — methods, papers, repos](../docs/QUALITY_SOURCES.md)
- [Overview papers and benchmarks behind these pages](../docs/REVIEWS.md)
- [High-quality annotation sources — journal allowlist only](../docs/RECENT_HIGH_QUALITY.md)
- [Citations](../docs/CITATIONS.md)
- [External tutorials & meetings — gene function](../docs/TUTORIALS_AND_MEETINGS.md)

<a id="example-code"></a>
## Example code and test data

The example code shows how each step is done. It is small and tested on toy data. Step scripts are listed under their topic above; this list has the shared parts.

- [Pipeline overview — function layer only](../pipeline/00_overview.md)
- [flow_tool (function) — step 1 (`pipeline/flow_tool/`)](../pipeline/flow_tool/README.md) · 3 files
- [`preflight.py`](../pipeline/preflight.py)
- [`print_qc_commands.py`](../pipeline/print_qc_commands.py)
- [`check_release_pack.py`](../pipeline/check_release_pack.py)
- [`_env_guards.sh`](../pipeline/_env_guards.sh)
- [`sbatch_f1_examples.sh`](../pipeline/sbatch_f1_examples.sh)
- [config/ (`config/`)](../config/) · 2 files
- [tests/ (`tests/`)](../tests/) · 4 files
- [testdata/ (`testdata/`)](../testdata/) · 18 files

<a id="figures"></a>
## Figures

- [Figures](../docs/figures/README.md); [Figures for the guide](../docs/figures/guide/README.md) · 46 files

<a id="older-pages"></a>
## Older pages and corrections

These pages are kept as a record and are unchanged. The sections above hold the current material.

| Page | Note |
|---|---|
| [Audit 2026-09-14 — gene-function-annotation](../docs/AUDIT_2026-09-14.md) | A check of these pages against the literature, dated 2026-09-14. |
| [Self-audit — gene-function-annotation](../docs/SELF_AUDIT.md) | A self-check of the frame chooser and peer list, dated 2026-09-14. |
| [Software, databases and ideas by type (functional) — 2026-11](../docs/CATALOG_BY_TYPE_2026-11.md) | The first 2026-11 list by type. The current catalogue is the Methods catalog on the home page and catalog/SOFTWARE_AUTHORITY.tsv. |
| [New tools, databases and ideas by step (functional) — 2026-11 survey](../docs/CATALOG_NEW_TOOLS_2026-11.md) | The first 2026-11 list by stage. The current catalogue is the same as above. |
| [Erratum to gene-function-annotation catalog v4 (NLR-Annotator, NLRSeek, plantiSMASH 2.0)](../docs/CATALOG_NEW_TOOLS_2026-11_ERRATUM_NLR_PLANTISMASH.md) | A correction to the 2026-11 list (NLR-Annotator, NLRSeek, plantiSMASH 2.0). |
| [Erratum: GSAman tool paper vs last-mile opinion DOI](../docs/GSAMAN_DOI_ERRATUM.md) | A correction on which DOI belongs to the GSAman tool paper. |
| [Classroom tonight (function) — offline mirror](../docs/CLASSROOM_TONIGHT.md) | An offline copy of a one-evening class checklist from the wiki. The current start page is docs/START_HERE.md. |
| [Structural main process — moved](../docs/steps/MAIN.md) | A pointer page: the structural route lives in gene-structure-annotation. |
| [Structural error classes — moved](../docs/ERROR_CLASSES.md) | A pointer page: gene-model error classes live in gene-structure-annotation. |
| [Wiki page Start-tonight](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Start-tonight) | A wiki page for a first evening, not in the clone. |
| [Annotation board (Project #2)](https://github.com/users/Xuzhen-Li/projects/2) | A task board for the annotation repositories. |

<a id="other-files"></a>
## Other repository files

- `.github/` · 5 files
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `README.zh.md`
- `CHANGELOG.md`
- `LICENSE`
- `NOTICE.md`
