# Flow tool — progressive automation (FA)

```bash
cp pipeline/flow_tool/answers.example.yaml fa_answers.yaml
python3 pipeline/flow_tool/flow.py --answers fa_answers.yaml -o fa_flow_plan.md
```

Step 1 = auto frame + narration. Execution of DIAMOND/IPS remains via existing `pipeline/F*.sh` helpers.

Structure upstream: [structure flow_tool](https://github.com/Xuzhen-Li/gene-structure-annotation/tree/main/pipeline/flow_tool).

Related: [`TOOLS.md`](TOOLS.md) · [`START_HERE.md`](START_HERE.md) · [`EVALUATION_CHECKLIST.md`](EVALUATION_CHECKLIST.md).
