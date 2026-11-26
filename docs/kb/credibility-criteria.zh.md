# 功能表可信到什么程度（判据）

[English](credibility-criteria.md) · [知识单元](README.zh.md)

这是一个判据单元。F-L0、F-L1 两个等级、各项门槛和不通过规则只写在一处：[`docs/EVALUATION.md`](../EVALUATION.md)。本页解释两个层面的可信度并指向原文，不抄阈值。

## 1. 是什么

可信度分两层。**单个标签：**每个 GO 条目都有证据代码，说明它靠什么支持；机器生成的标签属于电子注释（IEA）。**整次发布：**整张表给一个等级。本仓库中 F-L0 是精简或快速框架，F-L1 是通过全部门槛的默认框架 F1。

## 2. 证据的结构

| 层面 | 判断什么 | 规则在哪里 |
|---|---|---|
| 标签 | 每个 GO 条目的证据代码；机器预测保持 IEA | [书第 19 章](../../book/chapters/19-pitfalls-and-qc.zh.md)；本页第 1 条 |
| 输入 | 稳定的蛋白文件和上游 BUSCO 检查 | [Gate-F1、Gate-F2](../EVALUATION.md#gate-f1--stable-protein-input) |
| 过程 | 写明框架、固定版本、表格行数完整 | [Gate-F3 至 Gate-F5](../EVALUATION.md#gate-f3--default-frame-or-waiver) |
| 发布 | 写明等级、状态和框架；发布包；仓库中不放数据库 | [两个完成等级](../EVALUATION.md#two-finish-grades)；[Gate-F6、Gate-F7](../EVALUATION.md#gate-f6--release-pack) |

## 3. 怎样认出可信的功能表（现场卡片）

- 预测得到的 GO 和 EC 条目标为 IEA。
- `grade=`、`status=` 和 `frame=` 分开写。
- 不凭相似性转移声称预测准确率。
- 植物加件作为模块列出，不当作更高等级。

## 4. 本仓库的默认框架与分支

逐项核对用 [`docs/EVALUATION_CHECKLIST.md`](../EVALUATION_CHECKLIST.md)。质控和发布步骤对应目录文件夹 F10 和 Frelease（[`catalog/README.md`](../../catalog/README.md)）。

## 5. 植物与葡萄中已知的情况

- 社区评测表明 GO 预测仍然困难（书第 1 章 [1.4 节](../../book/chapters/01-concepts.md#14-why-errors-matter)）。
- 植物加件（F4、F6、F8、F9）本身不提高等级（第 4 条）。
- 葡萄蛋白的 GO 条目中有实验支持的比例，本页不给出：**[待确认]**。

## 6. 论断与来源

引文保留原文英文。

| 论断 | 来源 | 原文引句 | 读了什么 |
|---|---|---|---|
| 电子注释（IEA）通常无法追溯到实验。 | Gene Ontology，[Guide to GO evidence codes](https://geneontology.org/docs/guide-go-evidence-codes/) | “IEA-supported annotations are ultimately based on either homology and/or other experimental or sequence information, but cannot generally be traced to an experimental source.” | 网页中关于电子注释的一节 |
| 每条 GO 注释都带证据代码。 | Gene Ontology，同上 | “Each annotation includes an evidence code to indicate how the annotation to a particular term is supported.” | 网页开头一段 |
| 本仓库评的是过程，不是预测准确率。 | 本仓库 [`docs/EVALUATION.md`](../EVALUATION.md#knowledge-frame-why-evaluation-looks-like-this) | “This page therefore grades *process integrity*, not CAFA Fmax.” | 当前 main 分支上的文件 |
| 植物加件不是更高等级。 | 本仓库 [`docs/EVALUATION.md`](../EVALUATION.md#two-finish-grades) | “Plant add-ons (F4/F6/F8/F9) are **not** a higher grade by themselves” | 当前 main 分支上的文件 |

## 7. 相关页面

- 书：[第 19 章 常见陷阱与质控](../../book/chapters/19-pitfalls-and-qc.zh.md)；[第 1 章 1.3 节](../../book/chapters/01-concepts.md#13-vocabularies-and-evidence)
- 知识单元：[功能标签与四套编号](function-concepts.zh.md)；[按同源和直系同源转移功能](homology-transfer.zh.md)
- 上游检查：[gene-structure-annotation `docs/EVALUATION.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/EVALUATION.md)
