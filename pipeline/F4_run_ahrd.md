# F4 — run AHRD then join

After F1.1 DIAMOND (and ideally F1.3 InterProScan):

1. Build AHRD input YAML/CSV per [`docs/tools/ahrd.md`](../docs/tools/ahrd.md) using:
   - `$FUNCTION_DIR/diamond/swissprot.tsv`
   - `$FUNCTION_DIR/interpro/${FUN_PREFIX:-ann}_ips.tsv` (if present)
2. Run AHRD → `$FUNCTION_DIR/ahrd/ahrd_output.csv` (or `.tsv`)
3. Join:

```bash
python3 "$REPO_ROOT/pipeline/F4_join_ahrd.py" \
  --master "$FUNCTION_DIR/merge/merged_function_table.tsv" \
  --ahrd "$FUNCTION_DIR/ahrd/ahrd_output.csv" \
  --out "$FUNCTION_DIR/merge/merged_function_table.with_ahrd.tsv"
bash "$REPO_ROOT/pipeline/F_release.sh"
```
