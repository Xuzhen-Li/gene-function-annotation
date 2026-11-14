# gene-function-annotation
[中文](README.zh.md)

## Overview

This repository assigns functional labels such as names, GO/KEGG pathways, and domains to protein sequences after a structure release is available. It begins processing only after the structure pipeline outputs `proteins.faa`. It does not perform BRAKER, soft-masking, GFF editing, or gene finding. The upstream gene models are handled by [`gene-structure-annotation`](https://github.com/Xuzhen-Li/gene-structure-annotation). The boundary between structure and function is defined in [structure `docs/BOUNDARY.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/BOUNDARY.md). TE soft-masking and TE library building are excluded from this functional pipeline.

Chinese teaching: [`docs/zh/`](docs/zh/) (what it is, relationship with structure, how to run, F pipelines)
English ops: [`docs/BILINGUAL.md`](docs/BILINGUAL.md)
Plant sims (3): [`examples/plant_sim/`](examples/plant_sim/) (paired with structure Vitis+NLR, Oryza plain F1, Solanum+Mercator)

![Beginner spine](docs/figures/functional_spine.png)

The file `pipeline/F2_eggnog.sh` is the eggNOG step inside the default F1 framework, not the fast-frame branch F2.
Wiki Start-tonight: [Wiki Start-tonight](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Start-tonight) (GitHub Wiki, not in the clone).
Offline classroom: [`docs/CLASSROOM_TONIGHT.md`](docs/CLASSROOM_TONIGHT.md).
Track work: [Annotation board (Project #2)](https://github.com/users/Xuzhen-Li/projects/2).

## Concepts

1. Framework F1 / F2 / F3 / F5 denotes the whole annotation frame you claim. The default is F1, which includes DIAMOND, eggNOG, and IPS.
2. Script `F2_eggnog.sh` is the eggNOG step inside framework F1, not frame F2.
3. TOOLS F1a / F1b / F1c are literacy cards for the three F1 steps.
4. Gates such as `Gate-F1` are release hard checks, not a frame choice. Deep dive is at [`docs/zh/FAQ_入门.md`](docs/zh/FAQ_入门.md).


This page is also the 2026-11 methods catalog: 167 tools, databases and ideas in 15 type sections (updated 2026-11-14). Default frame F1 is unchanged (see Usage and `docs/ROADMAP.md`). Framework / step order stays in the roadmap and in `catalog/`.

## Usage

You must already have proteins. If not, run the structure pipeline's `flow_tool` first to get the GFF and `proteins.faa`. Refer to [`docs/HANDOFF_STRUCTURE_TO_FUNCTION.md`](docs/HANDOFF_STRUCTURE_TO_FUNCTION.md).

Auto-plan the FA frame:

```bash
git clone https://github.com/Xuzhen-Li/gene-function-annotation.git
cd gene-function-annotation
cp pipeline/flow_tool/answers.example.yaml my_answers.yaml
# edit: prefer_fast? plant add-ons?
python3 pipeline/flow_tool/flow.py --answers my_answers.yaml -o my_fa_plan.md
```

For the initial setup, finish `my_fa_plan.md` and list DB disk paths. InterProScan is not required at this stage. Check concepts at [Wiki Concepts](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Concepts) or offline at [`docs/zh/02_和结构注释的关系.md`](docs/zh/02_和结构注释的关系.md). Write `grade=` and `status=` separately. Do not write `status=F-L1`.

For cluster execution, proceed only after the [Done when](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Start-tonight#done-when) checklist is completed and `python3 pipeline/print_qc_commands.py` exits 0 with no `[STOP]`. Otherwise do not set `RUN=1`. Browsing with `--env config/example.env` will show `[STOP]` as expected. Required fields in METHODS must be draftable per [Wiki Evaluate-release](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Evaluate-release).

Follow [`docs/INSTALL_FUNCTIONAL.md`](docs/INSTALL_FUNCTIONAL.md) and [`docs/DB_INSTALL_CHECKLIST.md`](docs/DB_INSTALL_CHECKLIST.md). Then set `RUN=1` for framework F1 and complete [`docs/EVALUATION_CHECKLIST.md`](docs/EVALUATION_CHECKLIST.md). F-L1 is the acceptance bar, not a requirement to finish IPS immediately.

```bash
cp config/example.env config/local.env
# set PROTEINS_FA to your structure release proteins (one representative per gene)
# set DIAMOND_DB, EGGNOG_*, INTERPROSCAN_HOME, BUSCO_LINEAGE_PROTEIN, …
```

<details>
<summary>Namespace details</summary>

Four namespaces exist and should remain distinct in METHODS.
Framework: F1 / F2 / F3 / F5 indicates the whole annotation frame. Default F1 is DIAMOND+eggNOG+IPS.
Script filenames: `F1_diamond.sh`, `F2_eggnog.sh`, `F3_interproscan.sh` are steps inside framework F1.
TOOLS cards: F1a / F1b / F1c map to the three literacy pages.
Gates: Gate-F1 to Gate-F7 are release hard checks covering provenance, BUSCO, versions, and row counts.

The Chinese reference is [`docs/zh/FAQ_入门.md`](docs/zh/FAQ_入门.md).
</details>

## Documentation

Chinese teaching and start guide: [`docs/zh/`](docs/zh/)
Start here: [`docs/START_HERE.md`](docs/START_HERE.md)

<details>
<summary>Additional documentation</summary>

Flow tool: [`pipeline/flow_tool/`](pipeline/flow_tool/)
Install: [`docs/INSTALL_FUNCTIONAL.md`](docs/INSTALL_FUNCTIONAL.md)
Install checklist: [`docs/DB_INSTALL_CHECKLIST.md`](docs/DB_INSTALL_CHECKLIST.md)
Evaluation checklist: [`docs/EVALUATION_CHECKLIST.md`](docs/EVALUATION_CHECKLIST.md)
After structure: [`docs/POST_STRUCTURE.md`](docs/POST_STRUCTURE.md)
Stage IO: [`docs/STAGE_IO.md`](docs/STAGE_IO.md)
Roadmap: [`docs/ROADMAP.md`](docs/ROADMAP.md)
Workflow chart with frame choices and decision points (2026-11-14): [`docs/ROADMAP.md#workflow-2026-11-14`](docs/ROADMAP.md#workflow-2026-11-14)
Tool how-tos: [`docs/TOOLS.md`](docs/TOOLS.md)
Tool docs: [`docs/tools/`](docs/tools/)
Evaluation rules: [`docs/EVALUATION.md`](docs/EVALUATION.md)
QC methods and papers: [`docs/QUALITY_SOURCES.md`](docs/QUALITY_SOURCES.md)
Walkthrough: [`docs/QUICKSTART.md`](docs/QUICKSTART.md)
Mercator4 web: [`docs/MERCATOR_WHEN.md`](docs/MERCATOR_WHEN.md)
Tutorials: [`docs/TUTORIALS_AND_MEETINGS.md`](docs/TUTORIALS_AND_MEETINGS.md)
Recent high quality: [`docs/RECENT_HIGH_QUALITY.md`](docs/RECENT_HIGH_QUALITY.md)

</details>

<details>
<summary>Overview figure</summary>

![overview](docs/figures/functional_overview.png)

</details>

Author: Xuzhen Li, [ORCID](https://orcid.org/0000-0003-3670-6657)

## Methods catalog

This page lists, by type, the 167 methods, tools, databases and ideas from the 2026-11 survey (61 in the type catalog, 68 first-pass cards in `catalog/`) and the 2026-11-14 update (3 older-version entries merged, 41 added). The default frame is still F1 (DIAMOND + eggNOG + InterProScan); the catalog does not change it. Framework / step order stays in `docs/ROADMAP.md` and in `catalog/`. Full tables and errata are in `docs/CATALOG_BY_TYPE_2026-11.md` and `docs/CATALOG_NEW_TOOLS_2026-11.md`.

**2026-11-14 update.** Each section now opens with a **Clusters:** list. It groups the entries as alternatives (pick one), complementary (use together) or in order (run in sequence), with a note on when to pick which. Inside a list, “A or B” means pick one of the two and “A → B” is one fixed route. Different versions of one program are now one entry named for the latest version; older versions are only mentioned in that entry's note. A workflow chart with frame choices and decision points is in [`docs/ROADMAP.md`](docs/ROADMAP.md#workflow-2026-11-14).

## Contents

1. [Homology search](#section-1) (8)
2. [Reference sequence and ontology databases](#section-2) (11)
3. [Domain and family annotation](#section-3) (6)
4. [Orthology-based names, GO and KEGG](#section-4) (12)
5. [Machine-learning GO prediction](#section-5) (10)
6. [Pathways, KO and EC](#section-6) (17)
7. [Multi-genome orthology](#section-7) (11)
8. [Localization and topology](#section-8) (10)
9. [Plant gene families](#section-9) (16)
10. [Non-coding RNA function resources](#section-10) (11)
11. [Expression-supported function](#section-11) (8)
12. [Community catalogues and naming](#section-12) (4)
13. [Protein 3D structure](#section-13) (22)
14. [Downstream enrichment](#section-14) (12)
15. [Ideas, formats and merge rules](#section-15) (9)

- [Data needed alongside the proteins](#data-needs)
- [Figure credits](#figure-credits)

How the sections line up with this repo: input QC (F0) is under data needs, not a type section → default frame F1 (homology, domains, orthology/GO) → optional add-ons (pathways, multi-genome, localization, plant families) → merge `merged_function_table.tsv` → release. Frame IDs stay in `docs/ROADMAP.md` and `catalog/`.

<a id="section-1"></a>
## 1. Homology search

Sequence similarity engines used in the frame F1 homology-search step.

**Needs:** a local DIAMOND (or BLAST) database, typically Swiss-Prot or a documented equivalent, with the version recorded in METHODS. [Data needs by scenario](#data-needs)

**Clusters:**
- *Fast pairwise search* (alternatives): DIAMOND (v2), MMseqs2, BLAST+. DIAMOND is the F1 default; use MMseqs2 (CPU or GPU) for clustering and very large sets, and BLAST+ for small reference checks.
- *Profile search* (complementary): HMMER 3, HH-suite3. Use HMMER for Pfam-style HMMs and HH-suite3 for profile-profile hits on difficult cases.
- *Language-model remote homology* (alternatives): PLMSearch, pLM-BLAST, Dense Homolog Retriever (DHR). Use only for proteins without hits after DIAMOND and HMMER; report them as a separate evidence class.


- **BLAST+** (tool) — NCBI BLAST command-line suite (blastp, makeblastdb). [doi:10.1186/1471-2105-10-421](https://doi.org/10.1186/1471-2105-10-421) · [link](https://blast.ncbi.nlm.nih.gov/)
- **DIAMOND (v2)** (tool) — Fast protein aligner with BLAST-like sensitivity modes (--ultra-sensitive). [doi:10.1038/s41592-021-01101-x](https://doi.org/10.1038/s41592-021-01101-x) · [link](https://github.com/bbuchfink/diamond)
- **MMseqs2** (tool) — Fast, sensitive protein search and clustering. The GPU-accelerated release (MMseqs2-GPU, doi:10.1038/s41592-025-02819-8) uses the same codebase and also accelerates ColabFold MSAs. [doi:10.1038/nbt.3988](https://doi.org/10.1038/nbt.3988) · [link](https://github.com/soedinglab/MMseqs2)
- **HMMER 3** (tool) — Profile HMM search (hmmscan, hmmsearch, jackhmmer). [doi:10.1371/journal.pcbi.1002195](https://doi.org/10.1371/journal.pcbi.1002195) · [link](https://github.com/EddyRivasLab/hmmer) [待确认]
- **HH-suite3** (tool) — HMM-HMM comparison for remote homology (HHblits, HHsearch). [doi:10.1186/s12859-019-3019-7](https://doi.org/10.1186/s12859-019-3019-7) · [link](https://github.com/soedinglab/hh-suite)
- **PLMSearch** (tool) — Detects remote homologs by comparing protein language-model embeddings; recovers low-identity hits missed by BLAST and DIAMOND. [doi:10.1038/s41467-024-46808-5](https://doi.org/10.1038/s41467-024-46808-5) · [link](https://github.com/maovshao/PLMSearch)
- **pLM-BLAST** (tool) — Performs local alignment of per-residue language-model embeddings to detect distant homology and identify matching regions. [doi:10.1093/bioinformatics/btad579](https://doi.org/10.1093/bioinformatics/btad579) · [link](https://github.com/labstructbioinf/pLM-BLAST)
- **Dense Homolog Retriever (DHR)** (tool) — Fast, sensitive remote-homolog search based on dense retrieval; also builds MSAs for structure prediction. [doi:10.1038/s41587-024-02353-6](https://doi.org/10.1038/s41587-024-02353-6) · [link](https://github.com/ml4bio/Dense-Homolog-Retrieval)

<a id="section-2"></a>
## 2. Reference sequence and ontology databases

Reference sequence and ontology databases that the search and naming steps need.

**Needs:** the database files themselves (UniProt, GO, eggNOG, InterPro member data, and so on), with versions. These are not computed from the proteins alone. [Data needs by scenario](#data-needs)

**Clusters:**
- *Sequence targets* (complementary): UniRef, UniProt 2025, TAIR, Ensembl Plants, Carbon Annotation Database (CADB). Swiss-Prot is the F1 DIAMOND target; UniRef for wider coverage; TAIR and Swiss-Prot for curated names.
- *Signatures and families* (complementary): Pfam (2025), InterPro 2025, eggNOG 6. Pfam and InterPro power InterProScan; eggNOG 6 powers eggNOG-mapper.
- *Ontologies, reactions and networks* (complementary): Gene Ontology knowledgebase (2026), Rhea, STRING (2025). Pin the GO release; use Rhea for exact reactions and STRING for network context.


- **UniRef** (resource) — Clustered UniProt sets (UniRef100/90/50). [doi:10.1093/bioinformatics/btu739](https://doi.org/10.1093/bioinformatics/btu739) · [link](https://www.uniprot.org/help/uniref)
- **Pfam (2025)** (resource) — Protein family HMM library now hosted in InterPro; the 2025 paper covers AI-assisted family building. Earlier paper: Pfam 2021 (doi:10.1093/nar/gkaa913). [doi:10.1093/nar/gkae997](https://doi.org/10.1093/nar/gkae997) · [link](https://www.ebi.ac.uk/interpro/entry/pfam/)
- **TAIR** (resource) — The Arabidopsis Information Resource: curated Arabidopsis gene function and nomenclature. [doi:10.1002/dvg.22877](https://doi.org/10.1002/dvg.22877) · [link](https://www.arabidopsis.org/)
- **eggNOG 6** (resource) — Hierarchical orthology database behind eggNOG-mapper. [doi:10.1093/nar/gkac1022](https://doi.org/10.1093/nar/gkac1022) · [link](http://eggnog6.embl.de/) [待确认]
- **UniProt 2025** (resource) — Swiss-Prot/TrEMBL reference; cite the current NAR update for METHODS. [doi:10.1093/nar/gkae1010](https://doi.org/10.1093/nar/gkae1010) · [link](https://www.uniprot.org)
- **Carbon Annotation Database (CADB)** (resource) — Predicted protein-coding loci and proteins for ~48k GenBank eukaryote assemblies (Carbon-A). [doi:10.64898/2026.10.20.760448](https://doi.org/10.64898/2026.10.20.760448) · [link](https://huggingface.co/blog/HuggingFaceBio/carbon-annotator-genbank-genome-annotation)
- **Gene Ontology knowledgebase (2026)** (resource) — Current GO release paper (NAR, issue 2026; a correction notice exists, doi 10.1093/nar/gkag678). [doi:10.1093/nar/gkaf1292](https://doi.org/10.1093/nar/gkaf1292) · [link](https://geneontology.org)
- **Ensembl Plants** (resource) — Plant genomes with gene trees and projected annotation. [link](https://plants.ensembl.org)
- **InterPro 2025** (resource) — Integrated signature database behind InterProScan; the 2025 release adds AI-curated Pfam families and structure-based views. [doi:10.1093/nar/gkae1082](https://doi.org/10.1093/nar/gkae1082) · [link](https://www.ebi.ac.uk/interpro/)
- **Rhea** (resource) — Expert-curated biochemical reaction database used by UniProt for enzyme annotation; links EC numbers to exact reactions. [doi:10.1093/nar/gkab1016](https://doi.org/10.1093/nar/gkab1016) · [link](https://www.rhea-db.org/)
- **STRING (2025)** (resource) — Protein association networks across thousands of genomes, including Vitis; supports network-based function inference and enrichment. [doi:10.1093/nar/gkae1113](https://doi.org/10.1093/nar/gkae1113) · [link](https://string-db.org/)

<a id="section-3"></a>
## 3. Domain and family annotation

Domain and family annotation in the frame F1 domain step (InterProScan and related data).

**Needs:** a working InterProScan install and its data; this step is slow and is part of default frame F1, but F-L1 does not require finishing IPS the same day. [Data needs by scenario](#data-needs)

**Clusters:**
- *HMM signatures* (complementary): InterProScan 6, SMART (2021 update), CDD / CD-Search (2023). InterProScan is the F1 default; use SMART and CDD for signalling and domain-architecture checks.
- *Family-tree placement* (in order): PANTHER, TreeGrafter. TreeGrafter places proteins onto PANTHER trees for phylogenetic GO assignment.

![InterPro PIK3CA domains](docs/figures/catalog/04_interpro_pik3ca_domains.jpg)

*InterPro domain annotation of PIK3CA (Fig. 4). Blum, Andreeva, Florentino et al. 2025, Nucleic Acids Res., Fig. 4, doi:10.1093/nar/gkae1082, PMC11701551, CC BY.*

![InterProScan human runtime](docs/figures/catalog/05_interproscan_human_runtime.jpg)

*InterProScan runtime on a human proteome (Fig. 6). Blum, Andreeva, Florentino et al. 2025, Nucleic Acids Res., Fig. 6, doi:10.1093/nar/gkae1082, PMC11701551, CC BY.*

- **InterProScan 6** (tool) — Runs InterPro member databases (Pfam, PANTHER, SMART, CDD, Gene3D…) and maps InterPro2GO. Version 6 (2025–2026 Nextflow releases) is current, while the citable paper remains InterProScan 5. This repo's F1 runner was written for v5 [待确认: test v6 output columns before switching]. [doi:10.1093/bioinformatics/btu031](https://doi.org/10.1093/bioinformatics/btu031) · [link](https://github.com/ebi-pf-team/interproscan6)
- **SMART (2021 update)** (resource) — Signalling/extracellular domain resource (member DB of InterPro). [doi:10.1093/nar/gkaa937](https://doi.org/10.1093/nar/gkaa937) · [link](https://smart.embl.de)
- **CDD / CD-Search (2023)** (resource) — NCBI conserved-domain models and SPARCLE architectures. [doi:10.1093/nar/gkac1096](https://doi.org/10.1093/nar/gkac1096) · [link](https://www.ncbi.nlm.nih.gov/Structure/cdd/cdd.shtml)
- **PANTHER** (resource) — Phylogenetic protein families and subfamilies with tree-inferred GO annotations; InterProScan can report PANTHER hits. [doi:10.1002/pro.4218](https://doi.org/10.1002/pro.4218) · [link](https://www.pantherdb.org/)
- **TreeGrafter** (tool) — Grafts query proteins onto PANTHER family trees and transfers GO terms from the nearest annotated ancestor. [doi:10.1093/bioinformatics/bty625](https://doi.org/10.1093/bioinformatics/bty625) · [link](https://github.com/pantherdb/TreeGrafter)
- **ProteInfer** (tool) — Deep neural network that predicts Pfam, EC and GO labels directly from sequence; provides a fast check for proteins without HMM hits. [doi:10.7554/eLife.80942](https://doi.org/10.7554/eLife.80942) · [link](https://github.com/google-research/proteinfer)

<a id="section-4"></a>
## 4. Orthology-based names, GO and KEGG

Orthology or similarity-based names, GO and KEGG, including whole frames (F1 orthology step, fast frame F2, EnTAP frame F3, F4 readable names).

**Needs:** the eggNOG-mapper database (and, for names, optional AHRD / PANNZER inputs). Machine-assigned GO remains electronic evidence (IEA). [Data needs by scenario](#data-needs)

**Clusters:**
- *Readable names* (alternatives): AHRD, PANNZER2, Sma3s v2. AHRD is the F4 default; PANNZER2 adds scored GO predictions.
- *All-in-one suites* (alternatives): EnTAP, Trinotate, Blast2GO, FA-nf, GOMAP, TRAPID 2.0. Alternatives to F1 rather than add-ons: EnTAP (F3), Trinotate (F5); GOMAP is plant-focused, and Blast2GO is commercial.
- *Orthology and placement* (complementary): eggNOG-mapper v2, OMAmer, FANTASIA. eggNOG-mapper v2 is the F1 default for GO, KEGG and EC; OMAmer for quick family placement; FANTASIA only for proteins with no homology hits.

![eggNOG-mapper v2 runtime](docs/figures/catalog/01_eggnogmapper_v2_runtime.jpg)

*eggNOG-mapper v2 runtime compared with other annotators (Fig. 2). Cantalapiedra et al. 2021, Mol. Biol. Evol., Fig. 2, doi:10.1093/molbev/msab293, PMC8662613, CC BY.*

![eggNOG-mapper versus InterProScan](docs/figures/catalog/02_eggnogmapper_vs_interproscan.jpg)

*eggNOG-mapper compared with InterProScan (Fig. 3). Huerta-Cepas et al. 2017, Mol. Biol. Evol., Fig. 3, doi:10.1093/molbev/msx148, PMC5850834, CC BY.*

![eggNOG-mapper GO example](docs/figures/catalog/03_eggnogmapper_rhogap1_go.jpg)

*eggNOG-mapper GO assignment on a worked example (Fig. 4). Huerta-Cepas et al. 2017, Mol. Biol. Evol., Fig. 4, doi:10.1093/molbev/msx148, PMC5850834, CC BY.*

- **eggNOG-mapper v2** (tool) — Orthology-based functional annotation: names, GO, KEGG, EC, COG. [doi:10.1093/molbev/msab293](https://doi.org/10.1093/molbev/msab293) · [link](https://github.com/eggnogdb/eggnog-mapper)
- **PANNZER2** (tool) — Fast web/standalone GO and free-text description prediction. [doi:10.1093/nar/gky350](https://doi.org/10.1093/nar/gky350) · [link](http://ekhidna2.biocenter.helsinki.fi/sanspanz/) [待确认]
- **Blast2GO** (tool) — BLAST-based GO annotation and visualisation (now in commercial OmicsBox). [doi:10.1093/bioinformatics/bti610](https://doi.org/10.1093/bioinformatics/bti610) · [link](https://www.biobam.com/omicsbox/)
- **EnTAP** (tool) — Eukaryotic non-model annotation pipeline: filtering, similarity search, contaminant flags, eggNOG and InterPro. [doi:10.1111/1755-0998.13106](https://doi.org/10.1111/1755-0998.13106) · [link](https://github.com/harta55/EnTAP)
- **FA-nf** (tool) — Nextflow functional annotation pipeline for non-model proteins (BLAST, InterProScan, KEGG, signal peptides). [doi:10.3390/genes12101645](https://doi.org/10.3390/genes12101645) · [link](https://github.com/guigolab/FA-nf)
- **Sma3s v2** (tool) — Functional annotation of proteomes/transcriptomes against UniProt (GO, keywords, pathways). [doi:10.1002/pmic.201700071](https://doi.org/10.1002/pmic.201700071) · [link](https://github.com/UPOBioinfo/sma3s)
- **AHRD** (tool) — Automated assignment of Human Readable Descriptions from BLAST results. [link](https://github.com/groupschoof/AHRD)
- **GOMAP** (tool) — Gene Ontology Meta Annotator for Plants: combines sequence similarity, domains and mixed-method predictors into plant GO sets. [doi:10.1186/s13007-021-00754-1](https://doi.org/10.1186/s13007-021-00754-1) · [link](https://github.com/Dill-PICL/GOMAP)
- **TRAPID 2.0** (tool) — Web app for taxonomic and functional analysis of de novo plant transcriptomes using PLAZA references. [doi:10.1093/nar/gkab565](https://doi.org/10.1093/nar/gkab565) · [link](https://bioinformatics.psb.ugent.be/trapid_02/) [待确认]
- **OMAmer** (tool) — Alignment-free placement of proteins into OMA hierarchical orthologous groups; fast and subfamily-aware (also used by OMArk). [doi:10.1093/bioinformatics/btab219](https://doi.org/10.1093/bioinformatics/btab219) · [link](https://github.com/DessimozLab/omamer)
- **FANTASIA** (tool) — Transfers GO terms via embedding similarity across whole proteomes; targets "dark" proteins with no homology-based annotation. [doi:10.1038/s42003-025-08651-2](https://doi.org/10.1038/s42003-025-08651-2) · [link](https://github.com/CBBIO/FANTASIA)
- **Trinotate** (tool) — Annotation suite for de novo transcriptome peptides (loads BLAST, Pfam, SignalP and GO results into SQLite); serves as the F5 path. The cited study is the reference requested by the authors. [doi:10.1016/j.celrep.2016.12.063](https://doi.org/10.1016/j.celrep.2016.12.063) · [link](https://github.com/Trinotate/Trinotate)

<a id="section-5"></a>
## 5. Machine-learning GO prediction

Machine-learning GO prediction. Optional add-ons after frame F1, not a replacement for F1.

**Needs:** usually only the proteins, plus the tool’s own models. These are optional add-ons after frame F1, not a replacement for F1. [Data needs by scenario](#data-needs)

**Clusters:**
- *Sequence and language-model predictors* (alternatives): DeepGO-SE, GoPredSim, SPROF-GO, TALE, NetGO 3.0, ProtGO, AltereGO, DeepGOPlus. Prefer DeepGO-SE or GoPredSim to fill gaps left by F1; use DeepGOPlus mainly to reproduce older tables. Keep ML GO predictions in a separate evidence column.
- *Structure-aware predictors* (alternatives): DeepFRI, DPFunc. Require predicted structures (section 13); useful for divergent protein families.


- **DeepGOPlus** (tool) — CNN + DIAMOND GO prediction from sequence. [doi:10.1093/bioinformatics/btz595](https://doi.org/10.1093/bioinformatics/btz595) · [link](https://github.com/bio-ontology-research-group/deepgoplus)
- **NetGO 3.0** (tool) — Protein-language-model GO prediction server (CAFA top performer). [doi:10.1016/j.gpb.2023.04.001](https://doi.org/10.1016/j.gpb.2023.04.001)
- **DeepFRI** (tool) — Predicts protein function from 3D structure and sequence using graph convolutional networks. A scaled pipeline, metagenomic-DeepFRI (preprint 2026, doi:10.64898/2026.04.27.720983), applies the same method to large protein sets. [doi:10.1038/s41467-021-23303-9](https://doi.org/10.1038/s41467-021-23303-9) · [link](https://github.com/flatironinstitute/DeepFRI)
- **GoPredSim** (tool) — GO transfer by embedding similarity (SeqVec/ProtT5). [doi:10.1038/s41598-020-80786-0](https://doi.org/10.1038/s41598-020-80786-0) · [link](https://github.com/Rostlab/goPredSim)
- **DeepGO-SE** (tool) — GO prediction as approximate semantic entailment over ESM2 embeddings and GO axioms. [doi:10.1038/s42256-024-00795-w](https://doi.org/10.1038/s42256-024-00795-w) · [link](https://github.com/bio-ontology-research-group/deepgo2)
- **ProtGO** (tool) — Multi-modal GO prediction (PLM + text + taxonomy + GO graph). [doi:10.1093/bioinformatics/btaf390](https://doi.org/10.1093/bioinformatics/btaf390) · [link](https://github.com/sunyatawang/ProtGO)
- **AltereGO** (tool) — Score-level fusion of ESM2, ProtT5, Ankh and ProstT5-3Di predictors for GO molecular function (preprint 2026). [doi:10.64898/2026.10.23.761425](https://doi.org/10.64898/2026.10.23.761425)
- **DPFunc** (tool) — Deep learning GO prediction guided by domain + 3D-structure information. [doi:10.1038/s41467-024-54816-8](https://doi.org/10.1038/s41467-024-54816-8) · [link](https://github.com/CSUBioGroup/DPFunc)
- **SPROF-GO** (tool) — Predicts GO terms by combining protein language-model features with homology-based label diffusion. [doi:10.1093/bib/bbad117](https://doi.org/10.1093/bib/bbad117) · [link](https://github.com/biomed-AI/SPROF-GO)
- **TALE** (tool) — Transformer model that jointly embeds sequences and GO labels so it can rank rarely annotated terms. [doi:10.1093/bioinformatics/btab198](https://doi.org/10.1093/bioinformatics/btab198) · [link](https://github.com/Shen-Lab/TALE)

<a id="section-6"></a>
## 6. Pathways, KO and EC

Pathways, KO and EC (F1+ Kofam, frame F6 MapMan, and related add-ons).

**Needs:** for Kofam / KO, a hidden-Markov model set and its score thresholds; for MapMan (F6), a Mercator4 result (web or local — see `docs/MERCATOR_WHEN.md`). KEGG redistribution rules are `[待确认]` and are not assumed here. [Data needs by scenario](#data-needs)

**Clusters:**
- *KO assignment* (alternatives): KofamKOALA / KofamScan, BlastKOALA / GhostKOALA, KAAS. KofamScan runs locally (F1+ optional); BlastKOALA and KAAS are web-based alternatives.
- *Plant pathway frames and enzyme reference* (complementary): MapMan4 / Mercator4, Plant Reactome (2024), Plant Metabolic Network / E2P2, Pathway Tools, MetaCyc, KEGG (2025 NAR), BRENDA. Mercator4 (F6) for plant BINs; E2P2 predicts enzymes and Pathway Tools then builds a grape pathway database; BRENDA is the enzyme reference for checking EC calls.
- *EC predictors* (alternatives): DeepEC, CLEAN, EZpred, ProteEC-CLA. CLEAN first for enzymes without KO; check the calls against BRENDA.
- *Completeness and clusters* (complementary): KEGG Mapper, kegg-pathways-completeness, plantiSMASH 2.0. Assess pathway completeness from KO sets; use plantiSMASH for biosynthetic gene clusters.


- **MapMan4 / Mercator4** (tool / resource) — Plant-specific functional bins (MapMan4) assigned by Mercator4. [doi:10.1016/j.molp.2019.01.003](https://doi.org/10.1016/j.molp.2019.01.003) · [link](https://www.plabipd.de/mercator_main.html)
- **KofamKOALA / KofamScan** (tool) — KEGG Orthology assignment with adaptive-threshold profile HMMs. [doi:10.1093/bioinformatics/btz859](https://doi.org/10.1093/bioinformatics/btz859) · [link](https://www.genome.jp/tools/kofamkoala/)
- **BlastKOALA / GhostKOALA** (tool) — KEGG web servers assigning KO numbers by sequence similarity. [doi:10.1016/j.jmb.2015.11.006](https://doi.org/10.1016/j.jmb.2015.11.006) · [link](https://www.kegg.jp/blastkoala/)
- **KEGG Mapper** (tool) — Maps KO lists onto KEGG pathways, BRITE and modules. [doi:10.1002/pro.3711](https://doi.org/10.1002/pro.3711) · [link](https://www.kegg.jp/kegg/mapper/)
- **kegg-pathways-completeness** (tool) — Computes KEGG module completeness from a KO list. [link](https://github.com/EBI-Metagenomics/kegg-pathways-completeness-tool)
- **MetaCyc** (resource) — Curated metabolic pathways and enzymes across life. [doi:10.1093/nar/gkz862](https://doi.org/10.1093/nar/gkz862) · [link](https://metacyc.org/) [待确认]
- **BRENDA** (resource) — Comprehensive enzyme function database (EC). [doi:10.1093/nar/gkaa1025](https://doi.org/10.1093/nar/gkaa1025) · [link](https://www.brenda-enzymes.org/)
- **DeepEC** (tool) — Deep-learning EC number prediction. [doi:10.1073/pnas.1821905116](https://doi.org/10.1073/pnas.1821905116)
- **KEGG (2025 NAR)** (resource) — Current KEGG citation for KO/pathway mapping. [doi:10.1093/nar/gkae909](https://doi.org/10.1093/nar/gkae909) · [link](https://www.kegg.jp)
- **Plant Reactome (2024)** (resource) — Curated plant pathways (rice reference, projected to other plants). [doi:10.1093/nar/gkad1052](https://doi.org/10.1093/nar/gkad1052) · [link](https://plantreactome.gramene.org) [待确认]
- **Plant Metabolic Network / E2P2** (tool / resource) — PlantCyc and species pathway DBs built with the E2P2 enzyme predictor. [link](https://plantcyc.org) [待确认]
- **CLEAN** (tool) — Contrastive-learning EC number prediction. [doi:10.1126/science.adf2465](https://doi.org/10.1126/science.adf2465) · [link](https://github.com/tttianhao/CLEAN)
- **EZpred** (tool) — EC prediction using unlabeled sequence homologs (Advanced Science 2026). [doi:10.1002/advs.78703](https://doi.org/10.1002/advs.78703) [待确认]
- **ProteEC-CLA** (tool) — EC prediction with contrastive learning + agent attention on ESM2. [doi:10.1002/prot.26822](https://doi.org/10.1002/prot.26822)
- **plantiSMASH 2.0** (tool) — Plant biosynthetic gene cluster detection, substrate prediction for some enzyme families, promoter TF sites; DB of ~30k BGCs over 430 genomes. [doi:10.1016/j.jmb.2026.169798](https://doi.org/10.1016/j.jmb.2026.169798) · [link](https://github.com/plantismash/plantismash)
- **KAAS** (tool) — KEGG web server that assigns KO numbers via bidirectional best hits and reconstructs pathway maps. [doi:10.1093/nar/gkm321](https://doi.org/10.1093/nar/gkm321) · [link](https://www.genome.jp/kegg/kaas/)
- **Pathway Tools** (tool) — Builds an organism-specific pathway/genome database; in the PMN pipeline E2P2 first predicts enzymes, then Pathway Tools builds the database (as for PlantCyc). [doi:10.1093/bib/bbz104](https://doi.org/10.1093/bib/bbz104) · [link](https://bioinformatics.ai.sri.com/ptools/)

<a id="section-7"></a>
## 7. Multi-genome orthology

Orthogroups across genomes. Frame F7 annotates orthogroup representatives, not every gene.

**Needs:** protein FASTA from each genome in the panel. Frame F7 annotates orthogroup representatives, not every gene. [Data needs by scenario](#data-needs)

**Clusters:**
- *Orthogroup inference* (alternatives): OrthoFinder 3, SonicParanoid2, Broccoli, Proteinortho6, FastOMA. OrthoFinder 3 is the F7 default; use FastOMA or SonicParanoid2 for very large panels.
- *Reference catalogues* (complementary): PLAZA 5.0, OrthoDB v12, OMA browser 2024, PhylomeDB V5, OrthoVenn3. Cross-check orthogroups against plant and tree-based references.
- *Family evolution* (in order): OrthoFinder 3 or SonicParanoid2 or Broccoli or Proteinortho6 or FastOMA, CAFE 5. Fix orthogroups first, then estimate expansion and contraction with CAFE 5.

![OrthoFinder Chordata](docs/figures/catalog/06_orthofinder_chordata_summary.jpg)

*OrthoFinder summary for a Chordata example (Fig. 3). Emms and Kelly 2019, Genome Biol., Fig. 3, doi:10.1186/s13059-019-1832-y, PMC6857279, CC BY.*

- **Broccoli** (tool) — Orthology via phylogeny and network label propagation. [doi:10.1093/molbev/msaa159](https://doi.org/10.1093/molbev/msaa159) · [link](https://github.com/rderelle/Broccoli)
- **Proteinortho6** (tool) — Graph-based (co-)orthology detection at scale. [doi:10.3389/fbinf.2023.1322477](https://doi.org/10.3389/fbinf.2023.1322477) · [link](https://gitlab.com/paulklemm_PHD/proteinortho)
- **CAFE 5** (tool) — Gene family expansion/contraction under rate variation. [doi:10.1093/bioinformatics/btaa1022](https://doi.org/10.1093/bioinformatics/btaa1022) · [link](https://github.com/hahnlab/CAFE5)
- **PLAZA 5.0** (resource) — Plant comparative genomics: gene families, orthologs, GO/InterPro projections. [doi:10.1093/nar/gkab1024](https://doi.org/10.1093/nar/gkab1024) · [link](https://bioinformatics.psb.ugent.be/plaza/) [待确认]
- **OrthoFinder 3** (tool) — Scalable phylogenetic orthology (v3.x, FAMSA alignment). [doi:10.1101/2025.07.15.664860](https://doi.org/10.1101/2025.07.15.664860) · [link](https://github.com/OrthoFinder/OrthoFinder)
- **FastOMA** (tool) — Linear-scaling orthology inference (OMAmer placement). [doi:10.1038/s41592-024-02552-8](https://doi.org/10.1038/s41592-024-02552-8) · [link](https://github.com/DessimozLab/FastOMA)
- **SonicParanoid2** (tool) — Fast orthology with ML and language models. [doi:10.1186/s13059-024-03298-4](https://doi.org/10.1186/s13059-024-03298-4) · [link](https://gitlab.com/salvo981/sonicparanoid2)
- **OrthoDB v12** (resource) — Hierarchical orthologs with functional descriptors (OrthoDB + BUSCO update paper). [doi:10.1093/nar/gkae987](https://doi.org/10.1093/nar/gkae987) · [link](https://www.orthodb.org)
- **OMA browser 2024** (resource) — OMA orthology resource update. [doi:10.1093/nar/gkad1020](https://doi.org/10.1093/nar/gkad1020) · [link](https://omabrowser.org)
- **OrthoVenn3** (tool) — Web platform for clustering and comparing orthologous groups across multiple genomes, with Venn and phylogenetic views. [doi:10.1093/nar/gkad313](https://doi.org/10.1093/nar/gkad313) · [link](https://orthovenn3.bioinfotoolkits.net/)
- **PhylomeDB V5** (resource) — Genome-wide catalogues of gene trees and tree-based orthology predictions; serves as a check on graph-based orthogroups. [待确认: phylomedb.org returned 503 on 2026-11-14] [doi:10.1093/nar/gkab966](https://doi.org/10.1093/nar/gkab966)

<a id="section-8"></a>
## 8. Localization and topology

Signal peptides, topology and subcellular localization (F1+ add-ons).

**Needs:** usually only the proteins (SignalP, TargetP and similar). Keep these as F1+ add-on columns, not as a second master table. [Data needs by scenario](#data-needs)

**Clusters:**
- *Signal peptide and topology* (complementary): SignalP 6.0, DeepTMHMM or TMbed or TMHMM 2.0 or Phobius. SignalP 6.0 for signal peptides plus one topology tool: DeepTMHMM or TMbed by default, TMHMM 2.0 only to reproduce older tables. Phobius and TMbed also call signal peptides.
- *Organelle targeting* (alternatives): TargetP 2.0, LOCALIZER, DeepLoc 2.1, WoLF PSORT. Use TargetP 2.0 for plastid and mitochondrial targeting, and DeepLoc 2.1 for multi-compartment calls.
- *Plant secretome* (in order): SignalP 6.0, ApoplastP. After SignalP, ApoplastP separates apoplastic proteins.


- **SignalP 6.0** (tool) — Signal peptide prediction (all five types) with protein language model. [doi:10.1038/s41587-021-01156-3](https://doi.org/10.1038/s41587-021-01156-3) · [link](https://services.healthtech.dtu.dk/services/SignalP-6.0/)
- **TMHMM 2.0** (tool) — Transmembrane helix prediction (HMM). [doi:10.1006/jmbi.2000.4315](https://doi.org/10.1006/jmbi.2000.4315) · [link](https://services.healthtech.dtu.dk/services/TMHMM-2.0/)
- **Phobius** (tool) — Combined transmembrane topology and signal peptide predictor. [doi:10.1016/j.jmb.2004.03.016](https://doi.org/10.1016/j.jmb.2004.03.016) · [link](https://phobius.sbc.su.se/)
- **WoLF PSORT** (tool) — Subcellular localization prediction with a plant model. [doi:10.1093/nar/gkm259](https://doi.org/10.1093/nar/gkm259) · [link](https://wolfpsort.hgc.jp/)
- **LOCALIZER** (tool) — Predicts chloroplast, mitochondrial and nuclear localization of plant and effector proteins. [doi:10.1038/srep44598](https://doi.org/10.1038/srep44598) · [link](https://localizer.csiro.au/)
- **DeepLoc 2.1** (tool) — Subcellular localization + membrane protein type from PLMs. [doi:10.1093/nar/gkae237](https://doi.org/10.1093/nar/gkae237) · [link](https://services.healthtech.dtu.dk/services/DeepLoc-2.1/)
- **TargetP 2.0** (tool) — N-terminal targeting peptides (signal, mitochondrial, chloroplast, thylakoid). [doi:10.26508/lsa.201900429](https://doi.org/10.26508/lsa.201900429) · [link](https://services.healthtech.dtu.dk/services/TargetP-2.0/)
- **DeepTMHMM** (tool) — Transmembrane topology prediction (preprint). [doi:10.1101/2022.04.08.487609](https://doi.org/10.1101/2022.04.08.487609) · [link](https://dtu.biolib.com/DeepTMHMM)
- **TMbed** (tool) — Predicts transmembrane helices, beta-barrels and signal peptides from ProtT5 embeddings; fast across whole proteomes. [doi:10.1186/s12859-022-04873-x](https://doi.org/10.1186/s12859-022-04873-x) · [link](https://github.com/BernhoferM/TMbed)
- **ApoplastP** (tool) — Predicts whether a plant or effector protein localises to the apoplast; complements SignalP when defining a secretome. [doi:10.1111/nph.14946](https://doi.org/10.1111/nph.14946) · [link](https://apoplastp.csiro.au/)

<a id="section-9"></a>
## 9. Plant gene families

Plant gene-family classifiers (frame F8 NLR, frame F9 TF/kinase).

**Needs:** for NLR (F8), InterProScan output and optional HRP window lists; for TF / kinase (F9), iTAK (or a documented equivalent). Skip F8 if there is no disease / NLR story. [Data needs by scenario](#data-needs)

**Clusters:**
- *Transcription factors and kinases* (complementary): iTAK, TAPscan v4, PlantTFDB / PlantRegMap, PlantPAN (latest), JASPAR 2026. Use iTAK or TAPscan for family classification, and PlantTFDB, PlantPAN and JASPAR for binding motifs.
- *NLR calls on proteins* (alternatives): NLRtracker + RefPlantNLR, Resistify, NLRexpress, RGAugury. F8: NLRtracker works on InterProScan output; Resistify works directly on protein sequences; compare the two. PRGdb 4.0 is the reference database for resistance genes.
- *NLR loci on the genome* (alternatives): NLR-Annotator, NLRSeek. Pick one; either complements the protein calls, because many NLRs are missed by gene annotation. NLR-Annotator alone finds NLR loci on the genome without gene models (structure layer); NLRSeek already runs NLR-Annotator and adds targeted re-annotation and NLRtracker.
- *Enzyme and transporter classes* (complementary): dbCAN3, CAZy, MEROPS, TCDB (2021). dbCAN3 assigns CAZy families; use MEROPS for proteases and TCDB for transporters.


- **iTAK** (tool) — Plant transcription factor and protein kinase identification and classification. [doi:10.1016/j.molp.2016.09.014](https://doi.org/10.1016/j.molp.2016.09.014) · [link](https://github.com/kentnf/iTAK)
- **TAPscan v4** (tool / resource) — Detects transcription-associated proteins with family rules; streptophyte-wide database. [doi:10.1111/tpj.17184](https://doi.org/10.1111/tpj.17184) · [link](https://tapscan.plantcode.cup.uni-freiburg.de/)
- **PRGdb 4.0** (tool / resource) — Plant resistance gene database with DRAGO annotation pipeline. [doi:10.1093/nar/gkab1087](https://doi.org/10.1093/nar/gkab1087) · [link](http://prgdb.org/) [待确认]
- **RGAugury** (tool) — Pipeline identifying resistance gene analogs (NBS, RLK, RLP). [doi:10.1186/s12864-016-3197-x](https://doi.org/10.1186/s12864-016-3197-x) · [link](https://bitbucket.org/yaanlpc/rgaugury)
- **Resistify** (tool) — Fast NLR identification/classification from proteins using NLRexpress motifs. [doi:10.1177/11779322241308944](https://doi.org/10.1177/11779322241308944) · [link](https://github.com/SwiftSeal/resistify)
- **NLRtracker + RefPlantNLR** (tool / resource) — Extracts and classifies NLRs from proteomes/transcripts using features of RefPlantNLR. [doi:10.1371/journal.pbio.3001124](https://doi.org/10.1371/journal.pbio.3001124) · [link](https://github.com/slt666666/NLRtracker)
- **NLR-Annotator** (tool) — Annotation-independent NLR locus finder on genomic sequence. [doi:10.1104/pp.19.01273](https://doi.org/10.1104/pp.19.01273) · [link](https://github.com/steuernb/NLR-Annotator)
- **NLRexpress** (tool) — ML motif predictors for CC/TIR/NB-ARC/LRR motifs. [doi:10.3389/fpls.2022.975888](https://doi.org/10.3389/fpls.2022.975888) · [link](https://github.com/eliza-m/NLRexpress)
- **NLRSeek** (tool) — Combines NLR-Annotator loci, targeted re-annotation and NLRtracker to recover NLRs missing from proteomes. [doi:10.1016/j.abiote.2025.100001](https://doi.org/10.1016/j.abiote.2025.100001) · [link](https://github.com/Wang-Mengda/NLRSeek)
- **PlantTFDB / PlantRegMap** (resource) — Plant TF families, binding motifs and regulatory map. [doi:10.1093/nar/gkz1020](https://doi.org/10.1093/nar/gkz1020) · [link](http://planttfdb.gao-lab.org) [待确认]
- **PlantPAN (latest)** (resource) — Plant promoter / TF-binding analysis navigator. [doi:10.1093/nar/gkad945](https://doi.org/10.1093/nar/gkad945) · [link](https://plantpan.itps.ncku.edu.tw)
- **dbCAN3** (tool) — CAZyme and substrate annotation. [doi:10.1093/nar/gkad328](https://doi.org/10.1093/nar/gkad328) · [link](https://github.com/linnabrown/run_dbcan)
- **CAZy** (resource) — Reference classification of carbohydrate-active enzyme families; defines the class system assigned by dbCAN3. [doi:10.1093/nar/gkab1045](https://doi.org/10.1093/nar/gkab1045) · [link](http://www.cazy.org/)
- **MEROPS** (resource) — Database of peptidase and inhibitor families with curated substrates; use for protease gene-family tables. [doi:10.1093/nar/gkx1134](https://doi.org/10.1093/nar/gkx1134) · [link](https://www.ebi.ac.uk/merops/)
- **TCDB (2021)** (resource) — Transporter Classification Database; assigns TC families to membrane transporters, e.g. sugar and ion transporters in berries. [doi:10.1093/nar/gkaa1004](https://doi.org/10.1093/nar/gkaa1004) · [link](https://www.tcdb.org/)
- **JASPAR 2026** (resource) — Open database of curated transcription-factor binding profiles, including plant TFs; use to inspect the motifs behind PlantTFDB/PlantPAN predictions. [doi:10.1093/nar/gkaf1209](https://doi.org/10.1093/nar/gkaf1209) · [link](https://jaspar.elixir.no/)

<a id="section-10"></a>
## 10. Non-coding RNA function resources

Resources for non-coding RNA function. These usually need transcriptome or known ncRNA loci, not the protein table alone.

**Needs:** transcriptome or known ncRNA loci — not the protein table alone. Gene finders and TE libraries stay in the structure / vitis-te repos. [Data needs by scenario](#data-needs)

**Clusters:**
- *miRNA references* (complementary): miRBase, PmiREN 2.0, sRNAanno. Name miRNAs against miRBase and PmiREN; use sRNAanno for phasiRNA loci.
- *Targets* (in order): psRNATarget (2017 release) or psRobot, TarDB. Predict with psRNATarget or psRobot, then check degradome support in TarDB.
- *lncRNA and circRNA catalogues* (complementary): PLncDB V2.0, GreeNC 2.0, CANTATAdb 3.0, PlantCircRNA, ncPlantDB. Use for lookups only; they do not assign function on their own.


- **miRBase** (resource) — Reference microRNA sequence and nomenclature database. [doi:10.1093/nar/gky1141](https://doi.org/10.1093/nar/gky1141) · [link](https://www.mirbase.org/)
- **psRobot** (tool) — Plant small-RNA meta-analysis and target prediction. [doi:10.1093/nar/gks554](https://doi.org/10.1093/nar/gks554) · [link](http://omicslab.genetics.ac.cn/psRobot/) [待确认]
- **ncPlantDB** (resource) — Plant ncRNAs with potential ncRNA-encoded peptides and cell-type interactions (43 species). [doi:10.1093/nar/gkae1017](https://doi.org/10.1093/nar/gkae1017) · [link](https://bis.zju.edu.cn/ncPlantDB)
- **PLncDB V2.0** (resource) — Plant lncRNA encyclopedia. [doi:10.1093/nar/gkaa910](https://doi.org/10.1093/nar/gkaa910) · [link](https://www.tobaccodb.org/plncdb/) [待确认]
- **GreeNC 2.0** (resource) — Plant lncRNA catalog. [doi:10.1093/nar/gkab1014](https://doi.org/10.1093/nar/gkab1014) · [link](http://greenc.sequentiabiotech.com) [待确认]
- **CANTATAdb 3.0** (resource) — Updated plant lncRNA repository. [doi:10.1093/pcp/pcae081](https://doi.org/10.1093/pcp/pcae081) · [link](http://cantata.amu.edu.pl) [待确认]
- **PlantCircRNA** (resource) — Plant circular RNA database. [doi:10.1093/nar/gkae709](https://doi.org/10.1093/nar/gkae709) · [link](https://plant.deepbiology.cn/PlantCircRNA/)
- **psRNATarget (2017 release)** (tool) — Plant small-RNA target prediction server. [doi:10.1093/nar/gky316](https://doi.org/10.1093/nar/gky316) · [link](https://www.zhaolab.org/psRNATarget/) [待确认]
- **PmiREN 2.0** (resource) — Plant miRNA encyclopedia. [doi:10.1093/nar/gkab811](https://doi.org/10.1093/nar/gkab811) · [link](https://pmiren.com)
- **sRNAanno** (resource) — Uniformly annotated plant small-RNA loci (miRNA, phasiRNA, hc-siRNA) across many species, including grape. [doi:10.1038/s41438-021-00480-8](https://doi.org/10.1038/s41438-021-00480-8) · [link](http://www.plantsrnas.org/)
- **TarDB** (resource) — Database of plant miRNA targets supported by degradome data, plus miRNA-triggered phasiRNAs; serves as a check on psRNATarget predictions. [doi:10.1186/s12864-021-07680-5](https://doi.org/10.1186/s12864-021-07680-5) · [link](http://www.biosequencing.cn/TarDB/)

<a id="section-11"></a>
## 11. Expression-supported function

Expression or co-expression used to support a function hypothesis, not as experimental GO.

**Needs:** RNA-seq (preferably from the same genotype) if using expression to support a function claim. [Data needs by scenario](#data-needs)

**Clusters:**
- *Expression atlases* (complementary): Grapevine Expression Atlas, Expression Atlas (2024), scPlantDB. Show where and when a grape gene is expressed.
- *Network building* (alternatives): WGCNA, hdWGCNA, GENIE3. Use WGCNA for bulk data, hdWGCNA for single-cell data, and GENIE3 for TF-to-target links.
- *Co-expression portals* (complementary): ATTED-II v11, CoNekT. Provide quick guilt-by-association checks without building a network.


- **Grapevine Expression Atlas** (resource) — Organ/stage expression atlas of V. vinifera Corvina. [doi:10.1105/tpc.112.100230](https://doi.org/10.1105/tpc.112.100230)
- **ATTED-II v11** (resource) — Plant gene coexpression database. [doi:10.1093/pcp/pcac041](https://doi.org/10.1093/pcp/pcac041) · [link](https://atted.jp/)
- **scPlantDB** (resource) — Plant single-cell atlas: cell types and markers. [doi:10.1093/nar/gkad706](https://doi.org/10.1093/nar/gkad706) · [link](https://biobigdata.nju.edu.cn/scplantdb/) [待确认]
- **hdWGCNA** (tool) — Co-expression networks in single-cell/spatial data. [doi:10.1016/j.crmeth.2023.100498](https://doi.org/10.1016/j.crmeth.2023.100498) · [link](https://github.com/smorabit/hdWGCNA)
- **CoNekT** (tool / resource) — Co-expression network toolkit/framework for plants. [doi:10.1101/255075](https://doi.org/10.1101/255075) · [link](https://conekt.sbs.ntu.edu.sg) [待确认]
- **WGCNA** (tool) — Builds weighted gene co-expression modules from bulk RNA-seq; serves as the bulk counterpart to hdWGCNA for guilt-by-association inference. [doi:10.1186/1471-2105-9-559](https://doi.org/10.1186/1471-2105-9-559) · [link](https://cran.r-project.org/package=WGCNA)
- **GENIE3** (tool) — Infers transcription-factor-to-target links from expression data using tree ensembles; pairs well with iTAK/PlantTFDB TF lists. [doi:10.1371/journal.pone.0012776](https://doi.org/10.1371/journal.pone.0012776) · [link](https://github.com/aertslab/GENIE3)
- **Expression Atlas (2024)** (resource) — EMBL-EBI resource for baseline and differential expression across bulk and single-cell datasets, including plant experiments. [doi:10.1093/nar/gkad1021](https://doi.org/10.1093/nar/gkad1021) · [link](https://www.ebi.ac.uk/gxa/)

<a id="section-12"></a>
## 12. Community catalogues and naming

Curated community catalogues and naming sources.

**Needs:** access to the named community catalogue (and its version or date). [Data needs by scenario](#data-needs)

**Clusters:**
- *Grape naming* (in order): The grapevine gene nomenclature system, Grapedia Grapevine Reference Gene Catalogue, PN40024 reference annotation (PN_T2T / v5). Map IDs to the current PN_T2T version, then assign symbols from the Grapedia catalogue following the nomenclature rules.


- **The grapevine gene nomenclature system** (idea) — Proposed rules for naming grapevine genes. [doi:10.1186/1471-2164-15-1077](https://doi.org/10.1186/1471-2164-15-1077)
- **Grapedia Grapevine Reference Gene Catalogue** (resource) — Curated V. vinifera gene ID and symbol pairs with functional notes, literature links and confidence levels; v3.1 (Nov 2025) is aligned to the T2T v5.1 annotation. First described as the Grape Gene Reference Catalogue (doi:10.3389/fpls.2021.803977). [link](https://grapedia.org/genes/)
- **ProtNLM (UniProt names)** (idea) — UniProt uses a Google protein-naming model to propose names for unreviewed entries; names carry an automatic evidence tag. [link](https://www.uniprot.org/help/ProtNLM)
- **PN40024 reference annotation (PN_T2T / v5)** (resource) — Reference gene IDs on PN_T2T (v5), alongside earlier v4 (doi:10.1093/g3journal/jkad067) and VCost.v3 on 12X.v2 (doi:10.1016/j.gdata.2017.09.002); map names and IDs to the current version before release. [doi:10.1093/hr/uhad061](https://doi.org/10.1093/hr/uhad061) · [link](https://grapedia.org/)

<a id="section-13"></a>
## 13. Protein 3D structure

Protein 3D structure prediction, search and domains. “Structure” here means 3D structure, not gene models.

**Needs:** the proteins; some tools also need AlphaFold / PDB style libraries. “Structure” here means protein 3D structure, not gene models. [Data needs by scenario](#data-needs)

**Clusters:**
- *Whole-proteome monomers* (alternatives): ColabFold, ESMFold / ESM-2, AlphaFold2. ColabFold (AlphaFold2 with fast MSAs) or ESMFold for whole proteomes; AlphaFold2 itself has open code and weights.
- *Complexes* (alternatives): AlphaFold 3, RoseTTAFold All-Atom, Boltz-1. Only for complexes with proteins, nucleic acids or ligands; AlphaFold 3 weights are non-commercial and released on request.
- *Structure search then confirmation* (in order): Foldseek or TM-Vec 2s or AlphaFind v2 or DALI, TM-align or US-align. Search first (Foldseek against AFDB by default), then confirm a hit pairwise with TM-align, or US-align for complexes.
- *Structure target databases* (complementary): AlphaFold Protein Structure Database (2024), AFDB clusters (Foldseek). Search targets, not tools: AFDB clusters for a fast first pass, the full AFDB for detail.
- *Domains from structures* (complementary): TED (The Encyclopedia of Domains), CATH (2021), Merizo. Merizo segments custom structural models; TED and CATH provide reference domain definitions.
- *Embeddings* (complementary): ProtTrans (ProtT5), ESM3, ProstT5. Provide feature representations for the language-model tools in sections 1, 5 and 8.
- *Sites and pockets* (complementary): PARSE, WASP. Predict functional sites from structure; use for follow-up analysis only.


- **AlphaFold2** (tool) — Protein 3D structure prediction. [doi:10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2) · [link](https://github.com/google-deepmind/alphafold)
- **ColabFold** (tool) — Fast AlphaFold2 with MMseqs2 MSAs. [doi:10.1038/s41592-022-01488-1](https://doi.org/10.1038/s41592-022-01488-1) · [link](https://github.com/sokrypton/ColabFold)
- **ESMFold / ESM-2** (tool) — Single-sequence 3D structure prediction from a protein language model. [doi:10.1126/science.ade2574](https://doi.org/10.1126/science.ade2574) · [link](https://github.com/facebookresearch/esm)
- **AlphaFold 3** (tool) — Joint structure prediction of complexes with nucleic acids, ligands and ions. Model weights are released for non-commercial use on request; AlphaFold2 (separate entry) stays the open option for bulk monomer prediction. [doi:10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w) · [link](https://github.com/google-deepmind/alphafold3)
- **TED (The Encyclopedia of Domains)** (resource) — Structure-based domain segmentation of AlphaFold DB. [doi:10.1126/science.adq4946](https://doi.org/10.1126/science.adq4946) · [link](https://ted.cathdb.info/)
- **CATH (2021)** (resource) — Hierarchical classification of protein 3D domains. [doi:10.1093/nar/gkaa1079](https://doi.org/10.1093/nar/gkaa1079) · [link](https://www.cathdb.info/)
- **TM-align** (tool) — Structure alignment with TM-score. [doi:10.1093/nar/gki524](https://doi.org/10.1093/nar/gki524) · [link](https://zhanggroup.org/TM-align/)
- **US-align** (tool) — Universal structure alignment for proteins and nucleic acids. [doi:10.1038/s41592-022-01585-1](https://doi.org/10.1038/s41592-022-01585-1) · [link](https://github.com/pylelab/USalign)
- **DALI** (tool) — Structure comparison server against PDB/AlphaFold DB. [doi:10.1002/pro.3749](https://doi.org/10.1002/pro.3749) · [link](http://ekhidna2.biocenter.helsinki.fi/dali/) [待确认]
- **Foldseek** (tool) — Protein 3D-structure search via 3Di alphabet; finds remote homologs missed by sequence search. [doi:10.1038/s41587-023-01773-0](https://doi.org/10.1038/s41587-023-01773-0) · [link](https://github.com/steineggerlab/foldseek)
- **ProstT5** (tool) — Protein language model translating sequence to 3Di tokens so Foldseek can run without predicted structures. [doi:10.1093/nargab/lqae150](https://doi.org/10.1093/nargab/lqae150) · [link](https://github.com/mheinzinger/ProstT5)
- **TM-Vec 2s** (tool) — Embedding-based remote homology / TM-score prediction (preprint 2026). [doi:10.64898/2026.02.05.704073](https://doi.org/10.64898/2026.02.05.704073)
- **AlphaFold Protein Structure Database (2024)** (resource) — Predicted protein 3D structures for UniProt; target for Foldseek searches. [doi:10.1093/nar/gkad1011](https://doi.org/10.1093/nar/gkad1011) · [link](https://alphafold.ebi.ac.uk)
- **AlphaFind v2** (tool) — Similarity search over AlphaFold DB and TED domains. [doi:10.1093/nar/gkag372](https://doi.org/10.1093/nar/gkag372) · [link](https://alphafind.fi.muni.cz)
- **WASP** (tool) — Whole-proteome annotation via Foldseek against AlphaFold DB (GO, Pfam, PANTHER, CATH, Rhea, EC). [link](https://github.com/gioodm/wasp-proteins-annotation)
- **PARSE** (tool) — Functional site annotation from local 3D-structure embeddings. [doi:10.1073/pnas.2513219122](https://doi.org/10.1073/pnas.2513219122)
- **Merizo** (tool) — Domain segmentation of predicted 3D structures. [doi:10.1038/s41467-023-43934-4](https://doi.org/10.1038/s41467-023-43934-4) · [link](https://github.com/psipred/Merizo)
- **RoseTTAFold All-Atom** (tool) — Predicts protein structures together with ligands, nucleic acids and modifications; an open alternative for complexes. [doi:10.1126/science.adl2528](https://doi.org/10.1126/science.adl2528) · [link](https://github.com/baker-laboratory/RoseTTAFold-All-Atom)
- **Boltz-1** (tool) — Open-source biomolecular complex predictor (MIT licence) with AlphaFold 3-like accuracy; usable without AF3 weight restrictions. [preprint] [doi:10.1101/2024.11.19.624167](https://doi.org/10.1101/2024.11.19.624167) · [link](https://github.com/jwohlwend/boltz)
- **ESM3** (tool) — Multimodal protein language model trained across sequence, structure and function; provides an open small model for embeddings and design. [doi:10.1126/science.ads0018](https://doi.org/10.1126/science.ads0018) · [link](https://github.com/evolutionaryscale/esm)
- **ProtTrans (ProtT5)** (tool) — Pretrained protein language models; ProtT5 embeddings power goPredSim, TMbed, ProstT5 and other tools in this catalog. [doi:10.1109/TPAMI.2021.3095381](https://doi.org/10.1109/TPAMI.2021.3095381) · [link](https://github.com/agemagician/ProtTrans)
- **AFDB clusters (Foldseek)** (resource) — Structure-based clusters of the AlphaFold Database; reveals which unannotated "dark" families share folds with annotated ones. [doi:10.1038/s41586-023-06510-w](https://doi.org/10.1038/s41586-023-06510-w) · [link](https://cluster.foldseek.com/)

<a id="section-14"></a>
## 14. Downstream enrichment

Downstream GO/KEGG enrichment. This uses the finished function table; it is not a source of labels.

**Needs:** a finished function table plus a clearly defined gene-set background (usually all genes in the release). This is downstream of merge, not a source of labels. [Data needs by scenario](#data-needs)

**Clusters:**
- *Over-representation* (alternatives): topGO, GOATOOLS, clusterProfiler 4.0, GOseq, g:Profiler (2023), ShinyGO, DAVID (2025 update), agriGO v2.0. Run topGO or clusterProfiler with the grape background; use GOseq when gene length biases detection.
- *Ranked lists* (alternatives): GSEA, clusterProfiler 4.0. When the signal is a ranking, not a gene list: GSEA, or the GSEA mode of clusterProfiler.
- *Term reduction* (alternatives): Revigo, simplifyEnrichment. Reduce redundant terms before reporting; GOSemSim computes the semantic similarity behind such clustering and is used directly for custom comparisons.


- **topGO** (tool) — GO enrichment accounting for GO graph topology. [doi:10.18129/B9.bioc.topGO](https://doi.org/10.18129/B9.bioc.topGO) · [link](https://bioconductor.org/packages/topGO/)
- **GOATOOLS** (tool) — Python GO library: DAG propagation, slims, enrichment. [doi:10.1038/s41598-018-28948-z](https://doi.org/10.1038/s41598-018-28948-z) · [link](https://github.com/tanghaibao/goatools)
- **GOseq** (tool) — GO enrichment correcting for length bias in RNA-seq. [doi:10.1186/gb-2010-11-2-r14](https://doi.org/10.1186/gb-2010-11-2-r14) · [link](https://bioconductor.org/packages/goseq/)
- **ShinyGO** (tool) — Web enrichment with plant species from Ensembl/STRING. [doi:10.1093/bioinformatics/btz931](https://doi.org/10.1093/bioinformatics/btz931) · [link](http://bioinformatics.sdstate.edu/go/) [待确认]
- **DAVID (2025 update)** (tool) — Enrichment server; adds DAVID Ortholog for cross-species analysis. [doi:10.1093/nar/gkag470](https://doi.org/10.1093/nar/gkag470) · [link](https://davidbioinformatics.nih.gov)
- **g:Profiler (2023)** (tool) — Enrichment and ID conversion. [doi:10.1093/nar/gkad347](https://doi.org/10.1093/nar/gkad347) · [link](https://biit.cs.ut.ee/gprofiler)
- **agriGO v2.0** (tool) — GO enrichment for agricultural species. [doi:10.1093/nar/gkx382](https://doi.org/10.1093/nar/gkx382) · [link](http://systemsbiology.cau.edu.cn/agriGOv2/) [待确认]
- **clusterProfiler 4.0** (tool) — R enrichment with custom TERM2GENE from merged_function_table.tsv. [doi:10.1016/j.xinn.2021.100141](https://doi.org/10.1016/j.xinn.2021.100141) · [link](https://github.com/YuLab-SMU/clusterProfiler)
- **Revigo** (tool) — Summarises long lists of enriched GO terms into non-redundant groups by semantic similarity. [doi:10.1371/journal.pone.0021800](https://doi.org/10.1371/journal.pone.0021800) · [link](http://revigo.irb.hr/)
- **simplifyEnrichment** (tool) — Clusters enriched GO terms by semantic similarity and displays word-cloud summaries for each cluster. [doi:10.1016/j.gpb.2022.04.008](https://doi.org/10.1016/j.gpb.2022.04.008) · [link](https://github.com/jokergoo/simplifyEnrichment)
- **GOSemSim** (tool) — Computes semantic similarity among GO terms and genes; forms the backbone of term-reduction workflows. [doi:10.1093/bioinformatics/btq064](https://doi.org/10.1093/bioinformatics/btq064) · [link](https://github.com/YuLab-SMU/GOSemSim)
- **GSEA** (tool) — Evaluates gene-set enrichment across a ranked list without a cutoff; use when differential expression is graded rather than a gene list. [doi:10.1073/pnas.0506580102](https://doi.org/10.1073/pnas.0506580102)

<a id="section-15"></a>
## 15. Ideas, formats and merge rules

Ideas, formats and merge rules. The merge product remains `merged_function_table.tsv`. Nothing here changes frame F1 until tested.

**Needs:** depends on the idea; the merge product remains `merged_function_table.tsv`. Nothing here changes frame F1 until tested. [Data needs by scenario](#data-needs)

**Clusters:**
- *Formats and evidence* (complementary): Evidence & Conclusion Ontology (ECO, 2022), GO Annotation File (GAF 2.2) format, GO-CAM. Every GO row carries an ECO code; use GAF for releases and GO-CAM for curated pathways.
- *Error and specificity* (complementary): GO specificity balance (Genome Res 2026), CAFA lessons (idea), Misannotation in enzyme superfamilies. Explain why transferred labels fail and how to choose appropriate term specificity.
- *LLM agents* (alternatives): GeneAgent, LLM-assisted Reactome annotation, Agentic AI for gene function across genomes. Proposals only; retain human review.


- **Evidence & Conclusion Ontology (ECO, 2022)** (idea) — Ontology of evidence types behind annotations (maps to GO evidence codes). [doi:10.1093/nar/gkab1025](https://doi.org/10.1093/nar/gkab1025) · [link](https://evidenceontology.org/)
- **GO Annotation File (GAF 2.2) format** (idea) — Standard tab format for gene–GO associations with evidence codes. [link](https://geneontology.org/docs/go-annotation-file-gaf-format-2.2/)
- **GO specificity balance (Genome Res 2026)** (idea) — Balancing GO term specificity in sequence-language-model predictions. [doi:10.1101/gr.280816.125](https://doi.org/10.1101/gr.280816.125) [待确认]
- **CAFA lessons (idea)** (idea) — Community assessments keep showing GO prediction is hard for proteins with partial knowledge; publish ML GO as electronic evidence (IEA) only. [link](https://biofunctionprediction.org/cafa/) [待确认]
- **GeneAgent** (idea) — Self-verifying LLM agent for gene-set analysis using domain databases. [doi:10.1038/s41592-025-02748-6](https://doi.org/10.1038/s41592-025-02748-6)
- **LLM-assisted Reactome annotation** (idea) — LLM/RAG proposals of pathway annotations for curator review (preprint). [doi:10.64898/2025.12.20.695723](https://doi.org/10.64898/2025.12.20.695723)
- **Agentic AI for gene function across genomes** (idea) — GO curators' agent workflow with constrained schemas and validators (Zenodo record). [doi:10.5281/zenodo.18904049](https://doi.org/10.5281/zenodo.18904049)
- **Misannotation in enzyme superfamilies** (idea) — Quantifies error rates in transferred molecular-function labels; motivates retaining evidence codes and preferring curated sources. [doi:10.1371/journal.pcbi.1000605](https://doi.org/10.1371/journal.pcbi.1000605)
- **GO-CAM** (idea) — Links GO annotations into structured causal activity models; serves as a target format for curated grape pathways beyond flat GAF tables. [doi:10.1038/s41588-019-0500-1](https://doi.org/10.1038/s41588-019-0500-1) · [link](https://geneontology.org/docs/gocam-overview/)

<a id="data-needs"></a>
## Data needed alongside the proteins

The main input is `proteins.faa` from a structure release (one representative sequence per gene). The notes below say what else each step usually needs. They do not change default frame F1 until a change is tested.

| Situation | Minimum | Recommended | Typical tools in this repo | Common pitfall |
|---|---|---|---|---|
| Input QC (F0) | `PROTEINS_FA` + protein-mode BUSCO lineage | OMArk as an extra consistency check | BUSCO protein, OMArk (optional) | Treating F0 as a source of functional labels; trying to "fix" a bad proteome here instead of going back to structure |
| Default frame F1 | Local DIAMOND DB, eggNOG-mapper data, InterProScan data (versions in METHODS) | Swiss-Prot (or documented equivalent) for DIAMOND | `F1_diamond.sh`, `F2_eggnog.sh`, `F3_interproscan.sh` | Confusing script `F2_eggnog.sh` with alternate frame F2 |
| Fast frame F2 | eggNOG-mapper data only | Add Kofam later into merge | eggNOG-mapper ± Kofam | Shipping F2 as if IPS had been run |
| Names (F4, optional) | Blast/DIAMOND-style outputs that AHRD expects | A documented name source | AHRD, optional PANNZER (`[待确认]` site check in the 2026-11 catalog) | Treating names as a higher F-L grade by themselves |
| MapMan (F6, optional) | Mercator4 result (web or local) | Follow `docs/MERCATOR_WHEN.md` | `F6_ingest_mercator.py` | Running Mercator "because it is a plant" with no MapMan figure planned |
| Multi-genome (F7) | Proteins from every genome in the panel | Annotate orthogroup representatives, then merge | OrthoFinder, then F1 on representatives | Writing labels as if every gene had been through F1 |
| NLR (F8, optional) | InterProScan output; optional HRP windows from the structure overlay | Only if there is a disease / NLR story | `F8_run.sh` | Calling an IPS+HRP screen a curated NLR set |
| TF / kinase (F9, optional) | iTAK (or a documented equivalent) | Only if that family is needed | `F9_itak.sh` | Adding F9 as a plant-genome checklist item |
| Enrichment (downstream) | `merged_function_table.tsv` + a defined background | The full release gene set as background | clusterProfiler and similar are catalogued; some licenses are NC/ND and are not used for figures | Using a convenience subset as the background without saying so |
| Pathways / KO | Kofam HMM set and thresholds, or eggNOG KO fields | Record the library version | KofamScan, eggNOG | Assuming KEGG data can be redistributed (`[待确认]`) |

### Cross-cutting pitfalls

- No gene finding, soft-mask, TE library, or GFF editing happens here. Those belong to gene-structure-annotation or vitis-te.
- Four ID sets must stay distinct in METHODS: frame (F1/F2/F3/F5), script file (`F2_eggnog.sh` is a step inside frame F1), tool card (F1a/F1b/F1c), and gate (Gate-F1…F7).
- The merge product is `merged_function_table.tsv`. Machine-predicted GO/EC stays IEA.
- Frame F7 annotates orthogroup representatives, not each gene.
- "Structure" in Foldseek, DeepFRI or AlphaFold DB means protein 3D structure.
- InterProScan is part of default F1 but is slow; F-L1 is an acceptance bar, not a requirement to finish IPS tonight.
- Optional plant add-ons (F4/F6/F8/F9) are not a higher grade by themselves.

Catalog rows still marked `[待确认]` (HMMER 3, eggNOG 6, PANNZER2, MetaCyc, PRGdb 4.0, psRobot, DALI, ShinyGO — site checks on 2026-11-13) stay marked until a person opens the page. This text does not re-check those sites.

Longer notes, including the Chinese table, are in [`docs/SCENARIOS_FUNCTIONAL.md#data-needs-details`](docs/SCENARIOS_FUNCTIONAL.md#data-needs-details).

![OMArk versus BUSCO proteomes](docs/figures/catalog/07_omark_vs_busco_proteomes.jpg)

*OMArk compared with BUSCO completeness on 1,805 eukaryotic UniProt reference proteomes (Fig. 5). Shown here because F0 input QC is not a type section. Nevers et al. 2025, Nat. Biotechnol. 43(1):124-133, Fig. 5, doi:10.1038/s41587-024-02147-w (online 2024-02-21), PMC11738984, CC BY.*

<a id="figure-credits"></a>
## Figure credits

Self-drawn overview figures in `docs/figures/` belong to this repository. Catalog figures below are unaltered JPEGs from CC BY papers (Europe PMC license field `cc by`, checked 2026-11-13). No NC/ND material is used.

| File | Credit |
|---|---|
| [`docs/figures/catalog/01_eggnogmapper_v2_runtime.jpg`](docs/figures/catalog/01_eggnogmapper_v2_runtime.jpg) | eggNOG-mapper v2 runtime compared with other annotators (Fig. 2). Cantalapiedra et al. 2021, Mol. Biol. Evol., Fig. 2, doi:10.1093/molbev/msab293, PMC8662613, CC BY. |
| [`docs/figures/catalog/02_eggnogmapper_vs_interproscan.jpg`](docs/figures/catalog/02_eggnogmapper_vs_interproscan.jpg) | eggNOG-mapper compared with InterProScan (Fig. 3). Huerta-Cepas et al. 2017, Mol. Biol. Evol., Fig. 3, doi:10.1093/molbev/msx148, PMC5850834, CC BY. |
| [`docs/figures/catalog/03_eggnogmapper_rhogap1_go.jpg`](docs/figures/catalog/03_eggnogmapper_rhogap1_go.jpg) | eggNOG-mapper GO assignment on a worked example (Fig. 4). Huerta-Cepas et al. 2017, Mol. Biol. Evol., Fig. 4, doi:10.1093/molbev/msx148, PMC5850834, CC BY. |
| [`docs/figures/catalog/04_interpro_pik3ca_domains.jpg`](docs/figures/catalog/04_interpro_pik3ca_domains.jpg) | InterPro domain annotation of PIK3CA (Fig. 4). Blum, Andreeva, Florentino et al. 2025, Nucleic Acids Res., Fig. 4, doi:10.1093/nar/gkae1082, PMC11701551, CC BY. |
| [`docs/figures/catalog/05_interproscan_human_runtime.jpg`](docs/figures/catalog/05_interproscan_human_runtime.jpg) | InterProScan runtime on a human proteome (Fig. 6). Blum, Andreeva, Florentino et al. 2025, Nucleic Acids Res., Fig. 6, doi:10.1093/nar/gkae1082, PMC11701551, CC BY. |
| [`docs/figures/catalog/06_orthofinder_chordata_summary.jpg`](docs/figures/catalog/06_orthofinder_chordata_summary.jpg) | OrthoFinder summary for a Chordata example (Fig. 3). Emms and Kelly 2019, Genome Biol., Fig. 3, doi:10.1186/s13059-019-1832-y, PMC6857279, CC BY. |
| [`docs/figures/catalog/07_omark_vs_busco_proteomes.jpg`](docs/figures/catalog/07_omark_vs_busco_proteomes.jpg) | OMArk compared with BUSCO completeness on 1,805 eukaryotic UniProt reference proteomes (Fig. 5). Shown here because F0 input QC is not a type section. Nevers et al. 2025, Nat. Biotechnol. 43(1):124-133, Fig. 5, doi:10.1038/s41587-024-02147-w (online 2024-02-21), PMC11738984, CC BY. |

