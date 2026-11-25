# 第 6 章 机器学习 GO 预测

*本章收录[主页第 5 节](../../README.zh.md#section-5)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

基于机器学习的 GO 预测。属于框架 F1 之后的可选附加项，不能替代 F1。

**需要：** 通常只需输入蛋白序列，配合工具自带的模型。这些工具是框架 F1 之后的可选附加项，不能替代 F1。[按场景列出的数据需求](../../README.zh.md#data-needs)

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
