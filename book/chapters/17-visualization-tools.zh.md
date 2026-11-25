# 第 17 章 可视化工具

*本章收录[主页“可视化工具”一节](../../README.zh.md#visualization)：该节说明、含论文、实验室、权威度和评价的完整工具表，以及评测要点。链接指回仓库。*

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
