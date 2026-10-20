# gene-function-annotation
[English](README.md)

## Overview

本仓库在基因结构注释完成后，为蛋白质序列分配名称、GO/KEGG通路和结构域等功能标签。流程仅在结构注释输出 `proteins.faa` 后开始。本工具不执行 BRAKER、软屏蔽、GFF 编辑或基因预测。上游基因模型由 [`gene-structure-annotation`](https://github.com/Xuzhen-Li/gene-structure-annotation) 处理。结构与功能的边界在 [structure `docs/BOUNDARY.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/BOUNDARY.md) 中定义。转座子软屏蔽和转座子库构建不属于功能注释环节。

中文教学：[`docs/zh/`](docs/zh/)（是什么，与结构的关系，怎么跑，F线）
英文操作：[`docs/BILINGUAL.md`](docs/BILINGUAL.md)
植物模拟：[`examples/plant_sim/`](examples/plant_sim/)（与结构 Vitis+NLR，Oryza plain F1，Solanum+Mercator 配对）

![Beginner spine](docs/figures/functional_spine.png)

命名说明：文件 `pipeline/F2_eggnog.sh` 是默认 F1 框架内的 eggNOG 步骤，而不是快速框架分支 F2。
今晚入门：[Wiki Start-tonight](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Start-tonight)（GitHub Wiki，不在克隆仓库中）。
离线课堂：[`docs/CLASSROOM_TONIGHT.md`](docs/CLASSROOM_TONIGHT.md)。
进度追踪：[Annotation board (Project #2)](https://github.com/users/Xuzhen-Li/projects/2)。

## Concepts

1. 框架 F1 / F2 / F3 / F5 指代你声明的完整注释框架。默认 F1 包含 DIAMOND、eggNOG 和 IPS。
2. 脚本 `F2_eggnog.sh` 是 F1 框架内部的 eggNOG 步骤，并非 F2 框架。
3. 工具卡片 F1a / F1b / F1c 对应上述 F1 的三个步骤的知识页面。
4. 门控 `Gate-F1` 等是发布的硬性检查点，不是框架选择。深入说明见 [`docs/zh/FAQ_入门.md`](docs/zh/FAQ_入门.md)。

## Usage

你必须已经具备蛋白质序列。如果没有，请先用结构注释仓库的 `flow_tool` 跑完，得到 GFF 和 `proteins.faa`。参考 [`docs/HANDOFF_STRUCTURE_TO_FUNCTION.md`](docs/HANDOFF_STRUCTURE_TO_FUNCTION.md)。

自动规划 FA 框架：

```bash
git clone https://github.com/Xuzhen-Li/gene-function-annotation.git
cd gene-function-annotation
cp pipeline/flow_tool/answers.example.yaml my_answers.yaml
# edit: prefer_fast? plant add-ons?
python3 pipeline/flow_tool/flow.py --answers my_answers.yaml -o my_fa_plan.md
```

初始设置时，完成 `my_fa_plan.md` 并列出数据库磁盘路径。此时不需要 InterProScan。在 [Wiki Concepts](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Concepts) 或离线文件 [`docs/zh/02_和结构注释的关系.md`](docs/zh/02_和结构注释的关系.md) 检查概念。分开填写 `grade=` 和 `status=`，不要写成 `status=F-L1`。

在集群执行时，必须在勾选 [Done when](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Start-tonight#done-when) 且 `python3 pipeline/print_qc_commands.py` 退出码为 0 并无 `[STOP]` 时才可继续。否则不要设置 `RUN=1`。使用 `--env config/example.env` 浏览时会显示 `[STOP]`，这是预期行为。METHODS 必填字段必须能够起草，见 [Wiki Evaluate-release](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Evaluate-release)。

按照 [`docs/INSTALL_FUNCTIONAL.md`](docs/INSTALL_FUNCTIONAL.md) 和 [`docs/DB_INSTALL_CHECKLIST.md`](docs/DB_INSTALL_CHECKLIST.md) 安装。然后对 F1 框架设置 `RUN=1` 并勾选 [`docs/EVALUATION_CHECKLIST.md`](docs/EVALUATION_CHECKLIST.md)。F-L1 是验收标准，而不是要求今晚必须完成 IPS。

```bash
cp config/example.env config/local.env
# set PROTEINS_FA to your structure release proteins (one representative per gene)
# set DIAMOND_DB, EGGNOG_*, INTERPROSCAN_HOME, BUSCO_LINEAGE_PROTEIN, …
```

<details>
<summary>Namespace details</summary>

存在四个命名空间，在 METHODS 中不要混淆。
框架：F1 / F2 / F3 / F5 指代完整的注释框架。默认 F1 为 DIAMOND+eggNOG+IPS。
脚本文件名：`F1_diamond.sh`、`F2_eggnog.sh`、`F3_interproscan.sh` 是 F1 框架内的步骤。
工具卡片：F1a / F1b / F1c 映射到三个知识页面。
门控：Gate-F1 至 Gate-F7 是涵盖数据来源、BUSCO、版本和行数等发布的硬性检查点。

中文参考见 [`docs/zh/FAQ_入门.md`](docs/zh/FAQ_入门.md)。
</details>

## Documentation

中文教学与入门：[`docs/zh/`](docs/zh/)
从这里开始：[`docs/START_HERE.md`](docs/START_HERE.md)

<details>
<summary>Additional documentation</summary>

流程工具：[`pipeline/flow_tool/`](pipeline/flow_tool/)
安装：[`docs/INSTALL_FUNCTIONAL.md`](docs/INSTALL_FUNCTIONAL.md)
安装检查表：[`docs/DB_INSTALL_CHECKLIST.md`](docs/DB_INSTALL_CHECKLIST.md)
评估检查表：[`docs/EVALUATION_CHECKLIST.md`](docs/EVALUATION_CHECKLIST.md)
结构注释之后：[`docs/POST_STRUCTURE.md`](docs/POST_STRUCTURE.md)
阶段输入输出：[`docs/STAGE_IO.md`](docs/STAGE_IO.md)
路线图：[`docs/ROADMAP.md`](docs/ROADMAP.md)
工具指南：[`docs/TOOLS.md`](docs/TOOLS.md)
工具文档：[`docs/tools/`](docs/tools/)
评估规则：[`docs/EVALUATION.md`](docs/EVALUATION.md)
质控方法与文献：[`docs/QUALITY_SOURCES.md`](docs/QUALITY_SOURCES.md)
操作演练：[`docs/QUICKSTART.md`](docs/QUICKSTART.md)
Mercator4 网页版：[`docs/MERCATOR_WHEN.md`](docs/MERCATOR_WHEN.md)
教程：[`docs/TUTORIALS_AND_MEETINGS.md`](docs/TUTORIALS_AND_MEETINGS.md)
近期高质量资源：[`docs/RECENT_HIGH_QUALITY.md`](docs/RECENT_HIGH_QUALITY.md)

</details>

<details>
<summary>Overview figure</summary>

![overview](docs/figures/functional_overview.png)

</details>

作者：李旭真，[ORCID](https://orcid.org/0000-0003-3670-6657)