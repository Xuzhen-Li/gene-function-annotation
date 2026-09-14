# flow 工具怎么用（功能）

英文：[`../FLOW_TOOL.md`](../FLOW_TOOL.md) · [`../../pipeline/flow_tool/README.md`](../../pipeline/flow_tool/README.md)

## 为什么

1. FA 框选错（F2 当 F1）的 METHODS 成本很高。  
2. 计划书强迫写清 F0→框→加件→merge→release。  
3. 与结构 flow 分工：上游选 S，本仓选 F。  
4. Print-first 助手适配本地 DB 布局。  
5. 不宣称一键投递整条 FA — 边界诚实。

**反例：** 未改 answers 就默认植物加件全开，目录空着却写进 stub。
## Step 1：答题 → 选框 → 讲解计划

```bash
cd gene-function-annotation
cp pipeline/flow_tool/answers.example.yaml fa_answers.yaml
# 编辑：是否植物加件、能否等 IPS、是否转录组…
python3 pipeline/flow_tool/flow.py --answers fa_answers.yaml -o fa_flow_plan.md
```

计划会叙述 F0 → 主框（F1 或替代）→ 可选加件 → merge → release 的输入/目的/输出。

## 诚实边界

| 已有 | 仍靠现有助手 |
|------|----------------|
| 自动选 F 框 + 中文/英文可读讲解 | `F1_diamond.sh` / `F2_eggnog.sh` / `F3_interproscan.sh` 等 **print-first** 执行 |
| 与 ROADMAP 一致的 chooser | 一键投递整条 FA 到集群（未宣称） |

结构上游选路：[gene-structure-annotation flow_tool](https://github.com/Xuzhen-Li/gene-structure-annotation/tree/main/pipeline/flow_tool)。

下一页：[12_常见翻车.md](12_常见翻车.md)
