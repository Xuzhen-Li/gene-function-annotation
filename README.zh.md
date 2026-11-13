# gene-function-annotation
[English](README.md)

## Overview

本仓库在基因结构注释完成后，为蛋白质序列分配名称、GO/KEGG通路和结构域等功能标签。流程仅在结构注释输出 `proteins.faa` 后开始。本工具不执行 BRAKER、软屏蔽、GFF 编辑或基因预测。上游基因模型由 [`gene-structure-annotation`](https://github.com/Xuzhen-Li/gene-structure-annotation) 处理。结构与功能的边界在 [structure `docs/BOUNDARY.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/BOUNDARY.md) 中定义。转座子软屏蔽和转座子库构建不属于功能注释环节。

中文教学：[`docs/zh/`](docs/zh/)（是什么，与结构的关系，怎么跑，F线）
英文操作：[`docs/BILINGUAL.md`](docs/BILINGUAL.md)
植物模拟：[`examples/plant_sim/`](examples/plant_sim/)（与结构 Vitis+NLR，Oryza plain F1，Solanum+Mercator 配对）

![Beginner spine](docs/figures/functional_spine.png)

命名说明：文件 `pipeline/F2_eggnog.sh` 是默认 F1 框架内的 eggNOG 步骤，而不是快速框架分支 F2。
今晚入门：[Wiki Start-tonight](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Start-tonight)（GitHub Wiki，不在克隆仓库中）。
离线课堂：[`docs/CLASSROOM_TONIGHT.md`](docs/CLASSROOM_TONIGHT.md)。
进度追踪：[Annotation board (Project #2)](https://github.com/users/Xuzhen-Li/projects/2)。

## Concepts

1. 框架 F1 / F2 / F3 / F5 指代你声明的完整注释框架。默认 F1 包含 DIAMOND、eggNOG 和 IPS。
2. 脚本 `F2_eggnog.sh` 是 F1 框架内部的 eggNOG 步骤，并非 F2 框架。
3. 工具卡片 F1a / F1b / F1c 对应上述 F1 的三个步骤的知识页面。
4. 门控 `Gate-F1` 等是发布的硬性检查点，不是框架选择。深入说明见 [`docs/zh/FAQ_入门.md`](docs/zh/FAQ_入门.md)。


本页同时也是 2026-11 方法目录：15 个类型分节，共 129 条工具、数据库和想法。默认框架 F1 不变（见 Usage 和 `docs/ROADMAP.md`）。框架 / 步骤顺序仍在路线图和 `catalog/` 中。

## Usage

你必须已经具备蛋白质序列。如果没有，请先用结构注释仓库的 `flow_tool` 跑完，得到 GFF 和 `proteins.faa`。参考 [`docs/HANDOFF_STRUCTURE_TO_FUNCTION.md`](docs/HANDOFF_STRUCTURE_TO_FUNCTION.md)。

自动规划 FA 框架：

```bash
git clone https://github.com/Xuzhen-Li/gene-function-annotation.git
cd gene-function-annotation
cp pipeline/flow_tool/answers.example.yaml my_answers.yaml
# edit: prefer_fast? plant add-ons?
python3 pipeline/flow_tool/flow.py --answers my_answers.yaml -o my_fa_plan.md
```

初始设置时，完成 `my_fa_plan.md` 并列出数据库磁盘路径。此时不需要 InterProScan。在 [Wiki Concepts](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Concepts) 或离线文件 [`docs/zh/02_和结构注释的关系.md`](docs/zh/02_和结构注释的关系.md) 检查概念。分开填写 `grade=` 和 `status=`，不要写成 `status=F-L1`。

在集群执行时，必须在勾选 [Done when](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Start-tonight#done-when) 且 `python3 pipeline/print_qc_commands.py` 退出码为 0 并无 `[STOP]` 时才可继续。否则不要设置 `RUN=1`。使用 `--env config/example.env` 浏览时会显示 `[STOP]`，这是预期行为。METHODS 必填字段必须能够起草，见 [Wiki Evaluate-release](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Evaluate-release)。

按照 [`docs/INSTALL_FUNCTIONAL.md`](docs/INSTALL_FUNCTIONAL.md) 和 [`docs/DB_INSTALL_CHECKLIST.md`](docs/DB_INSTALL_CHECKLIST.md) 安装。然后对 F1 框架设置 `RUN=1` 并勾选 [`docs/EVALUATION_CHECKLIST.md`](docs/EVALUATION_CHECKLIST.md)。F-L1 是验收标准，而不是要求今晚必须完成 IPS。

```bash
cp config/example.env config/local.env
# set PROTEINS_FA to your structure release proteins (one representative per gene)
# set DIAMOND_DB, EGGNOG_*, INTERPROSCAN_HOME, BUSCO_LINEAGE_PROTEIN, …
```

<details>
<summary>Namespace details</summary>

存在四个命名空间，在 METHODS 中不要混淆。
框架：F1 / F2 / F3 / F5 指代完整的注释框架。默认 F1 为 DIAMOND+eggNOG+IPS。
脚本文件名：`F1_diamond.sh`、`F2_eggnog.sh`、`F3_interproscan.sh` 是 F1 框架内的步骤。
工具卡片：F1a / F1b / F1c 映射到三个知识页面。
门控：Gate-F1 至 Gate-F7 是涵盖数据来源、BUSCO、版本和行数等发布的硬性检查点。

中文参考见 [`docs/zh/FAQ_入门.md`](docs/zh/FAQ_入门.md)。
</details>

## Documentation

中文教学与入门：[`docs/zh/`](docs/zh/)
从这里开始：[`docs/START_HERE.md`](docs/START_HERE.md)

<details>
<summary>Additional documentation</summary>

流程工具：[`pipeline/flow_tool/`](pipeline/flow_tool/)
安装：[`docs/INSTALL_FUNCTIONAL.md`](docs/INSTALL_FUNCTIONAL.md)
安装检查表：[`docs/DB_INSTALL_CHECKLIST.md`](docs/DB_INSTALL_CHECKLIST.md)
评估检查表：[`docs/EVALUATION_CHECKLIST.md`](docs/EVALUATION_CHECKLIST.md)
结构注释之后：[`docs/POST_STRUCTURE.md`](docs/POST_STRUCTURE.md)
阶段输入输出：[`docs/STAGE_IO.md`](docs/STAGE_IO.md)
路线图：[`docs/ROADMAP.md`](docs/ROADMAP.md)
工具指南：[`docs/TOOLS.md`](docs/TOOLS.md)
工具文档：[`docs/tools/`](docs/tools/)
评估规则：[`docs/EVALUATION.md`](docs/EVALUATION.md)
质控方法与文献：[`docs/QUALITY_SOURCES.md`](docs/QUALITY_SOURCES.md)
操作演练：[`docs/QUICKSTART.md`](docs/QUICKSTART.md)
Mercator4 网页版：[`docs/MERCATOR_WHEN.md`](docs/MERCATOR_WHEN.md)
教程：[`docs/TUTORIALS_AND_MEETINGS.md`](docs/TUTORIALS_AND_MEETINGS.md)
近期高质量资源：[`docs/RECENT_HIGH_QUALITY.md`](docs/RECENT_HIGH_QUALITY.md)

</details>

<details>
<summary>Overview figure</summary>

![overview](docs/figures/functional_overview.png)

</details>

作者：李旭真，[ORCID](https://orcid.org/0000-0003-3670-6657)

## 方法目录

本页按类型列出 2026-11 调查中的 129 条方法、工具、数据库和想法（类型目录 61 条，`catalog/` 中第一轮卡片 68 条）。默认框架仍是 F1（DIAMOND + eggNOG + InterProScan），本目录不改变该框架。框架 / 步骤顺序仍在 `docs/ROADMAP.md` 和 `catalog/` 中。完整表格和勘误见 `docs/CATALOG_BY_TYPE_2026-11.md` 与 `docs/CATALOG_NEW_TOOLS_2026-11.md`。

## 目录

1. [同源搜索](#section-1) (6)
2. [参考序列与本体数据库](#section-2) (8)
3. [结构域与家族注释](#section-3) (5)
4. [基于直系同源的名称、GO 与 KEGG](#section-4) (9)
5. [机器学习 GO 预测](#section-5) (7)
6. [通路、KO 与 EC](#section-6) (16)
7. [多基因组直系同源](#section-7) (9)
8. [定位与拓扑](#section-8) (8)
9. [植物基因家族](#section-9) (11)
10. [非编码 RNA 功能资源](#section-10) (9)
11. [表达支持的功能](#section-11) (5)
12. [社区目录与命名](#section-12) (3)
13. [蛋白三维结构](#section-13) (17)
14. [下游富集](#section-14) (8)
15. [想法、格式与合并规则](#section-15) (8)

- [蛋白序列之外还需要的数据](#data-needs)
- [图注与许可](#figure-credits)

与本库框架的对应：输入质控（F0）在数据需求一节，不是类型分节 → 默认框架 F1（同源、结构域、直系同源/GO）→ 可选附加（通路、多基因组、定位、植物家族）→ 合并 `merged_function_table.tsv` → 发布。框架编号仍在 `docs/ROADMAP.md` 和 `catalog/`。

<a id="section-1"></a>
## 1. 同源搜索

框架 F1 同源搜索步骤所用的序列相似性引擎。

**需要：** 本地 DIAMOND（或 BLAST）库，一般为 Swiss-Prot 或书面指定的等效库，版本写入 METHODS。[按场景列出的数据需求](#data-needs)

各条目的一句介绍目前保持英文原句，供后续中文润色。


- **BLAST+** (tool) — NCBI BLAST command-line suite (blastp, makeblastdb). [doi:10.1186/1471-2105-10-421](https://doi.org/10.1186/1471-2105-10-421) · [link](https://blast.ncbi.nlm.nih.gov/)
- **DIAMOND (v2)** (tool) — Fast protein aligner with BLAST-like sensitivity modes (--ultra-sensitive). [doi:10.1038/s41592-021-01101-x](https://doi.org/10.1038/s41592-021-01101-x) · [link](https://github.com/bbuchfink/diamond)
- **MMseqs2** (tool) — Sensitive fast protein search and clustering. [doi:10.1038/nbt.3988](https://doi.org/10.1038/nbt.3988) · [link](https://github.com/soedinglab/MMseqs2)
- **HMMER 3** (tool) — Profile HMM search (hmmscan, hmmsearch, jackhmmer). [doi:10.1371/journal.pcbi.1002195](https://doi.org/10.1371/journal.pcbi.1002195) · [link](https://github.com/EddyRivasLab/hmmer) [待确认]
- **HH-suite3** (tool) — HMM-HMM comparison for remote homology (HHblits, HHsearch). [doi:10.1186/s12859-019-3019-7](https://doi.org/10.1186/s12859-019-3019-7) · [link](https://github.com/soedinglab/hh-suite)
- **MMseqs2-GPU** (tool) — GPU-accelerated MMseqs2 sequence search (also speeds ColabFold MSAs). [doi:10.1038/s41592-025-02819-8](https://doi.org/10.1038/s41592-025-02819-8) · [link](https://github.com/soedinglab/MMseqs2)

<a id="section-2"></a>
## 2. 参考序列与本体数据库

搜索和命名步骤需要的参考序列与本体数据库。

**需要：** 数据库文件本身（UniProt、GO、eggNOG、InterPro 成员数据等）及其版本。这些不能只从蛋白序列算出来。[按场景列出的数据需求](#data-needs)


- **UniRef** (resource) — Clustered UniProt sets (UniRef100/90/50). [doi:10.1093/bioinformatics/btu739](https://doi.org/10.1093/bioinformatics/btu739) · [link](https://www.uniprot.org/help/uniref)
- **Pfam (2021)** (resource) — Protein family HMM library (now hosted in InterPro). [doi:10.1093/nar/gkaa913](https://doi.org/10.1093/nar/gkaa913) · [link](https://www.ebi.ac.uk/interpro/entry/pfam/)
- **TAIR** (resource) — The Arabidopsis Information Resource: curated Arabidopsis gene function and nomenclature. [doi:10.1002/dvg.22877](https://doi.org/10.1002/dvg.22877) · [link](https://www.arabidopsis.org/)
- **eggNOG 6** (resource) — Hierarchical orthology database behind eggNOG-mapper. [doi:10.1093/nar/gkac1022](https://doi.org/10.1093/nar/gkac1022) · [link](http://eggnog6.embl.de/) [待确认]
- **UniProt 2025** (resource) — Swiss-Prot/TrEMBL reference; cite the current NAR update for METHODS. [doi:10.1093/nar/gkae1010](https://doi.org/10.1093/nar/gkae1010) · [link](https://www.uniprot.org)
- **Carbon Annotation Database (CADB)** (resource) — Predicted protein-coding loci and proteins for ~48k GenBank eukaryote assemblies (Carbon-A). [doi:10.64898/2026.10.20.760448](https://doi.org/10.64898/2026.10.20.760448) · [link](https://huggingface.co/blog/HuggingFaceBio/carbon-annotator-genbank-genome-annotation)
- **Gene Ontology knowledgebase (2026)** (resource) — Current GO release paper (NAR, issue 2026; a correction notice exists, doi 10.1093/nar/gkag678). [doi:10.1093/nar/gkaf1292](https://doi.org/10.1093/nar/gkaf1292) · [link](https://geneontology.org)
- **Ensembl Plants** (resource) — Plant genomes with gene trees and projected annotation. [link](https://plants.ensembl.org)

<a id="section-3"></a>
## 3. 结构域与家族注释

框架 F1 结构域步骤中的结构域与家族注释（InterProScan 及相关数据）。

**需要：** 可用的 InterProScan 安装及其数据；此步较慢，属于默认框架 F1，但 F-L1 并不要求当天做完 IPS。[按场景列出的数据需求](#data-needs)

![InterPro PIK3CA domains](docs/figures/catalog/04_interpro_pik3ca_domains.jpg)

*InterPro 对 PIK3CA 的结构域注释（图 4）。 Blum、Andreeva、Florentino 等 2025，《Nucleic Acids Research》图 4，doi:10.1093/nar/gkae1082，PMC11701551，CC BY。*

![InterProScan human runtime](docs/figures/catalog/05_interproscan_human_runtime.jpg)

*InterProScan 在人类蛋白组上的运行时间（图 6）。 Blum、Andreeva、Florentino 等 2025，《Nucleic Acids Research》图 6，doi:10.1093/nar/gkae1082，PMC11701551，CC BY。*

- **InterProScan 5** (tool) — Runs member databases (Pfam, PANTHER, SMART, CDD, Gene3D…) and maps InterPro2GO. [doi:10.1093/bioinformatics/btu031](https://doi.org/10.1093/bioinformatics/btu031) · [link](https://github.com/ebi-pf-team/interproscan)
- **SMART (2021 update)** (resource) — Signalling/extracellular domain resource (member DB of InterPro). [doi:10.1093/nar/gkaa937](https://doi.org/10.1093/nar/gkaa937) · [link](https://smart.embl.de)
- **CDD / CD-Search (2023)** (resource) — NCBI conserved-domain models and SPARCLE architectures. [doi:10.1093/nar/gkac1096](https://doi.org/10.1093/nar/gkac1096) · [link](https://www.ncbi.nlm.nih.gov/Structure/cdd/cdd.shtml)
- **Merizo** (tool) — Domain segmentation of predicted 3D structures. [doi:10.1038/s41467-023-43934-4](https://doi.org/10.1038/s41467-023-43934-4) · [link](https://github.com/psipred/Merizo)
- **DPFunc** (tool) — Deep learning GO prediction guided by domain + 3D-structure information. [doi:10.1038/s41467-024-54816-8](https://doi.org/10.1038/s41467-024-54816-8) · [link](https://github.com/CSUBioGroup/DPFunc)

<a id="section-4"></a>
## 4. 基于直系同源的名称、GO 与 KEGG

基于直系同源或相似性的名称、GO 和 KEGG，也包括整套框架（F1 直系同源步骤、快速框架 F2、EnTAP 框架 F3、F4 可读名称）。

**需要：** eggNOG-mapper 数据库（若做可读名称，再加可选的 AHRD / PANNZER 输入）。机器给出的 GO 仍是电子证据（IEA）。[按场景列出的数据需求](#data-needs)

![eggNOG-mapper v2 runtime](docs/figures/catalog/01_eggnogmapper_v2_runtime.jpg)

*eggNOG-mapper v2 与其他注释工具的运行时间比较（图 2）。 Cantalapiedra 等 2021，《Molecular Biology and Evolution》图 2，doi:10.1093/molbev/msab293，PMC8662613，CC BY。*

![eggNOG-mapper versus InterProScan](docs/figures/catalog/02_eggnogmapper_vs_interproscan.jpg)

*eggNOG-mapper 与 InterProScan 的比较（图 3）。 Huerta-Cepas 等 2017，《Molecular Biology and Evolution》图 3，doi:10.1093/molbev/msx148，PMC5850834，CC BY。*

![eggNOG-mapper GO example](docs/figures/catalog/03_eggnogmapper_rhogap1_go.jpg)

*eggNOG-mapper 在一个示例上的 GO 分配（图 4）。 Huerta-Cepas 等 2017，《Molecular Biology and Evolution》图 4，doi:10.1093/molbev/msx148，PMC5850834，CC BY。*

- **eggNOG-mapper v2** (tool) — Orthology-based functional annotation: names, GO, KEGG, EC, COG. [doi:10.1093/molbev/msab293](https://doi.org/10.1093/molbev/msab293) · [link](https://github.com/eggnogdb/eggnog-mapper)
- **PANNZER2** (tool) — Fast web/standalone GO and free-text description prediction. [doi:10.1093/nar/gky350](https://doi.org/10.1093/nar/gky350) · [link](http://ekhidna2.biocenter.helsinki.fi/sanspanz/) [待确认]
- **Blast2GO** (tool) — BLAST-based GO annotation and visualisation (now in commercial OmicsBox). [doi:10.1093/bioinformatics/bti610](https://doi.org/10.1093/bioinformatics/bti610) · [link](https://www.biobam.com/omicsbox/)
- **EnTAP** (tool) — Eukaryotic non-model annotation pipeline: filtering, similarity search, contaminant flags, eggNOG and InterPro. [doi:10.1111/1755-0998.13106](https://doi.org/10.1111/1755-0998.13106) · [link](https://github.com/harta55/EnTAP)
- **FA-nf** (tool) — Nextflow functional annotation pipeline for non-model proteins (BLAST, InterProScan, KEGG, signal peptides). [doi:10.3390/genes12101645](https://doi.org/10.3390/genes12101645) · [link](https://github.com/guigolab/FA-nf)
- **Sma3s v2** (tool) — Functional annotation of proteomes/transcriptomes against UniProt (GO, keywords, pathways). [doi:10.1002/pmic.201700071](https://doi.org/10.1002/pmic.201700071) · [link](https://github.com/UPOBioinfo/sma3s)
- **AHRD** (tool) — Automated assignment of Human Readable Descriptions from BLAST results. [link](https://github.com/groupschoof/AHRD)
- **GOMAP** (tool) — Gene Ontology Meta Annotator for Plants: combines sequence similarity, domains and mixed-method predictors into plant GO sets. [doi:10.1186/s13007-021-00754-1](https://doi.org/10.1186/s13007-021-00754-1) · [link](https://github.com/Dill-PICL/GOMAP)
- **TRAPID 2.0** (tool) — Web app for taxonomic and functional analysis of de novo plant transcriptomes using PLAZA references. [doi:10.1093/nar/gkab565](https://doi.org/10.1093/nar/gkab565) · [link](https://bioinformatics.psb.ugent.be/trapid_02/) [待确认]

<a id="section-5"></a>
## 5. 机器学习 GO 预测

机器学习 GO 预测。是框架 F1 之后的可选附加，不是 F1 的替代。

**需要：** 通常只需蛋白，外加工具自带的模型。这是框架 F1 之后的可选附加，不是 F1 的替代。[按场景列出的数据需求](#data-needs)


- **DeepGOPlus** (tool) — CNN + DIAMOND GO prediction from sequence. [doi:10.1093/bioinformatics/btz595](https://doi.org/10.1093/bioinformatics/btz595) · [link](https://github.com/bio-ontology-research-group/deepgoplus)
- **NetGO 3.0** (tool) — Protein-language-model GO prediction server (CAFA top performer). [doi:10.1016/j.gpb.2023.04.001](https://doi.org/10.1016/j.gpb.2023.04.001)
- **DeepFRI** (tool) — Graph-convolution function prediction from 3D structure and sequence. [doi:10.1038/s41467-021-23303-9](https://doi.org/10.1038/s41467-021-23303-9) · [link](https://github.com/flatironinstitute/DeepFRI)
- **GoPredSim** (tool) — GO transfer by embedding similarity (SeqVec/ProtT5). [doi:10.1038/s41598-020-80786-0](https://doi.org/10.1038/s41598-020-80786-0) · [link](https://github.com/Rostlab/goPredSim)
- **DeepGO-SE** (tool) — GO prediction as approximate semantic entailment over ESM2 embeddings and GO axioms. [doi:10.1038/s42256-024-00795-w](https://doi.org/10.1038/s42256-024-00795-w) · [link](https://github.com/bio-ontology-research-group/deepgo2)
- **ProtGO** (tool) — Multi-modal GO prediction (PLM + text + taxonomy + GO graph). [doi:10.1093/bioinformatics/btaf390](https://doi.org/10.1093/bioinformatics/btaf390) · [link](https://github.com/sunyatawang/ProtGO)
- **AltereGO** (tool) — Score-level fusion of ESM2, ProtT5, Ankh and ProstT5-3Di predictors for GO molecular function (preprint 2026). [doi:10.64898/2026.10.23.761425](https://doi.org/10.64898/2026.10.23.761425)

<a id="section-6"></a>
## 6. 通路、KO 与 EC

通路、KO 和 EC（F1+ Kofam、框架 F6 MapMan 及相关附加）。

**需要：** Kofam / KO 需要 HMM 库和分数阈值；MapMan（F6）需要 Mercator4 结果（网页或本地，见 `docs/MERCATOR_WHEN.md`）。KEGG 再分发规则标为 `[待确认]`，这里不作假定。[按场景列出的数据需求](#data-needs)


- **MapMan4 / Mercator4** (tool / resource) — Plant-specific functional bins (MapMan4) assigned by Mercator4. [doi:10.1016/j.molp.2019.01.003](https://doi.org/10.1016/j.molp.2019.01.003) · [link](https://www.plabipd.de/mercator_main.html)
- **KofamKOALA / KofamScan** (tool) — KEGG Orthology assignment with adaptive-threshold profile HMMs. [doi:10.1093/bioinformatics/btz859](https://doi.org/10.1093/bioinformatics/btz859) · [link](https://www.genome.jp/tools/kofamkoala/)
- **BlastKOALA / GhostKOALA** (tool) — KEGG web servers assigning KO numbers by sequence similarity. [doi:10.1016/j.jmb.2015.11.006](https://doi.org/10.1016/j.jmb.2015.11.006) · [link](https://www.kegg.jp/blastkoala/)
- **KEGG Mapper** (tool) — Maps KO lists onto KEGG pathways, BRITE and modules. [doi:10.1002/pro.3711](https://doi.org/10.1002/pro.3711) · [link](https://www.kegg.jp/kegg/mapper/)
- **kegg-pathways-completeness** (tool) — Computes KEGG module completeness from a KO list. [link](https://github.com/EBI-Metagenomics/kegg-pathways-completeness-tool)
- **MetaCyc** (resource) — Curated metabolic pathways and enzymes across life. [doi:10.1093/nar/gkz862](https://doi.org/10.1093/nar/gkz862) · [link](https://metacyc.org/) [待确认]
- **BRENDA** (resource) — Comprehensive enzyme function database (EC). [doi:10.1093/nar/gkaa1025](https://doi.org/10.1093/nar/gkaa1025) · [link](https://www.brenda-enzymes.org/)
- **DeepEC** (tool) — Deep-learning EC number prediction. [doi:10.1073/pnas.1821905116](https://doi.org/10.1073/pnas.1821905116)
- **KEGG (2025 NAR)** (resource) — Current KEGG citation for KO/pathway mapping. [doi:10.1093/nar/gkae909](https://doi.org/10.1093/nar/gkae909) · [link](https://www.kegg.jp)
- **Plant Reactome (2024)** (resource) — Curated plant pathways (rice reference, projected to other plants). [doi:10.1093/nar/gkad1052](https://doi.org/10.1093/nar/gkad1052) · [link](https://plantreactome.gramene.org) [待确认]
- **Plant Metabolic Network / E2P2** (tool / resource) — PlantCyc and species pathway DBs built with the E2P2 enzyme predictor. [link](https://plantcyc.org) [待确认]
- **CLEAN** (tool) — Contrastive-learning EC number prediction. [doi:10.1126/science.adf2465](https://doi.org/10.1126/science.adf2465) · [link](https://github.com/tttianhao/CLEAN)
- **EZpred** (tool) — EC prediction using unlabeled sequence homologs (Advanced Science 2026). [doi:10.1002/advs.78703](https://doi.org/10.1002/advs.78703) [待确认]
- **ProteEC-CLA** (tool) — EC prediction with contrastive learning + agent attention on ESM2. [doi:10.1002/prot.26822](https://doi.org/10.1002/prot.26822)
- **plantiSMASH 2.0** (tool) — Plant biosynthetic gene cluster detection, substrate prediction for some enzyme families, promoter TF sites; DB of ~30k BGCs over 430 genomes. [doi:10.1016/j.jmb.2026.169798](https://doi.org/10.1016/j.jmb.2026.169798) · [link](https://github.com/plantismash/plantismash)
- **dbCAN3** (tool) — CAZyme and substrate annotation. [doi:10.1093/nar/gkad328](https://doi.org/10.1093/nar/gkad328) · [link](https://github.com/linnabrown/run_dbcan)

<a id="section-7"></a>
## 7. 多基因组直系同源

跨基因组的直系同源组。框架 F7 注释的是直系同源组代表序列，不是每个基因。

**需要：** 面板中每个基因组的蛋白 FASTA。框架 F7 注释的是直系同源组代表序列，不是每个基因。[按场景列出的数据需求](#data-needs)

![OrthoFinder Chordata](docs/figures/catalog/06_orthofinder_chordata_summary.jpg)

*OrthoFinder 在一个脊索动物示例上的摘要（图 3）。 Emms 与 Kelly 2019，《Genome Biology》图 3，doi:10.1186/s13059-019-1832-y，PMC6857279，CC BY。*

- **Broccoli** (tool) — Orthology via phylogeny and network label propagation. [doi:10.1093/molbev/msaa159](https://doi.org/10.1093/molbev/msaa159) · [link](https://github.com/rderelle/Broccoli)
- **Proteinortho6** (tool) — Graph-based (co-)orthology detection at scale. [doi:10.3389/fbinf.2023.1322477](https://doi.org/10.3389/fbinf.2023.1322477) · [link](https://gitlab.com/paulklemm_PHD/proteinortho)
- **CAFE 5** (tool) — Gene family expansion/contraction under rate variation. [doi:10.1093/bioinformatics/btaa1022](https://doi.org/10.1093/bioinformatics/btaa1022) · [link](https://github.com/hahnlab/CAFE5)
- **PLAZA 5.0** (resource) — Plant comparative genomics: gene families, orthologs, GO/InterPro projections. [doi:10.1093/nar/gkab1024](https://doi.org/10.1093/nar/gkab1024) · [link](https://bioinformatics.psb.ugent.be/plaza/) [待确认]
- **OrthoFinder 3** (tool) — Scalable phylogenetic orthology (v3.x, FAMSA alignment). [doi:10.1101/2025.07.15.664860](https://doi.org/10.1101/2025.07.15.664860) · [link](https://github.com/OrthoFinder/OrthoFinder)
- **FastOMA** (tool) — Linear-scaling orthology inference (OMAmer placement). [doi:10.1038/s41592-024-02552-8](https://doi.org/10.1038/s41592-024-02552-8) · [link](https://github.com/DessimozLab/FastOMA)
- **SonicParanoid2** (tool) — Fast orthology with ML and language models. [doi:10.1186/s13059-024-03298-4](https://doi.org/10.1186/s13059-024-03298-4) · [link](https://gitlab.com/salvo981/sonicparanoid2)
- **OrthoDB v12** (resource) — Hierarchical orthologs with functional descriptors (OrthoDB + BUSCO update paper). [doi:10.1093/nar/gkae987](https://doi.org/10.1093/nar/gkae987) · [link](https://www.orthodb.org)
- **OMA browser 2024** (resource) — OMA orthology resource update. [doi:10.1093/nar/gkad1020](https://doi.org/10.1093/nar/gkad1020) · [link](https://omabrowser.org)

<a id="section-8"></a>
## 8. 定位与拓扑

信号肽、拓扑和亚细胞定位（F1+ 附加）。

**需要：** 通常只需蛋白（SignalP、TargetP 等）。作为 F1+ 附加列，不要另做一张主表。[按场景列出的数据需求](#data-needs)


- **SignalP 6.0** (tool) — Signal peptide prediction (all five types) with protein language model. [doi:10.1038/s41587-021-01156-3](https://doi.org/10.1038/s41587-021-01156-3) · [link](https://services.healthtech.dtu.dk/services/SignalP-6.0/)
- **TMHMM 2.0** (tool) — Transmembrane helix prediction (HMM). [doi:10.1006/jmbi.2000.4315](https://doi.org/10.1006/jmbi.2000.4315) · [link](https://services.healthtech.dtu.dk/services/TMHMM-2.0/)
- **Phobius** (tool) — Combined transmembrane topology and signal peptide predictor. [doi:10.1016/j.jmb.2004.03.016](https://doi.org/10.1016/j.jmb.2004.03.016) · [link](https://phobius.sbc.su.se/)
- **WoLF PSORT** (tool) — Subcellular localization prediction with a plant model. [doi:10.1093/nar/gkm259](https://doi.org/10.1093/nar/gkm259) · [link](https://wolfpsort.hgc.jp/)
- **LOCALIZER** (tool) — Predicts chloroplast, mitochondrial and nuclear localization of plant and effector proteins. [doi:10.1038/srep44598](https://doi.org/10.1038/srep44598) · [link](https://localizer.csiro.au/)
- **DeepLoc 2.1** (tool) — Subcellular localization + membrane protein type from PLMs. [doi:10.1093/nar/gkae237](https://doi.org/10.1093/nar/gkae237) · [link](https://services.healthtech.dtu.dk/services/DeepLoc-2.1/)
- **TargetP 2.0** (tool) — N-terminal targeting peptides (signal, mitochondrial, chloroplast, thylakoid). [doi:10.26508/lsa.201900429](https://doi.org/10.26508/lsa.201900429) · [link](https://services.healthtech.dtu.dk/services/TargetP-2.0/)
- **DeepTMHMM** (tool) — Transmembrane topology prediction (preprint). [doi:10.1101/2022.04.08.487609](https://doi.org/10.1101/2022.04.08.487609) · [link](https://dtu.biolib.com/DeepTMHMM)

<a id="section-9"></a>
## 9. 植物基因家族

植物基因家族分类（框架 F8 NLR、框架 F9 TF/激酶）。

**需要：** NLR（F8）需要 InterProScan 输出，可选 HRP 窗口列表；TF / 激酶（F9）需要 iTAK（或书面指定的等效工具）。没有病害 / NLR 故事就跳过 F8。[按场景列出的数据需求](#data-needs)


- **iTAK** (tool) — Plant transcription factor and protein kinase identification and classification. [doi:10.1016/j.molp.2016.09.014](https://doi.org/10.1016/j.molp.2016.09.014) · [link](https://github.com/kentnf/iTAK)
- **TAPscan v4** (tool / resource) — Detects transcription-associated proteins with family rules; streptophyte-wide database. [doi:10.1111/tpj.17184](https://doi.org/10.1111/tpj.17184) · [link](https://tapscan.plantcode.cup.uni-freiburg.de/)
- **PRGdb 4.0** (tool / resource) — Plant resistance gene database with DRAGO annotation pipeline. [doi:10.1093/nar/gkab1087](https://doi.org/10.1093/nar/gkab1087) · [link](http://prgdb.org/) [待确认]
- **RGAugury** (tool) — Pipeline identifying resistance gene analogs (NBS, RLK, RLP). [doi:10.1186/s12864-016-3197-x](https://doi.org/10.1186/s12864-016-3197-x) · [link](https://bitbucket.org/yaanlpc/rgaugury)
- **Resistify** (tool) — Fast NLR identification/classification from proteins using NLRexpress motifs. [doi:10.1177/11779322241308944](https://doi.org/10.1177/11779322241308944) · [link](https://github.com/SwiftSeal/resistify)
- **NLRtracker + RefPlantNLR** (tool / resource) — Extracts and classifies NLRs from proteomes/transcripts using features of RefPlantNLR. [doi:10.1371/journal.pbio.3001124](https://doi.org/10.1371/journal.pbio.3001124) · [link](https://github.com/slt666666/NLRtracker)
- **NLR-Annotator** (tool) — Annotation-independent NLR locus finder on genomic sequence. [doi:10.1104/pp.19.01273](https://doi.org/10.1104/pp.19.01273) · [link](https://github.com/steuernb/NLR-Annotator)
- **NLRexpress** (tool) — ML motif predictors for CC/TIR/NB-ARC/LRR motifs. [doi:10.3389/fpls.2022.975888](https://doi.org/10.3389/fpls.2022.975888) · [link](https://github.com/eliza-m/NLRexpress)
- **NLRSeek** (tool) — Combines NLR-Annotator loci, targeted re-annotation and NLRtracker to recover NLRs missing from proteomes. [doi:10.1016/j.abiote.2025.100001](https://doi.org/10.1016/j.abiote.2025.100001) · [link](https://github.com/Wang-Mengda/NLRSeek)
- **PlantTFDB / PlantRegMap** (resource) — Plant TF families, binding motifs and regulatory map. [doi:10.1093/nar/gkz1020](https://doi.org/10.1093/nar/gkz1020) · [link](http://planttfdb.gao-lab.org) [待确认]
- **PlantPAN (latest)** (resource) — Plant promoter / TF-binding analysis navigator. [doi:10.1093/nar/gkad945](https://doi.org/10.1093/nar/gkad945) · [link](https://plantpan.itps.ncku.edu.tw)

<a id="section-10"></a>
## 10. 非编码 RNA 功能资源

非编码 RNA 功能资源。通常需要转录组或已知 ncRNA 位点，不能只用蛋白表。

**需要：** 转录组或已知 ncRNA 位点，不能只用蛋白表。基因预测和 TE 库仍归结构库 / vitis-te。[按场景列出的数据需求](#data-needs)


- **miRBase** (resource) — Reference microRNA sequence and nomenclature database. [doi:10.1093/nar/gky1141](https://doi.org/10.1093/nar/gky1141) · [link](https://www.mirbase.org/)
- **psRobot** (tool) — Plant small-RNA meta-analysis and target prediction. [doi:10.1093/nar/gks554](https://doi.org/10.1093/nar/gks554) · [link](http://omicslab.genetics.ac.cn/psRobot/) [待确认]
- **ncPlantDB** (resource) — Plant ncRNAs with potential ncRNA-encoded peptides and cell-type interactions (43 species). [doi:10.1093/nar/gkae1017](https://doi.org/10.1093/nar/gkae1017) · [link](https://bis.zju.edu.cn/ncPlantDB)
- **PLncDB V2.0** (resource) — Plant lncRNA encyclopedia. [doi:10.1093/nar/gkaa910](https://doi.org/10.1093/nar/gkaa910) · [link](https://www.tobaccodb.org/plncdb/) [待确认]
- **GreeNC 2.0** (resource) — Plant lncRNA catalog. [doi:10.1093/nar/gkab1014](https://doi.org/10.1093/nar/gkab1014) · [link](http://greenc.sequentiabiotech.com) [待确认]
- **CANTATAdb 3.0** (resource) — Updated plant lncRNA repository. [doi:10.1093/pcp/pcae081](https://doi.org/10.1093/pcp/pcae081) · [link](http://cantata.amu.edu.pl) [待确认]
- **PlantCircRNA** (resource) — Plant circular RNA database. [doi:10.1093/nar/gkae709](https://doi.org/10.1093/nar/gkae709) · [link](https://plant.deepbiology.cn/PlantCircRNA/)
- **psRNATarget (2017 release)** (tool) — Plant small-RNA target prediction server. [doi:10.1093/nar/gky316](https://doi.org/10.1093/nar/gky316) · [link](https://www.zhaolab.org/psRNATarget/) [待确认]
- **PmiREN 2.0** (resource) — Plant miRNA encyclopedia. [doi:10.1093/nar/gkab811](https://doi.org/10.1093/nar/gkab811) · [link](https://pmiren.com)

<a id="section-11"></a>
## 11. 表达支持的功能

用表达或共表达支持功能假说，而不是作为实验 GO。

**需要：** 若用表达来支持功能判断，需要 RNA-seq（最好来自同一基因型）。[按场景列出的数据需求](#data-needs)


- **Grapevine Expression Atlas** (resource) — Organ/stage expression atlas of V. vinifera Corvina. [doi:10.1105/tpc.112.100230](https://doi.org/10.1105/tpc.112.100230)
- **ATTED-II v11** (resource) — Plant gene coexpression database. [doi:10.1093/pcp/pcac041](https://doi.org/10.1093/pcp/pcac041) · [link](https://atted.jp/)
- **scPlantDB** (resource) — Plant single-cell atlas: cell types and markers. [doi:10.1093/nar/gkad706](https://doi.org/10.1093/nar/gkad706) · [link](https://biobigdata.nju.edu.cn/scplantdb/) [待确认]
- **hdWGCNA** (tool) — Co-expression networks in single-cell/spatial data. [doi:10.1016/j.crmeth.2023.100498](https://doi.org/10.1016/j.crmeth.2023.100498) · [link](https://github.com/smorabit/hdWGCNA)
- **CoNekT** (tool / resource) — Co-expression network toolkit/framework for plants. [doi:10.1101/255075](https://doi.org/10.1101/255075) · [link](https://conekt.sbs.ntu.edu.sg) [待确认]

<a id="section-12"></a>
## 12. 社区目录与命名

经过整理的社区目录和命名来源。

**需要：** 能访问所点名的社区目录（及其版本或日期）。[按场景列出的数据需求](#data-needs)


- **The grapevine gene nomenclature system** (idea) — Proposed rules for naming grapevine genes. [doi:10.1186/1471-2164-15-1077](https://doi.org/10.1186/1471-2164-15-1077)
- **Grapedia Grapevine Reference Gene Catalogue** (resource) — Curated V. vinifera gene ID/symbol pairs with function, literature and confidence; v3.1 (Nov 2025) aligned to T2T v5.1 annotation. [link](https://grapedia.org/genes/)
- **Grape Gene Reference Catalogue (paper)** (resource) — Describes the catalogue as a standard for gene selection. [doi:10.3389/fpls.2021.803977](https://doi.org/10.3389/fpls.2021.803977)

<a id="section-13"></a>
## 13. 蛋白三维结构

蛋白三维结构的预测、搜索和结构域。这里的 structure 指三维结构，不是基因模型。

**需要：** 蛋白；有的工具还需要 AlphaFold / PDB 一类库。这里的 “structure” 指蛋白三维结构，不是基因模型。[按场景列出的数据需求](#data-needs)


- **AlphaFold2** (tool) — Protein 3D structure prediction. [doi:10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2) · [link](https://github.com/google-deepmind/alphafold)
- **ColabFold** (tool) — Fast AlphaFold2 with MMseqs2 MSAs. [doi:10.1038/s41592-022-01488-1](https://doi.org/10.1038/s41592-022-01488-1) · [link](https://github.com/sokrypton/ColabFold)
- **ESMFold / ESM-2** (tool) — Single-sequence 3D structure prediction from a protein language model. [doi:10.1126/science.ade2574](https://doi.org/10.1126/science.ade2574) · [link](https://github.com/facebookresearch/esm)
- **AlphaFold 3** (tool) — Joint structure prediction of complexes with nucleic acids, ligands and ions. [doi:10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w) · [link](https://github.com/google-deepmind/alphafold3)
- **TED (The Encyclopedia of Domains)** (resource) — Structure-based domain segmentation of AlphaFold DB. [doi:10.1126/science.adq4946](https://doi.org/10.1126/science.adq4946) · [link](https://ted.cathdb.info/)
- **CATH (2021)** (resource) — Hierarchical classification of protein 3D domains. [doi:10.1093/nar/gkaa1079](https://doi.org/10.1093/nar/gkaa1079) · [link](https://www.cathdb.info/)
- **TM-align** (tool) — Structure alignment with TM-score. [doi:10.1093/nar/gki524](https://doi.org/10.1093/nar/gki524) · [link](https://zhanggroup.org/TM-align/)
- **US-align** (tool) — Universal structure alignment for proteins and nucleic acids. [doi:10.1038/s41592-022-01585-1](https://doi.org/10.1038/s41592-022-01585-1) · [link](https://github.com/pylelab/USalign)
- **DALI** (tool) — Structure comparison server against PDB/AlphaFold DB. [doi:10.1002/pro.3749](https://doi.org/10.1002/pro.3749) · [link](http://ekhidna2.biocenter.helsinki.fi/dali/) [待确认]
- **Foldseek** (tool) — Protein 3D-structure search via 3Di alphabet; finds remote homologs missed by sequence search. [doi:10.1038/s41587-023-01773-0](https://doi.org/10.1038/s41587-023-01773-0) · [link](https://github.com/steineggerlab/foldseek)
- **ProstT5** (tool) — Protein language model translating sequence to 3Di tokens so Foldseek can run without predicted structures. [doi:10.1093/nargab/lqae150](https://doi.org/10.1093/nargab/lqae150) · [link](https://github.com/mheinzinger/ProstT5)
- **TM-Vec 2s** (tool) — Embedding-based remote homology / TM-score prediction (preprint 2026). [doi:10.64898/2026.02.05.704073](https://doi.org/10.64898/2026.02.05.704073)
- **AlphaFold Protein Structure Database (2024)** (resource) — Predicted protein 3D structures for UniProt; target for Foldseek searches. [doi:10.1093/nar/gkad1011](https://doi.org/10.1093/nar/gkad1011) · [link](https://alphafold.ebi.ac.uk)
- **AlphaFind v2** (tool) — Similarity search over AlphaFold DB and TED domains. [doi:10.1093/nar/gkag372](https://doi.org/10.1093/nar/gkag372) · [link](https://alphafind.fi.muni.cz)
- **WASP** (tool) — Whole-proteome annotation via Foldseek against AlphaFold DB (GO, Pfam, PANTHER, CATH, Rhea, EC). [link](https://github.com/gioodm/wasp-proteins-annotation)
- **PARSE** (tool) — Functional site annotation from local 3D-structure embeddings. [doi:10.1073/pnas.2513219122](https://doi.org/10.1073/pnas.2513219122)
- **metagenomic-DeepFRI** (tool) — Scaled DeepFRI (GO from protein 3D-structure graphs) (preprint 2026). [doi:10.64898/2026.04.27.720983](https://doi.org/10.64898/2026.04.27.720983)

<a id="section-14"></a>
## 14. 下游富集

下游 GO/KEGG 富集。使用已完成的功能表，不是标签来源。

**需要：** 已完成的功能表，以及定义清楚的基因集背景（通常是该次发布的全部基因）。这是合并之后的下游分析，不是标签来源。[按场景列出的数据需求](#data-needs)


- **topGO** (tool) — GO enrichment accounting for GO graph topology. [doi:10.18129/B9.bioc.topGO](https://doi.org/10.18129/B9.bioc.topGO) · [link](https://bioconductor.org/packages/topGO/)
- **GOATOOLS** (tool) — Python GO library: DAG propagation, slims, enrichment. [doi:10.1038/s41598-018-28948-z](https://doi.org/10.1038/s41598-018-28948-z) · [link](https://github.com/tanghaibao/goatools)
- **GOseq** (tool) — GO enrichment correcting for length bias in RNA-seq. [doi:10.1186/gb-2010-11-2-r14](https://doi.org/10.1186/gb-2010-11-2-r14) · [link](https://bioconductor.org/packages/goseq/)
- **ShinyGO** (tool) — Web enrichment with plant species from Ensembl/STRING. [doi:10.1093/bioinformatics/btz931](https://doi.org/10.1093/bioinformatics/btz931) · [link](http://bioinformatics.sdstate.edu/go/) [待确认]
- **DAVID (2025 update)** (tool) — Enrichment server; adds DAVID Ortholog for cross-species analysis. [doi:10.1093/nar/gkag470](https://doi.org/10.1093/nar/gkag470) · [link](https://davidbioinformatics.nih.gov)
- **g:Profiler (2023)** (tool) — Enrichment and ID conversion. [doi:10.1093/nar/gkad347](https://doi.org/10.1093/nar/gkad347) · [link](https://biit.cs.ut.ee/gprofiler)
- **agriGO v2.0** (tool) — GO enrichment for agricultural species. [doi:10.1093/nar/gkx382](https://doi.org/10.1093/nar/gkx382) · [link](http://systemsbiology.cau.edu.cn/agriGOv2/) [待确认]
- **clusterProfiler 4.0** (tool) — R enrichment with custom TERM2GENE from merged_function_table.tsv. [doi:10.1016/j.xinn.2021.100141](https://doi.org/10.1016/j.xinn.2021.100141) · [link](https://github.com/YuLab-SMU/clusterProfiler)

<a id="section-15"></a>
## 15. 想法、格式与合并规则

想法、格式和合并规则。合并产物仍是 `merged_function_table.tsv`。未实测前不改变框架 F1。

**需要：** 视具体想法而定；合并产物仍是 `merged_function_table.tsv`。未实测前不改变框架 F1。[按场景列出的数据需求](#data-needs)


- **Evidence & Conclusion Ontology (ECO, 2022)** (idea) — Ontology of evidence types behind annotations (maps to GO evidence codes). [doi:10.1093/nar/gkab1025](https://doi.org/10.1093/nar/gkab1025) · [link](https://evidenceontology.org/)
- **GO Annotation File (GAF 2.2) format** (idea) — Standard tab format for gene–GO associations with evidence codes. [link](https://geneontology.org/docs/go-annotation-file-gaf-format-2.2/)
- **GO specificity balance (Genome Res 2026)** (idea) — Balancing GO term specificity in sequence-language-model predictions. [doi:10.1101/gr.280816.125](https://doi.org/10.1101/gr.280816.125) [待确认]
- **CAFA lessons (idea)** (idea) — Community assessments keep showing GO prediction is hard for proteins with partial knowledge; publish ML GO as electronic evidence (IEA) only. [link](https://biofunctionprediction.org/cafa/) [待确认]
- **GeneAgent** (idea) — Self-verifying LLM agent for gene-set analysis using domain databases. [doi:10.1038/s41592-025-02748-6](https://doi.org/10.1038/s41592-025-02748-6)
- **LLM-assisted Reactome annotation** (idea) — LLM/RAG proposals of pathway annotations for curator review (preprint). [doi:10.64898/2025.12.20.695723](https://doi.org/10.64898/2025.12.20.695723)
- **Agentic AI for gene function across genomes** (idea) — GO curators' agent workflow with constrained schemas and validators (Zenodo record). [doi:10.5281/zenodo.18904049](https://doi.org/10.5281/zenodo.18904049)
- **ProtNLM (UniProt names)** (idea) — UniProt uses a Google protein-naming model to propose names for unreviewed entries; names carry an automatic evidence tag. [link](https://www.uniprot.org/help/ProtNLM)

<a id="data-needs"></a>
## 蛋白序列之外还需要的数据

主输入是结构库发布的 `proteins.faa`（每个基因一条代表序列）。下表说明各步骤通常还要什么。未实测前不改变默认框架 F1。

| 场景 | 最低要求 | 建议再加 | 本库常用工具 | 常见陷阱 |
|---|---|---|---|---|
| 输入质控（F0） | `PROTEINS_FA` + 蛋白模式 BUSCO lineage | 再用 OMArk 做一致性检查 | BUSCO 蛋白模式、OMArk（可选） | 把 F0 当成功能标签来源；想在这里“修好”差的蛋白组，而不是回到结构库 |
| 默认框架 F1 | 本地 DIAMOND 库、eggNOG-mapper 数据、InterProScan 数据（版本写入 METHODS） | DIAMOND 用 Swiss-Prot（或书面指定的等效库） | `F1_diamond.sh`、`F2_eggnog.sh`、`F3_interproscan.sh` | 把脚本 `F2_eggnog.sh` 和备用框架 F2 搞混 |
| 快速框架 F2 | 只需 eggNOG-mapper 数据 | 随后把 Kofam 并入合并表 | eggNOG-mapper ± Kofam | 把 F2 结果当成已经跑过 IPS 来发布 |
| 名称（F4，可选） | AHRD 所需的 Blast/DIAMOND 类输出 | 书面指定的名称来源 | AHRD，可选 PANNZER（2026-11 目录中网站检查为 `[待确认]`） | 仅凭名称就当作更高的 F-L 等级 |
| MapMan（F6，可选） | Mercator4 结果（网页或本地） | 按 `docs/MERCATOR_WHEN.md` 操作 | `F6_ingest_mercator.py` | 只因为“这是植物”就跑 Mercator，并无 MapMan 图计划 |
| 多基因组（F7） | 面板中每个基因组的蛋白 | 注释直系同源组代表序列，再合并 | OrthoFinder，然后对代表序列跑 F1 | 写成好像每个基因都跑过 F1 |
| NLR（F8，可选） | InterProScan 输出；可选结构叠加层给出的 HRP 窗口 | 仅在有病害 / NLR 故事时使用 | `F8_run.sh` | 把 IPS+HRP 筛查当成已审定的 NLR 集 |
| TF / 激酶（F9，可选） | iTAK（或书面指定的等效工具） | 仅在需要该家族时使用 | `F9_itak.sh` | 把 F9 当成植物基因组的检查清单项目 |
| 富集（下游） | `merged_function_table.tsv` + 定义清楚的背景 | 以该次发布的全部基因为背景 | 目录收录了 clusterProfiler 等；部分许可为 NC/ND，不用于配图 | 用方便的子集当背景却不说明 |
| 通路 / KO | Kofam HMM 库和阈值，或 eggNOG 的 KO 字段 | 记录库版本 | KofamScan、eggNOG | 假定 KEGG 数据可以再分发（`[待确认]`） |

### 跨切陷阱

- 这里不做基因预测、soft-mask、TE 库或 GFF 编辑。那些在结构库或 vitis-te。
- METHODS 里四套编号不要混：框架（F1/F2/F3/F5）、脚本（`F2_eggnog.sh` 是框架 F1 里的一步）、工具卡片（F1a/F1b/F1c）、门控（Gate-F1…F7）。
- 合并产物是 `merged_function_table.tsv`。机器预测的 GO/EC 仍是 IEA。
- 框架 F7 注释直系同源组代表序列，不是每个基因。
- Foldseek、DeepFRI、AlphaFold DB 里的 “structure” 指蛋白三维结构。
- InterProScan 属于默认 F1，但很慢；F-L1 是验收标准，不是今晚必须做完 IPS。
- F4/F6/F8/F9 这些植物可选步骤本身不会提高等级。

目录中仍标 `[待确认]` 的条目（HMMER 3、eggNOG 6、PANNZER2、MetaCyc、PRGdb 4.0、psRobot、DALI、ShinyGO — 2026-11-13 网站检查）保持原标记，直到有人打开页面。本文未重新检查那些网站。

更详细的说明（含英文表）见 [`docs/SCENARIOS_FUNCTIONAL.md#data-needs-zh`](docs/SCENARIOS_FUNCTIONAL.md#data-needs-zh)。

![OMArk versus BUSCO proteomes](docs/figures/catalog/07_omark_vs_busco_proteomes.jpg)

*OMArk 与 BUSCO 在 1,805 个真核 UniProt 参考蛋白组上的完整性比较（图 5）。放在这里是因为 F0 输入质控不是类型分节。 Nevers 等 2025，《Nature Biotechnology》43(1):124-133，图 5，doi:10.1038/s41587-024-02147-w（线上 2024-02-21），PMC11738984，CC BY。*

<a id="figure-credits"></a>
## 图注与许可

`docs/figures/` 中的自绘总图属于本仓库。下面目录配图是 CC BY 论文中的原始 JPEG（Europe PMC 许可字段为 `cc by`，2026-11-13 核实）。未使用 NC/ND 材料。

| 文件 | 图注与出处 |
|---|---|
| [`docs/figures/catalog/01_eggnogmapper_v2_runtime.jpg`](docs/figures/catalog/01_eggnogmapper_v2_runtime.jpg) | eggNOG-mapper v2 与其他注释工具的运行时间比较（图 2）。 Cantalapiedra 等 2021，《Molecular Biology and Evolution》图 2，doi:10.1093/molbev/msab293，PMC8662613，CC BY。 |
| [`docs/figures/catalog/02_eggnogmapper_vs_interproscan.jpg`](docs/figures/catalog/02_eggnogmapper_vs_interproscan.jpg) | eggNOG-mapper 与 InterProScan 的比较（图 3）。 Huerta-Cepas 等 2017，《Molecular Biology and Evolution》图 3，doi:10.1093/molbev/msx148，PMC5850834，CC BY。 |
| [`docs/figures/catalog/03_eggnogmapper_rhogap1_go.jpg`](docs/figures/catalog/03_eggnogmapper_rhogap1_go.jpg) | eggNOG-mapper 在一个示例上的 GO 分配（图 4）。 Huerta-Cepas 等 2017，《Molecular Biology and Evolution》图 4，doi:10.1093/molbev/msx148，PMC5850834，CC BY。 |
| [`docs/figures/catalog/04_interpro_pik3ca_domains.jpg`](docs/figures/catalog/04_interpro_pik3ca_domains.jpg) | InterPro 对 PIK3CA 的结构域注释（图 4）。 Blum、Andreeva、Florentino 等 2025，《Nucleic Acids Research》图 4，doi:10.1093/nar/gkae1082，PMC11701551，CC BY。 |
| [`docs/figures/catalog/05_interproscan_human_runtime.jpg`](docs/figures/catalog/05_interproscan_human_runtime.jpg) | InterProScan 在人类蛋白组上的运行时间（图 6）。 Blum、Andreeva、Florentino 等 2025，《Nucleic Acids Research》图 6，doi:10.1093/nar/gkae1082，PMC11701551，CC BY。 |
| [`docs/figures/catalog/06_orthofinder_chordata_summary.jpg`](docs/figures/catalog/06_orthofinder_chordata_summary.jpg) | OrthoFinder 在一个脊索动物示例上的摘要（图 3）。 Emms 与 Kelly 2019，《Genome Biology》图 3，doi:10.1186/s13059-019-1832-y，PMC6857279，CC BY。 |
| [`docs/figures/catalog/07_omark_vs_busco_proteomes.jpg`](docs/figures/catalog/07_omark_vs_busco_proteomes.jpg) | OMArk 与 BUSCO 在 1,805 个真核 UniProt 参考蛋白组上的完整性比较（图 5）。放在这里是因为 F0 输入质控不是类型分节。 Nevers 等 2025，《Nature Biotechnology》43(1):124-133，图 5，doi:10.1038/s41587-024-02147-w（线上 2024-02-21），PMC11738984，CC BY。 |

