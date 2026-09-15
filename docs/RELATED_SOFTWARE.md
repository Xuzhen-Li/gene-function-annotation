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
| KofamScan / KofamKOALA | HMM KO (optional **F1+**; not TOOLS F1b) |
| [DeepKOALA](https://github.com/zhaoxi120/deepkoala) | DL KO assignment; fast batch |
| DeepGOPlus (DeepGO family) | DL GO — post-F1 optional |
| [ProteInfer](https://github.com/google-research/proteinfer) | DL GO/EC from sequence |
| DeepFRI | DL GO (structure/sequence graphs) |
| [NetGO 3.0](https://dmiip.sjtu.edu.cn/ng3.0) | SJTU PLM GO (NAR 2023) |
| dbCAN3 | CAZyme FA |
| DeepLoc 2.0 · SignalP 6.0 | Localization / signal peptides |

## Haul 2026-09-14 — FA peers / reviews (below allowlist labelled)

Sources useful for teaching or speed, but **not** elevated to [`RECENT_HIGH_QUALITY.md`](RECENT_HIGH_QUALITY.md) unless venue is on the allowlist.

| Software / paper | Venue / link | Label | Maps to |
|------------------|--------------|-------|---------|
| **TransAnnot** — Zelenskaia et al. | *Bioinformatics Advances* 2024 doi:[10.1093/bioadv/vbae152](https://doi.org/10.1093/bioadv/vbae152) · [soedinglab/transannot](https://github.com/soedinglab/transannot) | **Below allowlist** (Bioinf Adv) | Fast MMseqs2 Swiss-Prot + eggNOG + Pfam; peer to F2 / EnTAP/Trinotate speed lane — **not** F1 replacement |
| **InterProScan 6** — Blum et al. | *Bioinformatics Advances* 2026 doi:[10.1093/bioadv/vbag141](https://doi.org/10.1093/bioadv/vbag141) · [ebi-pf-team/interproscan6](https://github.com/ebi-pf-team/interproscan6) | **Below allowlist** (tool paper venue) | Nextflow IPS rewrite — watch for F1 runner; cite **NAR** InterPro 2025 for DB |
| **InterPro 2025** — Blum et al. | **NAR** 2025 doi:[10.1093/nar/gkae1082](https://doi.org/10.1093/nar/gkae1082) | Allowlisted — also in RECENT_HIGH_QUALITY | F1 InterProScan DB citation |
| **CAFA4** — Ramola et al. | bioRxiv 2026 doi:[10.64898/2026.05.06.722942](https://doi.org/10.64898/2026.05.06.722942) | **Preprint** (not allowlist) | GO prediction still hard on “partial knowledge”; keeps electronic GO as hypothesis |
| **GenePAL** FA step | [Plant-Food-Research-Open/genepal](https://github.com/Plant-Food-Research-Open/genepal) Zenodo doi:[10.5281/zenodo.14195006](https://doi.org/10.5281/zenodo.14195006) | Pipeline (no allowlisted FA paper) | eggNOG into GFF — parallel to F1 emapper; structure peer lives upstream |
| **funannotate2-addons** | already listed above | — | eggNOG/IPS align with F1 |
| EnTAP vs Trinotate vs eggNOG speed notes | EnTAP docs / TransAnnot head-to-head | Teaching only | Prefer **F1** for papers; F3/F5 when lab-standard; TransAnnot = optional speed peer |

### GO assignment caveats (unchanged policy)

- Orthology-aware transfer (eggNOG-mapper) ≫ raw BLAST blast2go-style dumps for precision (classic eggNOG-mapper *MBE* / CAFA lore).
- InterPro → GO is domain-conservative (fewer, broader terms); emapper often assigns **more** terms — treat as hypotheses; keep evidence/reference codes when publishing.
- CAFA4 preprint: field improves, but partial-knowledge proteins remain weak — do not claim experimental GO from F1 alone.
