# Chapter 19. Pitfalls and quality control

## 19.1 Pitfalls the repository already names

These come from the README section Data needed alongside the proteins and from `docs/EVALUATION.md`.

- No gene finding, soft-masking, TE library or GFF editing happens here; those belong to gene-structure-annotation or vitis-te.
- Four ID sets must stay distinct in METHODS: frame (F1, F2, F3, F5), script file (`F2_eggnog.sh` is a step inside frame F1), tool card (F1a, F1b, F1c) and gate (Gate-F1 to F7).
- The merge product is `merged_function_table.tsv`; machine-predicted GO and EC stay IEA.
- Frame F7 annotates orthogroup representatives, not each gene.
- Structure in Foldseek, DeepFRI or AlphaFold DB means protein 3D structure.
- InterProScan is part of default F1 but slow; F-L1 is an acceptance bar, not a deadline.
- Optional plant add-ons (F4, F6, F8, F9) do not raise the grade by themselves.
- Enrichment needs a defined background, normally the full release gene set.

## 19.2 Pitfalls from the literature

- **Overprediction.** Transferring a specific molecular function from a weak hit is the most common error type in enzyme superfamilies; curated Swiss-Prot had near 0 percent errors while NR, TrEMBL and KEGG averaged 5 to 63 percent ([doi:10.1371/journal.pcbi.1000605](https://doi.org/10.1371/journal.pcbi.1000605)). Prefer curated hits and keep evidence codes.
- **Cellular component is hard.** CAFA3 saw no improvement for cellular component predictions ([doi:10.1186/s13059-019-1835-8](https://doi.org/10.1186/s13059-019-1835-8)); use dedicated targeting tools (SignalP, TargetP, DeepLoc) for location claims.
- **Specific terms are rare.** GO term specificity is imbalanced, so general terms are predicted far more easily than specific ones ([doi:10.1101/gr.280816.125](https://doi.org/10.1101/gr.280816.125)).
- **Upstream annotation changes results.** Orthology results differ markedly between annotation sources ([doi:10.1093/bioinformatics/btaf365](https://doi.org/10.1093/bioinformatics/btaf365)); record the structure release tag.
- **RNA-seq enrichment bias.** Long and highly expressed genes are detected as differentially expressed more often; correct for it ([doi:10.1186/gb-2010-11-2-r14](https://doi.org/10.1186/gb-2010-11-2-r14)).
- **Redundant GO lists.** Summarize them instead of reporting hundreds of overlapping terms ([doi:10.1371/journal.pone.0021800](https://doi.org/10.1371/journal.pone.0021800)).

## 19.3 A quality-control checklist

| Check | Tool | What a problem looks like | Source |
|---|---|---|---|
| Input proteome completeness (F0) | BUSCO protein mode | Low completeness: return to structure | [doi:10.1093/molbev/msab199](https://doi.org/10.1093/molbev/msab199) |
| Input consistency (optional) | OMArk | Many inconsistent or contaminant proteins | [doi:10.1038/s41587-024-02147-w](https://doi.org/10.1038/s41587-024-02147-w) |
| Merge completeness | `pipeline/F_merge_tables.py` | Row count far from the protein count; undocumented drops | `examples/plant_sim/01_vitis_s1_s7/plan.md` |
| Versions | METHODS | Database and mapper versions missing or mismatched | README, Data needed |
| Evidence codes | merged table | Predicted GO not marked IEA | [doi:10.1093/nar/gkab1025](https://doi.org/10.1093/nar/gkab1025); README |
| Enrichment background | clusterProfiler or GOseq | Subset background without a note; length bias untreated | [doi:10.1186/gb-2010-11-2-r14](https://doi.org/10.1186/gb-2010-11-2-r14) |

Acceptance levels and gates are defined in [`docs/EVALUATION.md`](../../docs/EVALUATION.md) and [`docs/EVALUATION_CHECKLIST.md`](../../docs/EVALUATION_CHECKLIST.md).
