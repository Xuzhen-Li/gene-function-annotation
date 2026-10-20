# Toy functional inputs (no databases required)

This toy data contains two genes. A toy dataset is a small example used only for testing. The first gene, geneA, has an InterProScan NB-ARC hit for Pfam PF00931, one eggNOG-mapper annotation, and one DIAMOND hit against Swiss-Prot. The second gene, geneB, has no hits at all.

<!-- Facts for writer (not finished prose):
- 2 genes: geneA (InterProScan NB-ARC, eggNOG, passing Swiss-Prot DIAMOND hit) and geneB (no hits).
- toy.diamond.tsv uses the F1_diamond.sh columns (... stitle qlen slen qcovhsp scovhsp).
- F_merge_tables.py is a deprecated wrapper that calls F_aggregate.py; both commands
  below give the same file as expected/merged_function_table.tsv.
- tests/test_function_fixes.py checks this automatically.
- Not for biological conclusions.
-->

```bash
python3 pipeline/F_aggregate.py \
  --proteins testdata/function/toy.faa \
  --emapper testdata/function/toy.emapper.annotations \
  --ips testdata/function/toy.ips.tsv \
  --diamond-swissprot testdata/function/toy.diamond.tsv \
  --out /tmp/toy_out/merged_function_table.tsv
diff /tmp/toy_out/merged_function_table.tsv testdata/function/expected/merged_function_table.tsv && echo "[OK] matches expected"
```

Legacy command (still works, prints a deprecation note):

```bash
python3 pipeline/F_merge_tables.py \
  --proteins testdata/function/toy.faa \
  --emapper testdata/function/toy.emapper.annotations \
  --ips testdata/function/toy.ips.tsv \
  --diamond testdata/function/toy.diamond.tsv \
  --out /tmp/toy_out/merged_function_table.tsv
```
