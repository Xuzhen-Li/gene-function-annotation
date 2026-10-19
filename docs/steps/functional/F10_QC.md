# F10 quality assessment

The script reads the merged gene table to report metrics for InterProScan, eggNOG, DIAMOND, and KofamScan. Every threshold is a rule of thumb. Compare the numbers with a close relative species annotated the same way. A homology hit does not prove function. A warn status means you should look closer. The name source check accepts both the Swiss-Prot name and the next source for a rounded DIAMOND boundary case. The DIAMOND pass share uses a strict comparison instead. Rows with only InterPro IDs and no useful domain description can have a source of none or interproscan_domain.

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

- `results/F10/function_qc_summary.tsv`: The summary file has columns for metric, value, threshold, status, threshold_label, and k_n. The k_n column shows the raw count behind a share to explain the status. This column is empty for metrics that are not shares. The status column shows pass, warn, na, or info. The script judges the status on the raw value instead of the rounded number.
- `results/F10/function_qc_summary.conflicts.tsv`: This file lists the gene_id, conflict, side_a, and side_b columns. It flags genes where the eggNOG KO and KofamScan KO share no KO, or where the eggNOG name shares no word with the Pfam domain text.

## Test

```bash
python3 -m unittest discover -s tests -v
```
