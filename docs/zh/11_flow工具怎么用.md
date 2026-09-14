# flow 工具怎么用（功能）

英文：[`../FLOW_TOOL.md`](../FLOW_TOOL.md) · [`../../pipeline/flow_tool/README.md`](../../pipeline/flow_tool/README.md)

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
