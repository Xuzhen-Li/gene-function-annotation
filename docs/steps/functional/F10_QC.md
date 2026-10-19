# F10 quality assessment

[[TODO-TEXT]]

## Input

- `--merged`: [[TODO-TEXT]] (columns: `pipeline/schema/merged_function_table.tsv`)
- `--relative`: [[TODO-TEXT]]
- `--thresholds`: `config/function_qc_thresholds.tsv` [[TODO-TEXT]]

## Run

```bash
python3 pipeline/F10_function_qc.py \
  --merged testdata/function_qc/merged.sim.tsv \
  --relative testdata/function_qc/relative.sim.tsv \
  --out results/F10/function_qc_summary.tsv
```

## Output

- `results/F10/function_qc_summary.tsv`: [[TODO-TEXT]]
- `results/F10/function_qc_summary.conflicts.tsv`: [[TODO-TEXT]]

## Test

```bash
python3 -m unittest discover -s tests -v
```
