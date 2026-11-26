# 功能标签与四套编号

[English](function-concepts.md) · [知识单元](README.zh.md)

## 1. 是什么

功能注释给结构注释发布的蛋白加上标签：易读名称、Gene Ontology（GO）条目、KEGG 直系同源（KO）和通路、蛋白结构域和家族，以及可选的植物类别，例如 MapMan 分类、NLR 和转录因子家族。输入是每个基因一条代表蛋白的 `proteins.faa`，产物是一张以基因为行的表 `merged_function_table.tsv`。每个标签都是带来源的陈述，不是对蛋白的实测结果。

## 2. 证据的结构

每个蛋白合并三条证据，每个标签保留给出它的那一条：

| 证据 | 提供什么 | 书 |
|---|---|---|
| 与人工校对蛋白的相似性 | 在 Swiss-Prot 等校对集中的最佳匹配 | [第 2 章](../../book/chapters/02-homology-search.zh.md) |
| 特征序列与结构域 | 家族、结构域和位点，并映射到 GO | [第 4 章](../../book/chapters/04-domain-and-family-annotation.zh.md) |
| 基于直系同源的转移 | 从直系同源基因带过来的名称、GO 和 KO | [第 5 章](../../book/chapters/05-orthology-based-names-go-and-kegg.zh.md) |

合并规则见[第 16 章](../../book/chapters/16-ideas-formats-and-merge-rules.zh.md)。每个标签可信到什么程度，见另一个单元：[功能表可信到什么程度](credibility-criteria.zh.md)。

## 3. 怎样认出可靠的功能表（现场卡片）

- 每个基因一行，行数与输入蛋白一致（或列出了去掉的条目）。
- 每个 GO 条目都带来源和证据代码。
- 写明所用框架（默认 `frame=F1`）。
- 正文里不混用下面四套编号。

## 4. 本仓库的默认框架与四套编号

默认框架是 **F1**：DIAMOND 比对 Swiss-Prot、eggNOG-mapper 和 InterProScan（[README 默认路线](../../README.zh.md#方法目录)；[`docs/workflow/README.zh.md`](../workflow/README.zh.md)）。有四套编号看起来很像，统一定义在 [`catalog/_namespaces.md`](../../catalog/_namespaces.md)：

| 编号体系 | 例子 | 含义 |
|---|---|---|
| 框架 | F1、F2、F3、F5 | 在 METHODS 中声明的整套框架 |
| 脚本文件 | `F1_diamond.sh`、`F2_eggnog.sh`、`F3_interproscan.sh` | 框架 F1 的三个步骤 |
| TOOLS 卡片 | F1a、F1b、F1c | F1 三个步骤的阅读页 |
| 门槛 | Gate-F1 至 Gate-F7 | [`docs/EVALUATION.md`](../EVALUATION.md) 中的发布检查 |

脚本 `F2_eggnog.sh` 是框架 F1 中的 eggNOG-mapper 步骤，**不是**框架 F2。旧的阶段编号和类型编号见[编号对照](NUMBERING.zh.md)。

## 5. 植物与葡萄中已知的情况

- MapMan4 与 Mercator 是专为植物设计的蛋白分类（[书 1.3 节](../../book/chapters/01-concepts.md#13-vocabularies-and-evidence)）。
- 功能标签会继承基因模型的全部错误，所以先做蛋白 BUSCO 检查（F0）（[书 1.5 节](../../book/chapters/01-concepts.md#15-structure-comes-first)）。
- 葡萄实例见 [`examples/plant_sim/01_vitis_s1_s7/`](../../examples/plant_sim/01_vitis_s1_s7/plan.md)。葡萄蛋白中有多少在 F1 下得不到任何标签，本页不给出：**[待确认]**。

## 6. 论断与来源

引文保留原文英文。

| 论断 | 来源 | 原文引句 | 读了什么 |
|---|---|---|---|
| GO 注释是把基因产物和 GO 条目联系起来的陈述。 | Gene Ontology，[Introduction to GO annotations](https://geneontology.org/docs/go-annotations/) | “A standard GO annotation is a statement that links a gene product and a GO term via a relation from the Relations Ontology (RO).” | 网页 Standard GO annotations 一节 |
| 每条 GO 注释都带证据代码。 | Gene Ontology，[Guide to GO evidence codes](https://geneontology.org/docs/guide-go-evidence-codes/) | “Each annotation includes an evidence code to indicate how the annotation to a particular term is supported.” | 网页开头一段 |
| 脚本 `F2_eggnog.sh` 属于框架 F1。 | 本仓库 [`catalog/_namespaces.md`](../../catalog/_namespaces.md) | “`F1_diamond.sh`, `F2_eggnog.sh`, `F3_interproscan.sh` are the **three steps of framework F1**” | 当前 main 分支上的文件 |
| 基因模型的错误会带进功能标签。 | 本仓库书第 1 章 1.5 节，引用 [doi:10.1093/bioinformatics/btaf365](https://doi.org/10.1093/bioinformatics/btaf365) | “Function labels inherit every error in the gene models.” | 章节正文；本页未重新打开所引论文 |

## 7. 相关页面

- 书：[第 1 章 概念与原则](../../book/chapters/01-concepts.zh.md)；[附录 A 术语表](../../book/chapters/appendix-a-glossary.zh.md)
- 知识单元：[按同源和直系同源转移功能](homology-transfer.zh.md)；[功能表可信到什么程度](credibility-criteria.zh.md)
- 按步骤查软件：[`catalog/README.by-type.md`](../../catalog/README.by-type.md)
- 上游：[gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation)
