# 流程索引

[English](README.md) · [首页](../../README.zh.md) · [知识地图](../KNOWLEDGE_MAP.zh.md)

本仓库是知识库，流程是贯穿其中的一条参考路线，配有小型示例脚本。本页说明每个流程问题以哪一页为准，其他页面中重复的内容按副本理解。

## 一句话路线

蛋白输入质控（F0）→ 框架 F1：DIAMOND 比对 Swiss-Prot、eggNOG-mapper、InterProScan → 可选加件（F4、F6–F9）→ 合并成 `merged_function_table.tsv` → 功能质控（F10）→ 发布。

![路线图](../figures/guide/function_route_map_v2.png)

## 以哪一页为准

| 问题 | 以此为准 | 重复或讲解它的页面 |
|---|---|---|
| 步骤顺序、框架与加件 | [`docs/ROADMAP.md`](../ROADMAP.md) | README 使用方法；[`catalog/_namespaces.md`](../../catalog/_namespaces.md)；书第 18 章 |
| 按你的数据选出的路线 | 由 [`pipeline/flow_tool/flow.py`](../../pipeline/flow_tool/flow.py) 根据你的回答生成的 `my_fa_plan.md` | README 使用方法 |
| 每个阶段的输入输出 | [`docs/STAGE_IO.md`](../STAGE_IO.md) | [`pipeline/00_overview.md`](../../pipeline/00_overview.md) |
| 各工具的命令 | [`docs/TOOLS.md`](../TOOLS.md) 和 [`pipeline/`](../../pipeline/00_overview.md) 中的脚本 | `docs/tools/`、`docs/notes/` |
| 结果是否合格 | [`docs/EVALUATION.md`](../EVALUATION.md) | [`docs/EVALUATION_CHECKLIST.md`](../EVALUATION_CHECKLIST.md)；判据类知识单元 |
| 安装工具和数据库 | [`docs/INSTALL_FUNCTIONAL.md`](../INSTALL_FUNCTIONAL.md) | [`docs/DB_INSTALL_CHECKLIST.md`](../DB_INSTALL_CHECKLIST.md) |
| 结构与功能之间的交接 | [`docs/HANDOFF_STRUCTURE_TO_FUNCTION.md`](../HANDOFF_STRUCTURE_TO_FUNCTION.md) | README 使用方法 |
| 第一次走一遍 | [`docs/QUICKSTART.md`](../QUICKSTART.md) | [`docs/START_HERE.md`](../START_HERE.md) |

## 旧的流程页面

以下页面作为记录保留；与上面所列页面不一致时，以上面所列为准。

- [`docs/CLASSROOM_TONIGHT.md`](../CLASSROOM_TONIGHT.md) 和 Wiki 页面 Start-tonight：早期的快速开始。
- [`docs/ROADMAP.md`](../ROADMAP.md) 末尾带日期的进度小节：各自日期的进度记录。
- [`catalog/`](../../catalog/README.md) 阶段文件夹中的步骤卡片：2026-11 首批，见 [`docs/kb/NUMBERING.zh.md`](../kb/NUMBERING.zh.md)。
- [`docs/STAGE_IO.md`](../STAGE_IO.md) 把 `F2_eggnog.sh` 和 `F3_interproscan.sh` 简写为 F1 的步骤；完整说法见 [`catalog/_namespaces.md`](../../catalog/_namespaces.md)。
