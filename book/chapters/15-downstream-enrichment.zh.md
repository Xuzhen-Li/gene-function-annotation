# 第 15 章 下游富集

*本章收录[主页第 14 节](../../README.zh.md#section-14)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

下游 GO/KEGG 富集分析。直接读取已生成的注释总表，本身不产出新的功能标签。

**需要：** 已完成的功能注释表，外加界定清晰的背景基因集（通常取当次发布的全部基因）。这属于合并总表之后的下游分析，并非功能标签的来源。[按场景列出的数据需求](../../README.zh.md#data-needs)

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
