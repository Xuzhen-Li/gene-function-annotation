# Chapter 18. Choosing a frame and add-ons

The repository names one whole annotation frame per release and keeps add-ons separate (README, Default route; [`docs/SCENARIOS_FUNCTIONAL.md`](../../docs/SCENARIOS_FUNCTIONAL.md)). The table restates that choice and adds the evidence behind the first tools.

| Situation | Frame or add-on | Tools | Why (source) | Main check |
|---|---|---|---|---|
| Default paper release | F1 | DIAMOND against Swiss-Prot, eggNOG-mapper, InterProScan | Three independent lines: curated similarity ([doi:10.1038/s41592-021-01101-x](https://doi.org/10.1038/s41592-021-01101-x)), orthology transfer ([doi:10.1093/molbev/msab293](https://doi.org/10.1093/molbev/msab293)), signatures ([doi:10.1093/bioinformatics/btu031](https://doi.org/10.1093/bioinformatics/btu031)) | Row count of the merged table close to the protein count (`examples/plant_sim/01_vitis_s1_s7/plan.md`) |
| Fast first pass | F2 | eggNOG-mapper, optional KofamScan | eggNOG 6.0 covers 12,535 reference species ([doi:10.1093/nar/gkac1022](https://doi.org/10.1093/nar/gkac1022)); Kofam uses adaptive thresholds ([doi:10.1093/bioinformatics/btz859](https://doi.org/10.1093/bioinformatics/btz859)) | Do not ship F2 as if InterProScan had been run (README, Data needed) |
| De novo transcriptome peptides | F3 EnTAP or F5 Trinotate | EnTAP, Trinotate | EnTAP was designed for de novo transcriptomes of non-model eukaryotes ([doi:10.1111/1755-0998.13106](https://doi.org/10.1111/1755-0998.13106)) | State which frame was used in METHODS |
| Several genomes in a panel | F7 | OrthoFinder, then F1 on representatives | Standardized orthology benchmarking ([doi:10.1038/nmeth.3830](https://doi.org/10.1038/nmeth.3830)); OrthoFinder 3 accuracy gain ([doi:10.1101/2025.07.15.664860](https://doi.org/10.1101/2025.07.15.664860)) | Labels apply to orthogroup representatives, not every gene |
| Readable names wanted | F4 add-on | AHRD | Names are a presentation layer (README, Data needed) | Names do not raise the grade by themselves |
| MapMan figure planned | F6 add-on | Mercator4 | Plant protein classification framework ([doi:10.1016/j.molp.2019.01.003](https://doi.org/10.1016/j.molp.2019.01.003)) | Run only when a MapMan figure is planned (`docs/MERCATOR_WHEN.md`) |
| Disease or NLR story | F8 add-on | InterProScan filter, NLR-Annotator, NLRtracker | NLR-Annotator was built because low expression and high similarity make NLRs hard to annotate ([doi:10.1104/pp.19.01273](https://doi.org/10.1104/pp.19.01273)); NLRtracker comes with a reference set of validated plant NLRs ([doi:10.1371/journal.pbio.3001124](https://doi.org/10.1371/journal.pbio.3001124)) | An InterProScan screen is not a curated NLR set |
| Transcription factors or kinases | F9 add-on | iTAK | Plant TF and kinase classification ([doi:10.1016/j.molp.2016.09.014](https://doi.org/10.1016/j.molp.2016.09.014)) | Only when that family is needed |

## How to read the tiers

The tier in every table (standard 500 or more citations, established 100 to 499, newer under 100 and published 2023 or later, niche under 100 and older) measures how widely a paper is cited. It says nothing about accuracy on your proteome. Databases and general tools (UniProt, InterPro, KEGG, Cytoscape) collect citations from every field. Community assessments are the better guide to accuracy: CAFA3 found top methods clearly better than baselines but with considerable room for improvement ([doi:10.1186/s13059-019-1835-8](https://doi.org/10.1186/s13059-019-1835-8)).

## Questions to ask before adding a tool

1. Does it add a new kind of evidence (similarity, signature, orthology, structure, language model), or repeat one already in F1?
2. Was it assessed independently (CAFA, Quest for Orthologs), or only by its authors?
3. Which evidence code will its output carry? Machine predictions stay IEA (README, Cross-cutting pitfalls).
4. Can its database version be recorded and its license allow redistribution? KEGG redistribution is still marked unconfirmed in the README.
