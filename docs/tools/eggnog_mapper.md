# eggNOG-mapper — orthology-aware transfer (F1 step / optional fast frame)

**Role in this playbook**
- **Default frame F1:** second of three tools (after DIAMOND, before InterProScan).  
- **Fast frame F2:** can be the main engine when IPS is deferred (label release **F-L0** unless you still complete IPS).  
- Helper script name is historical: [`../../pipeline/F2_eggnog.sh`](../../pipeline/F2_eggnog.sh) — **not** “you are on framework F2” by itself.

**Get it:** eggNOG-mapper docs / Singularity image · data pack must match **major** version (v3 ↔ eggNOG v7).  
Check: `emapper.py --version`.

## What it needs

| Input | `local.env` |
|-------|-------------|
| Proteins (1 / gene) | `PROTEINS_FA` |
| Data directory | `EGGNOG_DATA_DIR` |
| Tax scope | `EGGNOG_TAX_SCOPE` (plants often `Viridiplantae` or `auto`) |
| Optional image | `EGGNOG_SIF` |

## Command pattern

```bash
# print-first helper (writes under $FUNCTION_DIR/emapper/):
bash pipeline/F2_eggnog.sh          # DRY
RUN=1 bash pipeline/F2_eggnog.sh    # execute
```

Expected product: `$FUNCTION_DIR/emapper/${FUN_PREFIX}_fun.emapper.annotations` (exact suffix may vary by version).

## Outputs → merge

`F_merge_tables.py --emapper …annotations` pulls description / GOs / KEGG / PFAMs into `functional_master.tsv`.  
Do not treat emapper GO as CAFA-grade accuracy.

## Pitfalls

- emapper v3 binary + wrong-generation DB (or v2 + v7 data).  
- Running on TE-inflated ORFs that never passed structure QC.  
- Calling the run “framework F2” just because the script is named `F2_*.sh` while you still intend full F1.

Chinese FAQ: [`../zh/FAQ_入门.md`](../zh/FAQ_入门.md).
