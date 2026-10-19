# Simulated inputs for `pipeline/F_aggregate.py`

These simulated inputs contain deliberate edge cases to test the naming logic. Some proteins have only TrEMBL hits and remain uncharacterized. You can compare your output table with the expected file using diff. No difference means the script worked correctly. The quality check gives warnings on this small dataset without failing the format checks.

<!-- Facts for writer (not finished prose):
- 7 genes (FAKE_g0001-FAKE_g0007); 4 are deliberate edge cases:
  FAKE_g0006 no source at all; FAKE_g0004 and FAKE_g0005 TrEMBL-only (never named by TrEMBL);
  FAKE_g0003 eggNOG without a preferred name.
- Naming branches shown: swissprot (g0001), eggnog "similar to" (g0002),
  interproscan_domain (g0007), none (g0003-g0006).
- Under F10 (pipeline/F10_function_qc.py) the expected output intentionally shows 5 warns
  alongside passes: coverage_interproscan, coverage_eggnog, coverage_kofam,
  share_hypothetical, share_ge2_tools_agree.
- The warns are dataset-level coverage / naming shares, not format errors; all format checks
  (GO IEA, go_source, db_versions, name-source consistency) pass.
-->

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
