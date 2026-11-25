# 第 12 章 表达支持的功能

*本章收录[主页第 11 节](../../README.zh.md#section-11)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

利用基因表达或共表达数据佐证功能假说，但不作为实验级 GO 证据。

**需要：** 若要用表达数据佐证基因功能，需准备 RNA-seq 数据（最好来自同一基因型）。[按场景列出的数据需求](../../README.zh.md#data-needs)

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
