# 第 20 章 实例：葡萄蛋白走 F1 框架加 F8 加件

本章按 [`examples/plant_sim/01_vitis_s1_s7/plan.md`](../../examples/plant_sim/01_vitis_s1_s7/plan.md) 的教学计划走一遍。蛋白来自模拟的葡萄结构发布版（Vitis_sim.v0.1，自报结构等级 L1）；重点是决策顺序，不是真实数字。

## 20.1 框架选择

流程工具选 F1 框架（DIAMOND、eggNOG-mapper 和 InterProScan），加上 F8 处理 NLR 候选，目标等级 F-L1。加件是可选的，不是 F-L1 的门槛。

## 20.2 各阶段

| 序号 | 阶段 | 工具 | 产出 | 为什么 |
|---|---|---|---|---|
| 1 | F0 蛋白检查 | BUSCO 蛋白模式 | 带谱系的 BUSCO 汇总 | 结果很差就退回结构注释（[doi:10.1093/molbev/msab199](https://doi.org/10.1093/molbev/msab199)） |
| 2 | F1a 相似性 | DIAMOND 比 Swiss-Prot | `function/diamond/` | 校对库匹配给出的名称错误率最低（[doi:10.1371/journal.pcbi.1000605](https://doi.org/10.1371/journal.pcbi.1000605)） |
| 3 | F1b 直系同源 | eggNOG-mapper，EGGNOG_TAX_SCOPE 设为所属类群 | `function/emapper/` | 通过直系同源转移 GO、KEGG 和 COG（[doi:10.1093/molbev/msab293](https://doi.org/10.1093/molbev/msab293)） |
| 4 | F1c 特征签名 | InterProScan | `function/interpro/` | 结构域、位点和成员数据库签名（[doi:10.1093/nar/gkae1082](https://doi.org/10.1093/nar/gkae1082)） |
| 5 | 合并 | `pipeline/F_merge_tables.py` | `merged_function_table.tsv` | 每个基因一行；行数接近蛋白数 |
| 6 | F8 NLR 初筛 | InterProScan 过滤，可选 HRP | `nlr_candidates.tsv` | 抗病基因窗口的候选；用 `pipeline/F8b_nlr_to_families.py` 转换后可回馈结构叠加层 S7 |
| 7 | 发布 | `pipeline/F_release.sh` | `function/release/<TAG>/` | 门槛 F-L0 和 F-L1 见 `docs/EVALUATION.md` |

## 20.3 要点

- F1 的三个工具给出三种独立证据，这就是 F1 作为默认的原因。
- 脚本名和框架名不同：`F2_eggnog.sh` 是 F1 框架的第 2 步，不是快速框架 F2。
- F8 的产出是候选列表，不是人工校对的 NLR 集；可以回到结构注释做校对。
- 另外两个例子见 `examples/plant_sim/02_oryza_s1/` 和 `examples/plant_sim/03_solanum_s11/`。
