# 编号体系

[English](NUMBERING.md) · [知识单元](README.zh.md)

本仓库同时用到几套编号。新页面用现行编号；旧编号留在旧页面中，不重新编号。本页给出对照。

| 编号体系 | 标签 | 状态 | 定义在 |
|---|---|---|---|
| 目录类型小节 | 1–15 与可视化 | 现行 | [`catalog/METHODS_CATALOG.zh.md`](../../catalog/METHODS_CATALOG.zh.md)；TSV 的 `section` 列 |
| 书章 | 第 1–20 章与附录 A；第 *n* + 1 章对应类型小节 *n*，第 17 章对应可视化 | 现行 | [`book/`](../../book/README.zh.md) |
| 框架与加件阶段 | F1（默认）、F2、F3、F5；加件 F0、F4、F6–F10 | 现行 | [`catalog/_namespaces.md`](../../catalog/_namespaces.md) |
| 脚本文件 | `F1_diamond.sh`、`F2_eggnog.sh`、`F3_interproscan.sh` 是框架 F1 的三个步骤；`F1b_kofam.sh` 是 F1 的 Kofam 步骤 | 现行；不作阶段名 | [`catalog/_namespaces.md`](../../catalog/_namespaces.md) |
| TOOLS 卡片 | F1a、F1b、F1c；F1+、F2+ | 现行；只作卡片标签 | [`docs/TOOLS.md`](../TOOLS.md) |
| 完成等级与门槛 | F-L0、F-L1；Gate-F1–Gate-F7 | 现行 | [`docs/EVALUATION.md`](../EVALUATION.md) |
| 最初卡片的阶段文件夹 | `F0_protein_qc/`、`frame_F1/` … `Frelease/` | 旧视图（2026-11 最初） | [`catalog/README.md`](../../catalog/README.md) |
| 类型键 | `homology-search` … `idea` | 旧（2026-11 调研） | [`docs/CATALOG_BY_TYPE_2026-11.md`](../CATALOG_BY_TYPE_2026-11.md) |

## 类型小节、旧类型键与书章对照

| 类型小节（现行） | 类型键（旧） | 书章 |
|---|---|---|
| [1. 同源搜索](../../catalog/METHODS_CATALOG.zh.md#section-1) | `homology-search` | [第 2 章 同源搜索](../../book/chapters/02-homology-search.zh.md) |
| [2. 参考序列与本体数据库](../../catalog/METHODS_CATALOG.zh.md#section-2) | `reference-db` | [第 3 章 参考序列与本体数据库](../../book/chapters/03-reference-sequence-and-ontology-databases.zh.md) |
| [3. 结构域与家族注释](../../catalog/METHODS_CATALOG.zh.md#section-3) | `domain` | [第 4 章 结构域与家族注释](../../book/chapters/04-domain-and-family-annotation.zh.md) |
| [4. 基于直系同源的名称、GO 与 KEGG](../../catalog/METHODS_CATALOG.zh.md#section-4) | `orthology-go` | [第 5 章 基于直系同源的名称、GO 与 KEGG](../../book/chapters/05-orthology-based-names-go-and-kegg.zh.md) |
| [5. 机器学习 GO 预测](../../catalog/METHODS_CATALOG.zh.md#section-5) | `ml-go` | [第 6 章 机器学习 GO 预测](../../book/chapters/06-machine-learning-go-prediction.zh.md) |
| [6. 通路、KO 与 EC](../../catalog/METHODS_CATALOG.zh.md#section-6) | `pathway-enzyme` | [第 7 章 通路、KO 与 EC](../../book/chapters/07-pathways-ko-and-ec.zh.md) |
| [7. 多基因组直系同源](../../catalog/METHODS_CATALOG.zh.md#section-7) | `multi-genome-orthology` | [第 8 章 多基因组直系同源](../../book/chapters/08-multi-genome-orthology.zh.md) |
| [8. 定位与拓扑](../../catalog/METHODS_CATALOG.zh.md#section-8) | `localization` | [第 9 章 定位与拓扑](../../book/chapters/09-localization-and-topology.zh.md) |
| [9. 植物基因家族](../../catalog/METHODS_CATALOG.zh.md#section-9) | `plant-family` | [第 10 章 植物基因家族](../../book/chapters/10-plant-gene-families.zh.md) |
| [10. 非编码 RNA 功能资源](../../catalog/METHODS_CATALOG.zh.md#section-10) | `ncrna-function` | [第 11 章 非编码 RNA 功能资源](../../book/chapters/11-non-coding-rna-function-resources.zh.md) |
| [11. 表达支持的功能](../../catalog/METHODS_CATALOG.zh.md#section-11) | `expression` | [第 12 章 表达支持的功能](../../book/chapters/12-expression-supported-function.zh.md) |
| [12. 社区目录与命名](../../catalog/METHODS_CATALOG.zh.md#section-12) | `community-db` | [第 13 章 社区目录与命名](../../book/chapters/13-community-catalogues-and-naming.zh.md) |
| [13. 蛋白三维结构](../../catalog/METHODS_CATALOG.zh.md#section-13) | `protein-3d` | [第 14 章 蛋白三维结构](../../book/chapters/14-protein-3d-structure.zh.md) |
| [14. 下游富集](../../catalog/METHODS_CATALOG.zh.md#section-14) | `enrichment` | [第 15 章 下游富集](../../book/chapters/15-downstream-enrichment.zh.md) |
| [15. 想法、格式与合并规则](../../catalog/METHODS_CATALOG.zh.md#section-15) | `idea` | [第 16 章 想法、格式与合并规则](../../book/chapters/16-ideas-formats-and-merge-rules.zh.md) |
