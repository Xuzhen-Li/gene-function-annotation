# BUSCO — protein completeness (F0)

**Role in this repo:** protein-mode QC on `PROTEINS_FA` before spending InterProScan time.

Genome-mode / Asm1 BUSCO lives upstream in [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation).

## Get it
- https://busco.ezlab.org · bioconda `busco`  
- Download a lineage once for your clade (e.g. `eukaryota_odb10`, `viridiplantae_odb12`) — cache it.

## Protein mode (F0)
```bash
busco -i "$PROTEINS_FA" -l "${BUSCO_LINEAGE_PROTEIN:-eukaryota_odb10}"   -o prot_busco --out_path "$FUNCTION_DIR/qc" -m proteins -c "$THREADS"
```

## How to read scores
| Letter | Meaning |
|--------|---------|
| C | Complete |
| D | Duplicated (high → haplotigs / polyploid / isoforms) |
| F | Fragmented |
| M | Missing |

## Pitfalls
- Comparing different lineages across papers.  
- High D on proteins because you fed **all isoforms** — use one rep per gene.  
- Catastrophic Completeness → fix **structure** upstream before F1.
