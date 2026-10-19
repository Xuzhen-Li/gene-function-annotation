# F-aggregate — gene-level merged function table

This script merges outputs from InterProScan, eggNOG-mapper, DIAMOND, and KofamScan. The output is one table with 24 columns and one row per protein. The final name uses a passing Swiss-Prot hit first. The script tries an eggNOG-mapper name next and an InterProScan domain last. TrEMBL hits never name a gene. You should run the quality check step after this step finishes.

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
| `final_name` | 1. Swiss-Prot hit passing all DIAMOND filters (e-value, identity, query **and** subject coverage) → its name; 2. eggNOG `Preferred_name` → `similar to <name>`; 3. InterProScan domain (Pfam → SMART → ProSiteProfiles → CDD signature, else InterPro entry) → `<domain> domain-containing protein`; 4. `uncharacterized protein`. TrEMBL never names a gene |
| `final_name_source` | `swissprot` / `eggnog` / `interproscan_domain` / `none` |
| DIAMOND filters | `param_max_evalue`, `param_min_pident`, `param_min_qcov`, `param_min_scov` from `config/function_qc_thresholds.tsv`; `--max-evalue` / `--min-pident` / `--min-qcov` / `--min-scov` override |
| `diamond_*` | Swiss-Prot passing → TrEMBL passing → best failing hit (kept for QC) |
| `kofam_ko` | KofamScan rows marked `*` or score ≥ threshold; `eggnog_ko` is reported, not used as final KO |
| `go_terms` | union of `ips_go` + `eggnog_go` (suffixes such as `(InterPro)` / `(PANTHER)` stripped), deduplicated, sorted; `go_evidence` = `IEA` |
| `go_source` | `GO:xxxxxxx=interproscan,eggnog;...` — one entry per term in `go_terms` order |
| DIAMOND input | needs `qlen` (or `--proteins`) and `slen`; otherwise the step stops with an error |
| `db_versions` | `tool=version@YYYY-MM-DD;...` from `--db-version` / `--db-versions-file` |
| Columns | `pipeline/schema/merged_function_table.tsv` + `go_source` after `go_evidence` |

Every threshold is a rule of thumb. You should compare the numbers with a close relative species annotated the same way. A homology hit does not prove function. GO terms here are IEA electronic inferences that no person checked.
