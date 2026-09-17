# Start here — gene **function**

**中文请从这里进：** [`zh/README.md`](zh/README.md)（今天最短路径）

**Tonight:** [Wiki Start-tonight](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Start-tonight) (not in clone) · offline [`CLASSROOM_TONIGHT.md`](CLASSROOM_TONIGHT.md).

**F cheat:** Framework F1 ≠ script `F2_eggnog.sh` ≠ TOOLS F1b ≠ Gate-F* — see root README · FAQ [`zh/FAQ_入门.md`](zh/FAQ_入门.md).

You want **protein labels** (names / GO-ish / domains), not new exon coordinates.

1. Confirm you have `proteins.faa` from a structure release (TAG or hash).  
2. Flow tool → [`../pipeline/flow_tool/README.md`](../pipeline/flow_tool/README.md)  
3. Install DBs → [`INSTALL_FUNCTIONAL.md`](INSTALL_FUNCTIONAL.md) · tick [`DB_INSTALL_CHECKLIST.md`](DB_INSTALL_CHECKLIST.md) · per-tool → [`TOOLS.md`](TOOLS.md)  
4. Tick [`EVALUATION_CHECKLIST.md`](EVALUATION_CHECKLIST.md)  
   (Chinese: [`zh/验收勾选表.md`](zh/验收勾选表.md); full: [`EVALUATION.md`](EVALUATION.md))  
5. Optional: `python3 pipeline/print_qc_commands.py`
6. One-page after structure: [`POST_STRUCTURE.md`](POST_STRUCTURE.md)

One-sentence test: *Do I already have stable proteins?*  
No → [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation). Yes → this repo (default **F1**).

Chinese FAQ (numbering + install): [`zh/FAQ_入门.md`](zh/FAQ_入门.md).

**Classroom minimum ≠ finish IPS tonight.** Class delivery is often: read the plan + FAQ numbering + list DBs/disk budget. Write `grade=` and `status=` separately — never `status=F-L1`.

**When ready for `RUN=1`:** tick [Done when](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Start-tonight#done-when) **and** `python3 pipeline/print_qc_commands.py` exits 0 with **no** `[STOP]`. Otherwise **no** `RUN=1` / no cluster. Full InterProScan / eggNOG DB install is optional homework unless the instructor says otherwise.

Back to [`../README.md`](../README.md).
