# 按类型的目录索引

[English](README.by-type.md) · [完整目录](METHODS_CATALOG.zh.md) · [条目数](COUNTS.md) · [按阶段的索引](README.md)

方法目录每个类型小节一行。条目数来自 [`SOFTWARE_AUTHORITY.tsv`](SOFTWARE_AUTHORITY.tsv)（194 条，2026-11-26）。类型键是 2026-11 调研文件 [`docs/CATALOG_BY_TYPE_2026-11.md`](../docs/CATALOG_BY_TYPE_2026-11.md) 中的标签，该文件作为旧记录保留。本目录下的文件夹按阶段存放首批卡片，其索引 [`README.md`](README.md) 保持不变，作为第二种视图。

| # | 类型小节 | 类型键（旧） | 条目数 | 默认与分支工具 | 书章 | 知识单元 |
|---|---|---|---|---|---|---|
| 1 | [1. 同源搜索](METHODS_CATALOG.zh.md#section-1) | `homology-search` | 8 | DIAMOND (v2) | [第 2章](../book/chapters/02-homology-search.zh.md) | [homology-transfer](../docs/kb/homology-transfer.zh.md) |
| 2 | [2. 参考序列与本体数据库](METHODS_CATALOG.zh.md#section-2) | `reference-db` | 11 | — | [第 3章](../book/chapters/03-reference-sequence-and-ontology-databases.zh.md) | [homology-transfer](../docs/kb/homology-transfer.zh.md) |
| 3 | [3. 结构域与家族注释](METHODS_CATALOG.zh.md#section-3) | `domain` | 6 | InterProScan 6 | [第 4章](../book/chapters/04-domain-and-family-annotation.zh.md) | [homology-transfer](../docs/kb/homology-transfer.zh.md) |
| 4 | [4. 基于直系同源的名称、GO 与 KEGG](METHODS_CATALOG.zh.md#section-4) | `orthology-go` | 12 | eggNOG-mapper v2, AHRD, Trinotate | [第 5章](../book/chapters/05-orthology-based-names-go-and-kegg.zh.md) | [homology-transfer](../docs/kb/homology-transfer.zh.md) |
| 5 | [5. 机器学习 GO 预测](METHODS_CATALOG.zh.md#section-5) | `ml-go` | 11 | — | [第 6章](../book/chapters/06-machine-learning-go-prediction.zh.md) | [credibility-criteria](../docs/kb/credibility-criteria.zh.md) |
| 6 | [6. 通路、KO 与 EC](METHODS_CATALOG.zh.md#section-6) | `pathway-enzyme` | 18 | — | [第 7章](../book/chapters/07-pathways-ko-and-ec.zh.md) | — |
| 7 | [7. 多基因组直系同源](METHODS_CATALOG.zh.md#section-7) | `multi-genome-orthology` | 16 | OrthoFinder 3 | [第 8章](../book/chapters/08-multi-genome-orthology.zh.md) | — |
| 8 | [8. 定位与拓扑](METHODS_CATALOG.zh.md#section-8) | `localization` | 11 | SignalP 6.0, DeepTMHMM, TMbed | [第 9章](../book/chapters/09-localization-and-topology.zh.md) | — |
| 9 | [9. 植物基因家族](METHODS_CATALOG.zh.md#section-9) | `plant-family` | 20 | — | [第 10章](../book/chapters/10-plant-gene-families.zh.md) | — |
| 10 | [10. 非编码 RNA 功能资源](METHODS_CATALOG.zh.md#section-10) | `ncrna-function` | 11 | — | [第 11章](../book/chapters/11-non-coding-rna-function-resources.zh.md) | — |
| 11 | [11. 表达支持的功能](METHODS_CATALOG.zh.md#section-11) | `expression` | 9 | — | [第 12章](../book/chapters/12-expression-supported-function.zh.md) | — |
| 12 | [12. 社区目录与命名](METHODS_CATALOG.zh.md#section-12) | `community-db` | 4 | — | [第 13章](../book/chapters/13-community-catalogues-and-naming.zh.md) | — |
| 13 | [13. 蛋白三维结构](METHODS_CATALOG.zh.md#section-13) | `protein-3d` | 23 | Foldseek | [第 14章](../book/chapters/14-protein-3d-structure.zh.md) | — |
| 14 | [14. 下游富集](METHODS_CATALOG.zh.md#section-14) | `enrichment` | 15 | — | [第 15章](../book/chapters/15-downstream-enrichment.zh.md) | — |
| 15 | [15. 想法、格式与合并规则](METHODS_CATALOG.zh.md#section-15) | `idea` | 9 | — | [第 16章](../book/chapters/16-ideas-formats-and-merge-rules.zh.md) | [function-concepts](../docs/kb/function-concepts.zh.md) |
| viz | [可视化工具](METHODS_CATALOG.zh.md#visualization) | — | 10 | — | [第 17 章](../book/chapters/17-visualization-tools.zh.md) | — |

**合计：194**

## 没有卡片的阶段文件夹

以下阶段文件夹没有首批卡片，保留它们是为了让阶段链接仍然有效；这些步骤的工具见上面的类型小节。

- F0 · protein input QC (BUSCO protein mode): [`F0_protein_qc/`](F0_protein_qc/README.md)
- F2 · fast framework (eggNOG-mapper alone ± Kofam; KEGGaNOG plots): [`frame_F2/`](frame_F2/README.md)
- F3 · EnTAP framework: [`frame_F3/`](frame_F3/README.md)
- Merge / aggregate (`F_merge_tables.py`, `F_aggregate.py`): [`Fmerge_aggregate/`](Fmerge_aggregate/README.md)
