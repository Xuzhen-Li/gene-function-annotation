# 中文教学入口 — 基因**功能**注释

> 中文讲概念、**为什么**与选路；**跑 DIAMOND/eggNOG/InterPro、写 METHODS** 用英文文档。

[English policy](../BILINGUAL.md) · [仓库首页](../../README.md)  
上游结构教学：[gene-structure-annotation `docs/zh/`](https://github.com/Xuzhen-Li/gene-structure-annotation/tree/main/docs/zh)

---

## 完整课程（建议按序）

| 顺序 | 文档 | 你学到什么 |
|------|------|------------|
| 0 | [00_为什么要做功能注释.md](00_为什么要做功能注释.md) | **WHY**：第二层；FA 修不了什么 |
| 1 | [01_什么是功能注释.md](01_什么是功能注释.md) | 功能层回答什么；F1 三件套 |
| 2 | [02_和结构注释的关系.md](02_和结构注释的关系.md) | 先结构后功能；F0 急刹车 |
| 3 | [03_怎么开始跑.md](03_怎么开始跑.md) | flow + local.env |
| 4 | [04_F线怎么选.md](04_F线怎么选.md) | 主干 / 替代框 / 加件 |
| 5 | [05_F0蛋白BUSCO.md](05_F0蛋白BUSCO.md) | 为何 FA 前再跑蛋白 BUSCO |
| 6 | [06_F1精讲_DIAMOND_eggNOG_IPS.md](06_F1精讲_DIAMOND_eggNOG_IPS.md) | 默认论文骨架逐步讲 |
| 7 | [07_替代框架_F2F3F5.md](07_替代框架_F2F3F5.md) | 快框 / EnTAP / Trinotate |
| 8 | [08_植物加件_F4F6F8F9.md](08_植物加件_F4F6F8F9.md) | AHRD、MapMan、NLR、iTAK、F7 |
| 9 | [09_合并与放行.md](09_合并与放行.md) | master TSV + release 包 |
| 10 | [10_验收_FL0_FL1.md](10_验收_FL0_FL1.md) | F-L0/F-L1 门禁（指针英文 EVALUATION） |
| 11 | [11_flow工具怎么用.md](11_flow工具怎么用.md) | answers → plan；print-first |
| 12 | [12_常见翻车.md](12_常见翻车.md) | DB 错配、假 CAFA、无 provenance… |
| 13 | [13_为什么F1是三件套.md](13_为什么F1是三件套.md) | **WHY**：DIAMOND+eggNOG+IPS；非 BLAST-only |
| 14 | [14_为什么先结构后功能.md](14_为什么先结构后功能.md) | **WHY**：provenance；灾难 F0；装饰坏模型 |
| 15 | [15_为什么版本和谱系必须写清.md](15_为什么版本和谱系必须写清.md) | **WHY**：eggNOG 配对；IPS 日期；BUSCO 谱系 |
| 99 | [99_术语表.md](99_术语表.md) | F 线 / emapper / master TSV… |

> 课 00 / 13–15 是 **WHY 层**；课 01–12 正文里也有短 `## 为什么`（含反例）。操作与门禁仍以英文为准。

## 英文操作

| 需要 | 打开 |
|------|------|
| flow 工具 | [`../../pipeline/flow_tool/`](../../pipeline/flow_tool/) |
| 安装库 | [`../INSTALL_FUNCTIONAL.md`](../INSTALL_FUNCTIONAL.md) |
| 合格标准 | [`../EVALUATION.md`](../EVALUATION.md) |
| 路线图 | [`../ROADMAP.md`](../ROADMAP.md) |
| 综述指针 | [`../REVIEWS.md`](../REVIEWS.md) |
| 上手 | [`../QUICKSTART.md`](../QUICKSTART.md) |

## 一句话自测

> 我有没有稳定的 `proteins.faa`（来自结构放行）？  
> 没有 → 先去结构仓。有 → 本仓 F1。
