# flow_tool (function) — step 1

Chinese short path: [`docs/zh/`](../../docs/zh/) (今天最短路径).

```bash
cd gene-function-annotation
cp pipeline/flow_tool/answers.example.yaml /tmp/fa_answers.yaml
python3 pipeline/flow_tool/flow.py --answers /tmp/fa_answers.yaml -o /tmp/fa_flow_plan.md
```

Upstream structure chooser: [gene-structure-annotation flow_tool](https://github.com/Xuzhen-Li/gene-structure-annotation/tree/main/pipeline/flow_tool).

Related: [`../../docs/TOOLS.md`](../../docs/TOOLS.md) · [`../../docs/START_HERE.md`](../../docs/START_HERE.md).

Honesty: this step writes a **plan**; it does not one-click InterProScan on your HPC.

Chinese: when reading the English plan body, see [`docs/zh/读plan.md`](../../docs/zh/读plan.md) · glossary [`docs/zh/99_术语表.md`](../../docs/zh/99_术语表.md) · FAQ [`docs/zh/FAQ_入门.md`](../../docs/zh/FAQ_入门.md).
