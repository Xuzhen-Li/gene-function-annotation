# 知识地图

[English](KNOWLEDGE_MAP.md)

本页按主题和页面类型列出本仓库的全部内容。本仓库是关于植物蛋白的功能注释的知识库：书讲清每一步，目录比较软件和数据库，参考流程给出一种跑法，示例代码展示每一步在小数据上的样子。结构与 [TE-Lib](https://github.com/Xuzhen-Li/TE-Lib) 一致。

TE-Lib 原名 vitis-te。较早的页面仍用旧名，GitHub 会把旧链接转到新地址。

- [知识单元与流程索引](#knowledge-units)
- [主题](#topics)
- [学习](#learn)
- [参考流程](#reference-workflow)
- [软件清单与来源](#software-lists-and-sources)
- [示例代码与测试数据](#example-code)
- [图](#figures)
- [旧页面与勘误](#older-pages)
- [其他文件](#other-files)

<a id="knowledge-units"></a>
## 知识单元与流程索引

- [功能基因注释：概览](kb/field-overview.zh.md)
- [功能标签与四套编号](kb/function-concepts.zh.md)
- [按同源和直系同源转移功能](kb/homology-transfer.zh.md)
- [功能表可信到什么程度（判据）](kb/credibility-criteria.zh.md)
- 编号对照: [`kb/NUMBERING.zh.md`](kb/NUMBERING.zh.md)
- 流程索引: [`workflow/README.zh.md`](workflow/README.zh.md)
- 完整方法目录: [`catalog/METHODS_CATALOG.zh.md`](../catalog/METHODS_CATALOG.zh.md); [`catalog/README.by-type.zh.md`](../catalog/README.by-type.zh.md); [`catalog/COUNTS.md`](../catalog/COUNTS.md)
- docs/tools 与 docs/notes 的重叠: [`TOOLS_NOTES_OVERLAP.md`](TOOLS_NOTES_OVERLAP.md)

<a id="topics"></a>
## 主题

每个主题列出讲解它的书章、比较工具的目录小节，以及（如果有）单个工具笔记、带命令的工具卡片、早期步骤卡片、其他页面和示例代码。工具卡片和笔记多为英文。

### 概念与原理

- 书：[第 1 章 概念与原理](../book/chapters/01-concepts.zh.md)

### 输入蛋白质控（F0）

- 目录：[方法目录中的“还需要的数据”一节](../catalog/METHODS_CATALOG.zh.md#data-needs)
- 工具卡片：[BUSCO — protein completeness (F0)](../docs/tools/busco.md)
- 早期步骤卡片：[F0 · protein input QC (BUSCO protein mode)](../catalog/F0_protein_qc/README.md)
- 示例代码与数据：[`F0_clean_proteins.py`](../pipeline/F0_clean_proteins.py)

### 1. 同源搜索

- 书：[第 2 章 同源搜索](../book/chapters/02-homology-search.zh.md)
- 目录：[方法目录第 1 节](../catalog/METHODS_CATALOG.zh.md#section-1)
- 工具卡片：[DIAMOND — SwissProt hits for names / AHRD](../docs/tools/diamond_func.md)
- 示例代码与数据：[`F1_diamond.sh`](../pipeline/F1_diamond.sh)

### 2. 参考序列与本体数据库

- 书：[第 3 章 参考序列与本体数据库](../book/chapters/03-reference-sequence-and-ontology-databases.zh.md)
- 目录：[方法目录第 2 节](../catalog/METHODS_CATALOG.zh.md#section-2)
- 早期步骤卡片：[Database index](../catalog/_databases.md)

### 3. 结构域与家族注释

- 书：[第 4 章 结构域与家族注释](../book/chapters/04-domain-and-family-annotation.zh.md)
- 目录：[方法目录第 3 节](../catalog/METHODS_CATALOG.zh.md#section-3)
- 工具卡片：[InterProScan — domains and GO](../docs/tools/interproscan.md)
- 示例代码与数据：[`F3_interproscan.sh`](../pipeline/F3_interproscan.sh)

### 4. 基于直系同源的名称、GO 与 KEGG

- 书：[第 5 章 基于直系同源的名称、GO 与 KEGG](../book/chapters/05-orthology-based-names-go-and-kegg.zh.md)
- 目录：[方法目录第 4 节](../catalog/METHODS_CATALOG.zh.md#section-4)
- 单个工具笔记：[AHRD + eifunannot](../docs/notes/ahrd_eifunannot.md); [eggnogdb/eggnog-mapper](../docs/notes/eggnog.md); [EnTAP (PlantGenomicsLab)](../docs/notes/entap.md); [funannotate2-addons (FA peer)](../docs/notes/funannotate2_addons_fa.md); [Trinotate](../docs/notes/trinotate.md)
- 工具卡片：[AHRD — human-readable descriptions](../docs/tools/ahrd.md); [不需商业许可的 Blast2GO 式路线](../docs/tools/blast2go_style.md); [eggNOG-mapper — orthology-aware transfer (F1 step / optional fast frame)](../docs/tools/eggnog_mapper.md); [EnTAP](../docs/tools/entap.md); [PANNZER2 — GO + descriptions (Camellia T2T FA stack)](../docs/tools/pannzer2.md); [Trinotate](../docs/tools/trinotate.md)
- 早期步骤卡片：[F4 · readable names (AHRD, PANNZER2)](../catalog/F4_readable_names/README.md)
- 示例代码与数据：[`F2_eggnog.sh`](../pipeline/F2_eggnog.sh); [`F4_join_ahrd.py`](../pipeline/F4_join_ahrd.py); [F4 — run AHRD then join](../pipeline/F4_run_ahrd.md); [`F4b_join_pannzer.py`](../pipeline/F4b_join_pannzer.py)

### 5. 机器学习 GO 预测

- 书：[第 6 章 机器学习 GO 预测](../book/chapters/06-machine-learning-go-prediction.zh.md)
- 目录：[方法目录第 5 节](../catalog/METHODS_CATALOG.zh.md#section-5)
- 单个工具笔记：[DeepFRI](../docs/notes/deepfri.md); [DeepGOPlus (and DeepGO family)](../docs/notes/deepgoplus.md); [NetGO 3.0](../docs/notes/netgo3.md); [ProteInfer](../docs/notes/proteinfer.md)

### 6. 通路、KO 与 EC

- 书：[第 7 章 通路、KO 与 EC](../book/chapters/07-pathways-ko-and-ec.zh.md)
- 目录：[方法目录第 6 节](../catalog/METHODS_CATALOG.zh.md#section-6)
- 单个工具笔记：[DeepKOALA (+ BlastKOALA / GhostKOALA)](../docs/notes/deepkoala.md); [BlastKOALA / GhostKOALA](../docs/notes/ghostkoala.md)
- 工具卡片：[KEGGaNOG — pathway heatmaps from eggNOG](../docs/tools/kegganog.md); [KofamScan — KEGG KO on proteins](../docs/tools/kofamscan.md); [Mercator4 / MapMan4](../docs/tools/mercator.md)
- 早期步骤卡片：[F6 · MapMan BINs (Mercator4) and plant pathway views](../catalog/F6_mapman/README.md)
- 其他页面：[Mercator4 — when to use the web (F6)](../docs/MERCATOR_WHEN.md)
- 示例代码与数据：[`F1b_kofam.sh`](../pipeline/F1b_kofam.sh); [`F6_ingest_mercator.py`](../pipeline/F6_ingest_mercator.py)

### 7. 多基因组直系同源

- 书：[第 8 章 多基因组直系同源](../book/chapters/08-multi-genome-orthology.zh.md)
- 目录：[方法目录第 7 节](../catalog/METHODS_CATALOG.zh.md#section-7)
- 早期步骤卡片：[F7 · multi-genome orthogroups (OrthoFinder)](../catalog/F7_multi_genome/README.md)
- 示例代码与数据：[`F7_orthofinder.sh`](../pipeline/F7_orthofinder.sh)

### 8. 定位与拓扑

- 书：[第 9 章 定位与拓扑](../book/chapters/09-localization-and-topology.zh.md)
- 目录：[方法目录第 8 节](../catalog/METHODS_CATALOG.zh.md#section-8)
- 单个工具笔记：[dbCAN3 · DeepLoc 2.0 · SignalP 6.0](../docs/notes/dbcan_deeploc_signalp.md)
- 工具卡片：[Phobius / SignalP — secreted & TM (GeneForge-style)](../docs/tools/phobius_signalp.md)

### 9. 植物基因家族

- 书：[第 10 章 植物基因家族](../book/chapters/10-plant-gene-families.zh.md)
- 目录：[方法目录第 9 节](../catalog/METHODS_CATALOG.zh.md#section-9)
- 工具卡片：[HRP — NB-LRR / NLR helpers](../docs/tools/hrp.md); [iTAK — plant TF / TR / kinases](../docs/tools/itak.md)
- 早期步骤卡片：[F8 · NLR protein classification (IPS filter ± HRP)](../catalog/F8_nlr/README.md); [F9 · transcription factors / kinases (iTAK)](../catalog/F9_tf_kinase/README.md)
- 示例代码与数据：[`F8_list_nlr_from_ips.py`](../pipeline/F8_list_nlr_from_ips.py); [`F8_run.sh`](../pipeline/F8_run.sh); [`F8b_nlr_to_families.py`](../pipeline/F8b_nlr_to_families.py); [`F9_itak.sh`](../pipeline/F9_itak.sh)

### 10. 非编码 RNA 功能资源

- 书：[第 11 章 非编码 RNA 功能资源](../book/chapters/11-non-coding-rna-function-resources.zh.md)
- 目录：[方法目录第 10 节](../catalog/METHODS_CATALOG.zh.md#section-10)

### 11. 表达支持的功能

- 书：[第 12 章 表达支持的功能](../book/chapters/12-expression-supported-function.zh.md)
- 目录：[方法目录第 11 节](../catalog/METHODS_CATALOG.zh.md#section-11)

### 12. 社区目录与命名

- 书：[第 13 章 社区目录与命名](../book/chapters/13-community-catalogues-and-naming.zh.md)
- 目录：[方法目录第 12 节](../catalog/METHODS_CATALOG.zh.md#section-12)
- 早期步骤卡片：[跨阶段：整套流程、非蛋白资源与下游指引](../catalog/X_cross_stage/README.md)

### 13. 蛋白三维结构

- 书：[第 14 章 蛋白三维结构](../book/chapters/14-protein-3d-structure.zh.md)
- 目录：[方法目录第 13 节](../catalog/METHODS_CATALOG.zh.md#section-13)

### 14. 下游富集

- 书：[第 15 章 下游富集](../book/chapters/15-downstream-enrichment.zh.md)
- 目录：[方法目录第 14 节](../catalog/METHODS_CATALOG.zh.md#section-14)

### 15. 想法、格式与合并规则

- 书：[第 16 章 想法、格式与合并规则](../book/chapters/16-ideas-formats-and-merge-rules.zh.md)
- 目录：[方法目录第 15 节](../catalog/METHODS_CATALOG.zh.md#section-15)
- 早期步骤卡片：[Merge / aggregate (`F_merge_tables.py`, `F_aggregate.py`)](../catalog/Fmerge_aggregate/README.md); [Release (`F_release.sh`, Gate-F1–F7)](../catalog/Frelease/README.md); [Four numbering systems](../catalog/_namespaces.md)
- 示例代码与数据：[`F_aggregate.py`](../pipeline/F_aggregate.py); [`F_merge_tables.py`](../pipeline/F_merge_tables.py); [`F_release.sh`](../pipeline/F_release.sh); [pipeline/schema/ (`pipeline/schema/`)](../pipeline/schema/)

### 可视化工具

- 书：[第 17 章 可视化工具](../book/chapters/17-visualization-tools.zh.md)
- 目录：[方法目录中的可视化工具](../catalog/METHODS_CATALOG.zh.md#visualization)

### 怎么选框架和加件

- 书：[第 18 章 怎么选框架和加件](../book/chapters/18-choosing-tools.zh.md)
- 早期步骤卡片：[F1](../catalog/frame_F1/README.md); [F2 · fast framework (eggNOG-mapper alone ± Kofam; KEGGaNOG plots)](../catalog/frame_F2/README.md); [F3 · EnTAP framework](../catalog/frame_F3/README.md); [F5 · Trinotate framework (transcriptome CDS)](../catalog/frame_F5/README.md)

### 常见问题与质控

- 书：[第 19 章 常见问题与质控](../book/chapters/19-pitfalls-and-qc.zh.md)
- 早期步骤卡片：[F10 · function-table QC](../catalog/F10_function_qc/README.md)
- 示例代码与数据：[`F10_function_qc.py`](../pipeline/F10_function_qc.py)

### 实例：葡萄蛋白走 F1 框架加 F8 加件

- 书：[第 20 章 实例：葡萄蛋白走 F1 框架加 F8 加件](../book/chapters/20-worked-example.zh.md)
- 示例代码与数据：[植物模拟三例 (`examples/plant_sim/`)](../examples/plant_sim/README.md)

### 术语表

- 书：[附录 A 术语表](../book/chapters/appendix-a-glossary.zh.md)

<a id="learn"></a>
## 学习

- 书：[《植物基因功能注释学习笔记：以葡萄为例》](../book/README.zh.md); [《植物基因功能注释学习笔记：以葡萄为例》](../book/BOOK_full.zh.md); [Book file index · 全书文件索引](../book/INDEX.md); [前言](../book/chapters/00-preface.zh.md)
- 双语说明：[Bilingual teaching track](../docs/BILINGUAL.md)
- 中文教学页（26）：
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
## 参考流程

下列页面给出一条参考路线，以及怎样选分支、怎样检查结果。它们是知识库的一部分，不是维护中的软件。

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
## 软件清单与来源

- [按分析步骤整理的软件指南](../docs/software/README.zh.md)
- [`SOFTWARE_AUTHORITY.tsv`](../catalog/SOFTWARE_AUTHORITY.tsv)
- [Catalog — new functional tools, databases and ideas by stage (2026-11)](../catalog/README.md)
- [Tools — functional annotation](../docs/TOOLS.md)
- [Related software](../docs/RELATED_SOFTWARE.md)
- [Functional annotation quality — methods, papers, repos](../docs/QUALITY_SOURCES.md)
- [支撑本仓库的综述与评测论文](../docs/REVIEWS.md)
- [High-quality annotation sources — journal allowlist only](../docs/RECENT_HIGH_QUALITY.md)
- [Citations](../docs/CITATIONS.md)
- [External tutorials & meetings — gene function](../docs/TUTORIALS_AND_MEETINGS.md)

<a id="example-code"></a>
## 示例代码与测试数据

示例代码展示每一步怎么做，规模很小，在玩具数据上测试过。各步的脚本已在上面对应主题下列出，这里只列通用部分。

- [Pipeline overview — function layer only](../pipeline/00_overview.md)
- [flow_tool (function) — step 1 (`pipeline/flow_tool/`)](../pipeline/flow_tool/README.md) · 3 个文件
- [`preflight.py`](../pipeline/preflight.py)
- [`print_qc_commands.py`](../pipeline/print_qc_commands.py)
- [`check_release_pack.py`](../pipeline/check_release_pack.py)
- [`_env_guards.sh`](../pipeline/_env_guards.sh)
- [`sbatch_f1_examples.sh`](../pipeline/sbatch_f1_examples.sh)
- [config/ (`config/`)](../config/) · 2 个文件
- [tests/ (`tests/`)](../tests/) · 4 个文件
- [testdata/ (`testdata/`)](../testdata/) · 18 个文件

<a id="figures"></a>
## 图

- [Figures](../docs/figures/README.md); [Figures for the guide](../docs/figures/guide/README.md) · 46 个文件

<a id="older-pages"></a>
## 旧页面与勘误

下列页面保留作历史记录，内容未改。当前内容以上面各节为准。

| 页面 | 说明 |
|---|---|
| [Audit 2026-09-14 — gene-function-annotation](../docs/AUDIT_2026-09-14.md) | 2026-09-14 对照文献检查本仓库各页的记录。 |
| [Self-audit — gene-function-annotation](../docs/SELF_AUDIT.md) | 2026-09-14 对框架选择和同类流程清单的自查记录。 |
| [Software, databases and ideas by type (functional) — 2026-11](../docs/CATALOG_BY_TYPE_2026-11.md) | 2026-11 按类型整理的第一版清单。现行目录是首页的方法目录和 catalog/SOFTWARE_AUTHORITY.tsv。 |
| [New tools, databases and ideas by step (functional) — 2026-11 survey](../docs/CATALOG_NEW_TOOLS_2026-11.md) | 2026-11 按阶段整理的第一版清单。现行目录同上。 |
| [Erratum to gene-function-annotation catalog v4 (NLR-Annotator, NLRSeek, plantiSMASH 2.0)](../docs/CATALOG_NEW_TOOLS_2026-11_ERRATUM_NLR_PLANTISMASH.md) | 对 2026-11 清单的勘误（NLR-Annotator、NLRSeek、plantiSMASH 2.0）。 |
| [Erratum: GSAman tool paper vs last-mile opinion DOI](../docs/GSAMAN_DOI_ERRATUM.md) | 勘误：GSAman 工具论文对应哪个 DOI。 |
| [Classroom tonight (function) — offline mirror](../docs/CLASSROOM_TONIGHT.md) | Wiki 上一次课堂入门清单的离线副本。现行入口是 docs/START_HERE.md。 |
| [Structural main process — moved](../docs/steps/MAIN.md) | 指向页：结构注释路线在 gene-structure-annotation。 |
| [Structural error classes — moved](../docs/ERROR_CLASSES.md) | 指向页：基因模型错误类型在 gene-structure-annotation。 |
| [Wiki 页 Start-tonight](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Start-tonight) | 第一次上手用的 Wiki 页，不在克隆的仓库里。 |
| [Annotation board（Project #2）](https://github.com/users/Xuzhen-Li/projects/2) | 注释仓库的任务看板。 |

<a id="other-files"></a>
## 其他文件

- `.github/` · 5 个文件
- `.gitignore`
- `CONTRIBUTING.md`
- `README.md`
- `README.zh.md`
- `CHANGELOG.md`
- `LICENSE`
- `NOTICE.md`
