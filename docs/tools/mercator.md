# Mercator4 / MapMan4

**Role:** F6 — plant pathway BINs for figures and pathway enrichment.

**Citation:** Schwacke et al. *Molecular Plant* 2019 doi:10.1016/j.molp.2019.01.003

## In this playbook

1. Upload `$PROTEINS_FA` at the Mercator4 web service (Plabipd).  
2. Download results → `$FUNCTION_DIR/mercator/mercator_results.txt`.  
3. Ingest:

```bash
python3 "$REPO_ROOT/pipeline/F6_ingest_mercator.py" \
  --master "$FUNCTION_DIR/merge/functional_master.tsv" \
  --mercator-dir "$FUNCTION_DIR/mercator" \
  --out "$FUNCTION_DIR/merge/functional_master.with_mapman.tsv"
```

Scenario **F6**. Record job date in METHODS.

**When to open the web vs skip:** [`../MERCATOR_WHEN.md`](../MERCATOR_WHEN.md).
