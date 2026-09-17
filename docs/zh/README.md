# 中文教学入口 — 基因**功能**注释

> 中文讲概念、为什么与选路；**跑 DIAMOND/eggNOG/InterPro、写 METHODS** 用英文。

[English policy](../BILINGUAL.md) · [仓库首页](../../README.md)  
上游结构教学：[gene-structure-annotation `docs/zh/`](https://github.com/Xuzhen-Li/gene-structure-annotation/tree/main/docs/zh)

![功能注释简版主线](../figures/functional_spine.png)

读图：`proteins → F0 → 框架 F1 → merge →（加件）→ release`。Mercator/AHRD/NLR 是**加件**，不是第二套框架。

命名提醒：`pipeline/F2_eggnog.sh` 是默认 **F1 里的 eggNOG 一步**，不是快框分支 F2。详见 [编号对照](FAQ_入门.md)。

> 换作物对照：[植物三种模拟（结构仓）](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/zh/植物三种模拟.md) · 图 [`plant_sim_three_lines.png`](../figures/plant_sim_three_lines.png) · 本仓 [`examples/plant_sim/`](../../examples/plant_sim/)

<details>
<summary>进阶总览大图（可选，信息量大）</summary>

![功能注释进阶总览](../figures/functional_overview.png)

</details>

---

## 今天最短路径（先做这个）

| 步 | 打开 | 做什么 |
|----|------|--------|
| 1 | [01_什么是功能注释.md](01_什么是功能注释.md) | 给蛋白贴标签，不改 GFF 坐标 |
| 2 | [03_怎么开始跑.md](03_怎么开始跑.md) | 有 `proteins.faa` → `local.env` → `flow.py` → `my_fa_plan.md` |
| 3a | 读 plan + [FAQ 编号](FAQ_入门.md) + 磁盘/DB 清单 | **课堂默认可停这里**（无集群/无 IPS 也诚实） |
| 3b | [`../INSTALL_FUNCTIONAL.md`](../INSTALL_FUNCTIONAL.md) · 勾选 [`DB_INSTALL_CHECKLIST.md`](DB_INSTALL_CHECKLIST.md) | 有盘再装库 |
| 3c | 按 plan `RUN=1` 跑框架 F1 | diamond → `F2_eggnog.sh`（=F1 内步）→ IPS；见 [编号对照](FAQ_入门.md)。**上集群前必勾：** [Done when](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Start-tonight#done-when) + `python3 pipeline/print_qc_commands.py` 绿（无 `[STOP]`）；未勾 = **不许** `RUN=1` |
| 4 | [**验收勾选表**](验收勾选表.md) | 认清 **F-L1** 档位（≠今晚必交满跑） |

卡住再查：[04_F线怎么选](04_F线怎么选.md) · [12_常见翻车](12_常见翻车.md) · [99_术语表](99_术语表.md) · **[FAQ_入门.md](FAQ_入门.md)**（**先读 F 编号对照**）

**没有稳定 proteins？** 先回结构仓放行，再来本仓。

验收命令打印：`python3 pipeline/print_qc_commands.py`（需先 `source config/local.env`）。

<details>
<summary>英文操作入口（折叠）</summary>

[`START_HERE.md`](../START_HERE.md) · [`flow_tool/`](../../pipeline/flow_tool/) · [`TOOLS.md`](../TOOLS.md) · [`EVALUATION.md`](../EVALUATION.md)

</details>

---

## 完整课程（想系统学再按序）

| 顺序 | 文档 | 你学到什么 |
|------|------|------------|
| 0 | [00_为什么要做功能注释.md](00_为什么要做功能注释.md) | **WHY**：第二层；FA 修不了什么 |
| 1 | [01_什么是功能注释.md](01_什么是功能注释.md) | F1 三件套 |
| 2 | [02_和结构注释的关系.md](02_和结构注释的关系.md) | 先结构后功能；F0 |
| 3 | [03_怎么开始跑.md](03_怎么开始跑.md) | flow + local.env |
| 4 | [04_F线怎么选.md](04_F线怎么选.md) | 主干 / 替代 / 加件 |
| 5 | [05_F0蛋白BUSCO.md](05_F0蛋白BUSCO.md) | FA 前蛋白 BUSCO |
| 6 | [06_F1精讲_DIAMOND_eggNOG_IPS.md](06_F1精讲_DIAMOND_eggNOG_IPS.md) | 默认骨架 |
| 7 | [07_替代框架_F2F3F5.md](07_替代框架_F2F3F5.md) | 快框 / EnTAP / Trinotate |
| 8 | [08_植物加件_F4F6F8F9.md](08_植物加件_F4F6F8F9.md) | 植物加件 |
| 9 | [09_合并与放行.md](09_合并与放行.md) | master TSV + release |
| 10 | [10_验收_FL0_FL1.md](10_验收_FL0_FL1.md) | F-L0/F-L1 |
| 11 | [11_flow工具怎么用.md](11_flow工具怎么用.md) | answers → plan |
| 12 | [12_常见翻车.md](12_常见翻车.md) | 翻车清单 |
| 13–15 | [13](13_为什么F1是三件套.md) · [14](14_为什么先结构后功能.md) · [15](15_为什么版本和谱系必须写清.md) | WHY 深课 |
| — | （无课 16；跳到 17 是刻意留空，不是缺文件） |
| 17 | [外部教程与会议](17_外部教程与会议.md) | Galaxy / 会议 |
| 99 | [99_术语表.md](99_术语表.md) | 术语 |

> 课 00 / 13–15 是 **WHY 层**。操作与门禁仍以英文为准。


## 英文助手中文指针（3–5 行）

| 指针 | 对应英文 |
|------|----------|
| [DB_INSTALL_CHECKLIST.md](DB_INSTALL_CHECKLIST.md) | F1 装库勾选 |
| [golden_pack.md](golden_pack.md) | FA 放行包长什么样 |
| [MERCATOR_WHEN.md](MERCATOR_WHEN.md) | 何时用 Mercator 网页（F6） |

英文一页路径：[`../POST_STRUCTURE.md`](../POST_STRUCTURE.md)。

## 一句话自测

> 我有没有稳定的 `proteins.faa`（来自结构放行）？  
> 没有 → 先去结构仓。有 → 本仓 F1。
