# 按同源和直系同源转移功能

[English](homology-transfer.md) · [知识单元](README.zh.md)

## 1. 是什么

新蛋白组上的大多数标签是转移来的，不是测出来的：把蛋白和功能已知的蛋白比较，再把匹配对象的标签带过来。**同源**指两条序列有共同祖先，相似性检索的最佳匹配是同源的证据。**直系同源**范围更窄，指由物种分化分开的基因。直系同源基因比旁系同源基因更可能保留同样的功能，所以 GO 和 KEGG 优先用基于直系同源的转移。

## 2. 证据的结构

| 框架 F1 中的步骤 | 默认工具 | 增加什么 | 目录 |
|---|---|---|---|
| 与校对集做相似性检索 | DIAMOND v2 比对 Swiss-Prot | 最佳校对匹配 | [第 1 节](../../catalog/METHODS_CATALOG.zh.md#section-1) |
| 直系同源归属 | eggNOG-mapper | 直系同源组、名称、GO、KO | [第 4 节](../../catalog/METHODS_CATALOG.zh.md#section-4) |
| 结构域与家族 | InterProScan | 支持名称但不能代替名称的结构域证据 | [第 3 节](../../catalog/METHODS_CATALOG.zh.md#section-3) |

这些步骤背后的数据库（Swiss-Prot、eggNOG、InterPro）见[目录第 2 节](../../catalog/METHODS_CATALOG.zh.md#section-2)。

## 3. 怎样认出可靠的转移（现场卡片）

- 每次转移都写明数据库及其版本。
- 比对程序和数据库版本相互匹配（例如 eggNOG-mapper 的版本和 eggNOG 数据库的版本）。
- 只凭最佳匹配得到的标签，不称为直系同源归属。
- 没有命名步骤，不把结构域命中直接变成基因名。

## 4. 本仓库的默认框架与分支

默认是框架 F1；F2（只用 eggNOG-mapper）、F3（EnTAP）和 F5（Trinotate）更快，但等级较低（[`catalog/_namespaces.md`](../../catalog/_namespaces.md)；[`docs/EVALUATION.md`](../EVALUATION.md#gate-f3--default-frame-or-waiver)）。易读名称是加件（F4，AHRD）。步骤顺序见 [`docs/workflow/README.zh.md`](../workflow/README.zh.md)。

## 5. 植物与葡萄中已知的情况

- 未经人工校对的数据库里错误注释很常见；书第 1 章给出了酶家族研究及其数字（[1.4 节](../../book/chapters/01-concepts.md#14-why-errors-matter)）。
- NLR 等植物基因家族需要专门工具，见[目录第 9 节](../../catalog/METHODS_CATALOG.zh.md#section-9)。
- 葡萄蛋白功能转移的实测准确率，本页不给出：**[待确认]**。

## 6. 论断与来源

引文保留原文英文。

| 论断 | 来源 | 原文引句 | 读了什么 |
|---|---|---|---|
| DIAMOND v2 在生命之树尺度上达到 BLASTP 的灵敏度。 | Buchfink、Reuter 与 Drost 2021，*Nat Methods* 18:366，[doi:10.1038/s41592-021-01101-x](https://doi.org/10.1038/s41592-021-01101-x) | “harnesses supercomputing to perform tree-of-life scale protein alignments in hours, while matching the sensitivity of the gold standard BLASTP” | 摘要（PubMed 33828273） |
| eggNOG-mapper 通过预先计算的直系同源关系转移功能。 | Cantalapiedra 等 2021，*Mol Biol Evol* 38:5825，[doi:10.1093/molbev/msab293](https://doi.org/10.1093/molbev/msab293) | “a tool for functional annotation based on precomputed orthology assignments” | 摘要（PubMed 34597405） |
| 直系同源优于最佳匹配，但仍不是真值。 | 本仓库 [`docs/EVALUATION.md`](../EVALUATION.md#knowledge-frame-why-evaluation-looks-like-this) 知识框架 | “fine-grained orthologs beat raw homology for GO/KEGG transfer; still not ground truth” | 当前 main 分支上的文件 |
| 结构域是证据，不是名称。 | 同上 | “**Domains are evidence, not names**” | 当前 main 分支上的文件 |

## 7. 相关页面

- 书：[第 2 章 同源搜索](../../book/chapters/02-homology-search.zh.md)；[第 5 章 基于直系同源的名称、GO 与 KEGG](../../book/chapters/05-orthology-based-names-go-and-kegg.zh.md)；[第 8 章 多基因组直系同源](../../book/chapters/08-multi-genome-orthology.zh.md)
- 知识单元：[功能标签与四套编号](function-concepts.zh.md)；[功能表可信到什么程度](credibility-criteria.zh.md)
