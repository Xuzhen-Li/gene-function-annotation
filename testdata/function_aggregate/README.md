# Simulated inputs for `pipeline/F_aggregate.py`

[[TODO-TEXT]]

| File | Format |
|------|--------|
| `sim.faa` | proteins FASTA (fake IDs `FAKE_g0001`–`FAKE_g0007`) |
| `sim.ips.tsv` | InterProScan TSV |
| `sim.emapper.annotations` | eggNOG-mapper v2 annotations |
| `sim.diamond.swissprot.tsv` / `sim.diamond.trembl.tsv` | DIAMOND outfmt 6 (`F1_diamond.sh` columns + `qlen slen`) |
| `sim.kofam.detail.txt` | KofamScan detail |
| `sim.db_versions.tsv` | tool / version / date |
| `expected/merged_function_table.tsv` | expected output |

Run: see [`../../docs/steps/functional/F_AGGREGATE.md`](../../docs/steps/functional/F_AGGREGATE.md).
