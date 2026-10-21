# Stage I/O — functional annotation

Beginner path: [`QUICKSTART.md`](QUICKSTART.md).  
Upstream structure products: [gene-structure-annotation STAGE_IO](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/STAGE_IO.md).

## Big picture

| In | Out |
|----|-----|
| `PROTEINS_FA` (+ optional GFF for locus context) | `merged_function_table.tsv` |
| Tool databases (Swiss-Prot, eggNOG, InterPro) | Per-tool TSVs under `$FUNCTION_DIR/` |
| | `release/<TAG>/` package + METHODS stub |

## Stages

| Stage | Input | Helper | Output | Check |
|-------|-------|--------|--------|-------|
| **F0** | `PROTEINS_FA` | BUSCO proteins | `$FUNCTION_DIR/qc/` | Completeness + lineage named |
| **F1 DIAMOND** | proteins + `DIAMOND_DB` | `F1_diamond.sh` | `diamond/swissprot.tsv` | Rows > 0; spot-check stitle |
| **F1 eggNOG** | proteins | `F2_eggnog.sh` | `emapper/*` | Names/GO for controls |
| **F1 InterPro** | proteins | `F3_interproscan.sh` | `interpro/*` | Domains for controls |
| **Merge** | the three TSVs | `F_merge_tables.py` | `merge/merged_function_table.tsv` | One row/gene |
| **Aggregate** | IPS + eggNOG + DIAMOND (Swiss-Prot/TrEMBL) + KofamScan | `F_aggregate.py` | `merge/merged_function_table.tsv` | One row per protein. Stop on duplicate ID or missing DIAMOND lengths. |
| **F4** optional | master + BLAST-ish | AHRD helpers | master + readable names | Names improved, not hallucinated |
| **F6/F8/F9** optional | proteins / master | Mercator / NLR / iTAK | side tables | Plant METHODS only when needed |
| **Release** | master + proteins | `F_release.sh` | `release/<TAG>/` | METHODS versions filled |

## Not produced here

- New gene models / GFF exon fixes → structure repo  
- Automatic GFF column-9 GO write-back → not default  

## Suggested layout

```text
$FUNCTION_DIR/
  diamond/  emapper/  interpro/  merge/  qc/  release/<TAG>/
```
