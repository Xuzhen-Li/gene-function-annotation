# Software, databases and ideas by type (functional) — 2026-11

Second pass of the 2026-11 survey, sorted **by type** (按类型分类). It adds classic tools the pipelines already use and well-known tools the first pass skipped, so that the two files together form one inventory. It is a reading list: nothing here changes the default path in [`TOOLS.md`](TOOLS.md).

**Boundary (unchanged, see [`BOUNDARY.md`](BOUNDARY.md)).** F0 is input QC (BUSCO on proteins) and is not a source of functional labels, so no F0 entries appear here. Frame F7 annotates orthogroup representatives, not every gene. Protein "structure" means 3D structure. The merged product is `merged_function_table.tsv`. Steps are named "framework + step name".

First-pass file: [`CATALOG_NEW_TOOLS_2026-11.md`](CATALOG_NEW_TOOLS_2026-11.md). Rows already there are **not repeated**; the last section lists them by the same type classes so every entry has one class.

`·in repo` = the name already appears in this repo's docs (TOOLS, tools cards, notes, steps); the row adds the citation, release and type. `[待确认]` = something still unverified (named in the row). `[preprint]` = preprint only.

Snapshot: 2026-11-13 (Asia/Shanghai). DOIs resolved in Crossref (DataCite for Zenodo/Bioconductor) and titles matched; GitHub release/push dates from the GitHub API; other links by HTTP request, all on the same day.

## Type classes

| Type-class | Covers | New rows | First-pass rows |
|---|---|---|---|
| [homology-search](#homology-search) | Sequence similarity engines (frame F1 homology search step) | 5 | 1 |
| [reference-db](#reference-db) | Reference sequence and ontology databases | 4 | 4 |
| [domain](#domain) | Domain and family annotation (frame F1 domain step) | 1 | 4 |
| [orthology-go](#orthology-go) | Orthology/similarity-based names, GO and KEGG; whole frameworks (frame F1 orthology step, fast frame F2, EnTAP frame F3, F4 readable names) | 7 | 2 |
| [ml-go](#ml-go) | Machine-learning GO prediction (optional add-on after frame F1) | 4 | 3 |
| [pathway-enzyme](#pathway-enzyme) | Pathways, KO and EC (F1+ Kofam, frame F6 MapMan) | 8 | 8 |
| [multi-genome-orthology](#multi-genome-orthology) | Orthogroups across genomes (frame F7 annotates orthogroup representatives) | 3 | 6 |
| [localization](#localization) | Signal peptides, topology and subcellular localization (F1+ add-ons) | 5 | 3 |
| [plant-family](#plant-family) | Plant gene families (frame F8 NLR, frame F9 TF/kinase) | 4 | 7 |
| [ncrna-function](#ncrna-function) | Non-coding RNA function resources | 2 | 7 |
| [expression](#expression) | Expression-supported function | 2 | 3 |
| [community-db](#community-db) | Curated community catalogues and naming | 1 | 2 |
| [protein-3d](#protein-3d) | Protein 3D structure prediction, search and domains | 9 | 8 |
| [enrichment](#enrichment) | Downstream GO/KEGG enrichment | 4 | 4 |
| [idea](#idea) | Ideas, formats and merge rules (Merge / aggregate step) | 2 | 6 |

New rows in this file: 61. First-pass rows (indexed, not repeated): 68. Combined inventory: 129.

Columns: Name, Type (software / database / idea / software+database / database+software), Type-class, Framework / step, Year / latest release, What it does, Plant / eukaryote relevance, Source.

## Contents

- [homology-search](#homology-search) (5)
- [reference-db](#reference-db) (4)
- [domain](#domain) (1)
- [orthology-go](#orthology-go) (7)
- [ml-go](#ml-go) (4)
- [pathway-enzyme](#pathway-enzyme) (8)
- [multi-genome-orthology](#multi-genome-orthology) (3)
- [localization](#localization) (5)
- [plant-family](#plant-family) (4)
- [ncrna-function](#ncrna-function) (2)
- [expression](#expression) (2)
- [community-db](#community-db) (1)
- [protein-3d](#protein-3d) (9)
- [enrichment](#enrichment) (4)
- [idea](#idea) (2)
- [First-pass entries by type-class](#first-pass-entries-by-type-class)
- [Not verified yet](#not-verified-yet)
- [How entries were checked](#how-entries-were-checked)

## homology-search

Sequence similarity engines (frame F1 homology search step).

| Name | Type | Type-class | Framework / step | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|---|---|
| BLAST+ ·in repo | software | homology-search | F1 homology search | BMC Bioinformatics 2009 | NCBI BLAST command-line suite (blastp, makeblastdb). | Reference engine; slower than DIAMOND for whole proteomes. | doi:[10.1186/1471-2105-10-421](https://doi.org/10.1186/1471-2105-10-421) · [site](https://blast.ncbi.nlm.nih.gov/) |
| DIAMOND (v2) ·in repo | software | homology-search | F1 homology search | Nature Methods 2021; release v2.2.8 (2026-09-20); last push 2026-11-12 | Fast protein aligner with BLAST-like sensitivity modes (--ultra-sensitive). | Default frame F1 homology engine (F1_diamond.sh). | doi:[10.1038/s41592-021-01101-x](https://doi.org/10.1038/s41592-021-01101-x) · [GitHub](https://github.com/bbuchfink/diamond) |
| MMseqs2 ·in repo | software | homology-search | F1 homology search | Nature Biotechnology 2017; release 18-8cc5c (2025-07-27); last push 2026-11-11 | Sensitive fast protein search and clustering. | Alternative to DIAMOND; also used to cluster proteomes. (Base tool; the GPU version is in the overnight catalog.) | doi:[10.1038/nbt.3988](https://doi.org/10.1038/nbt.3988) · [GitHub](https://github.com/soedinglab/MMseqs2) |
| HMMER 3 | software | homology-search | F1 domain search | PLoS Computational Biology 2011; release hmmer-3.4 (2023-08-15); last push 2026-10-28 | Profile HMM search (hmmscan, hmmsearch, jackhmmer). | [待确认] Engine behind Pfam, KofamScan, plant family HMM scans. (site returned HTTP 500 at check) | doi:[10.1371/journal.pcbi.1002195](https://doi.org/10.1371/journal.pcbi.1002195) · [GitHub](https://github.com/EddyRivasLab/hmmer) · [site](http://hmmer.org/) |
| HH-suite3 | software | homology-search | F1 remote homology | BMC Bioinformatics 2019; release v3.3.0 (2020-08-25); last push 2026-10-07 | HMM-HMM comparison for remote homology (HHblits, HHsearch). | Remote homology for unannotated plant proteins. | doi:[10.1186/s12859-019-3019-7](https://doi.org/10.1186/s12859-019-3019-7) · [GitHub](https://github.com/soedinglab/hh-suite) |

[Back to contents](#contents)

## reference-db

Reference sequence and ontology databases.

| Name | Type | Type-class | Framework / step | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|---|---|
| UniRef | database | reference-db | F1 homology search | Bioinformatics 2015 | Clustered UniProt sets (UniRef100/90/50). | Smaller search space than full TrEMBL. | doi:[10.1093/bioinformatics/btu739](https://doi.org/10.1093/bioinformatics/btu739) · [site](https://www.uniprot.org/help/uniref) |
| Pfam (2021) ·in repo | database | reference-db | F1 domain step | Nucleic Acids Research 2021 | Protein family HMM library (now hosted in InterPro). | Core domain source in InterProScan output. | doi:[10.1093/nar/gkaa913](https://doi.org/10.1093/nar/gkaa913) · [site](https://www.ebi.ac.uk/interpro/entry/pfam/) |
| TAIR | database | reference-db | F4 readable names | genesis 2015 | The Arabidopsis Information Resource: curated Arabidopsis gene function and nomenclature. | Best-curated eudicot names for transfer by homology. | doi:[10.1002/dvg.22877](https://doi.org/10.1002/dvg.22877) · [site](https://www.arabidopsis.org/) |
| eggNOG 6 | database | reference-db | F1 orthology GO/KEGG step | Nucleic Acids Research 2023 | Hierarchical orthology database behind eggNOG-mapper. | [待确认] Note: eggNOG-mapper v2 still ships eggNOG 5 data unless updated. (site returned HTTP 500 at check) | doi:[10.1093/nar/gkac1022](https://doi.org/10.1093/nar/gkac1022) · [site](http://eggnog6.embl.de/) |

[Back to contents](#contents)

## domain

Domain and family annotation (frame F1 domain step).

| Name | Type | Type-class | Framework / step | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|---|---|
| InterProScan 5 ·in repo | software | domain | F1 domain step | Bioinformatics 2014; release 5.78-109.0 (2026-06-11); last push 2026-11-04 | Runs member databases (Pfam, PANTHER, SMART, CDD, Gene3D…) and maps InterPro2GO. | Frame F1 domain step (F3_interproscan.sh). | doi:[10.1093/bioinformatics/btu031](https://doi.org/10.1093/bioinformatics/btu031) · [GitHub](https://github.com/ebi-pf-team/interproscan) |

[Back to contents](#contents)

## orthology-go

Orthology/similarity-based names, GO and KEGG; whole frameworks (frame F1 orthology step, fast frame F2, EnTAP frame F3, F4 readable names).

| Name | Type | Type-class | Framework / step | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|---|---|
| eggNOG-mapper v2 ·in repo | software | orthology-go | F1 orthology GO/KEGG step | Molecular Biology and Evolution 2021; release v3.0.0-beta6 (2026-08-13); last push 2026-08-13 | Orthology-based functional annotation: names, GO, KEGG, EC, COG. | Frame F1 orthology step (F2_eggnog.sh) and fast frame F2. | doi:[10.1093/molbev/msab293](https://doi.org/10.1093/molbev/msab293) · [GitHub](https://github.com/eggnogdb/eggnog-mapper) |
| PANNZER2 ·in repo | software | orthology-go | F2 fast framework (peer) | Nucleic Acids Research 2018 | Fast web/standalone GO and free-text description prediction. | [待确认] Speed-lane peer of eggNOG-mapper for eukaryotes. (site returned HTTP 500 at check) | doi:[10.1093/nar/gky350](https://doi.org/10.1093/nar/gky350) · [site](http://ekhidna2.biocenter.helsinki.fi/sanspanz/) |
| Blast2GO ·in repo | software | orthology-go | F3 EnTAP framework (peer) | Bioinformatics 2005 | BLAST-based GO annotation and visualisation (now in commercial OmicsBox). | Historically the most-cited plant GO route; licence matters. | doi:[10.1093/bioinformatics/bti610](https://doi.org/10.1093/bioinformatics/bti610) · [site](https://www.biobam.com/omicsbox/) |
| EnTAP ·in repo | software | orthology-go | F3 EnTAP framework | Molecular Ecology Resources 2020; release v1.4.0 (2024-09-12); last push 2025-01-22 | Eukaryotic non-model annotation pipeline: filtering, similarity search, contaminant flags, eggNOG and InterPro. | Frame F3 itself; plant-tested (Wegrzyn lab). (GitHub repo archived (API)) | doi:[10.1111/1755-0998.13106](https://doi.org/10.1111/1755-0998.13106) · [GitHub](https://github.com/harta55/EnTAP) |
| FA-nf | software | orthology-go | F3 EnTAP framework (peer) | Genes 2021; release 0.4.0 (2022-02-28); last push 2022-02-28 | Nextflow functional annotation pipeline for non-model proteins (BLAST, InterProScan, KEGG, signal peptides). | Frame F3 peer with reproducible workflow. | doi:[10.3390/genes12101645](https://doi.org/10.3390/genes12101645) · [GitHub](https://github.com/guigolab/FA-nf) |
| Sma3s v2 | software | orthology-go | F3 EnTAP framework (peer) | PROTEOMICS 2017; release v3 (2026-09-28); last push 2026-09-28 | Functional annotation of proteomes/transcriptomes against UniProt (GO, keywords, pathways). | Frame F3 peer; light install. | doi:[10.1002/pmic.201700071](https://doi.org/10.1002/pmic.201700071) · [GitHub](https://github.com/UPOBioinfo/sma3s) |
| AHRD ·in repo | software | orthology-go | F4 readable names | release v3.3.3 (2017-02-16); last push 2023-08-16 | Automated assignment of Human Readable Descriptions from BLAST results. | Frame F4 readable-name helper in this repo. (no peer-reviewed paper found in this pass) | [GitHub](https://github.com/groupschoof/AHRD) |

[Back to contents](#contents)

## ml-go

Machine-learning GO prediction (optional add-on after frame F1).

| Name | Type | Type-class | Framework / step | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|---|---|
| DeepGOPlus ·in repo | software | ml-go | ML GO add-on | Bioinformatics 2020; release v1.0.2 (2024-04-23); last push 2026-10-01 | CNN + DIAMOND GO prediction from sequence. | Baseline of the DeepGO line. | doi:[10.1093/bioinformatics/btz595](https://doi.org/10.1093/bioinformatics/btz595) · [GitHub](https://github.com/bio-ontology-research-group/deepgoplus) |
| NetGO 3.0 ·in repo | software | ml-go | ML GO add-on | Genomics, Proteomics & Bioinformatics 2023 | Protein-language-model GO prediction server (CAFA top performer). | Web compare track for hard plant proteins. | doi:[10.1016/j.gpb.2023.04.001](https://doi.org/10.1016/j.gpb.2023.04.001) |
| DeepFRI ·in repo | software | ml-go | ML GO add-on | Nature Communications 2021; release v1.0.0 (2021-03-31); last push 2023-03-24 | Graph-convolution function prediction from 3D structure and sequence. | Uses predicted 3D structures. (Original DeepFRI; the overnight catalog lists the metagenomic-DeepFRI resource.) | doi:[10.1038/s41467-021-23303-9](https://doi.org/10.1038/s41467-021-23303-9) · [GitHub](https://github.com/flatironinstitute/DeepFRI) |
| GoPredSim | software | ml-go | ML GO add-on | Scientific Reports 2021; last push 2024-12-02 | GO transfer by embedding similarity (SeqVec/ProtT5). | Embedding-based annotation for remote homologs. | doi:[10.1038/s41598-020-80786-0](https://doi.org/10.1038/s41598-020-80786-0) · [GitHub](https://github.com/Rostlab/goPredSim) |

[Back to contents](#contents)

## pathway-enzyme

Pathways, KO and EC (F1+ Kofam, frame F6 MapMan).

| Name | Type | Type-class | Framework / step | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|---|---|
| MapMan4 / Mercator4 ·in repo | software+database | pathway-enzyme | F6 MapMan | Molecular Plant 2019 | Plant-specific functional bins (MapMan4) assigned by Mercator4. | Frame F6; plant-only ontology. | doi:[10.1016/j.molp.2019.01.003](https://doi.org/10.1016/j.molp.2019.01.003) · [site](https://www.plabipd.de/mercator_main.html) |
| KofamKOALA / KofamScan ·in repo | software | pathway-enzyme | F1+ Kofam | Bioinformatics 2020 | KEGG Orthology assignment with adaptive-threshold profile HMMs. | F1+ Kofam add-on and fast frame F2. | doi:[10.1093/bioinformatics/btz859](https://doi.org/10.1093/bioinformatics/btz859) · [site](https://www.genome.jp/tools/kofamkoala/) |
| BlastKOALA / GhostKOALA ·in repo | software | pathway-enzyme | F2 fast framework (peer) | Journal of Molecular Biology 2016 | KEGG web servers assigning KO numbers by sequence similarity. | Web alternative for KEGG mapping. | doi:[10.1016/j.jmb.2015.11.006](https://doi.org/10.1016/j.jmb.2015.11.006) · [site](https://www.kegg.jp/blastkoala/) |
| KEGG Mapper ·in repo | software | pathway-enzyme | F2 fast framework (KEGG plots) | Protein Science 2020 | Maps KO lists onto KEGG pathways, BRITE and modules. | Pathway plots after Kofam/eggNOG. | doi:[10.1002/pro.3711](https://doi.org/10.1002/pro.3711) · [site](https://www.kegg.jp/kegg/mapper/) |
| kegg-pathways-completeness | software | pathway-enzyme | F2 fast framework (KEGG plots) | release 1.4.4 (2026-07-27); last push 2026-10-01 | Computes KEGG module completeness from a KO list. | Module-level summary for a proteome. (no peer-reviewed paper found in this pass) | [GitHub](https://github.com/EBI-Metagenomics/kegg-pathways-completeness-tool) |
| MetaCyc | database | pathway-enzyme | F1+ pathways | Nucleic Acids Research 2020 | Curated metabolic pathways and enzymes across life. | [待确认] Reference for PMN/E2P2 pathway calls. (site returned HTTP 500 at check) | doi:[10.1093/nar/gkz862](https://doi.org/10.1093/nar/gkz862) · [site](https://metacyc.org/) |
| BRENDA | database | pathway-enzyme | F1+ enzymes | Nucleic Acids Research 2021 | Comprehensive enzyme function database (EC). | EC sanity checks. | doi:[10.1093/nar/gkaa1025](https://doi.org/10.1093/nar/gkaa1025) · [site](https://www.brenda-enzymes.org/) |
| DeepEC | software | pathway-enzyme | F1+ enzymes | Proceedings of the National Academy of Sciences 2019 | Deep-learning EC number prediction. | Compare track to CLEAN. | doi:[10.1073/pnas.1821905116](https://doi.org/10.1073/pnas.1821905116) |

[Back to contents](#contents)

## multi-genome-orthology

Orthogroups across genomes (frame F7 annotates orthogroup representatives).

| Name | Type | Type-class | Framework / step | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|---|---|
| Broccoli ·in repo | software | multi-genome-orthology | F7 multi-genome orthology | Molecular Biology and Evolution 2020; release v2.0.1 (2026-10-01); last push 2026-10-01 | Orthology via phylogeny and network label propagation. | F7 compare track. | doi:[10.1093/molbev/msaa159](https://doi.org/10.1093/molbev/msaa159) · [GitHub](https://github.com/rderelle/Broccoli) |
| Proteinortho6 | software | multi-genome-orthology | F7 multi-genome orthology | Frontiers in Bioinformatics 2023 | Graph-based (co-)orthology detection at scale. | Many haplotype proteomes. | doi:[10.3389/fbinf.2023.1322477](https://doi.org/10.3389/fbinf.2023.1322477) · [site](https://gitlab.com/paulklemm_PHD/proteinortho) |
| CAFE 5 | software | multi-genome-orthology | F7 multi-genome orthology | Bioinformatics 2021; release v5.1 (2023-04-17); last push 2026-10-23 | Gene family expansion/contraction under rate variation. | Family size changes after orthogroup inference. | doi:[10.1093/bioinformatics/btaa1022](https://doi.org/10.1093/bioinformatics/btaa1022) · [GitHub](https://github.com/hahnlab/CAFE5) |

[Back to contents](#contents)

## localization

Signal peptides, topology and subcellular localization (F1+ add-ons).

| Name | Type | Type-class | Framework / step | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|---|---|
| SignalP 6.0 ·in repo | software | localization | F1+ localization | Nature Biotechnology 2022 | Signal peptide prediction (all five types) with protein language model. | Secretome; plant-applicable. | doi:[10.1038/s41587-021-01156-3](https://doi.org/10.1038/s41587-021-01156-3) · [site](https://services.healthtech.dtu.dk/services/SignalP-6.0/) |
| TMHMM 2.0 | software | localization | F1+ localization | Journal of Molecular Biology 2001 | Transmembrane helix prediction (HMM). | Classic topology call; DeepTMHMM is newer. | doi:[10.1006/jmbi.2000.4315](https://doi.org/10.1006/jmbi.2000.4315) · [site](https://services.healthtech.dtu.dk/services/TMHMM-2.0/) |
| Phobius ·in repo | software | localization | F1+ localization | Journal of Molecular Biology 2004 | Combined transmembrane topology and signal peptide predictor. | Bundled in InterProScan. | doi:[10.1016/j.jmb.2004.03.016](https://doi.org/10.1016/j.jmb.2004.03.016) · [site](https://phobius.sbc.su.se/) |
| WoLF PSORT | software | localization | F1+ localization | Nucleic Acids Research 2007 | Subcellular localization prediction with a plant model. | Plant mode available. | doi:[10.1093/nar/gkm259](https://doi.org/10.1093/nar/gkm259) · [site](https://wolfpsort.hgc.jp/) |
| LOCALIZER | software | localization | F1+ localization | Scientific Reports 2017 | Predicts chloroplast, mitochondrial and nuclear localization of plant and effector proteins. | Plant-specific. | doi:[10.1038/srep44598](https://doi.org/10.1038/srep44598) · [site](https://localizer.csiro.au/) |

[Back to contents](#contents)

## plant-family

Plant gene families (frame F8 NLR, frame F9 TF/kinase).

| Name | Type | Type-class | Framework / step | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|---|---|
| iTAK ·in repo | software | plant-family | F9 TF/kinase | Molecular Plant 2016; release v2.0.7 (2026-04-08); last push 2026-04-08 | Plant transcription factor and protein kinase identification and classification. | Frame F9 tool in this repo. | doi:[10.1016/j.molp.2016.09.014](https://doi.org/10.1016/j.molp.2016.09.014) · [GitHub](https://github.com/kentnf/iTAK) |
| TAPscan v4 | software+database | plant-family | F9 TF/kinase | The Plant Journal 2025 | Detects transcription-associated proteins with family rules; streptophyte-wide database. | Plant TF/TR classification alternative to iTAK. | doi:[10.1111/tpj.17184](https://doi.org/10.1111/tpj.17184) · [site](https://tapscan.plantcode.cup.uni-freiburg.de/) |
| PRGdb 4.0 | database+software | plant-family | F8 NLR | Nucleic Acids Research 2022 | Plant resistance gene database with DRAGO annotation pipeline. | [待确认] NLR/RLK reference set. (site returned HTTP 500 at check) | doi:[10.1093/nar/gkab1087](https://doi.org/10.1093/nar/gkab1087) · [site](http://prgdb.org/) |
| RGAugury | software | plant-family | F8 NLR | BMC Genomics 2016 | Pipeline identifying resistance gene analogs (NBS, RLK, RLP). | Plant R-gene families. | doi:[10.1186/s12864-016-3197-x](https://doi.org/10.1186/s12864-016-3197-x) · [site](https://bitbucket.org/yaanlpc/rgaugury) |

[Back to contents](#contents)

## ncrna-function

Non-coding RNA function resources.

| Name | Type | Type-class | Framework / step | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|---|---|
| miRBase | database | ncrna-function | ncRNA function | Nucleic Acids Research 2019 | Reference microRNA sequence and nomenclature database. | Plant miRNA naming. | doi:[10.1093/nar/gky1141](https://doi.org/10.1093/nar/gky1141) · [site](https://www.mirbase.org/) |
| psRobot | software | ncrna-function | ncRNA function | Nucleic Acids Research 2012 | Plant small-RNA meta-analysis and target prediction. | [待确认] Plant-specific. (site returned HTTP 500 at check) | doi:[10.1093/nar/gks554](https://doi.org/10.1093/nar/gks554) · [site](http://omicslab.genetics.ac.cn/psRobot/) |

[Back to contents](#contents)

## expression

Expression-supported function.

| Name | Type | Type-class | Framework / step | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|---|---|
| Grapevine Expression Atlas | database | expression | Expression-supported function | The Plant Cell 2012 | Organ/stage expression atlas of V. vinifera Corvina. | Grape-specific expression support. | doi:[10.1105/tpc.112.100230](https://doi.org/10.1105/tpc.112.100230) |
| ATTED-II v11 | database | expression | Expression-supported function | Plant and Cell Physiology 2022 | Plant gene coexpression database. | Coexpression support for names. | doi:[10.1093/pcp/pcac041](https://doi.org/10.1093/pcp/pcac041) · [site](https://atted.jp/) |

[Back to contents](#contents)

## community-db

Curated community catalogues and naming.

| Name | Type | Type-class | Framework / step | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|---|---|
| The grapevine gene nomenclature system | idea | community-db | F4 readable names | BMC Genomics 2014 | Proposed rules for naming grapevine genes. | Readable-name rules for Vitis. | doi:[10.1186/1471-2164-15-1077](https://doi.org/10.1186/1471-2164-15-1077) |

[Back to contents](#contents)

## protein-3d

Protein 3D structure prediction, search and domains.

| Name | Type | Type-class | Framework / step | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|---|---|
| AlphaFold2 | software | protein-3d | Protein 3D structure | Nature 2021; release v2.3.2 (2023-04-05); last push 2026-04-22 | Protein 3D structure prediction. | Basis of AlphaFold DB. | doi:[10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2) · [GitHub](https://github.com/google-deepmind/alphafold) |
| ColabFold | software | protein-3d | Protein 3D structure | Nature Methods 2022; release v1.6.3 (2026-09-14); last push 2026-11-09 | Fast AlphaFold2 with MMseqs2 MSAs. | Batch 3D prediction for unannotated proteins. | doi:[10.1038/s41592-022-01488-1](https://doi.org/10.1038/s41592-022-01488-1) · [GitHub](https://github.com/sokrypton/ColabFold) |
| ESMFold / ESM-2 | software | protein-3d | Protein 3D structure | Science 2023; release v1.0.3 (2022-10-18); last push 2024-02-07 | Single-sequence 3D structure prediction from a protein language model. | Fast proteome-scale 3D models. (GitHub repo archived (API)) | doi:[10.1126/science.ade2574](https://doi.org/10.1126/science.ade2574) · [GitHub](https://github.com/facebookresearch/esm) |
| AlphaFold 3 | software | protein-3d | Protein 3D structure | Nature 2024; release v3.0.5 (2026-10-30); last push 2026-11-11 | Joint structure prediction of complexes with nucleic acids, ligands and ions. | Code for non-commercial use; weights on request. | doi:[10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w) · [GitHub](https://github.com/google-deepmind/alphafold3) |
| TED (The Encyclopedia of Domains) | database | protein-3d | Protein 3D structure | Science 2024 | Structure-based domain segmentation of AlphaFold DB. | Domain calls for plant proteins without Pfam hits. | doi:[10.1126/science.adq4946](https://doi.org/10.1126/science.adq4946) · [site](https://ted.cathdb.info/) |
| CATH (2021) | database | protein-3d | Protein 3D structure | Nucleic Acids Research 2021 | Hierarchical classification of protein 3D domains. | Structural domain families. | doi:[10.1093/nar/gkaa1079](https://doi.org/10.1093/nar/gkaa1079) · [site](https://www.cathdb.info/) |
| TM-align | software | protein-3d | Protein 3D structure | Nucleic Acids Research 2005 | Structure alignment with TM-score. | Compare predicted structures. | doi:[10.1093/nar/gki524](https://doi.org/10.1093/nar/gki524) · [site](https://zhanggroup.org/TM-align/) |
| US-align | software | protein-3d | Protein 3D structure | Nature Methods 2022; release 20260527 (2026-07-19); last push 2026-10-19 | Universal structure alignment for proteins and nucleic acids. | Successor to TM-align. | doi:[10.1038/s41592-022-01585-1](https://doi.org/10.1038/s41592-022-01585-1) · [GitHub](https://github.com/pylelab/USalign) |
| DALI | software | protein-3d | Protein 3D structure | Protein Science 2020 | Structure comparison server against PDB/AlphaFold DB. | [待确认] Fold-level function hints. (site returned HTTP 500 at check) | doi:[10.1002/pro.3749](https://doi.org/10.1002/pro.3749) · [site](http://ekhidna2.biocenter.helsinki.fi/dali/) |

[Back to contents](#contents)

## enrichment

Downstream GO/KEGG enrichment.

| Name | Type | Type-class | Framework / step | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|---|---|
| topGO | software | enrichment | Downstream enrichment | Bioconductor DOI 2017 | GO enrichment accounting for GO graph topology. | Works with custom gene2GO maps. | doi:[10.18129/B9.bioc.topGO](https://doi.org/10.18129/B9.bioc.topGO) · [site](https://bioconductor.org/packages/topGO/) |
| GOATOOLS | software | enrichment | Merge / aggregate (GO propagation) | Scientific Reports 2018; last push 2026-11-02 | Python GO library: DAG propagation, slims, enrichment. | Propagate/deduplicate GO before writing merged_function_table.tsv. | doi:[10.1038/s41598-018-28948-z](https://doi.org/10.1038/s41598-018-28948-z) · [GitHub](https://github.com/tanghaibao/goatools) |
| GOseq | software | enrichment | Downstream enrichment | Genome Biology 2010 | GO enrichment correcting for length bias in RNA-seq. | RNA-seq DE gene sets. | doi:[10.1186/gb-2010-11-2-r14](https://doi.org/10.1186/gb-2010-11-2-r14) · [site](https://bioconductor.org/packages/goseq/) |
| ShinyGO | software | enrichment | Downstream enrichment | Bioinformatics 2020 | Web enrichment with plant species from Ensembl/STRING. | [待确认] Quick plots. (site returned HTTP 500 at check) | doi:[10.1093/bioinformatics/btz931](https://doi.org/10.1093/bioinformatics/btz931) · [site](http://bioinformatics.sdstate.edu/go/) |

[Back to contents](#contents)

## idea

Ideas, formats and merge rules (Merge / aggregate step).

| Name | Type | Type-class | Framework / step | Year / latest release | What it does | Plant / eukaryote relevance | Source |
|---|---|---|---|---|---|---|---|
| Evidence & Conclusion Ontology (ECO, 2022) | idea | idea | Merge / aggregate (evidence priority) | Nucleic Acids Research 2022 | Ontology of evidence types behind annotations (maps to GO evidence codes). | Record evidence per column (IEA vs ISS) in merged_function_table.tsv. | doi:[10.1093/nar/gkab1025](https://doi.org/10.1093/nar/gkab1025) · [site](https://evidenceontology.org/) |
| GO Annotation File (GAF 2.2) format | idea | idea | Merge / aggregate (export) | — | Standard tab format for gene–GO associations with evidence codes. | Optional export of merged_function_table.tsv GO column. | [site](https://geneontology.org/docs/go-annotation-file-gaf-format-2.2/) |

[Back to contents](#contents)

## First-pass entries by type-class

Every row of [`CATALOG_NEW_TOOLS_2026-11.md`](CATALOG_NEW_TOOLS_2026-11.md), given a type-class. Details and sources stay in that file.

| Type-class | Name | Type | First-pass section |
|---|---|---|---|
| homology-search | MMseqs2-GPU | software | Frame F1 — homology search step (card F1a, `F1_diamond.sh`) |
| reference-db | UniProt 2025 | database | Reference protein and structure databases |
| reference-db | Carbon Annotation Database (CADB) | database | Reference protein and structure databases |
| reference-db | Gene Ontology knowledgebase (2026) | database | Curation and community databases |
| reference-db | Ensembl Plants | database | Curation and community databases |
| domain | SMART (2021 update) ·in repo | database | Frame F1 — domain step (card F1c, `F3_interproscan.sh`) |
| domain | CDD / CD-Search (2023) | database | Frame F1 — domain step (card F1c, `F3_interproscan.sh`) |
| domain | Merizo | software | Frame F1 — domain step (card F1c, `F3_interproscan.sh`) |
| domain | DPFunc | software | Frame F1 — domain step (card F1c, `F3_interproscan.sh`) |
| orthology-go | GOMAP | software | Frame F1 — orthology-based GO/KEGG step (card F1b, `F2_eggnog.sh`) and plant GO pipelines |
| orthology-go | TRAPID 2.0 | software | Frame F1 — orthology-based GO/KEGG step (card F1b, `F2_eggnog.sh`) and plant GO pipelines |
| ml-go | DeepGO-SE | software | Optional add-on — machine-learning GO prediction (after frame F1) |
| ml-go | ProtGO | software | Optional add-on — machine-learning GO prediction (after frame F1) |
| ml-go | AltereGO | software | Optional add-on — machine-learning GO prediction (after frame F1) |
| pathway-enzyme | KEGG (2025 NAR) ·in repo | database | Pathways and enzymes (F1+ Kofam, frame F6 Mercator, other add-ons) |
| pathway-enzyme | Plant Reactome (2024) | database | Pathways and enzymes (F1+ Kofam, frame F6 Mercator, other add-ons) |
| pathway-enzyme | Plant Metabolic Network / E2P2 | database+software | Pathways and enzymes (F1+ Kofam, frame F6 Mercator, other add-ons) |
| pathway-enzyme | CLEAN | software | Pathways and enzymes (F1+ Kofam, frame F6 Mercator, other add-ons) |
| pathway-enzyme | EZpred | software | Pathways and enzymes (F1+ Kofam, frame F6 Mercator, other add-ons) |
| pathway-enzyme | ProteEC-CLA | software | Pathways and enzymes (F1+ Kofam, frame F6 Mercator, other add-ons) |
| pathway-enzyme | plantiSMASH 2.0 | software | Pathways and enzymes (F1+ Kofam, frame F6 Mercator, other add-ons) |
| pathway-enzyme | dbCAN3 ·in repo | software | Pathways and enzymes (F1+ Kofam, frame F6 Mercator, other add-ons) |
| multi-genome-orthology | PLAZA 5.0 | database | Frame F1 — orthology-based GO/KEGG step (card F1b, `F2_eggnog.sh`) and plant GO pipelines |
| multi-genome-orthology | OrthoFinder 3 | software | Frame F7 — multi-genome orthology |
| multi-genome-orthology | FastOMA | software | Frame F7 — multi-genome orthology |
| multi-genome-orthology | SonicParanoid2 | software | Frame F7 — multi-genome orthology |
| multi-genome-orthology | OrthoDB v12 | database | Frame F7 — multi-genome orthology |
| multi-genome-orthology | OMA browser 2024 | database | Frame F7 — multi-genome orthology |
| localization | DeepLoc 2.1 | software | Localization and topology (F1+ add-ons) |
| localization | TargetP 2.0 | software | Localization and topology (F1+ add-ons) |
| localization | DeepTMHMM | software | Localization and topology (F1+ add-ons) |
| plant-family | Resistify | software | Plant gene families (frame F8 NLR, frame F9 TF/kinase) |
| plant-family | NLRtracker + RefPlantNLR | software+database | Plant gene families (frame F8 NLR, frame F9 TF/kinase) |
| plant-family | NLR-Annotator | software | Plant gene families (frame F8 NLR, frame F9 TF/kinase) |
| plant-family | NLRexpress | software | Plant gene families (frame F8 NLR, frame F9 TF/kinase) |
| plant-family | NLRSeek | software | Plant gene families (frame F8 NLR, frame F9 TF/kinase) |
| plant-family | PlantTFDB / PlantRegMap | database | Plant gene families (frame F8 NLR, frame F9 TF/kinase) |
| plant-family | PlantPAN (latest) | database | Plant gene families (frame F8 NLR, frame F9 TF/kinase) |
| ncrna-function | ncPlantDB | database | Non-coding RNA function resources |
| ncrna-function | PLncDB V2.0 | database | Non-coding RNA function resources |
| ncrna-function | GreeNC 2.0 | database | Non-coding RNA function resources |
| ncrna-function | CANTATAdb 3.0 | database | Non-coding RNA function resources |
| ncrna-function | PlantCircRNA | database | Non-coding RNA function resources |
| ncrna-function | psRNATarget (2017 release) | software | Non-coding RNA function resources |
| ncrna-function | PmiREN 2.0 | database | Non-coding RNA function resources |
| expression | scPlantDB | database | Expression-supported function |
| expression | hdWGCNA | software | Expression-supported function |
| expression | CoNekT | software+database | Expression-supported function |
| community-db | Grapedia Grapevine Reference Gene Catalogue | database | Curation and community databases |
| community-db | Grape Gene Reference Catalogue (paper) | database | Curation and community databases |
| protein-3d | Foldseek | software | Frame F1 — homology search step (card F1a, `F1_diamond.sh`) |
| protein-3d | ProstT5 | software | Frame F1 — homology search step (card F1a, `F1_diamond.sh`) |
| protein-3d | TM-Vec 2s | software | Frame F1 — homology search step (card F1a, `F1_diamond.sh`) |
| protein-3d | AlphaFold Protein Structure Database (2024) | database | Reference protein and structure databases |
| protein-3d | AlphaFind v2 | software | Reference protein and structure databases |
| protein-3d | WASP | software | Protein 3D-structure-based function |
| protein-3d | PARSE | software | Protein 3D-structure-based function |
| protein-3d | metagenomic-DeepFRI | software | Protein 3D-structure-based function |
| enrichment | DAVID (2025 update) | software | Downstream enrichment |
| enrichment | g:Profiler (2023) | software | Downstream enrichment |
| enrichment | agriGO v2.0 | software | Downstream enrichment |
| enrichment | clusterProfiler 4.0 | software | Downstream enrichment |
| idea | GO specificity balance (Genome Res 2026) | idea | Optional add-on — machine-learning GO prediction (after frame F1) |
| idea | CAFA lessons (idea) | idea | Optional add-on — machine-learning GO prediction (after frame F1) |
| idea | GeneAgent | idea | Ideas — LLMs and agents in curation |
| idea | LLM-assisted Reactome annotation | idea | Ideas — LLMs and agents in curation |
| idea | Agentic AI for gene function across genomes | idea | Ideas — LLMs and agents in curation |
| idea | ProtNLM (UniProt names) | idea | Ideas — LLMs and agents in curation |

Candidates from this pass that turned out to be already in the first-pass file and were dropped: Gene Ontology (2023) (= Gene Ontology knowledgebase (2026)), OrthoFinder 2 (= OrthoFinder 3), clusterProfiler 4.0 (= clusterProfiler 4.0), g:Profiler (2023) (= g:Profiler (2023)), agriGO v2.0 (= agriGO v2.0).

[Back to contents](#contents)

## Not verified yet

- HMMER 3 [待确认]: site returned HTTP 500 at check
- eggNOG 6 [待确认]: site returned HTTP 500 at check
- PANNZER2 [待确认]: site returned HTTP 500 at check
- MetaCyc [待确认]: site returned HTTP 500 at check
- PRGdb 4.0 [待确认]: site returned HTTP 500 at check
- psRobot [待确认]: site returned HTTP 500 at check
- DALI [待确认]: site returned HTTP 500 at check
- ShinyGO [待确认]: site returned HTTP 500 at check

[Back to contents](#contents)

## How entries were checked

- Candidates came from this repo's own pipeline docs (classics already in use), standard annotation literature and the gaps left by the first pass; checked 2026-11-13 (Asia/Shanghai).
- Each DOI was resolved in Crossref (DataCite for Zenodo and Bioconductor DOIs) and the returned title matched to the tool by hand; venue and year come from that record (print year where Crossref gives one).
- GitHub repositories were read with the GitHub API (latest release tag and date, last push, archived flag). Other official pages were requested over HTTP; a non-200 answer is noted in the row and the row is marked `[待确认]` until a person opens the page.
- No tool, paper, year or DOI was added from memory without a resolved record or official page. Items that could not be resolved keep `[待确认]`.

Total: 61 new entries in this file (44 software, 11 database, 3 idea, 3 combined software/database). With the first pass: 129.
