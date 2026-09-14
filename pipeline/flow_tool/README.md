# flow_tool (function) — step 1

```bash
cd gene-function-annotation
cp pipeline/flow_tool/answers.example.yaml /tmp/fa_answers.yaml
python3 pipeline/flow_tool/flow.py --answers /tmp/fa_answers.yaml -o /tmp/fa_flow_plan.md
```

Upstream structure chooser: [gene-structure-annotation flow_tool](https://github.com/Xuzhen-Li/gene-structure-annotation/tree/main/pipeline/flow_tool).
