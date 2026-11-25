# 第 18 章 怎么选框架和加件

仓库要求每个发布版声明一个完整的注释框架，加件单独列出（主页“默认路线”；[`docs/SCENARIOS_FUNCTIONAL.md`](../../docs/SCENARIOS_FUNCTIONAL.md)）。下表复述这一选择，并补上首选工具背后的证据。

| 情况 | 框架或加件 | 工具 | 理由（出处） | 主要检查 |
|---|---|---|---|---|
| 默认的论文发布 | F1 | DIAMOND 比 Swiss-Prot、eggNOG-mapper、InterProScan | 三条独立证据：校对库相似性（[doi:10.1038/s41592-021-01101-x](https://doi.org/10.1038/s41592-021-01101-x)）、直系同源转移（[doi:10.1093/molbev/msab293](https://doi.org/10.1093/molbev/msab293)）、特征签名（[doi:10.1093/bioinformatics/btu031](https://doi.org/10.1093/bioinformatics/btu031)） | 合并表行数接近蛋白数（`examples/plant_sim/01_vitis_s1_s7/plan.md`） |
| 快速初筛 | F2 | eggNOG-mapper，可选 KofamScan | eggNOG 6.0 覆盖 12,535 个参考物种（[doi:10.1093/nar/gkac1022](https://doi.org/10.1093/nar/gkac1022)）；Kofam 使用自适应阈值（[doi:10.1093/bioinformatics/btz859](https://doi.org/10.1093/bioinformatics/btz859)） | 不要把 F2 当作已跑过 InterProScan 来发布（主页“所需数据”） |
| 从头组装转录组的肽段 | F3 EnTAP 或 F5 Trinotate | EnTAP、Trinotate | EnTAP 为非模式真核生物的从头转录组设计（[doi:10.1111/1755-0998.13106](https://doi.org/10.1111/1755-0998.13106)） | 在 METHODS 中写明所用框架 |
| 多个基因组的面板 | F7 | OrthoFinder，再对代表序列跑 F1 | 标准化直系同源评测（[doi:10.1038/nmeth.3830](https://doi.org/10.1038/nmeth.3830)）；OrthoFinder 3 准确度提升（[doi:10.1101/2025.07.15.664860](https://doi.org/10.1101/2025.07.15.664860)） | 标签对应直系同源组代表序列，不是每个基因 |
| 需要可读名称 | F4 加件 | AHRD | 名称是展示层（主页“所需数据”） | 名称本身不提高等级 |
| 计划画 MapMan 图 | F6 加件 | Mercator4 | 植物蛋白分类框架（[doi:10.1016/j.molp.2019.01.003](https://doi.org/10.1016/j.molp.2019.01.003)） | 只有计划画 MapMan 图时才跑（`docs/MERCATOR_WHEN.md`） |
| 有抗病或 NLR 研究主线 | F8 加件 | InterProScan 过滤、NLR-Annotator、NLRtracker | NLR 表达低、家族内序列相似度高，难以注释，NLR-Annotator 为此而建（[doi:10.1104/pp.19.01273](https://doi.org/10.1104/pp.19.01273)）；NLRtracker 附带经实验验证的植物 NLR 参考集（[doi:10.1371/journal.pbio.3001124](https://doi.org/10.1371/journal.pbio.3001124)） | InterProScan 初筛不等于人工校对的 NLR 集 |
| 转录因子或激酶 | F9 加件 | iTAK | 植物转录因子和激酶分类（[doi:10.1016/j.molp.2016.09.014](https://doi.org/10.1016/j.molp.2016.09.014)） | 只在需要该家族时使用 |

## 权威度怎么看

各表的权威度（标准：被引 500 及以上；成熟：100 至 499；新近：不足 100 且 2023 年及以后发表；小众：不足 100 且更早）衡量论文被引的广度，不代表在你的蛋白组上更准。数据库和通用工具（UniProt、InterPro、KEGG、Cytoscape）会从所有领域获得引用。准确度更应看社区评测：CAFA3 发现最好的方法明显优于基线，但仍有很大改进空间（[doi:10.1186/s13059-019-1835-8](https://doi.org/10.1186/s13059-019-1835-8)）。

## 加新工具前要问的问题

1. 它是否带来新的证据类型（相似性、签名、直系同源、结构、语言模型），还是重复 F1 已有的？
2. 有没有独立评测（CAFA、Quest for Orthologs），还是只有作者自评？
3. 它的输出带什么证据代码？机器预测一律保持 IEA（主页“通用注意事项”）。
4. 数据库版本能否记录，许可是否允许再分发？主页中 KEGG 的再分发仍标为待确认。
