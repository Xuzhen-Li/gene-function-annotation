# AHRD — human-readable descriptions

**Role:** F4 — concise protein names from BLAST/DIAMOND (+ domain) evidence (HR HSE-style METHODS).

**Software:** [groupschoof/AHRD](https://github.com/groupschoof/AHRD)

## Inputs from this playbook

- `$FUNCTION_DIR/diamond/swissprot.tsv` (F1.1)
- `$FUNCTION_DIR/interpro/vitis_ips.tsv` (F1.3, optional but better)

## Outputs

- `$FUNCTION_DIR/ahrd/ahrd_output.csv` (or TSV with description column)
- Join: `pipeline/F4_join_ahrd.py` → `merged_function_table.with_ahrd.tsv`

## Notes

Follow upstream AHRD YAML example; point BLAST/DIAMOND tabular hits at Swiss-Prot.
After join, release with `pipeline/F_release.sh`.
