# 中文教学入口 — 基因**功能**注释

> 中文讲概念、为什么与选路；**跑 DIAMOND/eggNOG/InterPro、写 METHODS** 用英文。

[English policy](../BILINGUAL.md) · [仓库首页](../../README.md)  
上游结构教学：[gene-structure-annotation `docs/zh/`](https://github.com/Xuzhen-Li/gene-structure-annotation/tree/main/docs/zh)

---

## 今天最短路径（先做这个）

| 步 | 打开 | 做什么 |
|----|------|--------|
| 1 | [01_什么是功能注释.md](01_什么是功能注释.md) | 搞清：本仓给蛋白贴标签，不改 GFF 坐标 |
| 2 | [03_怎么开始跑.md](03_怎么开始跑.md) | 确认已有 `proteins.faa` → `flow.py` → `my_fa_plan.md` |
| 3 | [`../INSTALL_FUNCTIONAL.md`](../INSTALL_FUNCTIONAL.md) → 跑 F1 → [`../EVALUATION.md`](../EVALUATION.md) | 默认 **F1** 三件套 |

卡住再查：[04_F线怎么选](04_F线怎么选.md) · [12_常见翻车](12_常见翻车.md) · [99_术语表](99_术语表.md)

**没有稳定 proteins？** 先回结构仓放行，再来本仓。

**英文操作入口：** [`../../pipeline/flow_tool/`](../../pipeline/flow_tool/) · [`../INSTALL_FUNCTIONAL.md`](../INSTALL_FUNCTIONAL.md) · [`../EVALUATION.md`](../EVALUATION.md)

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
| 17 | [外部教程与会议](17_外部教程与会议.md) | Galaxy / 会议 |
| 99 | [99_术语表.md](99_术语表.md) | 术语 |

> 课 00 / 13–15 是 **WHY 层**。操作与门禁仍以英文为准。

## 一句话自测

> 我有没有稳定的 `proteins.faa`（来自结构放行）？  
> 没有 → 先去结构仓。有 → 本仓 F1。
