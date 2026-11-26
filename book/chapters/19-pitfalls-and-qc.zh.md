# 第 19 章 常见问题与质控

## 19.1 仓库已列出的问题

来自主页“蛋白之外还需要的数据”一节和 `docs/EVALUATION.md`。

- 这里不找基因、不做 soft-mask、不建 TE 库、不改 GFF；这些属于 gene-structure-annotation 或 TE-Lib。
- METHODS 中四套编号要分清：框架（F1、F2、F3、F5）、脚本文件（`F2_eggnog.sh` 是 F1 框架里的一步）、工具卡（F1a、F1b、F1c）和门槛（Gate-F1 至 F7）。
- 合并产物是 `merged_function_table.tsv`；机器预测的 GO 和 EC 保持 IEA。
- F7 框架注释的是直系同源组代表序列，不是每个基因。
- Foldseek、DeepFRI、AlphaFold DB 里的 structure 指蛋白三维结构。
- InterProScan 属于默认 F1 但很慢；F-L1 是验收标准，不是截止时间。
- 可选植物加件（F4、F6、F8、F9）本身不提高等级。
- 富集分析要有明确背景，通常是完整的发布基因集。

## 19.2 文献中的问题

- **过度预测。** 从弱匹配转移具体分子功能是酶超家族中最常见的错误；人工校对的 Swiss-Prot 错误接近 0%，而 NR、TrEMBL 和 KEGG 平均为 5% 至 63%（[doi:10.1371/journal.pcbi.1000605](https://doi.org/10.1371/journal.pcbi.1000605)）。优先用校对过的匹配，并保留证据代码。
- **细胞组分难。** CAFA3 中细胞组分预测没有进步（[doi:10.1186/s13059-019-1835-8](https://doi.org/10.1186/s13059-019-1835-8)）；定位结论应使用专门的定位工具（SignalP、TargetP、DeepLoc）。
- **具体条目少。** GO 条目的特异性不平衡，宽泛条目远比具体条目容易预测（[doi:10.1101/gr.280816.125](https://doi.org/10.1101/gr.280816.125)）。
- **上游注释影响结果。** 不同注释来源的直系同源结果明显不同（[doi:10.1093/bioinformatics/btaf365](https://doi.org/10.1093/bioinformatics/btaf365)）；要记录结构发布标签。
- **RNA-seq 富集偏差。** 长基因和高表达基因更容易被判为差异表达，需要校正（[doi:10.1186/gb-2010-11-2-r14](https://doi.org/10.1186/gb-2010-11-2-r14)）。
- **GO 列表冗余。** 应归纳，而不是列出几百个重叠条目（[doi:10.1371/journal.pone.0021800](https://doi.org/10.1371/journal.pone.0021800)）。

## 19.3 质控清单

| 检查 | 工具 | 出问题的表现 | 出处 |
|---|---|---|---|
| 输入蛋白组完整度（F0） | BUSCO 蛋白模式 | 完整度低：退回结构注释 | [doi:10.1093/molbev/msab199](https://doi.org/10.1093/molbev/msab199) |
| 输入一致性（可选） | OMArk | 大量不一致或污染蛋白 | [doi:10.1038/s41587-024-02147-w](https://doi.org/10.1038/s41587-024-02147-w) |
| 合并完整性 | `pipeline/F_merge_tables.py` | 行数与蛋白数差距大；丢弃未记录 | `examples/plant_sim/01_vitis_s1_s7/plan.md` |
| 版本 | METHODS | 数据库与比对器版本缺失或不匹配 | 主页“所需数据” |
| 证据代码 | 合并表 | 预测 GO 未标 IEA | [doi:10.1093/nar/gkab1025](https://doi.org/10.1093/nar/gkab1025)；主页 |
| 富集背景 | clusterProfiler 或 GOseq | 用子集作背景未说明；未处理长度偏差 | [doi:10.1186/gb-2010-11-2-r14](https://doi.org/10.1186/gb-2010-11-2-r14) |

验收等级和门槛见 [`docs/EVALUATION.md`](../../docs/EVALUATION.md) 和 [`docs/EVALUATION_CHECKLIST.md`](../../docs/EVALUATION_CHECKLIST.md)。
