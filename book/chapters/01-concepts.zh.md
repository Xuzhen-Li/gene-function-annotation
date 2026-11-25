# 第 1 章 概念与原理

## 1.1 功能注释产出什么

功能注释给结构发布版的蛋白加上标签：可读名称、Gene Ontology（GO）条目、KEGG 直系同源和通路、蛋白结构域和家族，以及可选的植物分类，如 MapMan 类别、NLR 或转录因子家族（主页“概述”）。输入是每个基因一条代表序列的 `proteins.faa`，产物是 `merged_function_table.tsv`（主页“蛋白之外还需要的数据”）。找基因和改 GFF 在 gene-structure-annotation 中完成，不在这里。

## 1.2 推断功能的三条路

- **与人工校对蛋白的相似性。** 用快速比对器把蛋白组比到 Swiss-Prot 等校对库。DIAMOND v2 作者称可在数小时内完成生命之树规模的搜索，灵敏度与 BLASTP 相当（[doi:10.1038/s41592-021-01101-x](https://doi.org/10.1038/s41592-021-01101-x)）。UniProtKB 依据文献人工校对补充功能信息，并正在把序列限定为高质量、非冗余的参考蛋白组（[doi:10.1093/nar/gkae1010](https://doi.org/10.1093/nar/gkae1010)）。
- **特征签名与结构域。** InterPro 整合多个成员数据库的签名，把序列分入家族并预测结构域和位点，并映射到 GO（[doi:10.1093/nar/gkae1082](https://doi.org/10.1093/nar/gkae1082)）；InterProScan 在本地对大量序列运行这些签名（[doi:10.1093/bioinformatics/btu031](https://doi.org/10.1093/bioinformatics/btu031)）。
- **基于直系同源的转移。** eggNOG-mapper 通过预先计算的直系同源关系转移注释（[doi:10.1093/molbev/msab293](https://doi.org/10.1093/molbev/msab293)）；eggNOG 6.0 数据库覆盖 12,535 个参考物种（[doi:10.1093/nar/gkac1022](https://doi.org/10.1093/nar/gkac1022)）。

较新的方法加入了蛋白语言模型和三维结构。FANTASIA 用于约 1,000 个动物蛋白组，为同源方法未能注释的蛋白中最多 50% 预测了功能（[doi:10.1038/s42003-025-08651-2](https://doi.org/10.1038/s42003-025-08651-2)）。AlphaFold DB 收录超过 2.14 亿个预测结构（[doi:10.1093/nar/gkad1011](https://doi.org/10.1093/nar/gkad1011)），Foldseek 搜索结构比旧的结构比对工具快四到五个数量级（[doi:10.1038/s41587-023-01773-0](https://doi.org/10.1038/s41587-023-01773-0)）。

## 1.3 词表与证据

- **GO** 是描述基因功能的资源，定期更新（[doi:10.1093/nar/gkaf1292](https://doi.org/10.1093/nar/gkaf1292)）；预测按分子功能、生物过程、细胞组分三个方面分别评测（[doi:10.1186/s13059-019-1835-8](https://doi.org/10.1186/s13059-019-1835-8)）。
- **证据代码。** Evidence and Conclusion Ontology 记录每条注释背后的证据类型，便于追溯来源（[doi:10.1093/nar/gkab1025](https://doi.org/10.1093/nar/gkab1025)）。本仓库中机器预测的 GO 和 EC 一律保持 IEA（电子注释推断）（主页“通用注意事项”）。
- **KEGG。** 每个 KEGG Ortholog（KO）是通用基因标识，通路图是由 KO 节点构成的网络（[doi:10.1093/nar/gkae909](https://doi.org/10.1093/nar/gkae909)）。KofamKOALA 用 profile HMM 和预先计算的自适应阈值分配 KO（[doi:10.1093/bioinformatics/btz859](https://doi.org/10.1093/bioinformatics/btz859)）。
- **MapMan。** MapMan4 是面向植物的蛋白分类框架，配套 Mercator 工具做自动注释（[doi:10.1016/j.molp.2019.01.003](https://doi.org/10.1016/j.molp.2019.01.003)）。

## 1.4 错误为什么要紧

一项针对 37 个酶家族的研究发现，GenBank NR、TrEMBL 和 KEGG 的错误注释率平均为 5% 至 63%，而人工校对的 Swiss-Prot 接近 0%，多数错误来自对分子功能的过度预测（[doi:10.1371/journal.pcbi.1000605](https://doi.org/10.1371/journal.pcbi.1000605)）。CAFA3 评测发现，分子功能和生物过程的预测只略有进步，细胞组分没有进步（[doi:10.1186/s13059-019-1835-8](https://doi.org/10.1186/s13059-019-1835-8)）。很具体的 GO 条目比宽泛条目更难预测（[doi:10.1101/gr.280816.125](https://doi.org/10.1101/gr.280816.125)）。所以仓库把预测标签始终标为预测，并在 METHODS 中记录数据库版本。

## 1.5 先结构后功能

功能标签会继承基因模型的所有错误。同一批基因组用不同注释来源，直系同源结果明显不同（[doi:10.1093/bioinformatics/btaf365](https://doi.org/10.1093/bioinformatics/btaf365)）。因此仓库先做 F0 蛋白 BUSCO 检查，蛋白组质量差就退回结构注释，而不是在这里修补（`examples/plant_sim/01_vitis_s1_s7/plan.md`；主页“所需数据”）。

## 1.6 跨基因组的直系同源

直系同源推断方法要在精确率和召回率之间取舍；Quest for Orthologs 服务用 20 个基准评测了 15 种方法（[doi:10.1038/nmeth.3830](https://doi.org/10.1038/nmeth.3830)）。OrthoFinder 3 称直系同源组准确度比上一版相对提高 7%（[doi:10.1101/2025.07.15.664860](https://doi.org/10.1101/2025.07.15.664860)）。对多基因组面板，仓库注释的是直系同源组代表序列（F7 框架），不是每个基因（主页“通用注意事项”）。

## 1.7 定位与拓扑

SignalP 6.0 能识别全部五类信号肽（[doi:10.1038/s41587-021-01156-3](https://doi.org/10.1038/s41587-021-01156-3)）；TargetP 2.0 识别通往分泌途径、线粒体和叶绿体的 N 端信号（[doi:10.26508/lsa.201900429](https://doi.org/10.26508/lsa.201900429)）；DeepLoc 2.1 预测亚细胞定位和膜蛋白类型（[doi:10.1093/nar/gkae237](https://doi.org/10.1093/nar/gkae237)）；DeepTMHMM 预测 α 螺旋和 β 桶跨膜蛋白的拓扑（[doi:10.1101/2022.04.08.487609](https://doi.org/10.1101/2022.04.08.487609)）。

## 1.8 富集分析

富集检验问的是：一个基因列表是否比背景更常带某些标签。标准方法在 RNA-seq 数据上有偏，因为长转录本和高表达转录本更容易被检出（[doi:10.1186/gb-2010-11-2-r14](https://doi.org/10.1186/gb-2010-11-2-r14)）。长 GO 列表冗余度高，可按语义相似性归纳（[doi:10.1371/journal.pone.0021800](https://doi.org/10.1371/journal.pone.0021800)）。背景应使用完整的发布基因集（主页“所需数据”）。
