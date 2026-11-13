# New tools, databases and ideas by step (functional) — 2026-11 survey

Survey of functional-annotation software, databases and ideas, mostly 2023–2026, sorted by the **functional steps** of this repo. Reading list only: the default framework F1 (DIAMOND + eggNOG-mapper + InterProScan) does not change until someone tests an entry.

**Input.** Proteins released by [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation) (`proteins.faa`, one representative per gene). Output table: `merged_function_table.tsv`. Gene finding, soft-masking and TE library work are out of scope here.

## Four numbering systems — read this first

This repo uses four separate ID sets. Section titles below use **framework + step name** only; the other IDs are given as jump links.

| ID set | Examples | Means | Used on this page as |
|---|---|---|---|
| Framework | F1, F2, F3, F5 (+ optional F4, F6–F9) | The whole frame you claim in METHODS (see [`steps/FUNCTIONAL_MAIN.md`](steps/FUNCTIONAL_MAIN.md)) | Section label, e.g. "frame F1 — eggNOG-mapper step" |
| Script file | `F1_diamond.sh`, `F2_eggnog.sh`, `F3_interproscan.sh`, `F1b_kofam.sh` | File names. `F2_eggnog.sh` and `F3_interproscan.sh` are **steps inside frame F1**, not frames F2/F3; `F1b_kofam.sh` is the optional F1+ Kofam add-on | Jump link only |
| Tool card | F1a DIAMOND, F1b eggNOG-mapper, F1c InterProScan, F1+ add-ons | Literacy pages in [`TOOLS.md`](TOOLS.md) | Jump link only |
| Gate | Gate-F1 … Gate-F7 | Release hard checks (provenance, BUSCO, versions, row counts) — not steps | Not used as a stage |

Notes on scope (from review):

- F0 protein BUSCO is an **input check** on the structure release, not a source of functional labels; no F0 entries are listed.
- Frame F7 (OrthoFinder → F1 on representatives) annotates **orthogroup representatives**, not each released gene. A single genome does not need F7 first.
- The optional Pfam/RNA filter in the structure repo (`A5c_expression_pfam_filter.md`) is a structure model-support filter; it is not counted as functional annotation here.
- "Structure" in protein tools (Foldseek, DeepFRI, AlphaFold DB …) means **protein 3D structure**, not gene structure.

`[待确认]` = not yet verified. Preprints are labelled. Machine-predicted GO/EC stays electronic evidence (IEA).

## Contents

- [Frame F1 — homology search step (card F1a, `F1_diamond.sh`)](#frame-f1--homology-search-step-card-f1a-f1_diamondsh) (4)
- [Reference protein and structure databases](#reference-protein-and-structure-databases) (4)
- [Frame F1 — domain step (card F1c, `F3_interproscan.sh`)](#frame-f1--domain-step-card-f1c-f3_interproscansh) (4)
- [Frame F1 — orthology-based GO/KEGG step (card F1b, `F2_eggnog.sh`) and plant GO pipelines](#frame-f1--orthology-based-gokegg-step-card-f1b-f2_eggnogsh-and-plant-go-pipelines) (3)
- [Optional add-on — machine-learning GO prediction (after frame F1)](#optional-add-on--machine-learning-go-prediction-after-frame-f1) (5)
- [Pathways and enzymes (F1+ Kofam, frame F6 Mercator, other add-ons)](#pathways-and-enzymes-f1-kofam-frame-f6-mercator-other-add-ons) (8)
- [Frame F7 — multi-genome orthology](#frame-f7--multi-genome-orthology) (5)
- [Localization and topology (F1+ add-ons)](#localization-and-topology-f1-add-ons) (3)
- [Plant gene families (frame F8 NLR, frame F9 TF/kinase)](#plant-gene-families-frame-f8-nlr-frame-f9-tfkinase) (7)
- [Non-coding RNA function resources](#non-coding-rna-function-resources) (7)
- [Expression-supported function](#expression-supported-function) (3)
- [Curation and community databases](#curation-and-community-databases) (4)
- [Protein 3D-structure-based function](#protein-3d-structure-based-function) (3)
- [Downstream enrichment](#downstream-enrichment) (4)
- [Ideas — LLMs and agents in curation](#ideas--llms-and-agents-in-curation) (4)
- [How entries were checked](#how-entries-were-checked)

## Frame F1 — homology search step (card F1a, `F1_diamond.sh`)

Sequence and protein-3D-structure search engines that can feed or check the DIAMOND step.

| Name | Type | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|
| MMseqs2-GPU | software | Nature Methods 2025; release 18-8cc5c (2025-07-27); last push 2026-11-11 | GPU-accelerated MMseqs2 sequence search (also speeds ColabFold MSAs). | Fast proteome-vs-UniRef search for large plant proteomes. | doi:[10.1038/s41592-025-02819-8](https://doi.org/10.1038/s41592-025-02819-8) · [GitHub](https://github.com/soedinglab/MMseqs2) |
| Foldseek | software | Nature Biotechnology 2023; release 10-941cd33 (2025-01-19); last push 2026-11-11 | Protein 3D-structure search via 3Di alphabet; finds remote homologs missed by sequence search. | Structure here = protein 3D structure (AlphaFold/ESMFold models), not gene structure. | doi:[10.1038/s41587-023-01773-0](https://doi.org/10.1038/s41587-023-01773-0) · [GitHub](https://github.com/steineggerlab/foldseek) |
| ProstT5 | software | NAR Genomics and Bioinformatics 2024; release 0.0.1 (2024-10-15); last push 2026-03-06 | Protein language model translating sequence to 3Di tokens so Foldseek can run without predicted structures. | Plant proteomes without AlphaFold models. | doi:[10.1093/nargab/lqae150](https://doi.org/10.1093/nargab/lqae150) · [GitHub](https://github.com/mheinzinger/ProstT5) |
| TM-Vec 2s | software | preprint 2026 | Embedding-based remote homology / TM-score prediction (preprint 2026). | Idea-level for unannotated plant proteins. | doi:[10.64898/2026.02.05.704073](https://doi.org/10.64898/2026.02.05.704073) |

[Back to contents](#contents)

## Reference protein and structure databases

Databases searched by the homology step; cite current versions in METHODS.

| Name | Type | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|
| UniProt 2025 | database | Nucleic Acids Research 2024 | Swiss-Prot/TrEMBL reference; cite the current NAR update for METHODS. | Core DB for every frame. | doi:[10.1093/nar/gkae1010](https://doi.org/10.1093/nar/gkae1010) · [site](https://www.uniprot.org) |
| AlphaFold Protein Structure Database (2024) | database | Nucleic Acids Research 2023 | Predicted protein 3D structures for UniProt; target for Foldseek searches. | Arabidopsis/rice/maize proteomes plus UniProt-wide models. | doi:[10.1093/nar/gkad1011](https://doi.org/10.1093/nar/gkad1011) · [site](https://alphafold.ebi.ac.uk) |
| AlphaFind v2 | software | Nucleic Acids Research 2026 | Similarity search over AlphaFold DB and TED domains. | Web lookup for single plant proteins. | doi:[10.1093/nar/gkag372](https://doi.org/10.1093/nar/gkag372) · [site](https://alphafind.fi.muni.cz) |
| Carbon Annotation Database (CADB) | database | preprint 2026 | Predicted protein-coding loci and proteins for ~48k GenBank eukaryote assemblies (Carbon-A). | Extra homolog source for under-sampled plant lineages; predictions, not curated (preprint). | doi:[10.64898/2026.10.20.760448](https://doi.org/10.64898/2026.10.20.760448) · [site](https://huggingface.co/blog/HuggingFaceBio/carbon-annotator-genbank-genome-annotation) |

[Back to contents](#contents)

## Frame F1 — domain step (card F1c, `F3_interproscan.sh`)

Domain/family resources beside InterProScan, and domain-aware predictors.

| Name | Type | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|
| SMART (2021 update) ·in repo | database | Nucleic Acids Research 2020 | Signalling/extracellular domain resource (member DB of InterPro). | Receptor-like kinase / LRR domains in plants. | doi:[10.1093/nar/gkaa937](https://doi.org/10.1093/nar/gkaa937) · [site](https://smart.embl.de) |
| CDD / CD-Search (2023) | database | Nucleic Acids Research 2022 | NCBI conserved-domain models and SPARCLE architectures. | Second opinion on domain architecture. | doi:[10.1093/nar/gkac1096](https://doi.org/10.1093/nar/gkac1096) · [site](https://www.ncbi.nlm.nih.gov/Structure/cdd/cdd.shtml) |
| Merizo | software | Nature Communications 2023; release v1.0.0 (2023-10-13); last push 2025-05-22 | Domain segmentation of predicted 3D structures. | Split multi-domain plant proteins before structure search. | doi:[10.1038/s41467-023-43934-4](https://doi.org/10.1038/s41467-023-43934-4) · [GitHub](https://github.com/psipred/Merizo) |
| DPFunc | software | Nature Communications 2025; last push 2026-03-18 | Deep learning GO prediction guided by domain + 3D-structure information. | Generic proteins; 3D = protein structure. | doi:[10.1038/s41467-024-54816-8](https://doi.org/10.1038/s41467-024-54816-8) · [GitHub](https://github.com/CSUBioGroup/DPFunc) |

[Back to contents](#contents)

## Frame F1 — orthology-based GO/KEGG step (card F1b, `F2_eggnog.sh`) and plant GO pipelines

Orthology/similarity transfer of GO and plant-specific GO pipelines. TRAPID suits transcript sets (frame F5-like).

| Name | Type | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|
| GOMAP | software | Plant Methods 2021; release v1.0.0 (2018-07-20); last push 2023-05-22 | Gene Ontology Meta Annotator for Plants: combines sequence similarity, domains and mixed-method predictors into plant GO sets. | Plant-specific (maize origin, applied to many crops). | doi:[10.1186/s13007-021-00754-1](https://doi.org/10.1186/s13007-021-00754-1) · [GitHub](https://github.com/Dill-PICL/GOMAP) |
| TRAPID 2.0 | software | Nucleic Acids Research 2021 | Web app for taxonomic and functional analysis of de novo plant transcriptomes using PLAZA references. | Plant transcript sets (frame F5-like use). | doi:[10.1093/nar/gkab565](https://doi.org/10.1093/nar/gkab565) · [site](https://bioinformatics.psb.ugent.be/trapid_02/) [待确认 link] |
| PLAZA 5.0 | database | Nucleic Acids Research 2021 | Plant comparative genomics: gene families, orthologs, GO/InterPro projections. | Includes Vitis vinifera; good cross-check for transferred GO. | doi:[10.1093/nar/gkab1024](https://doi.org/10.1093/nar/gkab1024) · [site](https://bioinformatics.psb.ugent.be/plaza/) [待确认 link] |

[Back to contents](#contents)

## Optional add-on — machine-learning GO prediction (after frame F1)

Electronic predictions; never replace F1 evidence.

| Name | Type | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|
| DeepGO-SE | software | Nature Machine Intelligence 2024; release v1.0.0 (2023-12-13); last push 2026-10-27 | GO prediction as approximate semantic entailment over ESM2 embeddings and GO axioms. | Generic; electronic evidence - keep as hypothesis. | doi:[10.1038/s42256-024-00795-w](https://doi.org/10.1038/s42256-024-00795-w) · [GitHub](https://github.com/bio-ontology-research-group/deepgo2) |
| ProtGO | software | Bioinformatics 2025; last push 2024-07-25 | Multi-modal GO prediction (PLM + text + taxonomy + GO graph). | Generic. | doi:[10.1093/bioinformatics/btaf390](https://doi.org/10.1093/bioinformatics/btaf390) · [GitHub](https://github.com/sunyatawang/ProtGO) |
| AltereGO | software | preprint 2026 | Score-level fusion of ESM2, ProtT5, Ankh and ProstT5-3Di predictors for GO molecular function (preprint 2026). | Low-homology proteins. | doi:[10.64898/2026.10.23.761425](https://doi.org/10.64898/2026.10.23.761425) |
| GO specificity balance (Genome Res 2026) | idea | Genome Research 2026 | Balancing GO term specificity in sequence-language-model predictions. | Avoids over-specific electronic GO on plant genes [待确认 details]. | doi:[10.1101/gr.280816.125](https://doi.org/10.1101/gr.280816.125) |
| CAFA lessons (idea) | idea | — | Community assessments keep showing GO prediction is hard for proteins with partial knowledge; publish ML GO as electronic evidence (IEA) only. | All frames. | [site](https://biofunctionprediction.org/cafa/) [待确认 link] |

[Back to contents](#contents)

## Pathways and enzymes (F1+ Kofam, frame F6 Mercator, other add-ons)

KO/pathway mapping, EC prediction, plant metabolic clusters.

| Name | Type | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|
| KEGG (2025 NAR) ·in repo | database | Nucleic Acids Research 2024 | Current KEGG citation for KO/pathway mapping. | Used via KofamScan (F1+) or eggNOG. | doi:[10.1093/nar/gkae909](https://doi.org/10.1093/nar/gkae909) · [site](https://www.kegg.jp) |
| Plant Reactome (2024) | database | Nucleic Acids Research 2023 | Curated plant pathways (rice reference, projected to other plants). | Projections include grapevine [待确认 species list]. | doi:[10.1093/nar/gkad1052](https://doi.org/10.1093/nar/gkad1052) · [site](https://plantreactome.gramene.org) |
| Plant Metabolic Network / E2P2 | database+software | — | PlantCyc and species pathway DBs built with the E2P2 enzyme predictor. | Plant-specific metabolism; DOI of current release [待确认]. | [site](https://plantcyc.org) |
| CLEAN | software | Science 2023; release v1.0.1 (2023-03-31); last push 2025-04-06 | Contrastive-learning EC number prediction. | Enzyme hypotheses for plant specialised metabolism. | doi:[10.1126/science.adf2465](https://doi.org/10.1126/science.adf2465) · [GitHub](https://github.com/tttianhao/CLEAN) |
| EZpred | software | Advanced Science 2026 | EC prediction using unlabeled sequence homologs (Advanced Science 2026). | Generic enzymes. DOI looks unusual [待确认] | doi:[10.1002/advs.78703](https://doi.org/10.1002/advs.78703) |
| ProteEC-CLA | software | Proteins: Structure, Function, and Bioinformatics 2025 | EC prediction with contrastive learning + agent attention on ESM2. | Generic enzymes. | doi:[10.1002/prot.26822](https://doi.org/10.1002/prot.26822) |
| plantiSMASH 2.0 | software | Journal of Molecular Biology 2026; release plantismash-2.0.4 (2025-10-25); last push 2026-02-26 | Plant biosynthetic gene cluster detection, substrate prediction for some enzyme families, promoter TF sites; DB of ~30k BGCs over 430 genomes. | Grapevine terpene/stilbene clusters. | doi:[10.1016/j.jmb.2026.169798](https://doi.org/10.1016/j.jmb.2026.169798) · [GitHub](https://github.com/plantismash/plantismash) |
| dbCAN3 ·in repo | software | Nucleic Acids Research 2023; release 4.1.4 (2024-01-23); last push 2025-04-23 | CAZyme and substrate annotation. | Cell-wall enzymes; already noted in this repo - cite NAR 2023. | doi:[10.1093/nar/gkad328](https://doi.org/10.1093/nar/gkad328) · [GitHub](https://github.com/linnabrown/run_dbcan) |

[Back to contents](#contents)

## Frame F7 — multi-genome orthology

Orthogroups across genomes. Annotating representatives is not per-gene annotation.

| Name | Type | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|
| OrthoFinder 3 | software | preprint 2025; release v3.2 (2026-10-23); last push 2026-10-23 | Scalable phylogenetic orthology (v3.x, FAMSA alignment). | Grapevine pangenome/clade comparisons; annotates orthogroup representatives, not each gene. | doi:[10.1101/2025.07.15.664860](https://doi.org/10.1101/2025.07.15.664860) · [GitHub](https://github.com/OrthoFinder/OrthoFinder) |
| FastOMA | software | Nature Methods 2025; release v0.5.1 (2025-12-19); last push 2026-11-12 | Linear-scaling orthology inference (OMAmer placement). | Thousands of proteomes. | doi:[10.1038/s41592-024-02552-8](https://doi.org/10.1038/s41592-024-02552-8) · [GitHub](https://github.com/DessimozLab/FastOMA) |
| SonicParanoid2 | software | Genome Biology 2024 | Fast orthology with ML and language models. | Generic. | doi:[10.1186/s13059-024-03298-4](https://doi.org/10.1186/s13059-024-03298-4) · [site](https://gitlab.com/salvo981/sonicparanoid2) |
| OrthoDB v12 | database | Nucleic Acids Research 2024 | Hierarchical orthologs with functional descriptors (OrthoDB + BUSCO update paper). | Includes many plants. | doi:[10.1093/nar/gkae987](https://doi.org/10.1093/nar/gkae987) · [site](https://www.orthodb.org) |
| OMA browser 2024 | database | Nucleic Acids Research 2023 | OMA orthology resource update. | Plants included. | doi:[10.1093/nar/gkad1020](https://doi.org/10.1093/nar/gkad1020) · [site](https://omabrowser.org) |

[Back to contents](#contents)

## Localization and topology (F1+ add-ons)

Targeting peptides, subcellular location, membrane topology.

| Name | Type | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|
| DeepLoc 2.1 | software | Nucleic Acids Research 2024 | Subcellular localization + membrane protein type from PLMs. | Includes plastid class. | doi:[10.1093/nar/gkae237](https://doi.org/10.1093/nar/gkae237) · [site](https://services.healthtech.dtu.dk/services/DeepLoc-2.1/) |
| TargetP 2.0 | software | Life Science Alliance 2019 | N-terminal targeting peptides (signal, mitochondrial, chloroplast, thylakoid). | Plant organelle targeting. | doi:[10.26508/lsa.201900429](https://doi.org/10.26508/lsa.201900429) · [site](https://services.healthtech.dtu.dk/services/TargetP-2.0/) |
| DeepTMHMM | software | preprint 2022 | Transmembrane topology prediction (preprint). | Generic. | doi:[10.1101/2022.04.08.487609](https://doi.org/10.1101/2022.04.08.487609) · [site](https://dtu.biolib.com/DeepTMHMM) |

[Back to contents](#contents)

## Plant gene families (frame F8 NLR, frame F9 TF/kinase)

Family classifiers. Window lists from here can be handed to structure scenario S7 for gene-model review; the classifiers stay in this repo.

| Name | Type | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|
| Resistify | software | Bioinformatics and Biology Insights 2025; release v2.4.0 (2026-07-22); last push 2026-07-22 | Fast NLR identification/classification from proteins using NLRexpress motifs. | Plant NLRs (frame F8 peer to HRP). | doi:[10.1177/11779322241308944](https://doi.org/10.1177/11779322241308944) · [GitHub](https://github.com/SwiftSeal/resistify) |
| NLRtracker + RefPlantNLR | software+database | PLOS Biology 2021; last push 2024-03-06 | Extracts and classifies NLRs from proteomes/transcripts using features of RefPlantNLR. | Plant NLRs. | doi:[10.1371/journal.pbio.3001124](https://doi.org/10.1371/journal.pbio.3001124) · [GitHub](https://github.com/slt666666/NLRtracker) |
| NLR-Annotator | software | Plant Physiology 2020; tag v0.7-beta; last push 2023-07-19 | Annotation-independent NLR locus finder on genomic sequence. | Window list can be handed to structure scenario S7 for model review. | doi:[10.1104/pp.19.01273](https://doi.org/10.1104/pp.19.01273) · [GitHub](https://github.com/steuernb/NLR-Annotator) |
| NLRexpress | software | Frontiers in Plant Science 2022; last push 2022-08-22 | ML motif predictors for CC/TIR/NB-ARC/LRR motifs. | Plant NLRs. | doi:[10.3389/fpls.2022.975888](https://doi.org/10.3389/fpls.2022.975888) · [GitHub](https://github.com/eliza-m/NLRexpress) |
| NLRSeek | software | aBIOTECH 2026; last push 2026-02-02 | Combines NLR-Annotator loci, targeted re-annotation and NLRtracker to recover NLRs missing from proteomes. | Its re-annotation output is a structure-side hint: send recovered loci to S7, do not merge them into the release GFF from here. | doi:[10.1016/j.abiote.2025.100001](https://doi.org/10.1016/j.abiote.2025.100001) · [GitHub](https://github.com/Wang-Mengda/NLRSeek) |
| PlantTFDB / PlantRegMap | database | Nucleic Acids Research 2019 | Plant TF families, binding motifs and regulatory map. | TF family calls beside iTAK (frame F9). | doi:[10.1093/nar/gkz1020](https://doi.org/10.1093/nar/gkz1020) · [site](http://planttfdb.gao-lab.org) [待确认 link] |
| PlantPAN (latest) | database | Nucleic Acids Research 2023 | Plant promoter / TF-binding analysis navigator. | Promoter/CNS context for TF families (115 species). | doi:[10.1093/nar/gkad945](https://doi.org/10.1093/nar/gkad945) · [site](https://plantpan.itps.ncku.edu.tw) |

[Back to contents](#contents)

## Non-coding RNA function resources

Functional context for ncRNA loci called on the structure side.

| Name | Type | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|
| ncPlantDB | database | Nucleic Acids Research 2024 | Plant ncRNAs with potential ncRNA-encoded peptides and cell-type interactions (43 species). | Plant-specific. | doi:[10.1093/nar/gkae1017](https://doi.org/10.1093/nar/gkae1017) · [site](https://bis.zju.edu.cn/ncPlantDB) |
| PLncDB V2.0 | database | Nucleic Acids Research 2020 | Plant lncRNA encyclopedia. | Plant-specific. | doi:[10.1093/nar/gkaa910](https://doi.org/10.1093/nar/gkaa910) · [site](https://www.tobaccodb.org/plncdb/) [待确认 link] |
| GreeNC 2.0 | database | Nucleic Acids Research 2021 | Plant lncRNA catalog. | Includes Vitis. | doi:[10.1093/nar/gkab1014](https://doi.org/10.1093/nar/gkab1014) · [site](http://greenc.sequentiabiotech.com) [待确认 link] |
| CANTATAdb 3.0 | database | Plant And Cell Physiology 2024 | Updated plant lncRNA repository. | Plant-specific. | doi:[10.1093/pcp/pcae081](https://doi.org/10.1093/pcp/pcae081) · [site](http://cantata.amu.edu.pl) [待确认 link] |
| PlantCircRNA | database | Nucleic Acids Research 2024 | Plant circular RNA database. | Plant-specific. | doi:[10.1093/nar/gkae709](https://doi.org/10.1093/nar/gkae709) · [site](https://plant.deepbiology.cn/PlantCircRNA/) |
| psRNATarget (2017 release) | software | Nucleic Acids Research 2018 | Plant small-RNA target prediction server. | miRNA-target function hypotheses. | doi:[10.1093/nar/gky316](https://doi.org/10.1093/nar/gky316) · [site](https://www.zhaolab.org/psRNATarget/) [待确认 link] |
| PmiREN 2.0 | database | Nucleic Acids Research 2021 | Plant miRNA encyclopedia. | Plant-specific. | doi:[10.1093/nar/gkab811](https://doi.org/10.1093/nar/gkab811) · [site](https://pmiren.com) |

[Back to contents](#contents)

## Expression-supported function

Expression and co-expression evidence; supports hypotheses, not experimental GO.

| Name | Type | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|
| scPlantDB | database | Nucleic Acids Research 2023 | Plant single-cell atlas: cell types and markers. | Cell-type context for candidate genes. | doi:[10.1093/nar/gkad706](https://doi.org/10.1093/nar/gkad706) · [site](https://biobigdata.nju.edu.cn/scplantdb/) [待确认 link] |
| hdWGCNA | software | Cell Reports Methods 2023; release v0.4.12 (2026-06-16); last push 2026-06-16 | Co-expression networks in single-cell/spatial data. | Module membership as function evidence (non-IEA labels only with experiments). | doi:[10.1016/j.crmeth.2023.100498](https://doi.org/10.1016/j.crmeth.2023.100498) · [GitHub](https://github.com/smorabit/hdWGCNA) |
| CoNekT | software+database | preprint 2018 | Co-expression network toolkit/framework for plants. | Comparative co-expression [待确认 journal DOI]. | doi:[10.1101/255075](https://doi.org/10.1101/255075) · [site](https://conekt.sbs.ntu.edu.sg) [待确认 link] |

[Back to contents](#contents)

## Curation and community databases

Curated names and reference catalogues, incl. grapevine.

| Name | Type | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|
| Grapedia Grapevine Reference Gene Catalogue | database | — | Curated V. vinifera gene ID/symbol pairs with function, literature and confidence; v3.1 (Nov 2025) aligned to T2T v5.1 annotation. | Grapevine-specific naming source. | [site](https://grapedia.org/genes/) |
| Grape Gene Reference Catalogue (paper) | database | Frontiers in Plant Science 2022 | Describes the catalogue as a standard for gene selection. | Grapevine. | doi:[10.3389/fpls.2021.803977](https://doi.org/10.3389/fpls.2021.803977) |
| Gene Ontology knowledgebase (2026) | database | Nucleic Acids Research 2025 | Current GO release paper (NAR, issue 2026; a correction notice exists, doi 10.1093/nar/gkag678). | Cite GO release date in METHODS. | doi:[10.1093/nar/gkaf1292](https://doi.org/10.1093/nar/gkaf1292) · [site](https://geneontology.org) |
| Ensembl Plants | database | — | Plant genomes with gene trees and projected annotation. | Vitis vinifera present. | [site](https://plants.ensembl.org) |

[Back to contents](#contents)

## Protein 3D-structure-based function

Function from predicted protein 3D structures.

| Name | Type | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|
| WASP | software | release v3.0 (2026-09-26); last push 2026-10-10 | Whole-proteome annotation via Foldseek against AlphaFold DB (GO, Pfam, PANTHER, CATH, Rhea, EC). | 3D-structure route for plant proteins without sequence hits. | [GitHub](https://github.com/gioodm/wasp-proteins-annotation) |
| PARSE | software | Proceedings of the National Academy of Sciences 2025 | Functional site annotation from local 3D-structure embeddings. | Generic. | doi:[10.1073/pnas.2513219122](https://doi.org/10.1073/pnas.2513219122) |
| metagenomic-DeepFRI | software | preprint 2026 | Scaled DeepFRI (GO from protein 3D-structure graphs) (preprint 2026). | Here 'structure' is protein 3D structure. | doi:[10.64898/2026.04.27.720983](https://doi.org/10.64898/2026.04.27.720983) |

[Back to contents](#contents)

## Downstream enrichment

Uses `merged_function_table.tsv` as the background annotation.

| Name | Type | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|
| DAVID (2025 update) | software | Nucleic Acids Research 2026 | Enrichment server; adds DAVID Ortholog for cross-species analysis. | Model-organism heavy; map plant genes via orthologs. | doi:[10.1093/nar/gkag470](https://doi.org/10.1093/nar/gkag470) · [site](https://davidbioinformatics.nih.gov) |
| g:Profiler (2023) | software | Nucleic Acids Research 2023 | Enrichment and ID conversion. | Supports Ensembl Plants species. | doi:[10.1093/nar/gkad347](https://doi.org/10.1093/nar/gkad347) · [site](https://biit.cs.ut.ee/gprofiler) |
| agriGO v2.0 | software | Nucleic Acids Research 2017 | GO enrichment for agricultural species. | Plant-focused. | doi:[10.1093/nar/gkx382](https://doi.org/10.1093/nar/gkx382) · [site](http://systemsbiology.cau.edu.cn/agriGOv2/) [待确认 link] |
| clusterProfiler 4.0 | software | The Innovation 2021; last push 2026-11-11 | R enrichment with custom TERM2GENE from merged_function_table.tsv. | Any species with your own GO table. | doi:[10.1016/j.xinn.2021.100141](https://doi.org/10.1016/j.xinn.2021.100141) · [GitHub](https://github.com/YuLab-SMU/clusterProfiler) |

[Back to contents](#contents)

## Ideas — LLMs and agents in curation

Ideas only; human sign-off required.

| Name | Type | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|
| GeneAgent | idea | Nature Methods 2025 | Self-verifying LLM agent for gene-set analysis using domain databases. | Idea for checking enrichment summaries; human review. | doi:[10.1038/s41592-025-02748-6](https://doi.org/10.1038/s41592-025-02748-6) |
| LLM-assisted Reactome annotation | idea | preprint 2025 | LLM/RAG proposals of pathway annotations for curator review (preprint). | Idea for plant pathway curation. | doi:[10.64898/2025.12.20.695723](https://doi.org/10.64898/2025.12.20.695723) |
| Agentic AI for gene function across genomes | idea | Zenodo 2026 | GO curators' agent workflow with constrained schemas and validators (Zenodo record). | Idea only. | doi:[10.5281/zenodo.18904049](https://doi.org/10.5281/zenodo.18904049) |
| ProtNLM (UniProt names) | idea | — | UniProt uses a Google protein-naming model to propose names for unreviewed entries; names carry an automatic evidence tag. | Explains machine names arriving via TrEMBL hits. | [site](https://www.uniprot.org/help/ProtNLM) |

[Back to contents](#contents)

## How entries were checked

- Searched 2026-11-12/13 (CST): Crossref title search, web search (papers 2023–2026, tool pages, NAR database issues), GitHub API, and the existing docs of this repo.
- Each DOI was resolved in Crossref (DataCite for Zenodo) and its title matched to the entry; venue/year come from that record (online year may precede the issue year). GitHub repos were opened with the API on the survey day.
- `[待确认 link]` = the website did not answer an automated check (often bot blocking); the DOI is still resolved.
- No tool or paper was added from memory without a resolved record or official page.

Entries: 68. Marked `·in repo` = name already appears somewhere in this repo's docs (entry adds a newer paper/release or a new angle).
