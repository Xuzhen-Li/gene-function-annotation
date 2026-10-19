# F-aggregate — gene-level merged function table

[[TODO-TEXT]]

## Run

```bash
python3 pipeline/F_aggregate.py \
  --proteins "$PROTEINS_FA" \
  --ips "$FUNCTION_DIR/interpro/${FUN_PREFIX}_ips.tsv" \
  --emapper "$FUNCTION_DIR/emapper/${FUN_PREFIX}_fun.emapper.annotations" \
  --diamond-swissprot "$FUNCTION_DIR/diamond/swissprot.tsv" \
  --diamond-trembl "$FUNCTION_DIR/diamond/trembl.tsv" \
  --kofam "$FUNCTION_DIR/kofam/kofam.tsv" \
  --db-versions-file "$FUNCTION_DIR/db_versions.tsv" \
  --out "$FUNCTION_DIR/merge/merged_function_table.tsv"
```

Example with simulated inputs:

```bash
python3 pipeline/F_aggregate.py \
  --proteins testdata/function_aggregate/sim.faa \
  --ips testdata/function_aggregate/sim.ips.tsv \
  --emapper testdata/function_aggregate/sim.emapper.annotations \
  --diamond-swissprot testdata/function_aggregate/sim.diamond.swissprot.tsv \
  --diamond-trembl testdata/function_aggregate/sim.diamond.trembl.tsv \
  --kofam testdata/function_aggregate/sim.kofam.detail.txt \
  --db-versions-file testdata/function_aggregate/sim.db_versions.tsv \
  --out /tmp/merged_function_table.tsv
diff /tmp/merged_function_table.tsv testdata/function_aggregate/expected/merged_function_table.tsv
python3 -m pytest -q tests/test_aggregate.py
```

## Rules

| Item | Rule |
|------|------|
| `final_name` | Swiss-Prot (passing filters) → `similar to <X>`, X from InterProScan → eggNOG → TrEMBL (passing) → `uncharacterized protein` |
| `final_name_source` | `swissprot` / `interproscan` / `eggnog` / `trembl` / `none` |
| DIAMOND filters | `param_max_evalue`, `param_min_pident`, `param_min_qcov`, `param_min_scov` from `config/function_qc_thresholds.tsv`; `--max-evalue` / `--min-pident` / `--min-qcov` / `--min-scov` override |
| `diamond_*` | Swiss-Prot passing → TrEMBL passing → best failing hit (kept for QC) |
| `kofam_ko` | KofamScan rows marked `*` or score ≥ threshold; `eggnog_ko` is reported, not used as final KO |
| `go_terms` | union of `ips_go` + `eggnog_go`, deduplicated, sorted; `go_evidence` = `IEA` |
| `db_versions` | `tool=version@YYYY-MM-DD;...` from `--db-version` / `--db-versions-file` |
| Columns | `pipeline/schema/merged_function_table.tsv` |

[[TODO-TEXT]]
