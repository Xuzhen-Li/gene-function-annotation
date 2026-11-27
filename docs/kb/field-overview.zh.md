# 功能基因注释：概览

[English](field-overview.md) · [知识单元](README.zh.md)

## 1. 是什么

功能基因注释回答基因组的蛋白和 RNA 产物做什么：执行哪些分子功能，参与哪些生物学过程，位于细胞的哪些部分，处在哪些通路中。它从 [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation) 发布的蛋白集（`proteins.faa`）出发（说法 1）。关于基因功能的知识，大多来自少数模式生物上的实验（说法 2），所以新基因组的标签多数是*推断*出来的：从相似序列或直系同源基因转移而来（说法 3）。标签附带的证据代码说明它是怎么得到的（说法 15）。

## 2. 问题与背后的概念

**从序列相似性和进化历史能推断什么？** 直系同源基因和旁系同源基因是两类同源基因：*直系同源基因*由同一祖先基因经垂直传递而来，*旁系同源基因*由复制产生；对新测序基因组做可靠的功能注释，区分两者至关重要（说法 4）。直系同源推断适合用来推断功能，但在大规模应用时计算量大，所以精度较低的同源转移仍是基因组注释的默认做法（说法 3）。Blast2GO 和 PANNZER2 这类基于相似性的工具，根据同源搜索给出 GO 条目（说法 5）。eggNOG-mapper 基于预先计算的直系同源关系做注释（说法 6），OrthoFinder 在多个基因组间推断直系同源组和直系同源基因（说法 7）。书：第 2、5、8 章。

**蛋白含有哪些部分和结构？** InterPro 这样的资源把蛋白归入家族和结构域，它整合了多个成员数据库的特征签名；Pfam 也做同样的分类（说法 8）。Foldseek 这类结构搜索工具把查询结构与结构数据库做比对（说法 9）。TargetP 2.0 这类定位预测器识别 N 端分选信号，这些信号把蛋白引向分泌途径、线粒体和叶绿体或其他质体（说法 10）。书：第 4、9、14 章。

**功能怎样写进标准词表和通路？** 自由文本的名称不便计算，所以功能要映射到受控系统。*基因本体*（GO）用结构化词表描述生物学过程、分子功能和细胞组分（说法 11 和 12）；GO *注释*是有证据支持的、关于某个基因产物的陈述（说法 11）。*酶学委员会*（EC）编号是 IUBMB 酶分类系统给出的四段编码（说法 13）。*KEGG 直系同源*（KO）把基因和蛋白连到通路图（说法 14）。*证据代码*记录标签的来源；代码 IEA 标记那些通常无法追溯到实验来源的注释（说法 15）。书：第 3、5、7 章。

**植物和非蛋白编码基因需要特别注意什么？** 许多植物免疫受体（NLR）在同一基因组内和同一物种的不同个体间高度多样化（说法 16）；植物基因家族在书中有单独一章。GO 也涵盖非编码 RNA（说法 11）。共表达网络提供了从表达数据探索功能关联的初步途径，但有注释传播和“近朱者赤”（guilt-by-association）等需要注意的地方（说法 17 和 18）。书：第 10 到 12 章。

**功能表能信到什么程度，下游怎么用？** 自动方法给出的标签不是实验结果：IEA 注释通常无法追溯到实验来源（说法 15）。忽略 GO 的一些要点会导致错误结果（说法 12），把碎片化的蛋白组当作参考时，错误会扩散，OMArk 在鸟类基因注释中发现了这种情况（说法 19）。富集分析把基因列表与本体和通路联系起来，其作者强调要用最新的注释数据库（说法 20）。阈值和门槛只写在 [`docs/EVALUATION.md`](../EVALUATION.md)。书：第 15、19 章。

## 3. 从书的哪里读起

- **刚接触功能注释：** [前言](../../book/chapters/00-preface.zh.md)和[第 1 章 概念与原理](../../book/chapters/01-concepts.zh.md)，旁边放着[附录 A 术语表](../../book/chapters/appendix-a-glossary.zh.md)。
- **同源、参考数据库、结构域和直系同源：** [第 2 章 同源搜索](../../book/chapters/02-homology-search.zh.md)、[第 3 章 参考序列与本体数据库](../../book/chapters/03-reference-sequence-and-ontology-databases.zh.md)、[第 4 章 结构域与家族注释](../../book/chapters/04-domain-and-family-annotation.zh.md)和[第 5 章 基于直系同源的名称、GO 与 KEGG](../../book/chapters/05-orthology-based-names-go-and-kegg.zh.md)。
- **通路、多基因组直系同源组、定位和三维结构：** [第 7 章 通路、KO 与 EC](../../book/chapters/07-pathways-ko-and-ec.zh.md)、[第 8 章 多基因组直系同源](../../book/chapters/08-multi-genome-orthology.zh.md)、[第 9 章 定位与拓扑](../../book/chapters/09-localization-and-topology.zh.md)和[第 14 章 蛋白三维结构](../../book/chapters/14-protein-3d-structure.zh.md)。
- **植物基因家族、非编码 RNA 和表达证据：** [第 10 章 植物基因家族](../../book/chapters/10-plant-gene-families.zh.md)、[第 11 章 非编码 RNA 功能资源](../../book/chapters/11-non-coding-rna-function-resources.zh.md)和[第 12 章 表达支持的功能](../../book/chapters/12-expression-supported-function.zh.md)。
- **富集分析：** [第 15 章 下游富集](../../book/chapters/15-downstream-enrichment.zh.md)。
- **选策略、检查质量或跟一个完整的植物实例：** [第 18 章 怎么选框架和加件](../../book/chapters/18-choosing-tools.zh.md)、[第 19 章 常见问题与质控](../../book/chapters/19-pitfalls-and-qc.zh.md)和[第 20 章 实例：葡萄蛋白走 F1 框架加 F8 加件](../../book/chapters/20-worked-example.zh.md)。

## 4. 植物和 *Vitis* 里已知什么

- 植物 NLR 基因高度多样化（说法 16）。
- 葡萄实例见书的第 20 章。本页不给出葡萄蛋白中有实验支持功能的比例的一般数字。

## 5. 说法与来源

引用的句子抄自同一行所列的来源，保持原文语言。摘要读自每篇论文的 Europe PMC 记录。

| # | 说法 | 来源 | 引用原句 | 读了什么 |
|---|---|---|---|---|
| 1 | 本仓库的功能注释从结构注释发布的蛋白集开始。 | [`docs/POST_STRUCTURE.md`](../POST_STRUCTURE.md)（本仓库） | “You already have a **structure release** (`proteins.faa` + `RELEASE_TAG` or hash). This repo only labels proteins.” | 页面开头几行 |
| 2 | 多数基因功能知识来自少数模式生物。 | Gene Ontology Consortium 2023, *Genetics*, [doi:10.1093/genetics/iyad031](https://doi.org/10.1093/genetics/iyad031) | “GO annotations cover genes from organisms across the tree of life as well as viruses, though most gene function knowledge currently derives from experiments carried out in a relatively small number of model organisms.” | 摘要（PMID 36866529） |
| 3 | 直系同源推断适合推断功能，但基于同源的转移仍是默认做法。 | Huerta-Cepas et al. 2017, *Mol Biol Evol*, [doi:10.1093/molbev/msx148](https://doi.org/10.1093/molbev/msx148) | “Orthology assignment is ideally suited for functional inference.”; “However, because predicting orthology is computationally intensive at large scale, and most pipelines are relatively inaccessible (e.g., new assignments only available through database updates), less precise homology-based functional transfer is still the default for (meta-)genome annotation.” | 摘要（PMID 28460117） |
| 4 | 直系同源和旁系同源来源不同，这一区分对注释很重要。 | Koonin 2005, *Annu Rev Genet*, [doi:10.1146/annurev.genet.39.073003.114725](https://doi.org/10.1146/annurev.genet.39.073003.114725) | “Orthologs and paralogs are two fundamentally different types of homologous genes that evolved, respectively, by vertical descent from a single ancestral gene and by duplication.”; “A clear distinction between orthologs and paralogs is critical for the construction of a robust evolutionary classification of genes and reliable functional annotation of newly sequenced genomes.” | 摘要（PMID 16285863） |
| 5 | Blast2GO 和 PANNZER2 根据相似性搜索给出 GO 条目。 | Conesa et al. 2005, *Bioinformatics*, [doi:10.1093/bioinformatics/bti610](https://doi.org/10.1093/bioinformatics/bti610); Törönen, Medlar and Holm 2018, *Nucleic Acids Res*, [doi:10.1093/nar/gky350](https://doi.org/10.1093/nar/gky350) | “B2G joints in one application GO annotation based on similarity searches with statistical analysis and highlighted visualization on directed acyclic graphs.”; “PANNZER2 uses SANSparallel to perform high-performance homology searches, making bulk annotation based on sequence similarity practical.” | 摘要（PMID 16081474; PMID 29741643） |
| 6 | eggNOG-mapper 基于预先计算的直系同源关系做注释。 | Cantalapiedra et al. 2021, *Mol Biol Evol*, [doi:10.1093/molbev/msab293](https://doi.org/10.1093/molbev/msab293) | “Here, we describe a major upgrade to eggNOG-mapper, a tool for functional annotation based on precomputed orthology assignments, now optimized for vast (meta)genomic data sets.” | 摘要（PMID 34597405） |
| 7 | OrthoFinder 推断直系同源组和直系同源基因。 | Emms and Kelly 2019, *Genome Biol*, [doi:10.1186/s13059-019-1832-y](https://doi.org/10.1186/s13059-019-1832-y) | “This extends OrthoFinder's high accuracy orthogroup inference to provide phylogenetic inference of orthologs, rooted gene trees, gene duplication events, the rooted species tree, and comparative genomics statistics.” | 摘要（PMID 31727128） |
| 8 | InterPro 和 Pfam 把蛋白分入家族和结构域。 | Blum et al. 2025, *Nucleic Acids Res*, [doi:10.1093/nar/gkae1082](https://doi.org/10.1093/nar/gkae1082); Mistry et al. 2021, *Nucleic Acids Res*, [doi:10.1093/nar/gkaa913](https://doi.org/10.1093/nar/gkaa913) | “It integrates predictive models, known as signatures, from multiple member databases to classify sequences into families and predict the presence of domains and significant sites.”; “The Pfam database is a widely used resource for classifying protein sequences into families and domains.” | 摘要（PMID 39565202; PMID 33125078） |
| 9 | Foldseek 用查询结构搜索结构数据库。 | van Kempen et al. 2024, *Nat Biotechnol*, [doi:10.1038/s41587-023-01773-0](https://doi.org/10.1038/s41587-023-01773-0) | “Foldseek aligns the structure of a query protein against a database by describing tertiary amino acid interactions within proteins as sequences over a structural alphabet.” | 摘要（PMID 37156916） |
| 10 | TargetP 2.0 识别把蛋白引向分泌途径、线粒体和叶绿体的 N 端分选信号。 | Almagro Armenteros et al. 2019, *Life Sci Alliance*, [doi:10.26508/lsa.201900429](https://doi.org/10.26508/lsa.201900429) | “Here, we demonstrate this by presenting TargetP 2.0, a novel state-of-the-art method to identify N-terminal sorting signals, which direct proteins to the secretory pathway, mitochondria, and chloroplasts or other plastids.” | 摘要（PMID 31570514） |
| 11 | GO 涵盖蛋白和非编码 RNA，其注释是有证据支持的陈述。 | Gene Ontology Consortium 2023, 同说法 2 | “The Gene Ontology (GO) knowledgebase (http://geneontology.org) is a comprehensive resource concerning the functions of genes and gene products (proteins and noncoding RNAs).”; “GO annotations-evidence-supported statements asserting that a specific gene product has a particular functional characteristic” | 摘要（PMID 36866529） |
| 12 | GO 有三套词表，忽略 GO 的一些要点会导致错误结果。 | Rhee et al. 2008, *Nat Rev Genet*, [doi:10.1038/nrg2363](https://doi.org/10.1038/nrg2363) | “GO produces sets of explicitly defined, structured vocabularies that describe biological processes, molecular functions and cellular components of gene products in both a computer- and human-readable manner.”; “Here we describe key aspects of GO, which, when overlooked, can cause erroneous results, and address how these pitfalls can be avoided.” | 摘要（PMID 18475267） |
| 13 | EC 编号是 IUBMB 酶分类系统给出的四段编码，酶命名法由 ExplorEnz 数据库维护。 | IUBMB, Enzyme Nomenclature, classification and nomenclature rules ([iubmb.qmul.ac.uk](https://iubmb.qmul.ac.uk/enzyme/rules.html)); McDonald, Boyce and Tipton 2009, *Nucleic Acids Res*, [doi:10.1093/nar/gkn582](https://doi.org/10.1093/nar/gkn582) | “The first Enzyme Commission, in its report in 1961, devised a system for classification of enzymes that also serves as a basis for assigning code numbers to them. These code numbers, prefixed by EC, which are now widely in use, contain four elements separated by points”; “ExplorEnz is the MySQL database that is used for the curation and dissemination of the International Union of Biochemistry and Molecular Biology (IUBMB) Enzyme Nomenclature.” | 规则页正文，第 3 节（酶分类方案）；摘要（PMID 18776214） |
| 14 | KO 把基因和蛋白连到通路图。 | Kanehisa et al. 2025, *Nucleic Acids Res*, [doi:10.1093/nar/gkae909](https://doi.org/10.1093/nar/gkae909) | “The KEGG Orthology (KO) system is a mechanism for linking genes and proteins to pathway maps and other molecular networks.” | 摘要（PMID 39417505） |
| 15 | IEA 注释通常无法追溯到实验来源。 | Gene Ontology Consortium，证据代码指南 ([geneontology.org](https://geneontology.org/docs/guide-go-evidence-codes/)) | “IEA-supported annotations are ultimately based on either homology and/or other experimental or sequence information, but cannot generally be traced to an experimental source.” | 页面正文，电子注释一节 |
| 16 | 植物 NLR 免疫受体高度多样化。 | Barragan and Weigel 2021, *Plant Cell*, [doi:10.1093/plcell/koaa002](https://doi.org/10.1093/plcell/koaa002) | “As a consequence, many members of the plant immune system, and especially the intracellular nucleotide-binding site leucine-rich repeat receptors, also known as NOD-like receptors (NLRs), are highly diversified, both among family members in the same genome, and between individuals in the same species.” | 摘要（PMID 33793812） |
| 17 | 共表达网络可以揭示功能关联。 | Rao and Dixon 2019, *Acta Biochim Biophys Sin*, [doi:10.1093/abbs/gmz080](https://doi.org/10.1093/abbs/gmz080) | “Such networks provide an initial way to explore functional associations from gene expression profiling and can be applied to various aspects of plant biology.” | 摘要（PMID 31436787） |
| 18 | 基于网络的功能预测有注释传播和“近朱者赤”等需要注意的地方。 | Rhee and Mutwil 2014, *Trends Plant Sci*, [doi:10.1016/j.tplants.2013.10.006](https://doi.org/10.1016/j.tplants.2013.10.006) | “We also discuss caveats associated with network-based function predictions such as performance assessment, annotation propagation, the guilt-by-association concept, and the meaning of hubs.” | 摘要（PMID 24231067） |
| 19 | 把碎片化的蛋白组当参考用时，错误会扩散。 | Nevers et al. 2025, *Nat Biotechnol*, [doi:10.1038/s41587-024-02147-w](https://doi.org/10.1038/s41587-024-02147-w) | “Analysis of 1,805 UniProt Eukaryotic Reference Proteomes with OMArk demonstrated strong evidence of contamination in 73 proteomes and identified error propagation in avian gene annotation resulting from the use of a fragmented zebra finch proteome as a reference.” | 摘要（PMID 38383603） |
| 20 | 富集分析使用本体和通路，需要最新的注释数据库。 | Wu et al. 2021, *Innovation*, [doi:10.1016/j.xinn.2021.100141](https://doi.org/10.1016/j.xinn.2021.100141) | “Functional enrichment analysis is pivotal for interpreting high-throughput omics data in life science. It is crucial for this type of tool to use the latest annotation databases for as many organisms as possible.”; “The new version provides a universal interface for functional enrichment analysis in thousands of organisms based on internally supported ontologies and pathways as well as annotation data provided by users or derived from online databases.” | 摘要（PMID 34557778） |

## 6. 另见

- 书：[前言](../../book/chapters/00-preface.zh.md)；[第 1 章 概念与原理](../../book/chapters/01-concepts.zh.md)；[第 20 章 实例](../../book/chapters/20-worked-example.zh.md)
- 知识单元：[功能标签与四套编号](function-concepts.zh.md)；[按同源和直系同源转移功能](homology-transfer.zh.md)；[功能表可信到什么程度（判据）](credibility-criteria.zh.md)
- 按步骤的软件：[`catalog/README.by-type.zh.md`](../../catalog/README.by-type.zh.md)
- 结构与功能工作的边界：[`docs/BOUNDARY.md`](../BOUNDARY.md)
