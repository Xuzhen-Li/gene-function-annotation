# Related software

Public tools useful when teaching or running **functional** annotation.  
This repo is a biology-general **function-layer** playbook (*Vitis*/plant notes are examples). Links are for citation and further reading.

## Functional

| Software | Notes in this repo |
|----------|-------------------|
| [eggnog-mapper](https://github.com/eggnogdb/eggnog-mapper) | Default F1/F2 |
| [InterProScan](https://www.ebi.ac.uk/interpro/download/) | Domains / GO |
| [DIAMOND](https://github.com/bbuchfink/diamond) | SwissProt / NR hits |
| [AHRD](https://github.com/groupschoof/AHRD) · [eifunannot](https://github.com/EI-CoreBioinformatics/eifunannot) | Readable names (F4) |
| [EnTAP](https://gitlab.com/PlantGenomicsLab/EnTAP) | Optional F3 frame |
| [Trinotate](https://github.com/Trinotate/Trinotate) | Transcriptome FA (F5) |
| [HRP](https://github.com/AndolfoG/HRP) | Plant NLR focus (optional F8) |
| Mercator4 / MapMan | Plant BINs (optional F6) |
| KofamScan | Optional KO |
| [funannotate2 addons](https://github.com/nextgenusfs/funannotate2-addons) | FA add-ons aligned with F1 — see [`notes/funannotate2_addons_fa.md`](notes/funannotate2_addons_fa.md) |

Short FA notes: [`notes/`](notes/).

## Structural (upstream)

Gene-finding / GFF release tools (BRAKER, GALBA, EviAnn, EVM, Liftoff, GSAman, EDTA, Helixer, …) are listed in the sibling repo — **not mirrored here**:

[gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation) · [`docs/TOOLS.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TOOLS.md) · [`docs/PEER_PIPELINES.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/PEER_PIPELINES.md)

## FA KO / GO peers

| Software | Notes |
|----------|-------|
| BlastKOALA / GhostKOALA | Kanehisa *JMB* 2016 — classic KEGG KO web |
| KofamScan / KofamKOALA | HMM KO (optional F1b) |
| [DeepKOALA](https://github.com/zhaoxi120/deepkoala) | DL KO assignment; fast batch |
| DeepGOPlus (DeepGO family) | DL GO — post-F1 optional |
| [ProteInfer](https://github.com/google-research/proteinfer) | DL GO/EC from sequence |
| DeepFRI | DL GO (structure/sequence graphs) |
| [NetGO 3.0](https://dmiip.sjtu.edu.cn/ng3.0) | SJTU PLM GO (NAR 2023) |
| dbCAN3 | CAZyme FA |
| DeepLoc 2.0 · SignalP 6.0 | Localization / signal peptides |
