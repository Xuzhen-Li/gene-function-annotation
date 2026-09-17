# Classroom tonight (function) — offline mirror

GitHub Wiki [Start-tonight](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Start-tonight) is **not** in the clone. Short checklist only — not a full Wiki copy.

## Done when

- [ ] You generated and **read** `my_fa_plan.md`.
- [ ] DB paths in `local.env` are listed **or** honestly left empty for tonight.
- [ ] You can say one line: write `grade=` and `status=` separately (never `status=F-L1`); name `frame=F1` (or waiver).

## Submit tonight

**Deliverable:** `my_fa_plan.md` only (± DB path list in `local.env`).  
Do **not** claim F-L1 / finished InterProScan.

## `print_qc` `[STOP]` — expected on example.env

```bash
python3 pipeline/print_qc_commands.py --env config/example.env
```

`[STOP]` / exit 1 with placeholders is **expected**, not a broken printer.  
Before any `RUN=1`: real `local.env` + exit 0 with **no** `[STOP]` + Wiki Done when (or this page) ticked.

## Concepts oral (pick one)

- Wiki: [Concepts](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Concepts)
- Offline: [`zh/02_和结构注释的关系.md`](zh/02_和结构注释的关系.md) — structure≠function; FA domains/GO≠model proof; F8≠NLR census

F-number cheat: root README · deep dive [`zh/FAQ_入门.md`](zh/FAQ_入门.md).
