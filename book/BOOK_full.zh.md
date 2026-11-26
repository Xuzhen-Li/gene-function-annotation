# 《植物基因功能注释学习笔记：以葡萄为例》

# 前言

本书是植物蛋白组功能注释的学习笔记，与 gene-function-annotation 仓库配套，讲每一步做什么、为什么要做、有哪些工具、结果怎么判断。可运行的框架（F1、F2、F3、F5、F7）、加件和验收等级仍以仓库为准（[`README.zh.md`](../README.zh.md)、[`docs/ROADMAP.md`](../docs/ROADMAP.md)、[`docs/EVALUATION.md`](../docs/EVALUATION.md)）；本书不改变默认框架。

## 怎么读

- 第 1 章讲概念：推断功能的三条路、词表（GO、KEGG、MapMan）、证据代码，以及错误为什么会扩散。
- 第 2 至 16 章对应主页目录的类型小节，一节一章。每章先给出主页该节的说明，再列出每个工具的论文、实验室、权威度和一句评价，最后是这一步的评测证据。
- 第 17 章讲可视化，第 18 章讲怎么选框架和加件，第 19 章汇总常见问题和质控，第 20 章用 `examples/plant_sim/01_vitis_s1_s7/` 的葡萄教学例子走一遍。
- 附录 A 是术语表。

## 出处与标注

每个说法都引用带 DOI 的论文或本仓库中的文件。标为“作者摘要原句”的引文是工具作者在自己摘要中的说法，不是独立结果；独立结果来自 CAFA3（[doi:10.1186/s13059-019-1835-8](https://doi.org/10.1186/s13059-019-1835-8)）和 Quest for Orthologs（[doi:10.1038/nmeth.3830](https://doi.org/10.1038/nmeth.3830)）这类社区评测。权威度和被引次数取自 OpenAlex（2026-11-25 取数）；被引多说明用的人多，不等于最准确。更细的仓库流程中文讲解见 [`docs/zh/`](../docs/zh/README.md)。


![Functional annotation route](../docs/figures/guide/function_route_map_v2.png)

*图：本仓库的功能注释路线：F0 蛋白质控、框架 F1（DIAMOND 比对 Swiss-Prot、eggNOG-mapper、InterProScan）、合并成 `merged_function_table.tsv`、功能质控与发布。可选加件（F4、F6、F8、F9）在合并时并入；其他框架（F2、F3、F5）和多基因组入口 F7 也在合并处汇合。示意图，据 `docs/ROADMAP.md` 与 README 为本仓库绘制；可编辑 SVG：[`function_route_map_v2.svg`](../docs/figures/guide/function_route_map_v2.svg)。*

# 第 1 章 概念与原理

## 1.1 功能注释产出什么

功能注释给结构发布版的蛋白加上标签：可读名称、Gene Ontology（GO）条目、KEGG 直系同源和通路、蛋白结构域和家族，以及可选的植物分类，如 MapMan 类别、NLR 或转录因子家族（主页“概述”）。输入是每个基因一条代表序列的 `proteins.faa`，产物是 `merged_function_table.tsv`（主页“蛋白之外还需要的数据”）。找基因和改 GFF 在 gene-structure-annotation 中完成，不在这里。

## 1.2 推断功能的三条路

- **与人工校对蛋白的相似性。** 用快速比对器把蛋白组比到 Swiss-Prot 等校对库。DIAMOND v2 作者称可在数小时内完成生命之树规模的搜索，灵敏度与 BLASTP 相当（[doi:10.1038/s41592-021-01101-x](https://doi.org/10.1038/s41592-021-01101-x)）。UniProtKB 依据文献人工校对补充功能信息，并正在把序列限定为高质量、非冗余的参考蛋白组（[doi:10.1093/nar/gkae1010](https://doi.org/10.1093/nar/gkae1010)）。
- **特征签名与结构域。** InterPro 整合多个成员数据库的签名，把序列分入家族并预测结构域和位点，并映射到 GO（[doi:10.1093/nar/gkae1082](https://doi.org/10.1093/nar/gkae1082)）；InterProScan 在本地对大量序列运行这些签名（[doi:10.1093/bioinformatics/btu031](https://doi.org/10.1093/bioinformatics/btu031)）。
- **基于直系同源的转移。** eggNOG-mapper 通过预先计算的直系同源关系转移注释（[doi:10.1093/molbev/msab293](https://doi.org/10.1093/molbev/msab293)）；eggNOG 6.0 数据库覆盖 12,535 个参考物种（[doi:10.1093/nar/gkac1022](https://doi.org/10.1093/nar/gkac1022)）。

较新的方法加入了蛋白语言模型和三维结构。FANTASIA 用于约 1,000 个动物蛋白组，为同源方法未能注释的蛋白中最多 50% 预测了功能（[doi:10.1038/s42003-025-08651-2](https://doi.org/10.1038/s42003-025-08651-2)）。AlphaFold DB 收录超过 2.14 亿个预测结构（[doi:10.1093/nar/gkad1011](https://doi.org/10.1093/nar/gkad1011)），Foldseek 搜索结构比旧的结构比对工具快四到五个数量级（[doi:10.1038/s41587-023-01773-0](https://doi.org/10.1038/s41587-023-01773-0)）。

![Three F1 evidence lines merged into one row](../docs/figures/guide/function_evidence_merge_v2.png)

*图：一条蛋白的三条 F1 证据如何合成 `merged_function_table.tsv` 中的一行：每个 GO 词条都保留给出它的来源，机器预测一律标 IEA。数值取自 `testdata/function_aggregate/expected/merged_function_table.tsv` 中的模拟测试行 FAKE_g0001，不是真实基因；示意图，为本仓库绘制。*

## 1.3 词表与证据

- **GO** 是描述基因功能的资源，定期更新（[doi:10.1093/nar/gkaf1292](https://doi.org/10.1093/nar/gkaf1292)）；预测按分子功能、生物过程、细胞组分三个方面分别评测（[doi:10.1186/s13059-019-1835-8](https://doi.org/10.1186/s13059-019-1835-8)）。
- **证据代码。** Evidence and Conclusion Ontology 记录每条注释背后的证据类型，便于追溯来源（[doi:10.1093/nar/gkab1025](https://doi.org/10.1093/nar/gkab1025)）。本仓库中机器预测的 GO 和 EC 一律保持 IEA（电子注释推断）（主页“通用注意事项”）。
- **KEGG。** 每个 KEGG Ortholog（KO）是通用基因标识，通路图是由 KO 节点构成的网络（[doi:10.1093/nar/gkae909](https://doi.org/10.1093/nar/gkae909)）。KofamKOALA 用 profile HMM 和预先计算的自适应阈值分配 KO（[doi:10.1093/bioinformatics/btz859](https://doi.org/10.1093/bioinformatics/btz859)）。
- **MapMan。** MapMan4 是面向植物的蛋白分类框架，配套 Mercator 工具做自动注释（[doi:10.1016/j.molp.2019.01.003](https://doi.org/10.1016/j.molp.2019.01.003)）。

## 1.4 错误为什么要紧

一项针对 37 个酶家族的研究发现，GenBank NR、TrEMBL 和 KEGG 的错误注释率平均为 5% 至 63%，而人工校对的 Swiss-Prot 接近 0%，多数错误来自对分子功能的过度预测（[doi:10.1371/journal.pcbi.1000605](https://doi.org/10.1371/journal.pcbi.1000605)）。CAFA3 评测发现，分子功能和生物过程的预测只略有进步，细胞组分没有进步（[doi:10.1186/s13059-019-1835-8](https://doi.org/10.1186/s13059-019-1835-8)）。很具体的 GO 条目比宽泛条目更难预测（[doi:10.1101/gr.280816.125](https://doi.org/10.1101/gr.280816.125)）。所以仓库把预测标签始终标为预测，并在 METHODS 中记录数据库版本。

## 1.5 先结构后功能

功能标签会继承基因模型的所有错误。同一批基因组用不同注释来源，直系同源结果明显不同（[doi:10.1093/bioinformatics/btaf365](https://doi.org/10.1093/bioinformatics/btaf365)）。因此仓库先做 F0 蛋白 BUSCO 检查，蛋白组质量差就退回结构注释，而不是在这里修补（`examples/plant_sim/01_vitis_s1_s7/plan.md`；主页“所需数据”）。

## 1.6 跨基因组的直系同源

直系同源推断方法要在精确率和召回率之间取舍；Quest for Orthologs 服务用 20 个基准评测了 15 种方法（[doi:10.1038/nmeth.3830](https://doi.org/10.1038/nmeth.3830)）。OrthoFinder 3 称直系同源组准确度比上一版相对提高 7%（[doi:10.1101/2025.07.15.664860](https://doi.org/10.1101/2025.07.15.664860)）。对多基因组面板，仓库注释的是直系同源组代表序列（F7 框架），不是每个基因（主页“通用注意事项”）。

## 1.7 定位与拓扑

SignalP 6.0 能识别全部五类信号肽（[doi:10.1038/s41587-021-01156-3](https://doi.org/10.1038/s41587-021-01156-3)）；TargetP 2.0 识别通往分泌途径、线粒体和叶绿体的 N 端信号（[doi:10.26508/lsa.201900429](https://doi.org/10.26508/lsa.201900429)）；DeepLoc 2.1 预测亚细胞定位和膜蛋白类型（[doi:10.1093/nar/gkae237](https://doi.org/10.1093/nar/gkae237)）；DeepTMHMM 预测 α 螺旋和 β 桶跨膜蛋白的拓扑（[doi:10.1101/2022.04.08.487609](https://doi.org/10.1101/2022.04.08.487609)）。

## 1.8 富集分析

富集检验问的是：一个基因列表是否比背景更常带某些标签。标准方法在 RNA-seq 数据上有偏，因为长转录本和高表达转录本更容易被检出（[doi:10.1186/gb-2010-11-2-r14](https://doi.org/10.1186/gb-2010-11-2-r14)）。长 GO 列表冗余度高，可按语义相似性归纳（[doi:10.1371/journal.pone.0021800](https://doi.org/10.1371/journal.pone.0021800)）。背景应使用完整的发布基因集（主页“所需数据”）。


# 第 2 章 同源搜索

*本章收录[主页第 1 节](../README.zh.md#section-1)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

框架 F1 同源搜索步骤所用的序列相似性比对工具。

**需要：** 本地 DIAMOND（或 BLAST）数据库，一般选用 Swiss-Prot 或有书面说明的同等级库，并将版本号记入 METHODS。[按场景列出的数据需求](../README.zh.md#data-needs)

![DIAMOND speed and sensitivity](../docs/figures/guide/published/diamond_2021_fig1.png)

*图：DIAMOND、MMseqs2 等各搜索模式相对 BLASTP 的加速倍数与比对灵敏度（a），以及每条查询的错误数与蛋白家族覆盖度的关系（b）。原图未修改，引自 Buchfink B、Reuter K、Drost H-G（2021），Sensitive protein alignments at tree-of-life scale using DIAMOND，Nature Methods 18:366-368，Fig. 1，doi:10.1038/s41592-021-01101-x，PMC8026399，许可 CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)。*

**分组：**
- *快速两两搜索*（可替代）：DIAMOND (v2)、MMseqs2、BLAST+。F1 默认用 DIAMOND；聚类和超大数据集用 MMseqs2（CPU 或 GPU）；小规模参考核对用 BLAST+。
- *谱搜索*（互补）：HMMER 3、HH-suite3。Pfam 式 HMM 搜索用 HMMER；疑难蛋白用 HH-suite3 做谱对谱比对。
- *语言模型远缘同源*（可替代）：PLMSearch、pLM-BLAST、Dense Homolog Retriever (DHR)。仅用于经 DIAMOND 和 HMMER 检索后仍无命中的蛋白；结果作为独立证据类别报告。

各条目的单句简介译自英文目录，英文原句见英文版 README。


| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [BLAST+](https://blast.ncbi.nlm.nih.gov/) | 备选 | NCBI BLAST 命令行工具集（含 blastp、makeblastdb）。 | [BMC Bioinformatics 2009](https://doi.org/10.1186/1471-2105-10-421) | Thomas Madden (National Institutes of Health) | 标准 · 25016 次 | 无摘要或仓库说明可引；见原文 |
| [DIAMOND (v2)](https://github.com/bbuchfink/diamond) | 默认（F1） | 高速蛋白序列比对工具，支持类 BLAST 的高灵敏度模式（`--ultra-sensitive`）。 | [Nature Methods 2021](https://doi.org/10.1038/s41592-021-01101-x) | Hajk‐Georg Drost (Max Planck Institute for Developmental Biology) | 标准 · 5873 次 | 作者摘要原句：“Here, we introduce an improved version of DIAMOND that greatly exceeds previous search performances and harnesses supercomputing to perform tree-of-life scale protein alignments in hours, while matching the sensitivity of the gold standard BLASTP.”；GitHub 最后提交 2026-11 |
| [MMseqs2](https://github.com/soedinglab/MMseqs2) | 备选 | 快速、高灵敏度的蛋白序列搜索与聚类工具。GPU 加速版（MMseqs2-GPU，doi:10.1038/s41592-025-02819-8）基于同一套代码，并能加速 ColabFold 的多序列比对。 | [Nature Biotechnology 2017](https://doi.org/10.1038/nbt.3988) | Johannes Söding (Max Planck Institute for Biophysical Chemistry) | 标准 · 5716 次 | GitHub 最后提交 2026-11 |
| [HMMER 3](https://github.com/EddyRivasLab/hmmer) | 备选 | 基于 profile HMM 的同源搜索工具（含 hmmscan、hmmsearch、jackhmmer）。 | [PLoS Computational Biology 2011](https://doi.org/10.1371/journal.pcbi.1002195) | Sean R. Eddy (Howard Hughes Medical Institute) | 标准 · 7895 次 | 作者摘要原句：“HMMER3 is substantially more sensitive and 100- to 1000-fold faster than HMMER2.”；GitHub 最后提交 2026-10 |
| [HH-suite3](https://github.com/soedinglab/hh-suite) | 备选 | 用于远缘同源检测的 HMM-HMM 比对工具（含 HHblits、HHsearch）。 | [BMC Bioinformatics 2019](https://doi.org/10.1186/s12859-019-3019-7) | Johannes Söding (Max Planck Institute for Biophysical Chemistry) | 标准 · 1253 次 | GitHub 最后提交 2026-10 |
| [PLMSearch](https://github.com/maovshao/PLMSearch) | 备选 | 通过比对蛋白语言模型嵌入检测远缘同源蛋白；能检出低序列一致性下被 BLAST 和 DIAMOND 遗漏的命中。 | [Nature Communications 2024](https://doi.org/10.1038/s41467-024-46808-5) | Jianyi Yang (Shandong University) +1 | 成熟 · 125 次 | 作者摘要原句：“Extensive experimental results show that PLMSearch can search millions of query-target protein pairs in seconds like MMseqs2 while increasing the sensitivity by more than threefold, and is comparable to state-of-the-art structure search methods.”；GitHub 最后提交 2025-09 |
| [pLM-BLAST](https://github.com/labstructbioinf/pLM-BLAST) | 备选 | 对逐残基语言模型嵌入执行局部比对，用于检测远缘同源关系并定位匹配区域。 | [Bioinformatics 2023](https://doi.org/10.1093/bioinformatics/btad579) | Stanisław Dunin-Horkawicz (Max Planck Institute for Biology) | 较新 · 96 次 | 作者摘要原句：“Our benchmarks reveal that pLM-BLAST maintains a level of accuracy on par with HHsearch for both highly similar sequences (with >50% identity) and markedly divergent sequences (with <30% identity), while being significantly faster.”；GitHub 最后提交 2026-10 |
| [Dense Homolog Retriever (DHR)](https://github.com/ml4bio/Dense-Homolog-Retrieval) | 备选 | 基于稠密检索的远缘同源搜索工具，兼顾速度与灵敏度；同时可为结构预测构建多序列比对。 | [Nature Biotechnology 2024](https://doi.org/10.1038/s41587-024-02353-6) | Siqi Sun (Fudan University) +2 | 较新 · 58 次 | 作者摘要原句：“Here, we offer an ultrafast, highly sensitive method, dense homolog retriever (DHR), for detecting homologs on the basis of a protein language model and dense retrieval techniques.”；GitHub 最后提交 2026-06 |


# 第 3 章 参考序列与本体数据库

*本章收录[主页第 2 节](../README.zh.md#section-2)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

序列搜索和基因命名步骤所需的参考序列与本体数据库。

**需要：** 数据库文件本体（UniProt、GO、eggNOG、InterPro 成员库等）及对应版本号。这些内容无法仅凭待测蛋白序列推算出来。[按场景列出的数据需求](../README.zh.md#data-needs)

**分组：**
- *序列检索库*（互补）：UniRef、UniProt 2025、TAIR、Ensembl Plants、Carbon Annotation Database (CADB)。F1 的 DIAMOND 比对 Swiss-Prot；需要更广覆盖时用 UniRef；人工审校的名称取自 TAIR 和 Swiss-Prot。
- *特征与家族*（互补）：Pfam (2025)、InterPro 2025、eggNOG 6。Pfam 和 InterPro 支撑 InterProScan；eggNOG 6 支撑 eggNOG-mapper。
- *本体、反应与网络*（互补）：Gene Ontology knowledgebase (2026)、Rhea、STRING (2025)。锁定 GO 版本；精确生化反应用 Rhea；互作网络背景用 STRING。


| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [UniRef](https://www.uniprot.org/help/uniref) | 资源 | 按序列相似性聚类的 UniProt 数据集（UniRef100/90/50）。 | [Bioinformatics 2014](https://doi.org/10.1093/bioinformatics/btu739) | Hongzhan Huang (European Bioinformatics Institute) | 标准 · 2209 次 | 作者摘要原句：“Non-redundancy and intra-cluster homogeneity in UniRef were recently improved by adding a sequence length overlap threshold.” |
| [Pfam (2025)](https://www.ebi.ac.uk/interpro/entry/pfam/) | 资源 | 蛋白家族 HMM 库，现已并入 InterPro；2025 年论文介绍了 AI 辅助的家族构建。早期论文：Pfam 2021（doi:10.1093/nar/gkaa913）。 | [Nucleic Acids Research 2024](https://doi.org/10.1093/nar/gkae997) | Typhaine Paysan‐Lafosse (European Bioinformatics Institute) | 标准 · 537 次 | 无摘要或仓库说明可引；见原文 |
| [TAIR](https://www.arabidopsis.org/) | 资源 | 拟南芥信息资源库（TAIR）：人工审定的拟南芥基因功能与命名数据库。 | [genesis 2015](https://doi.org/10.1002/dvg.22877) | Tanya Berardini (Phoenix Bioinformatics) | 标准 · 1358 次 | 无摘要或仓库说明可引；见原文 |
| [eggNOG 6](http://eggnog6.embl.de/) | 资源 | 支撑 eggNOG-mapper 的层级直系同源数据库。 | [Nucleic Acids Research 2022](https://doi.org/10.1093/nar/gkac1022) | Peer Bork (Yonsei University) +2 | 成熟 · 383 次 | 论文摘要：“Here, we present a major update of the database and website (version 6.0), which increases the number of covered organisms to 12 535 reference species, expands functional annotations, and implements new functionality.” |
| [UniProt 2025](https://www.uniprot.org) | 资源 | Swiss-Prot/TrEMBL 参考数据库；撰写 METHODS 时请引用最新的 NAR 年度更新论文。 | [Nucleic Acids Research 2024](https://doi.org/10.1093/nar/gkae1010) | Jian Zhang | 标准 · 3617 次 | 论文摘要：“In this publication, we describe ongoing changes to our production pipeline to limit the sequences available in UniProtKB to high-quality, non-redundant reference proteomes.” |
| [Carbon Annotation Database (CADB)](https://huggingface.co/blog/HuggingFaceBio/carbon-annotator-genbank-genome-annotation) | 资源 | 使用 Carbon-A 预测的约 48k 个 GenBank 真核组装的蛋白编码位点与蛋白序列库。 | [bioRxiv (Cold Spring Harbor Laboratory) 2026](https://doi.org/10.64898/2026.10.20.760448) | Qiuyi Li (Beijing Academy of Artificial Intelligence) | 较新 · 0 次 | 作者摘要原句：“Across 42 benchmark genomes, Carbon-A achieves the highest overall nucleotide-, exon-, and gene-level F1 scores among the evaluated models.” |
| [Gene Ontology knowledgebase (2026)](https://geneontology.org) | 资源 | 当前 GO 知识库发布论文（发表于 2026 年 NAR；附有一篇更正声明，doi 10.1093/nar/gkag678）。 | [Nucleic Acids Research 2025](https://doi.org/10.1093/nar/gkaf1292) | Monte Westerfield | 成熟 · 461 次 | 作者摘要原句：“The GO knowledgebase is regularly updated and improved.” |
| [Ensembl Plants](https://plants.ensembl.org) | 资源 | 收录植物基因组、基因树与投射注释的综合数据库。 | 无文章 | — | 无论文 | 无摘要或仓库说明可引；见原文 |
| [InterPro 2025](https://www.ebi.ac.uk/interpro/) | 资源 | 支撑 InterProScan 的综合特征数据库；2025 版新增了 AI 辅助整理的 Pfam 家族与基于三维结构的视图。 | [Nucleic Acids Research 2024](https://doi.org/10.1093/nar/gkae1082) | Matthias Blum (European Bioinformatics Institute) | 标准 · 1464 次 | 论文摘要：“In this publication, we report on the status of InterPro (version 101.0), detailing new developments in the database, associated web interface and software.” |
| [Rhea](https://www.rhea-db.org/) | 资源 | 经专家审校的生化反应数据库，供 UniProt 开展酶功能注释；将 EC 编号关联至具体化学反应。 | [Nucleic Acids Research 2021](https://doi.org/10.1093/nar/gkab1016) | Parit Bansal (SIB Swiss Institute of Bioinformatics) +2 | 成熟 · 319 次 | 论文摘要：“In this paper, we describe a number of key developments in Rhea since our last report in the database issue of Nucleic Acids Research in 2019.” |
| [STRING (2025)](https://string-db.org/) | 资源 | 覆盖数千个基因组（含葡萄属）的蛋白关联网络库；支持基于网络的功能推断与富集分析。 | [Nucleic Acids Research 2024](https://doi.org/10.1093/nar/gkae1113) | Peer Bork (Max Delbrück Center) +2 | 标准 · 1138 次 | 作者摘要原句：“The resource now also offers improved annotations of clustered networks and provides users with downloadable network embeddings, which facilitate the use of STRING networks in machine learning and allow cross-species transfer of protein information.” |


# 第 4 章 结构域与家族注释

*本章收录[主页第 3 节](../README.zh.md#section-3)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

框架 F1 结构域步骤中的蛋白结构域与家族注释（InterProScan 及配套数据）。

**需要：** 正常可用的 InterProScan 程序及配套数据库；这一步耗时较长，虽属默认框架 F1，但 F-L1 并不要求当天跑完 IPS。[按场景列出的数据需求](../README.zh.md#data-needs)

**分组：**
- *HMM 特征*（互补）：InterProScan 6、SMART (2021 update)、CDD / CD-Search (2023)。F1 默认用 InterProScan；信号域与结构域架构核对用 SMART 和 CDD。
- *家族树定位*（按顺序）：PANTHER、TreeGrafter。TreeGrafter 将蛋白放置到 PANTHER 进化树上，完成基于系统发育的 GO 注释。

![InterPro PIK3CA domains](../docs/figures/catalog/04_interpro_pik3ca_domains.jpg)

*InterPro 对 PIK3CA 蛋白的结构域注释展示（图 4）。 Blum、Andreeva、Florentino 等 2025，《Nucleic Acids Research》图 4，doi:10.1093/nar/gkae1082，PMC11701551，CC BY。*

![InterProScan human runtime](../docs/figures/catalog/05_interproscan_human_runtime.jpg)

*InterProScan 在人类蛋白组上的运行耗时表现（图 6）。 Blum、Andreeva、Florentino 等 2025，《Nucleic Acids Research》图 6，doi:10.1093/nar/gkae1082，PMC11701551，CC BY。*

| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [InterProScan 6](https://github.com/ebi-pf-team/interproscan6) | 默认（F1） | 调用 InterPro 各成员库（Pfam、PANTHER、SMART、CDD、Gene3D 等）并完成 InterPro2GO 映射。当前版本为 6（2025–2026 年基于 Nextflow 发布），引用论文仍沿用 InterProScan 5。本仓库 F1 的运行脚本针对 v5 编写 [待确认：切换前先测试 v6 的输出列]。 | [Bioinformatics 2014](https://doi.org/10.1093/bioinformatics/btu031) | Alex Mitchell (European Bioinformatics Institute) +1 | 标准 · 10656 次 | 论文摘要：“Here, we describe a new Java-based architecture for the widely used protein function prediction software package InterProScan.”；GitHub 最后提交 2026-11 |
| [SMART (2021 update)](https://smart.embl.de) | 资源 | 信号转导与胞外结构域资源库（InterPro 成员数据库）。 | [Nucleic Acids Research 2020](https://doi.org/10.1093/nar/gkaa937) | Peer Bork (Max Delbrück Center) | 标准 · 2441 次 | 无摘要或仓库说明可引；见原文 |
| [CDD / CD-Search (2023)](https://www.ncbi.nlm.nih.gov/Structure/cdd/cdd.shtml) | 资源 | NCBI 保守结构域模型与 SPARCLE 结构域架构数据库。 | [Nucleic Acids Research 2022](https://doi.org/10.1093/nar/gkac1096) | Aron Marchler‐Bauer (National Institutes of Health) | 标准 · 1479 次 | 无摘要或仓库说明可引；见原文 |
| [PANTHER](https://www.pantherdb.org/) | 资源 | 附带进化树推断 GO 注释的系统发育蛋白家族与亚家族数据库；InterProScan 可直接报告 PANTHER 命中。 | [Protein Science 2021](https://doi.org/10.1002/pro.4218) | Paul D. Thomas (University of Southern California) | 标准 · 2293 次 | 论文摘要：“Here, we describe in detail the current contents of PANTHER, how those contents are generated, and how they can be used in a variety of applications.” |
| [TreeGrafter](https://github.com/pantherdb/TreeGrafter) | 备选 | 将查询蛋白嫁接至 PANTHER 家族进化树，并从最近的已注释祖先节点转移 GO 条目。 | [Bioinformatics 2018](https://doi.org/10.1093/bioinformatics/bty625) | Paul D. Thomas (University of Southern California) | 小众 · 81 次 | 作者摘要原句：“We show that TreeGrafter outperforms subfamily HMM scoring for correctly assigning subfamily membership, and that it produces highly specific annotations of GO terms based on annotated reference phylogenetic trees.”；GitHub 最后提交 2026-04 |
| [ProteInfer](https://github.com/google-research/proteinfer) | 备选 | 直接从氨基酸序列预测 Pfam、EC 和 GO 标签的深度神经网络；适合快速核查无 HMM 命中的蛋白。 | [eLife 2023](https://doi.org/10.7554/eLife.80942) | Theo Sanderson (The Francis Crick Institute) | 成熟 · 216 次 | 论文摘要：“Here we introduce ProteInfer, which instead employs deep convolutional neural networks to directly predict a variety of protein functions - Enzyme Commission (EC) numbers and Gene Ontology (GO) terms - directly from an unaligned amino acid sequence.”；GitHub 最后提交 2026-03 |


# 第 5 章 基于直系同源的名称、GO 与 KEGG

*本章收录[主页第 4 节](../README.zh.md#section-4)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

基于直系同源或序列相似性的基因名称、GO 与 KEGG 注释，亦涵盖完整注释框架（F1 直系同源步骤、快速框架 F2、EnTAP 框架 F3、F4 可读名称）。

**需要：** eggNOG-mapper 数据库（若需生成可读名称，再补充可选的 AHRD / PANNZER 输入）。机器自动分配的 GO 仍归为电子注释证据（IEA）。[按场景列出的数据需求](../README.zh.md#data-needs)

**分组：**
- *可读名称*（可替代）：AHRD、PANNZER2、Sma3s v2。F4 默认用 AHRD；PANNZER2 同时输出带评分的 GO 预测。
- *一体化套件*（可替代）：EnTAP、Trinotate、Blast2GO、FA-nf、GOMAP、TRAPID 2.0。均为 F1 的替代方案而非附加步骤：含 EnTAP（F3）和 Trinotate（F5）；GOMAP 面向植物；Blast2GO 为商业软件。
- *直系同源转移与定位*（互补）：eggNOG-mapper v2、OMAmer、FANTASIA。eggNOG-mapper v2 是 F1 中 GO、KEGG 和 EC 的默认来源；OMAmer 用于快速定位家族；FANTASIA 只用于没有同源命中的蛋白。

![eggNOG-mapper v2 runtime](../docs/figures/catalog/01_eggnogmapper_v2_runtime.jpg)

*eggNOG-mapper v2 与其他功能注释工具的运行耗时对比（图 2）。 Cantalapiedra 等 2021，《Molecular Biology and Evolution》图 2，doi:10.1093/molbev/msab293，PMC8662613，CC BY。*

![eggNOG-mapper versus InterProScan](../docs/figures/catalog/02_eggnogmapper_vs_interproscan.jpg)

*eggNOG-mapper 与 InterProScan 的注释结果对比（图 3）。 Huerta-Cepas 等 2017，《Molecular Biology and Evolution》图 3，doi:10.1093/molbev/msx148，PMC5850834，CC BY。*

![eggNOG-mapper GO example](../docs/figures/catalog/03_eggnogmapper_rhogap1_go.jpg)

*eggNOG-mapper 在具体实例上的 GO 分配过程（图 4）。 Huerta-Cepas 等 2017，《Molecular Biology and Evolution》图 4，doi:10.1093/molbev/msx148，PMC5850834，CC BY。*

| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [eggNOG-mapper v2](https://github.com/eggnogdb/eggnog-mapper) | 默认（F1） | 基于直系同源的功能注释工具：分配基因名称、GO、KEGG、EC 与 COG。 | [Molecular Biology and Evolution 2021](https://doi.org/10.1093/molbev/msab293) | Peer Bork (Yonsei University) +1 | 标准 · 6146 次 | 论文摘要：“Here, we describe a major upgrade to eggNOG-mapper, a tool for functional annotation based on precomputed orthology assignments, now optimized for vast (meta)genomic data sets.”；GitHub 最后提交 2026-08 |
| [PANNZER2](http://ekhidna2.biocenter.helsinki.fi/sanspanz/) | 备选 | 快速的网页端及本地端 GO 与自由文本功能描述预测工具。 | [Nucleic Acids Research 2018](https://doi.org/10.1093/nar/gky350) | Petri Törönen (University of Helsinki) +1 | 标准 · 595 次 | 论文摘要：“Here, we introduce PANNZER2 (Protein ANNotation with Z-scoRE), a fast functional annotation web server that provides both Gene Ontology (GO) annotations and free text description predictions.” |
| [Blast2GO](https://www.biobam.com/omicsbox/) | 备选 | 基于 BLAST 的 GO 注释与可视化工具（现已并入商业软件 OmicsBox）。 | [Bioinformatics 2005](https://doi.org/10.1093/bioinformatics/bti610) | Ana Conesa (Alfred-Wegener-Institut Helmholtz-Zentrum für Polar- und Meeresforschung) | 标准 · 12842 次 | 论文摘要：“We present here Blast2GO (B2G), a research tool designed with the main purpose of enabling Gene Ontology (GO) based data mining on sequence data for which no GO annotation is yet available.” |
| [EnTAP](https://github.com/harta55/EnTAP) | 备选 | 非模式真核生物注释流程：整合序列过滤、相似性搜索、污染标记、eggNOG 与 InterPro。 | [Molecular Ecology Resources 2019](https://doi.org/10.1111/1755-0998.13106) | Jill Wegrzyn (University of Connecticut) | 成熟 · 250 次 | 作者摘要原句：“EnTAP (Eukaryotic Non-Model Transcriptome Annotation Pipeline) was designed to improve the accuracy, speed, and flexibility of functional gene annotation for de novo assembled transcriptomes in non-model eukaryotes.”；GitHub 已归档（最后提交 2025-01） |
| [FA-nf](https://github.com/guigolab/FA-nf) | 备选 | 面向非模式生物蛋白的 Nextflow 功能注释流程（串联 BLAST、InterProScan、KEGG 与信号肽预测）。 | [Genes 2021](https://doi.org/10.3390/genes12101645) | Antonio Hermoso (Barcelona Institute of Science and Technology) | 小众 · 7 次 | 作者摘要原句：“It is also useful for proofreading and improving gene structural annotation.”；GitHub 最后提交 2022-02 |
| [Sma3s v2](https://github.com/UPOBioinfo/sma3s) | 备选 | 比对 UniProt 为蛋白组或转录组分配 GO、关键词与代谢通路的功能注释工具。 | [PROTEOMICS 2017](https://doi.org/10.1002/pmic.201700071) | Antonio J. Pérez‐Pulido (Consejo Superior de Investigaciones Científicas) | 成熟 · 107 次 | 作者摘要原句：“Sma3s is an accurate computational tool for annotating proteins in an unattended way.”；GitHub 最后提交 2026-09 |
| [AHRD](https://github.com/groupschoof/AHRD) | 默认（F4） | 根据 BLAST 比对结果自动分配可读基因功能描述（Human Readable Descriptions）的工具。 | 无文章 | — | 无论文 | 仓库简介：“High throughput protein function annotation with Human Readable Description (HRDs) and Gene Ontology (GO) Terms.”；GitHub 最后提交 2023-08 |
| [GOMAP](https://github.com/Dill-PICL/GOMAP) | 备选 | 面向植物的 GO 元注释工具（GOMAP）：整合序列相似性、结构域与混合方法预测结果以生成植物 GO 集。 | [Plant Methods 2021](https://doi.org/10.1186/s13007-021-00754-1) | Kokulapalan Wimalanathan (Iowa State University) +1 | 小众 · 56 次 | 作者摘要原句：“Assessment shows that GOMAP expands and improves the number of genes annotated and annotations assigned per gene as well as the quality (based on [Formula: see text]) of GO assignments in maize.”；GitHub 最后提交 2023-05 |
| [TRAPID 2.0](https://bioinformatics.psb.ugent.be/trapid_02/) | 备选 | 基于 PLAZA 参考库对从头组装的植物转录组做分类学与功能分析的网页工具。 | [Nucleic Acids Research 2021](https://doi.org/10.1093/nar/gkab565) | Klaas Vandepoele (Ghent University) | 小众 · 79 次 | 论文摘要：“To alleviate some of these challenges, we developed TRAPID 2.0, a web application for the fast and efficient processing of assembled transcriptome data.” |
| [OMAmer](https://github.com/DessimozLab/omamer) | 备选 | 将蛋白免比对归入 OMA 层级直系同源群；运行速度快且能区分亚家族（OMArk 底层亦调用该工具）。 | [Bioinformatics 2021](https://doi.org/10.1093/bioinformatics/btab219) | Marc Robinson‐Rechavi (SIB Swiss Institute of Bioinformatics) +1 | 小众 · 25 次 | 作者摘要原句：“Whilst able to reject non-homologous family-level assignments, we show that OMAmer provides better and quicker subfamily-level assignments than approaches relying on the closest sequence, whether inferred exactly by Smith-Waterman or by the fast heuristic …”；GitHub 最后提交 2026-11 |
| [FANTASIA](https://github.com/CBBIO/FANTASIA) | 备选 | 基于嵌入相似度在全蛋白组范围转移 GO 条目；专用于缺乏同源注释的"暗"蛋白。 | [Communications Biology 2025](https://doi.org/10.1038/s42003-025-08651-2) | Gemma I. Martínez‐Redondo (Institut de Biologia Evolutiva) +2 | 较新 · 38 次 | 作者摘要原句：“FANTASIA holds particular promise for functional discovery in non-model taxa, offering advantages over homology-based tools in sensitivity and generalizability.”；GitHub 最后提交 2026-09 |
| [Trinotate](https://github.com/Trinotate/Trinotate) | F5 路线 | 面向从头组装转录组预测肽段的注释套件（将 BLAST、Pfam、SignalP 和 GO 结果汇总至 SQLite）；对应 F5 路线。此处列出的是作者指定引用的文献。 | [Cell Reports 2017](https://doi.org/10.1016/j.celrep.2016.12.063) | Brian J. Haas (Broad Institute) +1 | 标准 · 1176 次 | GitHub 最后提交 2026-11 |


# 第 6 章 机器学习 GO 预测

*本章收录[主页第 5 节](../README.zh.md#section-5)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

基于机器学习的 GO 预测。属于框架 F1 之后的可选附加项，不能替代 F1。

**需要：** 通常只需输入蛋白序列，配合工具自带的模型。这些工具是框架 F1 之后的可选附加项，不能替代 F1。[按场景列出的数据需求](../README.zh.md#data-needs)

**分组：**
- *序列与语言模型预测器*（可替代）：DeepGO-SE、GoPredSim、SPROF-GO、TALE、NetGO 3.0、ProtGO、AltereGO、DeepGOPlus。填补 F1 注释空白时优先选用 DeepGO-SE 或 GoPredSim；DeepGOPlus 主要用于复现旧表。机器学习预测的 GO 须单独存为一列证据。
- *利用结构的预测器*（可替代）：DeepFRI、DPFunc。依赖预测的三维结构（第 13 节）；适用于序列分化较大的蛋白家族。


| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [DeepGOPlus](https://github.com/bio-ontology-research-group/deepgoplus) | 备选 | 结合 CNN 与 DIAMOND 从序列预测 GO 的工具。 | [Bioinformatics 2019](https://doi.org/10.1093/bioinformatics/btz595) | Robert Hoehndorf (King Abdullah University of Science and Technology) | 标准 · 562 次 | 作者摘要原句：“DeepGOPlus can annotate around 40 protein sequences per second on common hardware, thereby making fast and accurate function predictions available for a wide range of proteins.”；GitHub 最后提交 2026-10 |
| NetGO 3.0 | 备选 | 基于蛋白语言模型的 GO 预测在线服务（CAFA 评测名列前茅）。 | [Genomics Proteomics & Bioinformatics 2023](https://doi.org/10.1016/j.gpb.2023.04.001) | Shanfeng Zhu (Fudan University) | 成熟 · 108 次 | 作者摘要原句：“As one of the state-of-the-art automated function prediction (AFP) methods, NetGO 2.0 integrates multi-source information to improve the performance.” |
| [DeepFRI](https://github.com/flatironinstitute/DeepFRI) | 备选 | 结合三维结构与蛋白序列预测功能的图卷积网络工具。规模化流程 metagenomic-DeepFRI（2026 预印本，doi:10.64898/2026.04.27.720983）将该算法扩展至大规模蛋白集。 | [Nature Communications 2021](https://doi.org/10.1038/s41467-021-23303-9) | Vladimir Gligorijević (Flatiron Institute) +1 | 标准 · 1186 次 | 作者摘要原句：“It outperforms current leading methods and sequence-based Convolutional Neural Networks and scales to the size of current sequence repositories.”；GitHub 最后提交 2023-03 |
| [GoPredSim](https://github.com/Rostlab/goPredSim) | 备选 | 基于序列嵌入向量（SeqVec/ProtT5）相似性转移 GO 标签的工具。 | [Scientific Reports 2021](https://doi.org/10.1038/s41598-020-80786-0) | Maria Littmann (Technical University of Munich) | 成熟 · 216 次 | GitHub 最后提交 2024-12 |
| [DeepGO-SE](https://github.com/bio-ontology-research-group/deepgo2) | 备选 | 基于 ESM2 嵌入向量与 GO 公理、通过近似语义蕴涵预测 GO 的工具。 | [Nature Machine Intelligence 2024](https://doi.org/10.1038/s42256-024-00795-w) | Maxat Kulmanov (King Abdullah University of Science and Technology) +1 | 成熟 · 173 次 | 作者摘要原句：“We show, using several benchmarks, that the approach effectively exploits background knowledge in the GO and improves protein function prediction compared to state-of-the-art methods.”；GitHub 最后提交 2026-10 |
| [ProtGO](https://github.com/sunyatawang/ProtGO) | 备选 | 多模态 GO 预测工具（整合蛋白语言模型、文本、分类学信息与 GO 图结构）。 | [Bioinformatics 2025](https://doi.org/10.1093/bioinformatics/btaf390) | Jie Tang (Tsinghua University) +1 | 较新 · 15 次 | 作者摘要原句：“Extensive experiments demonstrate that ProtGO significantly advances the abilities of state-of-the-art PLMs to predict protein functions: approximately 8% to 27% increase in the maximum F1 measure (Fmax) compared to base models.”；GitHub 最后提交 2024-07 |
| AltereGO | 备选 | 在打分层面融合 ESM2、ProtT5、Ankh 与 ProstT5-3Di 预测器以预测 GO 分子功能的工具（2026 预印本）。 | [bioRxiv (Cold Spring Harbor Laboratory) 2026](https://doi.org/10.64898/2026.10.23.761425) | J. Andrew Amburn (University of Tennessee at Knoxville) | 较新 · 0 次 | 作者摘要原句：“In matched comparisons with eight released prediction methods, AltereGO achieved significantly improved ranking capabilities AUPRC in every comparison and significantly better F max and S min in six.” |
| [DPFunc](https://github.com/CSUBioGroup/DPFunc) | 备选 | 结合结构域与三维结构信息的深度学习 GO 预测工具。 | [Nature Communications 2025](https://doi.org/10.1038/s41467-024-54816-8) | Min Li (Central South University) | 较新 · 81 次 | 作者摘要原句：“In this study, we propose a deep learning-based solution, named DPFunc, for accurate protein function prediction with domain-guided structure information.”；GitHub 最后提交 2026-03 |
| [SPROF-GO](https://github.com/biomed-AI/SPROF-GO) | 备选 | 结合蛋白语言模型特征与基于同源的标签扩散算法预测 GO 条目。 | [Briefings in Bioinformatics 2023](https://doi.org/10.1093/bib/bbad117) | Huiying Zhao (Sun Yat-sen University) +1 | 成熟 · 107 次 | 作者摘要原句：“Due to the explosive growth of proteins in sequence databases and the diversity of their functions, it remains challenging to fast and accurately predict protein functions from sequences alone.”；GitHub 最后提交 2024-07 |
| [TALE](https://github.com/Shen-Lab/TALE) | 备选 | 用 Transformer 把序列和 GO 标签联合嵌入，因此能为很少被注释的条目排序。 | [Bioinformatics 2021](https://doi.org/10.1093/bioinformatics/btab198) | Yang Shen (Texas A&M University) | 成熟 · 178 次 | 作者摘要原句：“Combining TALE and a sequence similarity-based method, TALE+ outperformed competing methods when only sequence input is available.”；GitHub 最后提交 2024-12 |
| [CAFA3 assessment](https://biofunctionprediction.org/cafa/) | 参考 | 蛋白功能预测方法的社区评测。 | [Genome biology 2019](https://doi.org/10.1186/s13059-019-1835-8) | Iddo Friedberg (Iowa State University) | 标准 · 561 次 | 作者摘要原句：“We conclude that while predictions of the molecular function and biological process annotations have slightly improved over time, those of the cellular component have not.” |

> 评测要点： CAFA3：分子功能和生物过程的预测比早期略有提升，细胞组分没有提升，最好的方法仍有很大改进空间（doi:10.1186/s13059-019-1835-8）。机器学习得到的 GO 只能当候选。


# 第 7 章 通路、KO 与 EC

*本章收录[主页第 6 节](../README.zh.md#section-6)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

代谢通路、KO 与 EC 注释（F1+ Kofam、框架 F6 MapMan 及相关附加项）。

**需要：** 跑 Kofam / KO 需准备 HMM 模型库及打分阈值；跑 MapMan（F6）需准备 Mercator4 结果（网页版或本地版，见 `docs/MERCATOR_WHEN.md`）。KEGG 的再分发规定目前标为 `[待确认]`，此处不作预设。[按场景列出的数据需求](../README.zh.md#data-needs)

**分组：**
- *KO 分配*（可替代）：KofamKOALA / KofamScan、BlastKOALA / GhostKOALA、KAAS。KofamScan 支持本地运行（F1+ 可选）；BlastKOALA 和 KAAS 为网页端替代方案。
- *植物通路框架与酶参考*（互补）：MapMan4 / Mercator4、Plant Reactome (2024)、Plant Metabolic Network / E2P2、Pathway Tools、MetaCyc、KEGG (2025 NAR)、BRENDA。植物 BIN 用 Mercator4（F6）；先用 E2P2 预测酶，再用 Pathway Tools 构建葡萄通路数据库；核对 EC 结果时以 BRENDA 为酶参考。
- *EC 预测*（可替代）：DeepEC、CLEAN、EZpred、ProteEC-CLA。没有 KO 的酶先用 CLEAN；结果对照 BRENDA 核对。
- *完整度与基因簇*（互补）：KEGG Mapper、kegg-pathways-completeness、plantiSMASH 2.0。基于 KO 集合评估通路完整度；生物合成基因簇识别用 plantiSMASH。


| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [MapMan4 / Mercator4](https://www.plabipd.de/mercator_main.html) | 备选 | 由 Mercator4 分配的植物专用功能分类体系（MapMan4）。 | [Molecular Plant 2019](https://doi.org/10.1016/j.molp.2019.01.003) | Marie Bolger (Forschungszentrum Jülich) | 标准 · 585 次 | 论文摘要：“Here we present a redesigned and significantly enhanced MapMan4 framework, together with a revised version of the associated online Mercator annotation tool.” |
| [KofamKOALA / KofamScan](https://www.genome.jp/tools/kofamkoala/) | 备选 | 利用自适应阈值 profile HMM 分配 KEGG Orthology（KO）的工具。 | [Bioinformatics 2019](https://doi.org/10.1093/bioinformatics/btz859) | Hiroyuki Ogata (Kyoto University) | 标准 · 2358 次 | 作者摘要原句：“KofamKOALA is faster than existing KO assignment tools with its accuracy being comparable to the best performing tools.” |
| [BlastKOALA / GhostKOALA](https://www.kegg.jp/blastkoala/) | 备选 | 基于序列相似性分配 KO 编号的 KEGG 在线服务。 | [Journal of Molecular Biology 2015](https://doi.org/10.1016/j.jmb.2015.11.006) | Minoru I. Kanehisa (Kyoto University) | 标准 · 4552 次 | 无摘要或仓库说明可引；见原文 |
| [KEGG Mapper](https://www.kegg.jp/kegg/mapper/) | 备选 | 将 KO 列表映射至 KEGG 代谢通路、BRITE 层级与功能模块的工具。 | [Protein Science 2019](https://doi.org/10.1002/pro.3711) | Minoru I. Kanehisa (Kyoto University Institute for Chemical Research) | 标准 · 1339 次 | 论文摘要：“Here we report a new version of KEGG Mapper, a suite of KEGG mapping tools available at the KEGG website (https://www.kegg.jp/ or https://www.genome.jp/kegg/), together with the KOALA family tools for automatic assignment of KO (KEGG Orthology) identifiers …” |
| [kegg-pathways-completeness](https://github.com/EBI-Metagenomics/kegg-pathways-completeness-tool) | 备选 | 根据 KO 列表计算 KEGG 功能模块完整度的工具。 | 无文章 | — | 无论文 | 仓库简介：“This tool estimates the completeness of KEGG pathway modules from the presence or absence of KEGG orthologues (KOs)”；GitHub 最后提交 2026-10 |
| [MetaCyc](https://metacyc.org/) | 资源 | 跨物种的人工审定代谢通路与酶数据库。 | [Nucleic Acids Research 2019](https://doi.org/10.1093/nar/gkz862) | Ron Caspi (SRI International) +1 | 标准 · 1617 次 | 无摘要或仓库说明可引；见原文 |
| [BRENDA](https://www.brenda-enzymes.org/) | 资源 | 综合性的酶功能与 EC 编号数据库。 | [Nucleic Acids Research 2020](https://doi.org/10.1093/nar/gkaa1025) | Dietmar Schomburg (Technische Universität Braunschweig) | 标准 · 899 次 | 无摘要或仓库说明可引；见原文 |
| DeepEC | 备选 | 基于深度学习预测 EC 编号的工具。 | [Proceedings of the National Academy of Sciences 2019](https://doi.org/10.1073/pnas.1821905116) | Sang Yup Lee (Korea Advanced Institute of Science and Technology) | 成熟 · 346 次 | 作者摘要原句：“Here, we report DeepEC, a deep learning-based computational framework that predicts EC numbers for protein sequences with high precision and in a high-throughput manner.” |
| [KEGG (2025 NAR)](https://www.kegg.jp) | 资源 | 用于 KO 与代谢通路映射的当前 KEGG 引用文献（2025 NAR）。 | [Nucleic Acids Research 2024](https://doi.org/10.1093/nar/gkae909) | Minoru I. Kanehisa (Kyoto University) | 标准 · 3418 次 | 无摘要或仓库说明可引；见原文 |
| [Plant Reactome (2024)](https://plantreactome.gramene.org) | 资源 | 人工审定的植物代谢通路数据库（以水稻为参考并投射至其他植物）。 | [Nucleic Acids Research 2023](https://doi.org/10.1093/nar/gkad1052) | Pankaj Jaiswal (Oregon State University) +1 | 较新 · 16 次 | 作者摘要原句：“It provides curated reference pathways from rice (Oryza sativa) and gene-orthology-based pathway projections to 129 additional species, spanning single-cell photoautotrophs, non-vascular plants, and higher plants, thus encompassing a wide-ranging taxonomic …” |
| [Plant Metabolic Network / E2P2](https://plantcyc.org) | 备选 | 利用 E2P2 酶预测工具构建的 PlantCyc 及各物种代谢通路数据库。 | 无文章 | — | 无论文 | 无摘要或仓库说明可引；见原文 |
| [CLEAN](https://github.com/tttianhao/CLEAN) | 备选 | 基于对比学习预测 EC 编号的工具。 | [Science 2023](https://doi.org/10.1126/science.adf2465) | Tianhao Yu (University of Illinois Urbana-Champaign) +2 | 标准 · 566 次 | 作者摘要原句：“We present a machine learning algorithm named CLEAN (contrastive learning-enabled enzyme annotation) to assign EC numbers to enzymes with better accuracy, reliability, and sensitivity compared with the state-of-the-art tool BLASTp.”；GitHub 最后提交 2025-04 |
| EZpred | 备选 | 利用无标签同源序列预测 EC 编号的工具（发表于 Advanced Science 2026）。 | [Advanced Science 2026](https://doi.org/10.1002/advs.78703) | Quancheng Liu (University of Michigan) +1 | 较新 · 1 次 | 作者摘要原句：“For test enzymes with < 30% sequence identity to any training proteins, the F1‐score of EZpred EC number prediction is at least 34% higher than state‐of‐the‐art EC number prediction models.” |
| ProteEC-CLA | 备选 | 在 ESM2 基础上结合对比学习与代理注意力机制（agent attention）预测 EC 编号的工具。 | [Proteins Structure Function and Bioinformatics 2025](https://doi.org/10.1002/prot.26822) | Yue Zhao (Beijing Forestry University) | 较新 · 3 次 | 作者摘要原句：“ProteEC-CLA utilizes contrastive learning to construct positive and negative sample pairs, which not only enhances sequence feature extraction but also improves the utilization of unlabeled data.” |
| [plantiSMASH 2.0](https://github.com/plantismash/plantismash) | 备选 | 植物生物合成基因簇（BGC）检测工具，支持部分酶家族底物预测与启动子 TF 结合位点分析；内置覆盖 430 个基因组约 30k 个 BGC 的数据库。 | [Journal of Molecular Biology 2026](https://doi.org/10.1016/j.jmb.2026.169798) | Elena Del Pup (Wageningen University & Research) +3 | 较新 · 21 次 | 作者摘要原句：“Together, these improvements make plantiSMASH 2.0 a powerful and comprehensive platform for the detection and characterization of plant biosynthetic pathways, supporting and accelerating research in plant specialized metabolism and plant natural product …”；GitHub 最后提交 2026-02 |
| [KAAS](https://www.genome.jp/kegg/kaas/) | 备选 | KEGG 在线注释服务，通过双向最佳命中分配 KO 编号并重建通路图。 | [Nucleic Acids Research 2007](https://doi.org/10.1093/nar/gkm321) | Minoru I. Kanehisa (Kyoto University Institute for Chemical Research) | 标准 · 4594 次 | 论文摘要：“Here, we have developed a web-based server called KAAS (KEGG Automatic Annotation Server: http://www.genome.jp/kegg/kaas/) i.e. an implementation of a rapid method to automatically assign K numbers to genes in the genome, enabling reconstruction of KEGG …” |
| [Pathway Tools](https://bioinformatics.ai.sri.com/ptools/) | 备选 | 构建物种专属的通路/基因组数据库；在 PMN 流程中，先由 E2P2 预测酶，再用 Pathway Tools 建库（PlantCyc 即如此构建）。 | [Briefings in Bioinformatics 2019](https://doi.org/10.1093/bib/bbz104) | Peter E Midford (SRI International) | 成熟 · 260 次 | 作者摘要原句：“It can now support metabolic-model execution through the Web, it provides a more accurate gap filler for metabolic models; it supports development of models for organism communities distributed across a spatial grid; and model results may be visualized …” |
| [DeepECtransformer](https://github.com/kaistsystemsbiology/DeepProZyme) | 备选 | 基于 Transformer 从序列预测 EC 号。 | [Nature Communications 2023](https://doi.org/10.1038/s41467-023-43216-z) | Sang Yup Lee (Korea Advanced Institute of Science and Technology) | 成熟 · 144 次 | 论文摘要：“Here we present a deep learning model, DeepECtransformer, which utilizes transformer layers as a neural network architecture to predict EC numbers.”；GitHub 最后提交 2023-10 |


# 第 8 章 多基因组直系同源

*本章收录[主页第 7 节](../README.zh.md#section-7)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

跨基因组的直系同源基因群划分。框架 F7 仅对直系同源群的代表序列做功能注释，而非逐个基因注释。

**需要：** 数据集中各个基因组的蛋白 FASTA。框架 F7 仅注释直系同源群的代表序列，而非每个基因。[按场景列出的数据需求](../README.zh.md#data-needs)

**分组：**
- *直系同源群推断*（可替代）：OrthoFinder 3、SonicParanoid2、Broccoli、Proteinortho6、FastOMA。F7 默认用 OrthoFinder 3；物种面板很大时选用 FastOMA 或 SonicParanoid2。
- *参考目录*（互补）：PLAZA 5.0、OrthoDB v12、OMA browser 2024、PhylomeDB V5、OrthoVenn3。利用植物库和基于进化树的参考库交叉核对直系同源群。
- *家族演化*（按顺序）：OrthoFinder 3 或 SonicParanoid2 或 Broccoli 或 Proteinortho6 或 FastOMA、CAFE 5。先确定直系同源群，再用 CAFE 5 估计扩张和收缩。

![OrthoFinder Chordata](../docs/figures/catalog/06_orthofinder_chordata_summary.jpg)

*OrthoFinder 在脊索动物数据集上的分析结果概览（图 3）。 Emms 与 Kelly 2019，《Genome Biology》图 3，doi:10.1186/s13059-019-1832-y，PMC6857279，CC BY。*

| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [Broccoli](https://github.com/rderelle/Broccoli) | 备选 | 结合系统发育树与网络标签传播推断直系同源关系的工具。 | [Molecular Biology and Evolution 2020](https://doi.org/10.1093/molbev/msaa159) | Romain Derelle (University of Birmingham) | 成熟 · 113 次 | 作者摘要原句：“In this article, we introduce Broccoli, a user-friendly pipeline designed to infer, with high precision, orthologous groups, and pairs of proteins using a phylogeny-based approach.”；GitHub 最后提交 2026-10 |
| [Proteinortho6](https://gitlab.com/paulklemm_PHD/proteinortho) | 备选 | 面向大规模数据的图算法（共）直系同源检测工具。 | [Frontiers in Bioinformatics 2023](https://doi.org/10.3389/fbinf.2023.1322477) | Marcus Lechner (Philipps University of Marburg) | 较新 · 46 次 | 作者摘要原句：“In this contribution, we evaluate and implement major algorithmic improvements that significantly enhance the speed of the analysis without reducing precision.” |
| [CAFE 5](https://github.com/hahnlab/CAFE5) | 备选 | 在演化速率变异模型下分析基因家族扩张与收缩的工具。 | [Bioinformatics 2020](https://doi.org/10.1093/bioinformatics/btaa1022) | Dan Vanderpool (Indiana University Bloomington) | 标准 · 949 次 | 作者摘要原句：“These include improved support for multithreading, the explicit modeling of rate variation among families using gamma-distributed rate categories, and command-line arguments that preclude the use of accessory scripts.”；GitHub 最后提交 2026-10 |
| [PLAZA 5.0](https://bioinformatics.psb.ugent.be/plaza/) | 资源 | 植物比较基因组学平台：涵盖基因家族、直系同源与 GO/InterPro 注释投射。 | [Nucleic Acids Research 2021](https://doi.org/10.1093/nar/gkab1024) | Klaas Vandepoele (Ghent University) | 成熟 · 281 次 | 作者摘要原句：“This latest release also comes with a set of new and updated features: a new BED import functionality for the workbench, improved interactive visualizations for functional enrichments and genome-wide mapping of gene sets, and a fully redesigned and extended …” |
| [OrthoFinder 3](https://github.com/OrthoFinder/OrthoFinder) | 默认（F7） | 可扩展的系统发育直系同源推断工具（v3.x 版本采用 FAMSA 比对）。 | [Nature Methods 2026](https://doi.org/10.1101/2025.07.15.664860) | Steven L. Kelly (University of Oxford) | 成熟 · 122 次 | 作者摘要原句：“This extends OrthoFinder's high-accuracy comparative genomic framework to provide substantially enhanced scalability and accuracy.”；GitHub 最后提交 2026-11 |
| [FastOMA](https://github.com/DessimozLab/FastOMA) | 备选 | 呈线性扩展的快速直系同源推断工具（基于 OMAmer 归置）。 | [Nature Methods 2025](https://doi.org/10.1038/s41592-024-02552-8) | Christophe Dessimoz (SIB Swiss Institute of Bioinformatics) | 较新 · 37 次 | 作者摘要原句：“Here, addressing this, 'FastOMA' provides linear scalability for orthology inference, enabling the processing of thousands of eukaryotic genomes within a day.”；GitHub 最后提交 2026-11 |
| [SonicParanoid2](https://gitlab.com/salvo981/sonicparanoid2) | 备选 | 结合机器学习与语言模型的快速直系同源推断工具。 | [Genome biology 2024](https://doi.org/10.1186/s13059-024-03298-4) | Wataru Iwasaki (Institute for Quantitative Biosciences, The University of Tokyo) | 较新 · 56 次 | 作者摘要原句：“SonicParanoid is one of the fastest tools for orthology inference; however, its scalability and accuracy have been hampered by time-consuming all-versus-all alignments and the existence of proteins with complex domain architectures.” |
| [OrthoDB v12](https://www.orthodb.org) | 资源 | 附带功能描述的层级直系同源数据库（见 OrthoDB 与 BUSCO 联合更新论文）。 | [Nucleic Acids Research 2024](https://doi.org/10.1093/nar/gkae987) | Evgeny M. Zdobnov (University of Geneva) +1 | 标准 · 592 次 | 无摘要或仓库说明可引；见原文 |
| [OMA browser 2024](https://omabrowser.org) | 资源 | OMA 直系同源数据库 2024 更新版。 | [Nucleic Acids Research 2023](https://doi.org/10.1093/nar/gkad1020) | Natasha Glover (SIB Swiss Institute of Bioinformatics) | 成熟 · 112 次 | 论文摘要：“In this update paper, we present the latest developments in the OMA browser knowledgebase, which aims to provide high-quality orthology inferences and facilitate the study of gene families, genomes and their evolution.” |
| [OrthoVenn3](https://orthovenn3.bioinfotoolkits.net/) | 备选 | 在线比较基因组平台，支持跨多个基因组聚类并对比直系同源群，提供韦恩图与系统发育视图。 | [Nucleic Acids Research 2023](https://doi.org/10.1093/nar/gkad313) | Ling Xu (China Agricultural University) +1 | 标准 · 582 次 | 作者摘要原句：“Furthermore, OrthoVenn3 now provides gene family contraction and expansion analysis to support researchers better understanding the evolutionary history of gene families, as well as collinearity analysis to detect conserved and variable genomic structures.” |
| PhylomeDB V5 | 资源 | 全基因组基因树目录及基于进化树的直系同源预测库；可用于核对基于图聚类的直系同源群。[待确认: 2026-11-14 访问 phylomedb.org 返回 503] | [Nucleic Acids Research 2021](https://doi.org/10.1093/nar/gkab966) | Toni Gabaldón (Institució Catalana de Recerca i Estudis Avançats) | 小众 · 99 次 | 论文摘要：“Here, we describe the latest evolution of PhylomeDB (version 5).” |
| [OrthoMCL](https://orthomcl.org/) | 备选 | 经典图聚类直系同源分组；仍被引用，新项目多改用 OrthoFinder。 | [Genome Research 2003](https://doi.org/10.1101/gr.1224503) | David S. Roos (University of Pennsylvania) | 标准 · 6548 次 | 作者摘要原句：“OrthoMCL provides a scalable method for constructing orthologous groups across multiple eukaryotic taxa, using a Markov Cluster algorithm to group (putative) orthologs and paralogs.” |
| [Quest for Orthologs benchmark](https://orthology.benchmarkservice.org/) | 参考 | 直系同源推断方法的标准基准评测服务。 | [Nature Methods 2016](https://doi.org/10.1038/nmeth.3830) | Christophe Dessimoz (SIB Swiss Institute of Bioinformatics) | 成熟 · 259 次 | 作者摘要原句：“Achieving high accuracy in orthology inference is essential for many comparative, evolutionary and functional genomic analyses, yet the true evolutionary history of genes is generally unknown and orthologs are used for very different applications across …” |
| [OMA standalone](https://omabrowser.org/standalone/) | 备选 | 在自有基因组和转录组上运行 OMA 直系同源算法，可并入 OMA 公共基因组。 | [Genome Research 2019](https://doi.org/10.1101/gr.243212.118) | Christophe Dessimoz (SIB Swiss Institute of Bioinformatics) | 成熟 · 187 次 | 论文摘要：“Here, we describe the OMA pipeline available as a standalone program for Linux and Mac.” |
| [Count](https://www.iro.umontreal.ca/~csuros/gene_content/count.html) | 备选 | 在系统树上用简约法或似然法分析基因家族获得/丢失与大小演化。 | [Bioinformatics 2010](https://doi.org/10.1093/bioinformatics/btq315) | Miklós Csűös (Université de Montréal) | 标准 · 506 次 | 无摘要或仓库说明可引；见原文 |
| [BadiRate](https://github.com/fgvieira/badirate) | 备选 | 按分支估计基因家族出生、死亡与创新速率的似然方法。 | [Bioinformatics 2011](https://doi.org/10.1093/bioinformatics/btr623) | Julio Rozas (Institut de Recerca de la Biodiversitat de la Universitat de Barcelona) | 成熟 · 133 次 | 作者摘要原句：“We have assessed the accuracy of BadiRate by computer simulations, and have also illustrated its functionality by analyzing a representative empirical dataset.”；GitHub 最后提交 2020-08 |

> 评测要点： Quest for Orthologs 基准服务在 20 个基准上比较直系同源方法，各有不同的精度与召回取舍；按与自己用途最接近的基准选方法（doi:10.1038/nmeth.3830）。


# 第 9 章 定位与拓扑

*本章收录[主页第 8 节](../README.zh.md#section-8)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

信号肽、跨膜拓扑结构与亚细胞定位预测（F1+ 附加项）。

**需要：** 通常只需蛋白序列（用于 SignalP、TargetP 等工具）。结果应作为 F1+ 的附加列并入总表，不要另建第二张主表。[按场景列出的数据需求](../README.zh.md#data-needs)

**分组：**
- *信号肽与拓扑*（互补）：SignalP 6.0、DeepTMHMM 或 TMbed 或 TMHMM 2.0 或 Phobius。信号肽用 SignalP 6.0，再加一个跨膜拓扑工具：默认用 DeepTMHMM 或 TMbed，TMHMM 2.0 只用于复现旧表。Phobius 和 TMbed 也能判定信号肽。
- *细胞器定位*（可替代）：TargetP 2.0、LOCALIZER、DeepLoc 2.1、WoLF PSORT。质体与线粒体定位用 TargetP 2.0；多亚细胞区室判定用 DeepLoc 2.1。
- *植物分泌组*（按顺序）：SignalP 6.0、ApoplastP。在 SignalP 之后用 ApoplastP 区分质外体蛋白。


| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [SignalP 6.0](https://services.healthtech.dtu.dk/services/SignalP-6.0/) | 默认（信号肽） | 基于蛋白语言模型预测全部五类信号肽的工具。 | [Nature Biotechnology 2022](https://doi.org/10.1038/s41587-021-01156-3) | Henrik Nielsen (Technical University of Denmark) | 标准 · 3441 次 | 论文摘要：“We introduce SignalP 6.0, a machine learning model that detects all five SP types and is applicable to metagenomic data.” |
| [TMHMM 2.0](https://services.healthtech.dtu.dk/services/TMHMM-2.0/) | 备选 | 基于 HMM 预测跨膜螺旋的工具。 | [Journal of Molecular Biology 2001](https://doi.org/10.1006/jmbi.2000.4315) | Anders Krogh (Technical University of Denmark) | 标准 · 14533 次 | 无摘要或仓库说明可引；见原文 |
| [Phobius](https://phobius.sbc.su.se/) | 备选 | 联合预测跨膜拓扑结构与信号肽的工具。 | [Journal of Molecular Biology 2004](https://doi.org/10.1016/j.jmb.2004.03.016) | Erik L. L. Sonnhammer (Karolinska Institutet) | 标准 · 2783 次 | 无摘要或仓库说明可引；见原文 |
| [WoLF PSORT](https://wolfpsort.hgc.jp/) | 备选 | 内置植物模型的亚细胞定位预测工具。 | [Nucleic Acids Research 2007](https://doi.org/10.1093/nar/gkm259) | Kenta Nakai (Korea Center for Disease Control and Prevention) | 标准 · 4718 次 | 无摘要或仓库说明可引；见原文 |
| [LOCALIZER](https://localizer.csiro.au/) | 备选 | 预测植物蛋白与病原效应蛋白在叶绿体、线粒体及细胞核定位的工具。 | [Scientific Reports 2017](https://doi.org/10.1038/srep44598) | Jana Sperschneider (Commonwealth Scientific and Industrial Research Organisation) | 标准 · 521 次 | 作者摘要原句：“LOCALIZER shows greater prediction accuracy for chloroplast and mitochondrial targeting compared to other methods for 652 plant proteins.” |
| [DeepLoc 2.1](https://services.healthtech.dtu.dk/services/DeepLoc-2.1/) | 备选 | 基于蛋白语言模型预测亚细胞定位与膜蛋白类型的工具。 | [Nucleic Acids Research 2024](https://doi.org/10.1093/nar/gkae237) | Henrik Nielsen (Technical University of Denmark) | 成熟 · 290 次 | 作者摘要原句：“Notably, DeepLoc 2.1 outperforms existing models, with the larger ProtT5 model exhibiting a marginal advantage over the ESM-1B model.” |
| [TargetP 2.0](https://services.healthtech.dtu.dk/services/TargetP-2.0/) | 备选 | 预测 N 端靶向肽（信号肽、线粒体、叶绿体与类囊体转运肽）的工具。 | [Life Science Alliance 2019](https://doi.org/10.26508/lsa.201900429) | Arne Elofsson (Stockholm University) +1 | 标准 · 1263 次 | 论文摘要：“Here, we demonstrate this by presenting TargetP 2.0, a novel state-of-the-art method to identify N-terminal sorting signals, which direct proteins to the secretory pathway, mitochondria, and chloroplasts or other plastids.” |
| [DeepTMHMM](https://dtu.biolib.com/DeepTMHMM) | 默认拓扑（DeepTMHMM 或 TMbed） | 跨膜拓扑结构预测工具（预印本）。 | [bioRxiv (Cold Spring Harbor Laboratory) 2022](https://doi.org/10.1101/2022.04.08.487609) | Ole Winther (University of Copenhagen) | 标准 · 1984 次 | 作者摘要原句：“We introduce DeepTMHMM, a deep learning protein language model-based algorithm that can detect and predict the topology of both alpha helical and beta barrels proteins with unprecedented accuracy.” |
| [TMbed](https://github.com/BernhoferM/TMbed) | 默认拓扑（DeepTMHMM 或 TMbed） | 基于 ProtT5 嵌入预测跨膜螺旋、β-桶和信号肽；在全蛋白组规模下运行很快。 | [BMC Bioinformatics 2022](https://doi.org/10.1186/s12859-022-04873-x) | Michael Bernhofer (Technical University of Munich) | 成熟 · 122 次 | 作者摘要原句：“TMbed completes predictions for entire proteomes within hours on a single consumer-grade desktop machine at performance levels similar or better than methods, which are using evolutionary information from multiple sequence alignments (MSAs) of protein …”；GitHub 最后提交 2026-02 |
| [ApoplastP](https://apoplastp.csiro.au/) | 备选 | 预测植物蛋白或效应蛋白是否定位于质外体；构建分泌组时可与 SignalP 互补。 | [New Phytologist 2017](https://doi.org/10.1111/nph.14946) | Jana Sperschneider (Commonwealth Scientific and Industrial Research Organisation) | 成熟 · 225 次 | 作者摘要原句：“ApoplastP predicts apoplastic localization in effectors with a sensitivity of 75% and a false positive rate of 5%, improving the accuracy of cysteine-rich classifiers by > 13%.” |
| [SUBA3](https://suba.live/) | 备选 | 整合实验与预测的拟南芥亚细胞定位数据库；用于核对植物定位预测。 | [Nucleic Acids Research 2012](https://doi.org/10.1093/nar/gks1151) | A. Harvey Millar (The University of Western Australia) | 成熟 · 318 次 | 无摘要或仓库说明可引；见原文 |


# 第 10 章 植物基因家族

*本章收录[主页第 9 节](../README.zh.md#section-9)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

植物特定基因家族分类工具（框架 F8 NLR、框架 F9 TF/激酶）。

**需要：** NLR（F8）需输入 InterProScan 结果，并可附上可选的 HRP 窗口列表；TF / 激酶（F9）需使用 iTAK（或有书面说明的同等级工具）。若课题不涉及抗病或 NLR 分析，可直接跳过 F8。[按场景列出的数据需求](../README.zh.md#data-needs)

**分组：**
- *转录因子与激酶*（互补）：iTAK、TAPscan v4、PlantTFDB / PlantRegMap、PlantPAN (latest)、JASPAR 2026。家族分类用 iTAK 或 TAPscan；结合基序分析用 PlantTFDB、PlantPAN 和 JASPAR。
- *蛋白组上的 NLR 识别*（可替代）：NLRtracker + RefPlantNLR、Resistify、NLRexpress、RGAugury。F8：NLRtracker 基于 InterProScan 的输出；Resistify 直接读蛋白序列；两者对比使用。抗病基因的参考数据库是 PRGdb 4.0。
- *基因组上的 NLR 位点*（可替代）：NLR-Annotator、NLRSeek。二选一；两者都与蛋白侧的识别互补，因为很多 NLR 在基因注释中被漏掉。NLR-Annotator 单独使用时不依赖基因模型、直接在基因组上找 NLR 位点（结构层）；NLRSeek 已包含 NLR-Annotator，并加上定点重注释和 NLRtracker。
- *酶与转运蛋白分类*（互补）：dbCAN3、CAZy、MEROPS、TCDB (2021)。dbCAN3 用于分配 CAZy 家族；蛋白酶用 MEROPS；转运蛋白用 TCDB。


| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [iTAK](https://github.com/kentnf/iTAK) | 备选 | 植物转录因子与蛋白激酶识别及分类工具。 | [Molecular Plant 2016](https://doi.org/10.1016/j.molp.2016.09.014) | Zhangjun Fei (Robert W. Holley Center for Agriculture & Health) | 标准 · 1466 次 | GitHub 最后提交 2026-04 |
| [TAPscan v4](https://tapscan.plantcode.cup.uni-freiburg.de/) | 备选 | 基于家族规则检测转录相关蛋白的工具，配套链型植物（streptophyte）范围的数据库。 | [The Plant Journal 2024](https://doi.org/10.1111/tpj.17184) | Stefan Andreas Rensing (University of Freiburg) | 较新 · 20 次 | 论文摘要：“Here, we present TAPscan v4, including an updated web interface (https://tapscan.plantcode.cup.uni-freiburg.de/), which enables an in-depth representation of the distribution of 138 TAP families across 678 species from diverse groups of organisms, with a …” |
| [PRGdb 4.0](http://prgdb.org/) | 备选 | 附带 DRAGO 注释流程的植物抗病基因数据库。 | [Nucleic Acids Research 2021](https://doi.org/10.1093/nar/gkab1087) | Walter Sanseverino +1 | 小众 · 97 次 | 作者摘要原句：“DRAGO3, the tool for automatic annotation and prediction of plant resistance genes behind PRGdb, has been improved in both accuracy and sensitivity, leading to more reliable predictions.” |
| [RGAugury](https://bitbucket.org/yaanlpc/rgaugury) | 备选 | 识别抗病基因类似物（NBS、RLK、RLP）的分析流程。 | [BMC Genomics 2016](https://doi.org/10.1186/s12864-016-3197-x) | Frank M. You (Agriculture and Agri-Food Canada) | 成熟 · 280 次 | 无摘要或仓库说明可引；见原文 |
| [Resistify](https://github.com/SwiftSeal/resistify) | 备选 | 利用 NLRexpress 基序从蛋白序列中快速识别并分类 NLR 的工具。 | [Bioinformatics and Biology Insights 2025](https://doi.org/10.1177/11779322241308944) | Moray Smith (James Hutton Institute) | 较新 · 26 次 | 作者摘要原句：“Accurately identifying NLRs from these genomes is a prerequisite for improving our understanding of NLRs and identifying novel sources of disease resistance.”；GitHub 最后提交 2026-07 |
| [NLRtracker + RefPlantNLR](https://github.com/slt666666/NLRtracker) | 备选 | 利用 RefPlantNLR 特征从蛋白组或转录本中提取并分类 NLR 的工具与参考集。 | [PLoS Biology 2021](https://doi.org/10.1371/journal.pbio.3001124) | Sophien Kamoun (University of East Anglia) | 成熟 · 223 次 | 论文摘要：“Here, we describe a comprehensive reference dataset of experimentally validated plant nucleotide-binding leucine-rich repeat (NLR) immune receptors.”；GitHub 最后提交 2024-03 |
| [NLR-Annotator](https://github.com/steuernb/NLR-Annotator) | 备选 | 不依赖已有基因注释、直接在基因组序列上定位 NLR 位点的工具。 | [PLANT PHYSIOLOGY 2020](https://doi.org/10.1104/pp.19.01273) | Brande B. H. Wulff (John Innes Centre) | 成熟 · 273 次 | 论文摘要：“Here, we developed NLR-Annotator, a software tool for in silico NLR identification independent of transcript support.”；GitHub 最后提交 2023-07 |
| [NLRexpress](https://github.com/eliza-m/NLRexpress) | 备选 | 基于机器学习预测 CC/TIR/NB-ARC/LRR 基序的工具。 | [Frontiers in Plant Science 2022](https://doi.org/10.3389/fpls.2022.975888) | Andrei‐José Petrescu (Institute of Biochemistry) | 小众 · 26 次 | GitHub 最后提交 2022-08 |
| [NLRSeek](https://github.com/Wang-Mengda/NLRSeek) | 备选 | 结合 NLR-Annotator 位点、靶向重注释与 NLRtracker 以找回蛋白组中遗漏 NLR 的流程。 | [aBIOTECH 2025](https://doi.org/10.1016/j.abiote.2025.100001) | Jinding Liu (Nanjing Agricultural University) +1 | 较新 · 0 次 | 论文摘要：“To address this problem, we developed NLRSeek ( https://github.com/Wang-Mengda/NLRSeek ), a genome reannotation–based pipeline for NLR identification.”；GitHub 最后提交 2026-02 |
| [PlantTFDB / PlantRegMap](http://planttfdb.gao-lab.org) | 资源 | 植物转录因子家族、结合基序与调控网络数据库。 | [Nucleic Acids Research 2019](https://doi.org/10.1093/nar/gkz1020) | Jinpu Jin (Peking University) +1 | 标准 · 1310 次 | 无摘要或仓库说明可引；见原文 |
| [PlantPAN (latest)](https://plantpan.itps.ncku.edu.tw) | 资源 | 植物启动子与转录因子结合位点分析平台。 | [Nucleic Acids Research 2023](https://doi.org/10.1093/nar/gkad945) | Wen-Chi Chang (Academia Sinica) | 成熟 · 183 次 | 作者摘要原句：“These improvements included easy-to-read experimental condition clusters, searchable gene-centered interfaces for the identification of promoter regions' binding preferences by considering experimental condition clusters and peak visualization for all …” |
| [dbCAN3](https://github.com/linnabrown/run_dbcan) | 备选 | 碳水化合物活性酶（CAZyme）及其底物注释工具。 | [Nucleic Acids Research 2023](https://doi.org/10.1093/nar/gkad328) | Yanbin Yin (University of Nebraska–Lincoln) | 标准 · 1282 次 | 作者摘要原句：“We have updated the meta server to dbCAN3 with the following new functions and components: (i) dbCAN-sub as a profile Hidden Markov Model database (HMMdb) for substrate prediction at the CAZyme subfamily level; (ii) searching against experimentally …”；GitHub 最后提交 2025-04 |
| [CAZy](http://www.cazy.org/) | 资源 | 碳水化合物活性酶家族的参考分类体系，也是 dbCAN3 注释所依据的分类标准。 | [Nucleic Acids Research 2021](https://doi.org/10.1093/nar/gkab1045) | Nicolas Terrapon (Centre National de la Recherche Scientifique) | 标准 · 2795 次 | 论文摘要：“Here we briefly summarize the increase in novel families and the annotations conducted during the last 8 years.” |
| [MEROPS](https://www.ebi.ac.uk/merops/) | 资源 | 肽酶与蛋白酶抑制剂家族数据库，附带经审校的底物信息；用于整理蛋白酶基因家族表。 | [Nucleic Acids Research 2017](https://doi.org/10.1093/nar/gkx1134) | Neil David Rawlings (European Bioinformatics Institute) | 标准 · 1961 次 | 作者摘要原句：“Cross-references have been established between MEROPS and the PANTHER database at both the family and protein-species level, which will help to improve curation and coverage between the resources.” |
| [TCDB (2021)](https://www.tcdb.org/) | 资源 | 转运蛋白分类数据库；为膜转运蛋白（如浆果中的糖和离子转运蛋白）分配 TC 家族。 | [Nucleic Acids Research 2020](https://doi.org/10.1093/nar/gkaa1004) | Milton H. Saier (University of California San Diego) +1 | 标准 · 511 次 | 无摘要或仓库说明可引；见原文 |
| [JASPAR 2026](https://jaspar.elixir.no/) | 资源 | 开放的经审校转录因子结合谱数据库（含植物转录因子）；可用于查看 PlantTFDB/PlantPAN 预测结果背后的基序。 | [Nucleic Acids Research 2025](https://doi.org/10.1093/nar/gkaf1209) | Boris Lenhard (Hammersmith Hospital) +5 | 成熟 · 216 次 | 无摘要或仓库说明可引；见原文 |
| [NLR-Parser](https://github.com/steuernb/NLR-Parser) | 备选 | 基于 MEME 基序的植物 NLR 基因筛查；NLR-Annotator 或 NLRtracker 之前的快速初筛。 | [Bioinformatics 2015](https://doi.org/10.1093/bioinformatics/btv005) | Burkhard Steuernagel (John Innes Centre) +1 | 成熟 · 130 次 | GitHub 最后提交 2018-12 |
| [CUPP](https://cupp.info/) | 备选 | 基于保守肽段模式的 CAZyme 家族与功能注释；dbCAN HMM 的替代。 | [Biotechnology for Biofuels 2019](https://doi.org/10.1186/s13068-019-1436-5) | Kristian Barrett (Technical University of Denmark) | 小众 · 78 次 | 作者摘要原句：“The CUPP runtime, F-score, sensitivity, and precisions of family and subfamily annotations match or represent an improvement compared to state-of-the-art tools.” |
| [TransportDB 2.0](http://www.membranetransport.org/transportDB2/index.html) | 备选 | 已测序基因组的转运蛋白注释，附 TransAAP 注释流程。 | [Nucleic Acids Research 2016](https://doi.org/10.1093/nar/gkw1068) | Liam D. H. Elbourne (Macquarie University) | 成熟 · 358 次 | 作者摘要原句：“This pipeline is now fully automated enabling it to better keep pace with the accelerating rate of genome sequencing.” |
| ARAMEMNON | 备选 | 拟南芥膜蛋白数据库，提供共识拓扑与定位预测。 | [PLANT PHYSIOLOGY 2003](https://doi.org/10.1104/pp.011577) | Reinhard Kunze (University of Cologne) | 标准 · 751 次 | 无摘要或仓库说明可引；见原文 |


# 第 11 章 非编码 RNA 功能资源

*本章收录[主页第 10 节](../README.zh.md#section-10)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

非编码 RNA 功能注释资源。通常需要转录组或已知的 ncRNA 位点，不能单靠蛋白表。

**需要：** 转录组数据或已知的 ncRNA 位点——不能只靠蛋白表。基因结构预测与 TE 库构建仍分别归属结构注释库和 vitis-te。[按场景列出的数据需求](../README.zh.md#data-needs)

**分组：**
- *miRNA 参考*（互补）：miRBase、PmiREN 2.0、sRNAanno。对照 miRBase 和 PmiREN 为 miRNA 命名；phasiRNA 位点注释用 sRNAanno。
- *靶标*（按顺序）：psRNATarget (2017 release) 或 psRobot、TarDB。先用 psRNATarget 或 psRobot 预测，再到 TarDB 查降解组支持。
- *lncRNA 与 circRNA 目录*（互补）：PLncDB V2.0、GreeNC 2.0、CANTATAdb 3.0、PlantCircRNA、ncPlantDB。仅用于查询，本身不直接赋予功能注释。


| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [miRBase](https://www.mirbase.org/) | 资源 | microRNA 参考序列与命名数据库。 | [Nucleic Acids Research 2018](https://doi.org/10.1093/nar/gky1141) | Sam Griffiths‐Jones (University of Manchester) | 标准 · 5364 次 | 作者摘要原句：“We describe improvements to the database and website to provide more information about the quality of microRNA gene annotations, and the cellular functions of their products.” |
| [psRobot](http://omicslab.genetics.ac.cn/psRobot/) | 备选 | 植物小 RNA 荟萃分析与靶基因预测工具。 | [Nucleic Acids Research 2012](https://doi.org/10.1093/nar/gks554) | Meng Wang (Chinese Academy of Sciences) +1 | 标准 · 660 次 | 无摘要或仓库说明可引；见原文 |
| [ncPlantDB](https://bis.zju.edu.cn/ncPlantDB) | 资源 | 涵盖 43 个物种的植物 ncRNA 数据库，包含潜在 ncRNA 编码小肽与细胞类型互作信息。 | [Nucleic Acids Research 2024](https://doi.org/10.1093/nar/gkae1017) | Ming Chen (Zhejiang University) | 较新 · 16 次 | 论文摘要：“To address this gap, we present ncPlantDB (https://bis.zju.edu.cn/ncPlantDB), a comprehensive database integrating ncRNA and ncPEP data across 43 plant species. ncPlantDB encompasses 353 140 ncRNAs, 3799 ncPEPs and 4 647 071 interactions, sourced from …” |
| [PLncDB V2.0](https://www.tobaccodb.org/plncdb/) | 资源 | 植物 lncRNA 百科数据库。 | [Nucleic Acids Research 2020](https://doi.org/10.1093/nar/gkaa910) | Peijian Cao (China Tobacco) | 成熟 · 188 次 | 无摘要或仓库说明可引；见原文 |
| [GreeNC 2.0](http://greenc.sequentiabiotech.com) | 资源 | 植物 lncRNA 目录数据库。 | [Nucleic Acids Research 2021](https://doi.org/10.1093/nar/gkab1014) | Riccardo Aiese Cigliano | 小众 · 82 次 | 论文摘要：“Here we present our most recent update where 16 species have been updated, while 78 species have been added, resulting in the annotation of more than 495 000 lncRNAs.” |
| [CANTATAdb 3.0](http://cantata.amu.edu.pl) | 资源 | 更新版植物 lncRNA 数据库。 | [Plant and Cell Physiology 2024](https://doi.org/10.1093/pcp/pcae081) | Michał Wojciech Szcześniak (Adam Mickiewicz University in Poznań) | 较新 · 20 次 | 无摘要或仓库说明可引；见原文 |
| [PlantCircRNA](https://plant.deepbiology.cn/PlantCircRNA/) | 资源 | 植物环状 RNA（circRNA）数据库。 | [Nucleic Acids Research 2024](https://doi.org/10.1093/nar/gkae709) | Xiaoyong Sun (Shandong Agricultural University) | 较新 · 15 次 | 论文摘要：“We developed PlantCircRNA (https://plant.deepbiology.cn/PlantCircRNA/) to fill this gap.” |
| [psRNATarget (2017 release)](https://www.zhaolab.org/psRNATarget/) | 备选 | 植物小 RNA 靶基因预测在线服务。 | [Nucleic Acids Research 2018](https://doi.org/10.1093/nar/gky316) | Patrick Xuechun Zhao (Noble Research Institute) | 标准 · 1644 次 | 作者摘要原句：“This update enhances its analytical performance by developing a new scoring schema that is capable of discovering miRNA-mRNA interactions at higher 'recall rates' without significantly increasing total prediction output.” |
| [PmiREN 2.0](https://pmiren.com) | 资源 | 植物 miRNA 百科数据库。 | [Nucleic Acids Research 2021](https://doi.org/10.1093/nar/gkab811) | Lei Li (Peking University) +1 | 成熟 · 129 次 | 论文摘要：“Here we report the update of PmiREN2.0 (https://pmiren.com/) with an addition of 19 363 miRNA entries from 91 plants, doubling the amount of data in the original version.” |
| [sRNAanno](http://www.plantsrnas.org/) | 资源 | 跨多个植物物种（含葡萄）统一注释的小 RNA 位点资源库（涵盖 miRNA、phasiRNA 和 hc-siRNA）。 | [Horticulture Research 2021](https://doi.org/10.1038/s41438-021-00480-8) | Rui Xia (South China Agricultural University) | 成熟 · 159 次 | 无摘要或仓库说明可引；见原文 |
| [TarDB](http://www.biosequencing.cn/TarDB/) | 资源 | 具降解组数据支持的植物 miRNA 靶标及 miRNA 触发的 phasiRNA 数据库；可用于核验 psRNATarget 的预测结果。 | [BMC Genomics 2021](https://doi.org/10.1186/s12864-021-07680-5) | Xuan Ma (Tianjin Normal University) | 小众 · 69 次 | 论文摘要：“Here, we report TarDB, an online database that collects three categories of relatively high-confidence plant miRNA targets: (i) cross-species conserved miRNA targets; (ii) degradome/PARE (Parallel Analysis of RNA Ends) sequencing supported miRNA targets; …” |


# 第 12 章 表达支持的功能

*本章收录[主页第 11 节](../README.zh.md#section-11)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

利用基因表达或共表达数据佐证功能假说，但不作为实验级 GO 证据。

**需要：** 若要用表达数据佐证基因功能，需准备 RNA-seq 数据（最好来自同一基因型）。[按场景列出的数据需求](../README.zh.md#data-needs)

**分组：**
- *表达图谱*（互补）：Grapevine Expression Atlas、Expression Atlas (2024)、scPlantDB。查询葡萄基因的时空表达模式。
- *网络构建*（可替代）：WGCNA、hdWGCNA、GENIE3。bulk 转录组用 WGCNA，单细胞数据用 hdWGCNA，推断转录因子-靶基因调控关系用 GENIE3。
- *共表达门户*（互补）：ATTED-II v11、CoNekT。无需自行建网即可快速完成“关联推断功能”核查。


| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| Grapevine Expression Atlas | 资源 | 欧亚葡萄（V. vinifera Corvina）多器官与发育时期表达图谱。 | [The Plant Cell 2012](https://doi.org/10.1105/tpc.112.100230) | Mario Pezzotti (University of Verona) | 成熟 · 461 次 | 论文摘要：“We developed a genome-wide transcriptomic atlas of grapevine (Vitis vinifera) based on 54 samples representing green and woody tissues and organs at different developmental stages as well as specialized tissues such as pollen and senescent leaves.” |
| [ATTED-II v11](https://atted.jp/) | 资源 | 植物基因共表达数据库。 | [Plant and Cell Physiology 2022](https://doi.org/10.1093/pcp/pcac041) | Takeshi Obayashi (Tohoku University) | 成熟 · 141 次 | 作者摘要原句：“We believe that with these improvements, ATTED-II is more valuable and powerful for supporting interspecies comparative studies and integrated analyses using heterogeneous data.” |
| [scPlantDB](https://biobigdata.nju.edu.cn/scplantdb/) | 资源 | 植物单细胞图谱数据库：收录细胞类型与标记基因。 | [Nucleic Acids Research 2023](https://doi.org/10.1093/nar/gkad706) | Dijun Chen (State Key Laboratory of Pharmaceutical Biotechnology) | 较新 · 99 次 | 论文摘要：“In this study, we present a systematic approach to construct a plant single-cell database, scPlantDB, which is publicly available at https://biobigdata.nju.edu.cn/scplantdb.” |
| [hdWGCNA](https://github.com/smorabit/hdWGCNA) | 备选 | 面向单细胞与空间转录组数据的共表达网络分析工具。 | [Cell Reports Methods 2023](https://doi.org/10.1016/j.crmeth.2023.100498) | Vivek Swarup (University of California, Irvine) | 标准 · 1047 次 | 作者摘要原句：“We showcase hdWGCNA using data from autism spectrum disorder and Alzheimer's disease brain samples, identifying disease-relevant co-expression network modules. hdWGCNA is directly compatible with Seurat, a widely used R package for single-cell and spatial …”；GitHub 最后提交 2026-06 |
| [CoNekT](https://conekt.sbs.ntu.edu.sg) | 备选 | 面向植物的共表达网络分析工具包与平台。 | [Nucleic Acids Research 2018](https://doi.org/10.1101/255075) | Sebastian Proost (Max Planck Institute of Molecular Plant Physiology) +1 | 成熟 · 128 次 | 论文摘要：“Here, we present CoNekT (Co-expression Network Toolkit), an open source web server, that contains user-friendly tools and interactive visualizations for comparative analyses of gene expression data and co-expression networks.” |
| [WGCNA](https://cran.r-project.org/package=WGCNA) | 备选 | 基于 bulk RNA-seq 构建加权基因共表达模块；与单细胞工具 hdWGCNA 对应，用于通过共表达关联推断基因功能。 | [BMC Bioinformatics 2008](https://doi.org/10.1186/1471-2105-9-559) | Steve Horvath (University of California, Los Angeles) | 标准 · 31417 次 | 无摘要或仓库说明可引；见原文 |
| [GENIE3](https://github.com/aertslab/GENIE3) | 备选 | 利用树集成算法从表达矩阵推断转录因子与靶基因的调控关系；可搭配 iTAK/PlantTFDB 的转录因子列表使用。 | [PLoS ONE 2010](https://doi.org/10.1371/journal.pone.0012776) | Vân Anh Huynh‐Thu (University of Liège) | 标准 · 2449 次 | 作者摘要原句：“It doesn't make any assumption about the nature of gene regulation, can deal with combinatorial and non-linear interactions, produces directed GRNs, and is fast and scalable.”；GitHub 最后提交 2022-04 |
| [Expression Atlas (2024)](https://www.ebi.ac.uk/gxa/) | 资源 | EMBL-EBI 旗下的基线与差异表达数据库，涵盖 bulk 和单细胞数据集（含植物实验）。 | [Nucleic Acids Research 2023](https://doi.org/10.1093/nar/gkad1021) | Irene Papatheodorou (European Bioinformatics Institute) | 较新 · 60 次 | 无摘要或仓库说明可引；见原文 |
| [GRNBoost2 / Arboreto](https://github.com/aertslab/arboreto) | 备选 | 可扩展的 GENIE3 式基因调控网络推断。 | [Bioinformatics 2018](https://doi.org/10.1093/bioinformatics/bty916) | Stein Aerts (VIB-KU Leuven Center for Brain & Disease Research) | 标准 · 745 次 | 作者摘要原句：“Arboreto includes both GRNBoost2 and an improved implementation of GENIE3, as a user-friendly open source Python package.”；GitHub 最后提交 2024-04 |


# 第 13 章 社区目录与命名

*本章收录[主页第 12 节](../README.zh.md#section-12)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

经整理的社区目录与命名参考源。

**需要：** 能够访问指定的社区目录（并记录其版本号或访问日期）。[按场景列出的数据需求](../README.zh.md#data-needs)

**分组：**
- *葡萄命名*（按顺序）：The grapevine gene nomenclature system、Grapedia Grapevine Reference Gene Catalogue、PN40024 reference annotation (PN_T2T / v5)。先将基因 ID 映射至当前 PN_T2T 版本，再按命名规范从 Grapedia 目录提取基因符号。


| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| The grapevine gene nomenclature system | 思路 | 葡萄基因命名规则建议。 | [BMC Genomics 2014](https://doi.org/10.1186/1471-2164-15-1077) | Jérôme Grimplet (Consejo Superior de Investigaciones Científicas) | 成熟 · 124 次 | 作者摘要原句：“To better exploit the results obtained by the international community, we think that a coordinated nomenclature for gene naming in species with sequenced genomes is essential.” |
| [Grapedia Grapevine Reference Gene Catalogue](https://grapedia.org/genes/) | 资源 | 经人工审校的欧亚葡萄（V. vinifera）基因 ID 与符号对照目录，附带功能描述、文献及置信度；v3.1 版（2025 年 11 月）已对齐至 T2T v5.1 注释。最早以 Grape Gene Reference Catalogue 为名发表（doi:10.3389/fpls.2021.803977）。 | 无文章 | — | 无论文 | 无摘要或仓库说明可引；见原文 |
| [ProtNLM (UniProt names)](https://www.uniprot.org/help/ProtNLM) | 思路 | UniProt 采用 Google 蛋白命名模型为未审定条目提供推荐名称，并附带自动注释证据标签。 | 无文章 | — | 无论文 | 无摘要或仓库说明可引；见原文 |
| [PN40024 reference annotation (PN_T2T / v5)](https://grapedia.org/) | 资源 | PN_T2T（v5）参考基因 ID，并含早期 v4（doi:10.1093/g3journal/jkad067）及 12X.v2 上的 VCost.v3（doi:10.1016/j.gdata.2017.09.002）；发布前须将基因名称与 ID 映射至当前版本。 | [Horticulture Research 2023](https://doi.org/10.1093/hr/uhad061) | Camille Rustenholz (Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement) +3 | 成熟 · 294 次 | 作者摘要原句：“Even though PN40024 derives from nine generations of selfing, we still found nine genomic hotspots of heterozygous sites associated with biological processes, such as the oxidation-reduction process and protein phosphorylation.” |


# 第 14 章 蛋白三维结构

*本章收录[主页第 13 节](../README.zh.md#section-13)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

蛋白三维结构预测、搜索与结构域划分。此处的 structure 指蛋白三维空间结构，而非基因模型。

**需要：** 蛋白序列；部分工具还需搭配 AlphaFold / PDB 类结构库。此处的 “structure” 指蛋白三维结构，不是基因模型。[按场景列出的数据需求](../README.zh.md#data-needs)

![Foldseek workflow](../docs/figures/guide/published/foldseek_2024_fig1.png)

*图：Foldseek：查询和目标结构先转成 3Di 序列，以同一对角线上的两个 k-mer 命中预筛，再做无空位和有空位比对（a）；每个残基的 3Di 状态由该残基及其空间最近邻残基的特征学习得到（b）。原图未修改，引自 van Kempen M、Kim SS、Tumescheit C、Mirdita M、Lee J、Gilchrist CLM、Söding J、Steinegger M（2024），Fast and accurate protein structure search with Foldseek，Nature Biotechnology 42:243-246，Fig. 1，doi:10.1038/s41587-023-01773-0，PMC10869269，许可 CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)。*

**分组：**
- *整组蛋白单体预测*（可替代）：ColabFold、ESMFold / ESM-2、AlphaFold2。整个蛋白组用 ColabFold（带快速多序列比对的 AlphaFold2）或 ESMFold；AlphaFold2 本身的代码和权重都是开放的。
- *复合物预测*（可替代）：AlphaFold 3、RoseTTAFold All-Atom、Boltz-1。只用于蛋白与蛋白、核酸或配体的复合物；AlphaFold 3 的权重仅限非商业用途，需申请获取。
- *结构检索后确认*（按顺序）：Foldseek 或 TM-Vec 2s 或 AlphaFind v2 或 DALI、TM-align 或 US-align。先检索（默认用 Foldseek 搜 AFDB），再用 TM-align 逐对确认命中；复合物用 US-align。
- *结构检索目标库*（互补）：AlphaFold Protein Structure Database (2024)、AFDB clusters (Foldseek)。它们是检索的目标库，不是工具：先用 AFDB clusters 快速初筛，再用完整的 AFDB 看细节。
- *基于结构的结构域*（互补）：TED (The Encyclopedia of Domains)、CATH (2021)、Merizo。Merizo 用于切分自建结构模型；TED 和 CATH 提供参考结构域定义。
- *嵌入*（互补）：ProtTrans (ProtT5)、ESM3、ProstT5。为第 1、5、8 节中的语言模型工具提供特征输入。
- *位点与口袋*（互补）：PARSE、WASP。从三维结构推断功能位点；仅用于后续深入分析。


| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [AlphaFold2](https://github.com/google-deepmind/alphafold) | 备选 | 蛋白三维结构预测工具。 | [Nature 2021](https://doi.org/10.1038/s41586-021-03819-2) | John Jumper (Google DeepMind (United Kingdom)) +1 | 标准 · 51454 次 | GitHub 最后提交 2026-04 |
| [ColabFold](https://github.com/sokrypton/ColabFold) | 备选 | 采用 MMseqs2 生成多序列比对的快速 AlphaFold2 流程。 | [Nature Methods 2022](https://doi.org/10.1038/s41592-022-01488-1) | Milot Mirdita (Max Planck Institute for Multidisciplinary Sciences) +2 | 标准 · 9964 次 | 作者摘要原句：“ColabFold's 40-60-fold faster search and optimized model utilization enables prediction of close to 1,000 structures per day on a server with one graphics processing unit.”；GitHub 最后提交 2026-11 |
| [ESMFold / ESM-2](https://github.com/facebookresearch/esm) | 备选 | 基于蛋白语言模型的单序列三维结构预测工具。 | [Science 2023](https://doi.org/10.1126/science.ade2574) | Alexander W. Rives (New York University) | 标准 · 7612 次 | GitHub 已归档（最后提交 2024-02） |
| [AlphaFold 3](https://github.com/google-deepmind/alphafold3) | 备选 | 联合预测蛋白与核酸、配体及离子复合物三维结构的工具。 模型权重只按申请提供，且仅限非商业用途；批量预测单体时，开放的 AlphaFold2（另列一条）仍是可用选择。 | [Nature 2024](https://doi.org/10.1038/s41586-024-07487-w) | Max Jaderberg +2 | 标准 · 19677 次 | 作者摘要原句：“The new AlphaFold model demonstrates substantially improved accuracy over many previous specialized tools: far greater accuracy for protein–ligand interactions compared with state-of-the-art docking tools, much higher accuracy for protein–nucleic acid …”；GitHub 最后提交 2026-11 |
| [TED (The Encyclopedia of Domains)](https://ted.cathdb.info/) | 资源 | 对 AlphaFold DB 做基于三维结构的结构域切分数据库（TED）。 | [Science 2024](https://doi.org/10.1126/science.adq4946) | Christine Anne Orengo (Institute of Structural and Molecular Biology) +1 | 成熟 · 181 次 | 无摘要或仓库说明可引；见原文 |
| [CATH (2021)](https://www.cathdb.info/) | 资源 | 蛋白三维结构域层级分类数据库。 | [Nucleic Acids Research 2020](https://doi.org/10.1093/nar/gkaa1079) | Ian Sillitoe (Institute of Structural and Molecular Biology) | 标准 · 578 次 | 作者摘要原句：“Finally, we have improved links to and from CATH including SCOP, InterPro, Aquaria and 2DProt.” |
| [TM-align](https://zhanggroup.org/TM-align/) | 备选 | 基于 TM-score 的蛋白三维结构比对工具。 | [Nucleic Acids Research 2005](https://doi.org/10.1093/nar/gki524) | Yang Zhang (University at Buffalo, State University of New York) | 标准 · 4278 次 | 作者摘要原句：“On average, the resulting structure alignments have higher accuracy and coverage than those provided by these most often-used methods.” |
| [US-align](https://github.com/pylelab/USalign) | 备选 | 通用于蛋白与核酸的三维结构比对工具。 | [Nature Methods 2022](https://doi.org/10.1038/s41592-022-01585-1) | Yang Zhang (University of Michigan) | 标准 · 595 次 | 作者摘要原句：“Detailed analyses showed that the main advantage of US-align lies in the extensive optimization of the unified objective function powered by efficient heuristic search iterations, which substantially improve the accuracy and speed of the structural alignment …”；GitHub 最后提交 2026-10 |
| [DALI](http://ekhidna2.biocenter.helsinki.fi/dali/) | 备选 | 比对 PDB 或 AlphaFold DB 的三维结构比较在线服务。 | [Protein Science 2019](https://doi.org/10.1002/pro.3749) | Liisa Holm (University of Helsinki) | 标准 · 737 次 | 作者摘要原句：“Meta-analysis of independent reference-based evaluations of alignment accuracy and fold discrimination shows DALI at top rank in six out of 12 studies.” |
| [Foldseek](https://github.com/steineggerlab/foldseek) | 默认（结构搜索） | 基于 3Di 字母表的蛋白三维结构搜索工具，可检出序列搜索遗漏的远缘同源蛋白。 | [Nature Biotechnology 2023](https://doi.org/10.1038/s41587-023-01773-0) | Johannes Söding (Max Planck Institute for Multidisciplinary Sciences) +1 | 标准 · 3169 次 | 作者摘要原句：“Foldseek decreases computation times by four to five orders of magnitude with 86%, 88% and 133% of the sensitivities of Dali, TM-align and CE, respectively.”；GitHub 最后提交 2026-11 |
| [ProstT5](https://github.com/mheinzinger/ProstT5) | 备选 | 将氨基酸序列直接翻译为 3Di 符号的蛋白语言模型，使 Foldseek 无需预先预测三维结构即可运行。 | [NAR Genomics and Bioinformatics 2024](https://doi.org/10.1093/nargab/lqae150) | Michael Heinzinger (Technical University of Munich) | 成熟 · 454 次 | 作者摘要原句：“As a proof-of-concept for our novel approach, dubbed Protein ‘structure-sequence’ T5 (ProstT5), we showed improved performance for subsequent, structure-related prediction tasks, leading to three orders of magnitude speedup for deriving 3Di.”；GitHub 最后提交 2026-03 |
| TM-Vec 2s | 备选 | 基于嵌入向量做远缘同源检测与 TM-score 预测的工具（2026 预印本）。 | [bioRxiv (Cold Spring Harbor Laboratory) 2026](https://doi.org/10.64898/2026.02.05.704073) | Qiyun Zhu (Arizona State University) | 较新 · 2 次 | 作者摘要原句：“Benchmarks on the CATH and SCOPe domains for large-scale database queries showed that TM-Vec 2s is 185× faster than the original TM-Vec, while achieving higher TM-score prediction accuracy.” |
| [AlphaFold Protein Structure Database (2024)](https://alphafold.ebi.ac.uk) | 资源 | 覆盖 UniProt 的预测蛋白三维结构数据库；常作为 Foldseek 的搜索目标库。 | [Nucleic Acids Research 2023](https://doi.org/10.1093/nar/gkad1011) | Demis Hassabis (Google DeepMind (United Kingdom)) +1 | 标准 · 2431 次 | 作者摘要原句：“We also discuss the improvements and services added since its initial release, including enhancements to the Predicted Aligned Error viewer, customisation options for the 3D viewer, and improvements in the search engine of AlphaFold DB.” |
| [AlphaFind v2](https://alphafind.fi.muni.cz) | 备选 | 在 AlphaFold DB 与 TED 结构域上做三维结构相似性搜索的工具。 | [Nucleic Acids Research 2026](https://doi.org/10.1093/nar/gkag372) | Matej Antol (Masaryk University) | 较新 · 2 次 | 论文摘要：“In this paper, we present AlphaFind v2, an application for finding structurally similar proteins in the AlphaFold Database (https://alphafold.ebi.ac.uk/) of predicted structures.” |
| [WASP](https://github.com/gioodm/wasp-proteins-annotation) | 备选 | 通过 Foldseek 比对 AlphaFold DB 完成全蛋白组注释（涵盖 GO、Pfam、PANTHER、CATH、Rhea、EC）的工具。 | 无文章 | — | 无论文 | 仓库简介：“Python command-line software for whole-proteomes annotation based on structural homology.”；GitHub 最后提交 2026-10 |
| PARSE | 备选 | 利用局部三维结构嵌入向量注释蛋白功能位点的工具。 | [Proceedings of the National Academy of Sciences 2025](https://doi.org/10.1073/pnas.2513219122) | Russ Biagio Altman (Stanford Medicine) | 较新 · 27 次 | 作者摘要原句：“For the task of predicting the catalytic function of enzymes, PARSE achieves comparable or superior global performance to state-of-the-art machine learning methods (F1 score [Formula: see text] 85%) while simultaneously annotating the specific residues …” |
| [Merizo](https://github.com/psipred/Merizo) | 备选 | 对预测的蛋白三维结构做结构域切分的工具。 | [Nature Communications 2023](https://doi.org/10.1038/s41467-023-43934-4) | David T. Jones (University College London) | 较新 · 63 次 | 论文摘要：“Here, we describe a deep learning method for domain segmentation called Merizo, which learns to cluster residues into domains in a bottom-up manner.”；GitHub 最后提交 2025-05 |
| [RoseTTAFold All-Atom](https://github.com/baker-laboratory/RoseTTAFold-All-Atom) | 备选 | 联合预测蛋白与配体、核酸及修饰的三维结构；是复合物建模的开源替代方案。 | [Science 2024](https://doi.org/10.1126/science.adl2528) | Rohith Krishna (University of Washington) +6 | 标准 · 1298 次 | 论文摘要：“We describe RoseTTAFold All-Atom (RFAA), which combines a residue-based representation of amino acids and DNA bases with an atomic representation of all other groups to model assemblies that contain proteins, nucleic acids, small molecules, metals, and …”；GitHub 最后提交 2026-05 |
| [Boltz-1](https://github.com/jwohlwend/boltz) | 备选 | 开源生物分子复合物结构预测工具（MIT 许可），准确度接近 AlphaFold 3，且不受 AF3 权重条款限制。 [preprint] | [bioRxiv (Cold Spring Harbor Laboratory) 2024](https://doi.org/10.1101/2024.11.19.624167) | Jeremy Wohlwend (MIT Computer Science and Artificial Intelligence Laboratory) | 标准 · 795 次 | 作者摘要原句：“In this paper, we introduce Boltz-1, an open-source deep learning model incorporating innovations in model architecture, speed optimization, and data processing achieving Alphafold3-level accuracy in predicting the 3D structures of biomolecular complexes.”；GitHub 最后提交 2026-05 |
| [ESM3](https://github.com/evolutionaryscale/esm) | 备选 | 融合序列、结构与功能的多模态蛋白语言模型；提供开源轻量模型用于特征嵌入提取与蛋白设计。 | [Science 2025](https://doi.org/10.1126/science.ads0018) | Alexander W. Rives | 标准 · 1442 次 | 作者摘要原句：“ESM3 can follow complex prompts combining its modalities and is highly responsive to alignment to improve its fidelity.”；GitHub 最后提交 2026-11 |
| [ProtTrans (ProtT5)](https://github.com/agemagician/ProtTrans) | 备选 | 预训练蛋白语言模型；其生成的 ProtT5 嵌入是本目录中 goPredSim、TMbed、ProstT5 等多款工具的输入特征。 | [IEEE Transactions on Pattern Analysis and Machine Intelligence 2021](https://doi.org/10.1109/TPAMI.2021.3095381) | Burkhard Rost (Technical University of Munich) | 标准 · 3008 次 | 作者摘要原句：“We validated the advantage of using the embeddings as exclusive input for several subsequent tasks: (1) a per-residue (per-token) prediction of protein secondary structure (3-state accuracy Q3=81%-87%); (2) per-protein (pooling) predictions of protein …”；GitHub 最后提交 2025-05 |
| [AFDB clusters (Foldseek)](https://cluster.foldseek.com/) | 资源 | 基于三维结构的 AlphaFold 数据库聚类资源；可揭示哪些缺乏注释的"暗"蛋白家族与已知家族共享折叠构象。 | [Nature 2023](https://doi.org/10.1038/s41586-023-06510-w) | Pedro Beltrão (SIB Swiss Institute of Bioinformatics) +1 | 成熟 · 421 次 | 论文摘要：“Here, we developed a structural-alignment-based clustering algorithm—Foldseek cluster—that can cluster hundreds of millions of structures.” |
| [SWISS-MODEL](https://swissmodel.expasy.org/) | 备选 | 基于模板的同源建模服务。 | [Nucleic Acids Research 2018](https://doi.org/10.1093/nar/gky427) | Torsten F. Schwede (SIB Swiss Institute of Bioinformatics) | 标准 · 14323 次 | 论文摘要：“Here, we present an update to the SWISS-MODEL server, which pioneered the field of automated modelling 25 years ago and been continuously further developed.” |


# 第 15 章 下游富集

*本章收录[主页第 14 节](../README.zh.md#section-14)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

下游 GO/KEGG 富集分析。直接读取已生成的注释总表，本身不产出新的功能标签。

**需要：** 已完成的功能注释表，外加界定清晰的背景基因集（通常取当次发布的全部基因）。这属于合并总表之后的下游分析，并非功能标签的来源。[按场景列出的数据需求](../README.zh.md#data-needs)

**分组：**
- *过表示分析*（可替代）：topGO、GOATOOLS、clusterProfiler 4.0、GOseq、g:Profiler (2023)、ShinyGO、DAVID (2025 update)、agriGO v2.0。以葡萄背景集运行 topGO 或 clusterProfiler；存在基因长度检出偏倚时选用 GOseq。
- *排序列表*（可替代）：GSEA、clusterProfiler 4.0。信号是一个排序而不是基因名单时：用 GSEA，或 clusterProfiler 的 GSEA 模式。
- *条目精简*（可替代）：Revigo、simplifyEnrichment。报告前先去掉冗余条目；GOSemSim 计算这类聚类所依据的语义相似度，做自定义比较时直接用它。


| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [topGO](https://bioconductor.org/packages/topGO/) | 备选 | 兼顾 GO 图拓扑结构的 GO 富集分析工具。 | [NCI BioConductor 2017](https://doi.org/10.18129/B9.bioc.topGO) | Adrian Alexa, Jorg Rahnenfuhrer | 成熟 · 445 次 | 无摘要或仓库说明可引；见原文 |
| [GOATOOLS](https://github.com/tanghaibao/goatools) | 备选 | Python GO 分析库：支持有向无环图（DAG）向上传播、GO slim 提取与富集分析。 | [Scientific Reports 2018](https://doi.org/10.1038/s41598-018-28948-z) | Haibao Tang (Fujian Agriculture and Forestry University) | 标准 · 1572 次 | GitHub 最后提交 2026-11 |
| [GOseq](https://bioconductor.org/packages/goseq/) | 备选 | 校正 RNA-seq 基因长度偏好性的 GO 富集分析工具。 | [Genome biology 2010](https://doi.org/10.1186/gb-2010-11-2-r14) | Alicia Oshlack (Walter and Eliza Hall Institute of Medical Research) | 标准 · 8066 次 | 论文摘要：“We present GOseq, an application for performing Gene Ontology (GO) analysis on RNA-seq data.” |
| [ShinyGO](http://bioinformatics.sdstate.edu/go/) | 备选 | 收录 Ensembl/STRING 植物物种的在线富集分析工具。 | [Bioinformatics 2019](https://doi.org/10.1093/bioinformatics/btz931) | Xijin Ge (South Dakota State University) | 标准 · 6004 次 | 论文摘要：“To complement existing tools, we developed ShinyGO based on a large annotation database derived from Ensembl and STRING-db for 59 plant, 256 animal, 115 archeal and 1678 bacterial species.” |
| [DAVID (2025 update)](https://davidbioinformatics.nih.gov) | 备选 | 在线富集分析服务；2025 更新版新增用于跨物种分析的 DAVID Ortholog。 | [Nucleic Acids Research 2026](https://doi.org/10.1093/nar/gkag470) | Weizhong Chang (Frederick National Laboratory for Cancer Research) | 较新 · 39 次 | 作者摘要原句：“Since its initial release in 2003, DAVID developments have been published in 12 papers and cited >80 000 times.” |
| [g:Profiler (2023)](https://biit.cs.ut.ee/gprofiler) | 备选 | 功能富集分析与基因 ID 转换工具。 | [Nucleic Acids Research 2023](https://doi.org/10.1093/nar/gkad347) | Hedi Peterson (University of Tartu) | 标准 · 1981 次 | 论文摘要：“In this update article, we introduce a novel filtering method highlighting Gene Ontology driver terms, accompanied by new graph visualizations providing a broader context for significant Gene Ontology terms.” |
| [agriGO v2.0](http://systemsbiology.cau.edu.cn/agriGOv2/) | 备选 | 面向农业物种的 GO 富集分析平台。 | [Nucleic Acids Research 2017](https://doi.org/10.1093/nar/gkx382) | Tian Tian (State Key Laboratory of Plant Physiology and Biochemistry) +4 | 标准 · 2700 次 | 论文摘要：“Here, we present our updated agriGO that has a largely expanded number of supporting species (394) and datatypes (865).” |
| [clusterProfiler 4.0](https://github.com/YuLab-SMU/clusterProfiler) | 备选 | R 语言富集分析包，支持直接读取 `merged_function_table.tsv` 构建自定义 TERM2GENE。 | [The Innovation 2021](https://doi.org/10.1016/j.xinn.2021.100141) | Xiaochen Bo (Beijing Radiation Center) +1 | 标准 · 17017 次 | 论文摘要：“To meet these requirements, we present here an updated version of our popular Bioconductor package, clusterProfiler 4.0.”；GitHub 最后提交 2026-11 |
| [Revigo](http://revigo.irb.hr/) | 备选 | 按语义相似度将冗长的富集 GO 条目列表归并为精简的分组。 | [PLoS ONE 2011](https://doi.org/10.1371/journal.pone.0021800) | Fran Supek (Universitat Pompeu Fabra) | 标准 · 7068 次 | 作者摘要原句：“Furthermore, REVIGO visualizes this non-redundant GO term set in multiple ways to assist in interpretation: multidimensional scaling and graph-based visualizations accurately render the subdivisions and the semantic relationships in the data, while treemaps …” |
| [simplifyEnrichment](https://github.com/jokergoo/simplifyEnrichment) | 备选 | 按语义相似度对富集 GO 条目进行聚类，并为每个聚类生成词云摘要。 | [Genomics Proteomics & Bioinformatics 2022](https://doi.org/10.1016/j.gpb.2022.04.008) | Zuguang Gu (National Center for Tumor Diseases) +1 | 成熟 · 348 次 | GitHub 最后提交 2026-01 |
| [GOSemSim](https://github.com/YuLab-SMU/GOSemSim) | 备选 | 计算 GO 条目间及基因间的语义相似度；是冗余条目精简步骤的底层工具。 | [Bioinformatics 2010](https://doi.org/10.1093/bioinformatics/btq064) | Xiaochen Bo (Anhui Medical University) +1 | 标准 · 1599 次 | GitHub 最后提交 2026-11 |
| GSEA | 备选 | 对不设阈值的排序基因列表开展基因集富集分析；适用于差异表达呈连续梯度而非一份基因列表的场景。 | [Proceedings of the National Academy of Sciences 2005](https://doi.org/10.1073/pnas.0506580102) | Jill P. Mesirov (Broad Institute) | 标准 · 59736 次 | 论文摘要：“Here, we describe a powerful analytical method called Gene Set Enrichment Analysis (GSEA) for interpreting gene expression data.” |
| [KOBAS-i](https://github.com/xmao/kobas) | 备选 | 网页和命令行的 GO/KEGG 富集，带探索性图；支持多物种。 | [Nucleic Acids Research 2021](https://doi.org/10.1093/nar/gkab447) | Yi Chen Zhao (Chinese Academy of Sciences) +1 | 标准 · 2208 次 | 论文摘要：“Here we presented version 3.0 of KOBAS, which is named KOBAS-i (short for KOBAS intelligent version).”；GitHub 最后提交 2026-05 |
| [WebGestalt 2024](https://www.webgestalt.org/) | 备选 | 网页基因集分析（ORA、GSEA、网络）并出图。 | [Nucleic Acids Research 2024](https://doi.org/10.1093/nar/gkae456) | Bing Zhang (Baylor College of Medicine) | 成熟 · 499 次 | 作者摘要原句：“Notably, the adoption of a Rust backend reduced gene set enrichment analysis time by 95% from 270.64 to 12.41 s and network topology-based analysis by 89% from 159.59 to 17.31 s in our evaluation.” |
| [ClueGO](https://apps.cytoscape.org/apps/cluego) | 备选 | Cytoscape 插件，把富集的 GO 术语和通路分组成网络。 | [Bioinformatics 2009](https://doi.org/10.1093/bioinformatics/btp101) | Jérôme Galon (Inserm) | 标准 · 6926 次 | 作者摘要原句：“We have developed ClueGO, an easy to use Cytoscape plug-in that strongly improves biological interpretation of large lists of genes.” |


# 第 16 章 想法、格式与合并规则

*本章收录[主页第 15 节](../README.zh.md#section-15)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

相关思路、文件格式与总表合并规则。最终合并产物仍为 `merged_function_table.tsv`。在完成实测前，不改变框架 F1。

**需要：** 视具体思路而定；合并产物仍为 `merged_function_table.tsv`。在完成实测前，不改变框架 F1。[按场景列出的数据需求](../README.zh.md#data-needs)

![Three F1 evidence lines merged into one row](../docs/figures/guide/function_evidence_merge_v2.png)

*图：一条蛋白的三条 F1 证据如何合成 `merged_function_table.tsv` 中的一行：每个 GO 词条都保留给出它的来源，机器预测一律标 IEA。数值取自 `testdata/function_aggregate/expected/merged_function_table.tsv` 中的模拟测试行 FAKE_g0001，不是真实基因；示意图，为本仓库绘制。*

**分组：**
- *格式与证据*（互补）：Evidence & Conclusion Ontology (ECO, 2022)、GO Annotation File (GAF 2.2) format、GO-CAM。每条 GO 注释均须附带 ECO 证据代码；发布用 GAF 格式，经审校的通路用 GO-CAM。
- *错误与特异性*（互补）：GO specificity balance (Genome Res 2026)、CAFA lessons (idea)、Misannotation in enzyme superfamilies。阐明转移标签出错的原因，以及如何把握 GO 条目的特异性层级。
- *大语言模型代理*（可替代）：GeneAgent、LLM-assisted Reactome annotation、Agentic AI for gene function across genomes。目前仅处方案阶段；使用时必须保留人工审核。


| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [Evidence & Conclusion Ontology (ECO, 2022)](https://evidenceontology.org/) | 思路 | 描述注释背后证据类型的标准本体（可映射至 GO 证据代码）。 | [Nucleic Acids Research 2021](https://doi.org/10.1093/nar/gkab1025) | Michelle Gwinn Giglio (University of Maryland, Baltimore) | 小众 · 62 次 | 论文摘要：“Here we report on recent updates to the ECO ontology itself as well as associated resources that are available through this project.” |
| [GO Annotation File (GAF 2.2) format](https://geneontology.org/docs/go-annotation-file-gaf-format-2.2/) | 思路 | 记录基因与 GO 关联及证据代码的标准制表符分隔格式（GAF 2.2）。 | 无文章 | — | 无论文 | 无摘要或仓库说明可引；见原文 |
| GO specificity balance (Genome Res 2026) | 思路 | 探讨如何在序列语言模型预测中平衡 GO 条目特异度的论文（Genome Res 2026）。 | [Genome Research 2026](https://doi.org/10.1101/gr.280816.125) | Bin Liu (Beijing Institute of Technology) | 较新 · 1 次 | 作者摘要原句：“Our model consistently outperforms state-of-the-art methods by 5%-15% across all specificity levels and on both a benchmark data set and an independent test set, demonstrating robust generalization.” |
| [CAFA lessons (idea)](https://biofunctionprediction.org/cafa/) | 思路 | 社区评测（CAFA）持续表明，对背景知识有限的蛋白做 GO 预测依然困难；机器学习给出的 GO 仅可作为电子注释证据（IEA）发布。 | 无文章 | — | 无论文 | 无摘要或仓库说明可引；见原文 |
| GeneAgent | 思路 | 结合领域数据库做基因集分析并支持自我核验的大语言模型智能体（LLM agent）。 | [Nature Methods 2025](https://doi.org/10.1038/s41592-025-02748-6) | Zhiyong Lu (National Institutes of Health) | 成熟 · 160 次 | 作者摘要原句：“Here we present GeneAgent, an LLM-based AI agent for gene-set analysis that reduces hallucinations by autonomously interacting with biological databases to verify its own output.” |
| LLM-assisted Reactome annotation | 思路 | 利用 LLM/RAG 生成代谢通路注释草稿供审定员复核的方法（预印本）。 | [bioRxiv (Cold Spring Harbor Laboratory) 2025](https://doi.org/10.64898/2025.12.20.695723) | Guanming Wu (Oregon Health & Science University) | 较新 · 4 次 | 论文摘要：“We developed an LLM workflow that can assist curators in adding new genes to existing pathways and refining the functional annotations of existing ones.” |
| Agentic AI for gene function across genomes | 思路 | GO 审定团队采用受控模式（schema）与校验器构建的跨基因组基因功能智能体工作流（Zenodo 记录）。 | [Zenodo (CERN European Organization for Nuclear Research) 2026](https://doi.org/10.5281/zenodo.18904049) | Chris Mungall (Lawrence Berkeley National Laboratory) | 较新 · 0 次 | 无摘要或仓库说明可引；见原文 |
| Misannotation in enzyme superfamilies | 思路 | 量化了酶超家族中转移分子功能标签的错误率；论证了保留证据代码并优先采用人工审校资源的必要性。 | [PLoS Computational Biology 2009](https://doi.org/10.1371/journal.pcbi.1000605) | Patricia Clement Babbitt (QB3) | 标准 · 842 次 | 无摘要或仓库说明可引；见原文 |
| [GO-CAM](https://geneontology.org/docs/gocam-overview/) | 思路 | 将 GO 注释连接为结构化的因果活性模型；对于经人工整理的葡萄通路，是超越扁平 GAF 表格的目标格式。 | [Nature Genetics 2019](https://doi.org/10.1038/s41588-019-0500-1) | Paul D. Thomas (University of Southern California) | 成熟 · 148 次 | 无摘要或仓库说明可引；见原文 |


# 第 17 章 可视化工具

*本章收录[主页“可视化工具”一节](../README.zh.md#visualization)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

用于查看基因模型和作图的工具。标为“通用工具”的不专属于注释。已在前面类型小节出现的条目在这里再次列出并注明所在小节，不重复计数。

<a id="viz-1"></a>
## 结构域与基序图

| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [IBS 2.0](https://ibs.renlab.org/) | 备选，通用工具 | 绘制蛋白结构域和基序示意图。 | [Nucleic Acids Research 2022](https://doi.org/10.1093/nar/gkac373) | Jian Min Ren (Sun Yat-sen University) | 成熟 · 279 次 | 论文摘要：“Here, we present a professional tool called IBS 2.0 for illustrating the organization of both protein and nucleotide sequences.” |
| [drawProteins](https://bioconductor.org/packages/drawProteins/) | 备选 | R/Bioconductor 包，按 UniProt 特征画结构域架构图。 | [F1000Research 2018](https://doi.org/10.12688/f1000research.14541.1) | Paul Brennan (Cardiff University) | 小众 · 66 次 | 无摘要或仓库说明可引；见原文 |

<a id="viz-2"></a>
## GO 与富集图

| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [enrichplot](https://github.com/YuLab-SMU/enrichplot) | 备选 | clusterProfiler 结果的点图、柱图、cnet 和 emap 图（无单独论文）。 | 无文章 | — | 无论文 | 仓库简介：“Visualization of Functional Enrichment Result”；GitHub 最后提交 2026-11 |
| [GOplot](https://github.com/wencke/wencke.github.io) | 备选 | R 包，把富集结果与表达量结合作图（弦图、圈图）。 | [Bioinformatics 2015](https://doi.org/10.1093/bioinformatics/btv300) | Fátima Sánchez‐Cabo (Spanish National Centre for Cardiovascular Research) +1 | 标准 · 2053 次 | 论文摘要：“Here we present an R package called GOplot, based on ggplot2, for enhanced graphical representation.”；GitHub 最后提交 2016-12 |
| [Revigo](http://revigo.irb.hr/) | 备选 | 按语义相似度将冗长的富集 GO 条目列表归并为精简的分组。（见第 14 节） | [PLoS ONE 2011](https://doi.org/10.1371/journal.pone.0021800) | Fran Supek (Universitat Pompeu Fabra) | 标准 · 7068 次 | 作者摘要原句：“Furthermore, REVIGO visualizes this non-redundant GO term set in multiple ways to assist in interpretation: multidimensional scaling and graph-based visualizations accurately render the subdivisions and the semantic relationships in the data, while treemaps …” |
| [simplifyEnrichment](https://github.com/jokergoo/simplifyEnrichment) | 备选 | 按语义相似度对富集 GO 条目进行聚类，并为每个聚类生成词云摘要。（见第 14 节） | [Genomics Proteomics & Bioinformatics 2022](https://doi.org/10.1016/j.gpb.2022.04.008) | Zuguang Gu (National Center for Tumor Diseases) +1 | 成熟 · 348 次 | GitHub 最后提交 2026-01 |
| [clusterProfiler 4.0](https://github.com/YuLab-SMU/clusterProfiler) | 备选 | R 语言富集分析包，支持直接读取 `merged_function_table.tsv` 构建自定义 TERM2GENE。（见第 14 节） | [The Innovation 2021](https://doi.org/10.1016/j.xinn.2021.100141) | Xiaochen Bo (Beijing Radiation Center) +1 | 标准 · 17017 次 | 论文摘要：“To meet these requirements, we present here an updated version of our popular Bioconductor package, clusterProfiler 4.0.”；GitHub 最后提交 2026-11 |
| [ClueGO](https://apps.cytoscape.org/apps/cluego) | 备选 | Cytoscape 插件，把富集的 GO 术语和通路分组成网络。（见第 14 节） | [Bioinformatics 2009](https://doi.org/10.1093/bioinformatics/btp101) | Jérôme Galon (Inserm) | 标准 · 6926 次 | 作者摘要原句：“We have developed ClueGO, an easy to use Cytoscape plug-in that strongly improves biological interpretation of large lists of genes.” |

<a id="viz-3"></a>
## 通路图

| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [Pathview](https://bioconductor.org/packages/pathview/) | 备选 | 把基因或化合物数据画到 KEGG 通路图上。 | [Bioinformatics 2013](https://doi.org/10.1093/bioinformatics/btt285) | Weijun Luo (University of North Carolina at Charlotte) | 标准 · 2671 次 | 无摘要或仓库说明可引；见原文 |
| [iPath3.0](https://pathways.embl.de/) | 备选 | 代谢总览交互图，可为 KO/EC 集合着色。 | [Nucleic Acids Research 2018](https://doi.org/10.1093/nar/gky299) | Peer Bork (Max Delbrück Center) +1 | 成熟 · 343 次 | 无摘要或仓库说明可引；见原文 |
| [MapMan (viewer)](https://mapman.gabipd.org/) | 备选 | 把植物组学数据画到 MapMan 通路图上；与 Mercator4 分箱配合。 | [The Plant Journal 2004](https://doi.org/10.1111/j.1365-313X.2004.02016.x) | Mark Stitt (Max Planck Society) | 标准 · 3804 次 | 无摘要或仓库说明可引；见原文 |
| [KEGG Mapper](https://www.kegg.jp/kegg/mapper/) | 备选 | 将 KO 列表映射至 KEGG 代谢通路、BRITE 层级与功能模块的工具。（见第 6 节） | [Protein Science 2019](https://doi.org/10.1002/pro.3711) | Minoru I. Kanehisa (Kyoto University Institute for Chemical Research) | 标准 · 1339 次 | 论文摘要：“Here we report a new version of KEGG Mapper, a suite of KEGG mapping tools available at the KEGG website (https://www.kegg.jp/ or https://www.genome.jp/kegg/), together with the KOALA family tools for automatic assignment of KO (KEGG Orthology) identifiers …” |

<a id="viz-4"></a>
## 网络图

| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [Cytoscape](https://cytoscape.org/) | 备选，通用工具 | 网络可视化平台，用于共表达、蛋白互作和富集网络。 | [Genome Research 2003](https://doi.org/10.1101/gr.1239303) | Trey Ideker (University of California San Diego) | 标准 · 57947 次 | 无摘要或仓库说明可引；见原文 |
| [ClueGO](https://apps.cytoscape.org/apps/cluego) | 备选 | Cytoscape 插件，把富集的 GO 术语和通路分组成网络。（见第 14 节） | [Bioinformatics 2009](https://doi.org/10.1093/bioinformatics/btp101) | Jérôme Galon (Inserm) | 标准 · 6926 次 | 作者摘要原句：“We have developed ClueGO, an easy to use Cytoscape plug-in that strongly improves biological interpretation of large lists of genes.” |

<a id="viz-5"></a>
## 三维结构查看器

| 工具 | 角色 | 用途 / 何时用 | 原始论文 | 实验室（通讯作者，机构） | 权威度（档位 · 被引） | 评价（出处） |
|---|---|---|---|---|---|---|
| [UCSF ChimeraX](https://www.cgl.ucsf.edu/chimerax/) | 备选，通用工具 | 桌面三维结构查看器，可显示预测模型（pLDDT 着色、叠合）。 | [Protein Science 2020](https://doi.org/10.1002/pro.3943) | Thomas E. Ferrin (University of California, San Francisco) | 标准 · 10274 次 | 作者摘要原句：“ChimeraX brings (a) significant performance and graphics enhancements; (b) new implementations of Chimera's most highly used tools, many with further improvements; (c) several entirely new analysis features; (d) support for new areas such as virtual reality, …” |
| [Mol* Viewer](https://molstar.org/) | 备选，通用工具 | 网页三维结构查看器，RCSB PDB 和 AlphaFold DB 使用它。 | [Nucleic Acids Research 2021](https://doi.org/10.1093/nar/gkab314) | Alexander Rose (San Diego Supercomputer Center) | 标准 · 1333 次 | 无摘要或仓库说明可引；见原文 |


# 第 18 章 怎么选框架和加件

仓库要求每个发布版声明一个完整的注释框架，加件单独列出（主页“默认路线”；[`docs/SCENARIOS_FUNCTIONAL.md`](../docs/SCENARIOS_FUNCTIONAL.md)）。下表复述这一选择，并补上首选工具背后的证据。

| 情况 | 框架或加件 | 工具 | 理由（出处） | 主要检查 |
|---|---|---|---|---|
| 默认的论文发布 | F1 | DIAMOND 比 Swiss-Prot、eggNOG-mapper、InterProScan | 三条独立证据：校对库相似性（[doi:10.1038/s41592-021-01101-x](https://doi.org/10.1038/s41592-021-01101-x)）、直系同源转移（[doi:10.1093/molbev/msab293](https://doi.org/10.1093/molbev/msab293)）、特征签名（[doi:10.1093/bioinformatics/btu031](https://doi.org/10.1093/bioinformatics/btu031)） | 合并表行数接近蛋白数（`examples/plant_sim/01_vitis_s1_s7/plan.md`） |
| 快速初筛 | F2 | eggNOG-mapper，可选 KofamScan | eggNOG 6.0 覆盖 12,535 个参考物种（[doi:10.1093/nar/gkac1022](https://doi.org/10.1093/nar/gkac1022)）；Kofam 使用自适应阈值（[doi:10.1093/bioinformatics/btz859](https://doi.org/10.1093/bioinformatics/btz859)） | 不要把 F2 当作已跑过 InterProScan 来发布（主页“所需数据”） |
| 从头组装转录组的肽段 | F3 EnTAP 或 F5 Trinotate | EnTAP、Trinotate | EnTAP 为非模式真核生物的从头转录组设计（[doi:10.1111/1755-0998.13106](https://doi.org/10.1111/1755-0998.13106)） | 在 METHODS 中写明所用框架 |
| 多个基因组的面板 | F7 | OrthoFinder，再对代表序列跑 F1 | 标准化直系同源评测（[doi:10.1038/nmeth.3830](https://doi.org/10.1038/nmeth.3830)）；OrthoFinder 3 准确度提升（[doi:10.1101/2025.07.15.664860](https://doi.org/10.1101/2025.07.15.664860)） | 标签对应直系同源组代表序列，不是每个基因 |
| 需要可读名称 | F4 加件 | AHRD | 名称是展示层（主页“所需数据”） | 名称本身不提高等级 |
| 计划画 MapMan 图 | F6 加件 | Mercator4 | 植物蛋白分类框架（[doi:10.1016/j.molp.2019.01.003](https://doi.org/10.1016/j.molp.2019.01.003)） | 只有计划画 MapMan 图时才跑（`docs/MERCATOR_WHEN.md`） |
| 有抗病或 NLR 研究主线 | F8 加件 | InterProScan 过滤、NLR-Annotator、NLRtracker | NLR 表达低、家族内序列相似度高，难以注释，NLR-Annotator 为此而建（[doi:10.1104/pp.19.01273](https://doi.org/10.1104/pp.19.01273)）；NLRtracker 附带经实验验证的植物 NLR 参考集（[doi:10.1371/journal.pbio.3001124](https://doi.org/10.1371/journal.pbio.3001124)） | InterProScan 初筛不等于人工校对的 NLR 集 |
| 转录因子或激酶 | F9 加件 | iTAK | 植物转录因子和激酶分类（[doi:10.1016/j.molp.2016.09.014](https://doi.org/10.1016/j.molp.2016.09.014)） | 只在需要该家族时使用 |

![Which frame to use](../docs/figures/guide/function_frame_decision_v2.png)

*图：按数据与时间选择框架，再只加论文需要的加件（与第 18 章表格及 `docs/ROADMAP.md` 一致）。示意图，为本仓库绘制；可编辑 SVG：[`function_frame_decision_v2.svg`](../docs/figures/guide/function_frame_decision_v2.svg)。*

## 权威度怎么看

各表的权威度（标准：被引 500 及以上；成熟：100 至 499；新近：不足 100 且 2023 年及以后发表；小众：不足 100 且更早）衡量论文被引的广度，不代表在你的蛋白组上更准。数据库和通用工具（UniProt、InterPro、KEGG、Cytoscape）会从所有领域获得引用。准确度更应看社区评测：CAFA3 发现最好的方法明显优于基线，但仍有很大改进空间（[doi:10.1186/s13059-019-1835-8](https://doi.org/10.1186/s13059-019-1835-8)）。

![Publication year against citations](../docs/figures/guide/function_catalog_year_citations_v2.png)

*图：184 条有论文的目录条目的发表年份与 OpenAlex 被引数；菱形为本仓库默认工具。数据库和通用工具会从各个领域获得引用；被引数不代表在你的蛋白组上的准确度。数据：`catalog/SOFTWARE_AUTHORITY.tsv`；脚本 `docs/figures/guide/src/make_catalog_charts.py`。*

## 加新工具前要问的问题

1. 它是否带来新的证据类型（相似性、签名、直系同源、结构、语言模型），还是重复 F1 已有的？
2. 有没有独立评测（CAFA、Quest for Orthologs），还是只有作者自评？
3. 它的输出带什么证据代码？机器预测一律保持 IEA（主页“通用注意事项”）。
4. 数据库版本能否记录，许可是否允许再分发？主页中 KEGG 的再分发仍标为待确认。


# 第 19 章 常见问题与质控

## 19.1 仓库已列出的问题

来自主页“蛋白之外还需要的数据”一节和 `docs/EVALUATION.md`。

- 这里不找基因、不做 soft-mask、不建 TE 库、不改 GFF；这些属于 gene-structure-annotation 或 vitis-te。
- METHODS 中四套编号要分清：框架（F1、F2、F3、F5）、脚本文件（`F2_eggnog.sh` 是 F1 框架里的一步）、工具卡（F1a、F1b、F1c）和门槛（Gate-F1 至 F7）。
- 合并产物是 `merged_function_table.tsv`；机器预测的 GO 和 EC 保持 IEA。
- F7 框架注释的是直系同源组代表序列，不是每个基因。
- Foldseek、DeepFRI、AlphaFold DB 里的 structure 指蛋白三维结构。
- InterProScan 属于默认 F1 但很慢；F-L1 是验收标准，不是截止时间。
- 可选植物加件（F4、F6、F8、F9）本身不提高等级。
- 富集分析要有明确背景，通常是完整的发布基因集。

## 19.2 文献中的问题

- **过度预测。** 从弱匹配转移具体分子功能是酶超家族中最常见的错误；人工校对的 Swiss-Prot 错误接近 0%，而 NR、TrEMBL 和 KEGG 平均为 5% 至 63%（[doi:10.1371/journal.pcbi.1000605](https://doi.org/10.1371/journal.pcbi.1000605)）。优先用校对过的匹配，并保留证据代码。
- **细胞组分难。** CAFA3 中细胞组分预测没有进步（[doi:10.1186/s13059-019-1835-8](https://doi.org/10.1186/s13059-019-1835-8)）；定位结论应使用专门的定位工具（SignalP、TargetP、DeepLoc）。
- **具体条目少。** GO 条目的特异性不平衡，宽泛条目远比具体条目容易预测（[doi:10.1101/gr.280816.125](https://doi.org/10.1101/gr.280816.125)）。
- **上游注释影响结果。** 不同注释来源的直系同源结果明显不同（[doi:10.1093/bioinformatics/btaf365](https://doi.org/10.1093/bioinformatics/btaf365)）；要记录结构发布标签。
- **RNA-seq 富集偏差。** 长基因和高表达基因更容易被判为差异表达，需要校正（[doi:10.1186/gb-2010-11-2-r14](https://doi.org/10.1186/gb-2010-11-2-r14)）。
- **GO 列表冗余。** 应归纳，而不是列出几百个重叠条目（[doi:10.1371/journal.pone.0021800](https://doi.org/10.1371/journal.pone.0021800)）。

## 19.3 质控清单

| 检查 | 工具 | 出问题的表现 | 出处 |
|---|---|---|---|
| 输入蛋白组完整度（F0） | BUSCO 蛋白模式 | 完整度低：退回结构注释 | [doi:10.1093/molbev/msab199](https://doi.org/10.1093/molbev/msab199) |
| 输入一致性（可选） | OMArk | 大量不一致或污染蛋白 | [doi:10.1038/s41587-024-02147-w](https://doi.org/10.1038/s41587-024-02147-w) |
| 合并完整性 | `pipeline/F_merge_tables.py` | 行数与蛋白数差距大；丢弃未记录 | `examples/plant_sim/01_vitis_s1_s7/plan.md` |
| 版本 | METHODS | 数据库与比对器版本缺失或不匹配 | 主页“所需数据” |
| 证据代码 | 合并表 | 预测 GO 未标 IEA | [doi:10.1093/nar/gkab1025](https://doi.org/10.1093/nar/gkab1025)；主页 |
| 富集背景 | clusterProfiler 或 GOseq | 用子集作背景未说明；未处理长度偏差 | [doi:10.1186/gb-2010-11-2-r14](https://doi.org/10.1186/gb-2010-11-2-r14) |

验收等级和门槛见 [`docs/EVALUATION.md`](../docs/EVALUATION.md) 和 [`docs/EVALUATION_CHECKLIST.md`](../docs/EVALUATION_CHECKLIST.md)。


# 第 20 章 实例：葡萄蛋白走 F1 框架加 F8 加件

本章按 [`examples/plant_sim/01_vitis_s1_s7/plan.md`](../examples/plant_sim/01_vitis_s1_s7/plan.md) 的教学计划走一遍。蛋白来自模拟的葡萄结构发布版（Vitis_sim.v0.1，自报结构等级 L1）；重点是决策顺序，不是真实数字。

## 20.1 框架选择

流程工具选 F1 框架（DIAMOND、eggNOG-mapper 和 InterProScan），加上 F8 处理 NLR 候选，目标等级 F-L1。加件是可选的，不是 F-L1 的门槛。

## 20.2 各阶段

| 序号 | 阶段 | 工具 | 产出 | 为什么 |
|---|---|---|---|---|
| 1 | F0 蛋白检查 | BUSCO 蛋白模式 | 带谱系的 BUSCO 汇总 | 结果很差就退回结构注释（[doi:10.1093/molbev/msab199](https://doi.org/10.1093/molbev/msab199)） |
| 2 | F1a 相似性 | DIAMOND 比 Swiss-Prot | `function/diamond/` | 校对库匹配给出的名称错误率最低（[doi:10.1371/journal.pcbi.1000605](https://doi.org/10.1371/journal.pcbi.1000605)） |
| 3 | F1b 直系同源 | eggNOG-mapper，EGGNOG_TAX_SCOPE 设为所属类群 | `function/emapper/` | 通过直系同源转移 GO、KEGG 和 COG（[doi:10.1093/molbev/msab293](https://doi.org/10.1093/molbev/msab293)） |
| 4 | F1c 特征签名 | InterProScan | `function/interpro/` | 结构域、位点和成员数据库签名（[doi:10.1093/nar/gkae1082](https://doi.org/10.1093/nar/gkae1082)） |
| 5 | 合并 | `pipeline/F_merge_tables.py` | `merged_function_table.tsv` | 每个基因一行；行数接近蛋白数 |
| 6 | F8 NLR 初筛 | InterProScan 过滤，可选 HRP | `nlr_candidates.tsv` | 抗病基因窗口的候选；用 `pipeline/F8b_nlr_to_families.py` 转换后可回馈结构叠加层 S7 |
| 7 | 发布 | `pipeline/F_release.sh` | `function/release/<TAG>/` | 门槛 F-L0 和 F-L1 见 `docs/EVALUATION.md` |

## 20.3 要点

- F1 的三个工具给出三种独立证据，这就是 F1 作为默认的原因。
- 脚本名和框架名不同：`F2_eggnog.sh` 是 F1 框架的第 2 步，不是快速框架 F2。
- F8 的产出是候选列表，不是人工校对的 NLR 集；可以回到结构注释做校对。
- 另外两个例子见 `examples/plant_sim/02_oryza_s1/` 和 `examples/plant_sim/03_solanum_s11/`。


# 附录 A 术语表

| 术语 | 含义 | 出处 |
|---|---|---|
| BUSCO (protein mode) | 用某谱系的保守单拷贝直系同源基因检查蛋白组完整度。 | [doi:10.1093/molbev/msab199](https://doi.org/10.1093/molbev/msab199) |
| ECO | 证据与结论本体：描述注释背后证据类型的术语。 | [doi:10.1093/nar/gkab1025](https://doi.org/10.1093/nar/gkab1025) |
| Enrichment | 检验一个基因列表是否比背景更常带某个标签。 | [doi:10.1186/gb-2010-11-2-r14](https://doi.org/10.1186/gb-2010-11-2-r14) |
| GO | 基因本体：描述基因功能的资源，定期更新。 | [doi:10.1093/nar/gkaf1292](https://doi.org/10.1093/nar/gkaf1292) |
| GO-CAM | GO 因果活动模型：把 GO 注释连成通路模型。 | [doi:10.1093/nar/gkaf1292](https://doi.org/10.1093/nar/gkaf1292) |
| IEA | 电子注释推断：机器预测使用的证据代码。 | `README.md (Cross-cutting pitfalls)` |
| InterPro signature | 成员数据库提供的预测模型（HMM、模式），定义家族、结构域或位点。 | [doi:10.1093/nar/gkae1082](https://doi.org/10.1093/nar/gkae1082) |
| KO | KEGG 直系同源编号：把基因连到通路图的通用标识。 | [doi:10.1093/nar/gkae909](https://doi.org/10.1093/nar/gkae909) |
| MapMan bin | MapMan4 植物蛋白分类中的一个类别。 | [doi:10.1016/j.molp.2019.01.003](https://doi.org/10.1016/j.molp.2019.01.003) |
| NLR | 含核苷酸结合位点和富亮氨酸重复的植物免疫受体蛋白。 | [doi:10.1104/pp.19.01273](https://doi.org/10.1104/pp.19.01273) |
| Orthogroup | OrthoFinder 在所比较基因组间推断出的一组基因；F7 框架对每个直系同源组注释一条代表序列。 | `docs/SCENARIOS_FUNCTIONAL.md (frame F7)` |
| Signal peptide | 控制蛋白分泌和转运的 N 端短序列。 | [doi:10.1038/s41587-021-01156-3](https://doi.org/10.1038/s41587-021-01156-3) |
| Swiss-Prot | UniProtKB 中人工校对的部分。 | [doi:10.1371/journal.pcbi.1000605](https://doi.org/10.1371/journal.pcbi.1000605) |
