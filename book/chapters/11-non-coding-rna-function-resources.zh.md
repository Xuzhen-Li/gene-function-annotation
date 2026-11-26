# 第 11 章 非编码 RNA 功能资源

*本章收录[主页第 10 节](../../README.zh.md#section-10)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

非编码 RNA 功能注释资源。通常需要转录组或已知的 ncRNA 位点，不能单靠蛋白表。

**需要：** 转录组数据或已知的 ncRNA 位点——不能只靠蛋白表。基因结构预测与 TE 库构建仍分别归属结构注释库和 TE-Lib。[按场景列出的数据需求](../../README.zh.md#data-needs)

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
