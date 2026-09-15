# Start here — gene **function**

**中文请从这里进：** [`zh/README.md`](zh/README.md)（今天最短路径）

You want **protein labels** (names / GO-ish / domains), not new exon coordinates.

1. Confirm you have `proteins.faa` from a structure release (TAG or hash).  
2. Flow tool → [`../pipeline/flow_tool/README.md`](../pipeline/flow_tool/README.md)  
3. Install DBs → [`INSTALL_FUNCTIONAL.md`](INSTALL_FUNCTIONAL.md) · per-tool pages → [`TOOLS.md`](TOOLS.md)  
4. Tick [`EVALUATION_CHECKLIST.md`](EVALUATION_CHECKLIST.md)  
   (Chinese: [`zh/验收勾选表.md`](zh/验收勾选表.md); full: [`EVALUATION.md`](EVALUATION.md))  
5. Optional: `python3 pipeline/print_qc_commands.py`

One-sentence test: *Do I already have stable proteins?*  
No → [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation). Yes → this repo (default **F1**).

Chinese FAQ (numbering + install): [`zh/FAQ_入门.md`](zh/FAQ_入门.md).

**Classroom minimum ≠ finish IPS tonight.** Class delivery is often: read the plan + FAQ numbering + list DBs/disk budget. Full InterProScan / eggNOG DB install is optional homework unless the instructor says otherwise.

Back to [`../README.md`](../README.md).
