# Chapter 20. Worked example: grapevine proteins through frame F1 and add-on F8

This chapter walks through the teaching plan in [`examples/plant_sim/01_vitis_s1_s7/plan.md`](../../examples/plant_sim/01_vitis_s1_s7/plan.md). The proteins come from a simulated grapevine structure release (Vitis_sim.v0.1, self-declared structure grade L1); the point is the order of decisions, not real numbers.

## 20.1 The chooser decision

The flow tool picks frame F1 (DIAMOND, eggNOG-mapper and InterProScan), adds F8 for NLR candidates, and targets grade F-L1. Add-ons are optional and are not F-L1 gates.

## 20.2 The stages

| No. | Stage | Tools | Output | Why |
|---|---|---|---|---|
| 1 | F0 protein sanity | BUSCO protein mode | BUSCO summary with lineage | A catastrophic result goes back to structure ([doi:10.1093/molbev/msab199](https://doi.org/10.1093/molbev/msab199)) |
| 2 | F1a similarity | DIAMOND against Swiss-Prot | `function/diamond/` | Curated hits give names with the lowest error rate ([doi:10.1371/journal.pcbi.1000605](https://doi.org/10.1371/journal.pcbi.1000605)) |
| 3 | F1b orthology | eggNOG-mapper with EGGNOG_TAX_SCOPE set to the clade | `function/emapper/` | GO, KEGG and COG transfer through orthology ([doi:10.1093/molbev/msab293](https://doi.org/10.1093/molbev/msab293)) |
| 4 | F1c signatures | InterProScan | `function/interpro/` | Domains, sites and member-database signatures ([doi:10.1093/nar/gkae1082](https://doi.org/10.1093/nar/gkae1082)) |
| 5 | Merge | `pipeline/F_merge_tables.py` | `merged_function_table.tsv` | One row per gene; row count close to the protein count |
| 6 | F8 NLR screen | InterProScan filter, optional HRP | `nlr_candidates.tsv` | Candidates for disease-gene windows; convert with `pipeline/F8b_nlr_to_families.py` to feed structure overlay S7 |
| 7 | Release | `pipeline/F_release.sh` | `function/release/<TAG>/` | Gates F-L0 and F-L1 in `docs/EVALUATION.md` |

## 20.3 What to take away

- The three F1 tools give three independent kinds of evidence, which is why F1 is the default.
- Script names and frame names differ: `F2_eggnog.sh` is step 2 of frame F1, not the fast frame F2.
- The F8 output is a candidate list, not a curated NLR set; it can loop back to structure curation.
- Two more examples are in `examples/plant_sim/02_oryza_s1/` and `examples/plant_sim/03_solanum_s11/`.
