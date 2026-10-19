# F10 quality assessment

This script reads the merged gene table to check the annotation quality. It calculates metrics for InterProScan, eggNOG-mapper, DIAMOND, and KofamScan results. Every threshold is a rule of thumb. You should compare the numbers with a close relative species annotated the same way. A homology hit does not prove function. A warn status means you should look closer.

## Input

- `--merged`: This file must have one row per gene and all 24 columns. The script stops with an error if one column is missing. (columns: `pipeline/schema/merged_function_table.tsv`)
- `--relative`: This optional file is the same kind of table for a close relative species. It only needs the gene_id, final_name, kofam_ko, and eggnog_ko columns.
- `--thresholds`: `config/function_qc_thresholds.tsv` This file holds every threshold. Every threshold is a rule of thumb.

## Run

```bash
python3 pipeline/F10_function_qc.py \
  --merged testdata/function_qc/merged.sim.tsv \
  --relative testdata/function_qc/relative.sim.tsv \
  --out results/F10/function_qc_summary.tsv
```

## Output

- `results/F10/function_qc_summary.tsv`: [[TODO-TEXT]]
- `results/F10/function_qc_summary.conflicts.tsv`: This file lists the gene_id, conflict, side_a, and side_b columns. It flags genes where the eggNOG KO and KofamScan KO share no KO, or where the eggNOG name shares no word with the Pfam domain text.

## Test

```bash
python3 -m unittest discover -s tests -v
```
