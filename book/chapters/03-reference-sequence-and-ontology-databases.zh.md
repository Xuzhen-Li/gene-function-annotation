# 第 3 章 参考序列与本体数据库

*本章收录[主页第 2 节](../../README.zh.md#section-2)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

序列搜索和基因命名步骤所需的参考序列与本体数据库。

**需要：** 数据库文件本体（UniProt、GO、eggNOG、InterPro 成员库等）及对应版本号。这些内容无法仅凭待测蛋白序列推算出来。[按场景列出的数据需求](../../README.zh.md#data-needs)

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
