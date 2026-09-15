# Tools — functional annotation

Workflow order: [`FUNCTIONAL_GUIDE.md`](FUNCTIONAL_GUIDE.md) · [`steps/FUNCTIONAL_MAIN.md`](steps/FUNCTIONAL_MAIN.md).  
This page is **tool literacy** for the **function layer**. Structural gene-finding tools live in the sibling repo.

Prefer **containers** (Docker / Singularity / Apptainer) over compiling by hand. Paths below are templates — put image tags and module names in `config/local.env`.

## Functional tools (this repo)

> **Numbering:** table IDs F1a/F1b/F1c = steps inside **frame F1**. Scripts are named `F1_diamond.sh` / `F2_eggnog.sh` / `F3_interproscan.sh` (F2 script ≠ frame F2). Checklist gates F1–F7 are yet another index — see [`zh/FAQ_入门.md`](zh/FAQ_入门.md).

| Order | Tool | Makes |
|-------|------|-------|
| F0 | [BUSCO](tools/busco.md) proteins | completeness |
| F1a | [DIAMOND](tools/diamond_func.md) | SwissProt hits |
| F1b | [eggNOG-mapper](tools/eggnog_mapper.md) | GO/KEGG/COG/Pfam |
| F1c | [InterProScan](tools/interproscan.md) | domains + GO |
| F1+ | [KofamScan](tools/kofamscan.md) | optional KO |
| F4 | [AHRD](tools/ahrd.md) / [PANNZER2](tools/pannzer2.md) | readable names / GO |
| F3 | [EnTAP](tools/entap.md) | alt frame |
| F5 | [Trinotate](tools/trinotate.md) | transcriptome |
| F2+ | [KEGGaNOG](tools/kegganog.md) | pathway plots |
| F1+ | [Phobius/SignalP](tools/phobius_signalp.md) | secreted/TM |
| F6 | [Mercator](tools/mercator.md) | MapMan BINs (plant) |
| F8 | [HRP](tools/hrp.md) | NLR |
| F9 | [iTAK](tools/itak.md) | TF / kinase (plant) |
| — | [Blast2GO-style](tools/blast2go_style.md) | GO assignment notes |

Merge: `pipeline/F_merge_tables.py`. Release: `pipeline/F_release.sh`.

## Upstream structural tools

Assembly, soft-mask, BRAKER/GALBA/EviAnn, EVM/TSEBRA/Mikado, Liftoff, GSAman, SynGAP, AGAT, PSAURON, OMArk, etc. are documented in:

**[gene-structure-annotation `docs/TOOLS.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TOOLS.md)**

Finish structure release there (or bring your own GFF+proteins), set `PROTEINS_FA`, then run **F1** here.

## Shared habits (FA)

1. One representative protein **per gene** in `PROTEINS_FA`.  
2. Record tool/DB versions for METHODS (`diamond --version`, InterProScan build, eggNOG DB).  
3. If a script prints `[STOP]`, it printed the command for *you* to run in your container — expected until you set `RUN=1` / wire the image.  
4. Do not invent GO/KEGG counts — read them from files under `$FUNCTION_DIR/`.
