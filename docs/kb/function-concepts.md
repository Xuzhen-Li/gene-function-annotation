# Functional labels and the four numbering schemes

[中文](function-concepts.zh.md) · [Knowledge units](README.md)

## 1. What it is

Functional annotation attaches labels to the proteins of a structure release: readable names, Gene Ontology (GO) terms, KEGG orthologs (KO) and pathways, protein domains and families, and optional plant classes such as MapMan bins or NLR and transcription-factor families. The input is `proteins.faa` with one representative protein per gene; the product is one gene-centric table, `merged_function_table.tsv`. Each label is a statement with a source, not a measured fact about the protein.

## 2. How the evidence is structured

Three lines of evidence are merged per protein, and each label keeps the line that gave it:

| Line | What it gives | Book |
|---|---|---|
| Similarity to curated proteins | best matches in a curated set such as Swiss-Prot | [chapter 2](../../book/chapters/02-homology-search.md) |
| Signatures and domains | families, domains and sites, with mappings to GO | [chapter 4](../../book/chapters/04-domain-and-family-annotation.md) |
| Orthology-based transfer | names, GO and KO carried over from orthologs | [chapter 5](../../book/chapters/05-orthology-based-names-go-and-kegg.md) |

The merge rules are in [chapter 16](../../book/chapters/16-ideas-formats-and-merge-rules.md). How far to trust each label is a separate unit: [How far to trust a function table](credibility-criteria.md).

## 3. How to recognise a sound function table (field card)

- One row per gene, and the row count matches the input proteins (or the drops are listed).
- Every GO term carries its source and an evidence code.
- The frame is named (`frame=F1` by default).
- The four numbering schemes below are not mixed in the text.

## 4. Repository default and the four numbering schemes

The default frame is **F1**: DIAMOND against Swiss-Prot, eggNOG-mapper and InterProScan ([README, Default route](../../README.md#default-route); [`docs/workflow/README.md`](../workflow/README.md)). Four schemes use labels that look alike. They are defined once in [`catalog/_namespaces.md`](../../catalog/_namespaces.md):

| Scheme | Example labels | Meaning |
|---|---|---|
| Framework | F1, F2, F3, F5 | the whole frame you claim in METHODS |
| Script file | `F1_diamond.sh`, `F2_eggnog.sh`, `F3_interproscan.sh` | the three steps of framework F1 |
| TOOLS card | F1a, F1b, F1c | reading pages for the three F1 steps |
| Gate | Gate-F1 to Gate-F7 | release checks in [`docs/EVALUATION.md`](../EVALUATION.md) |

The script `F2_eggnog.sh` is the eggNOG-mapper step of framework F1. It is **not** framework F2. Older stage and type numbers are mapped in [Numbering schemes](NUMBERING.md).

## 5. What is known in plants and in *Vitis*

- MapMan4 with Mercator is a protein classification made for plants ([book section 1.3](../../book/chapters/01-concepts.md#13-vocabularies-and-evidence)).
- Function labels inherit every error in the gene models, so a protein BUSCO check (F0) comes first ([book section 1.5](../../book/chapters/01-concepts.md#15-structure-comes-first)).
- The grapevine worked example is [`examples/plant_sim/01_vitis_s1_s7/`](../../examples/plant_sim/01_vitis_s1_s7/plan.md). How many grapevine proteins get no label from F1 is not given here: **[待确认]**.

## 6. Claims and sources

| Claim | Source | Quoted sentence or figure | What was read |
|---|---|---|---|
| A GO annotation is a statement that links a gene product to a GO term. | Gene Ontology, [Introduction to GO annotations](https://geneontology.org/docs/go-annotations/) | “A standard GO annotation is a statement that links a gene product and a GO term via a relation from the Relations Ontology (RO).” | The web page, section Standard GO annotations |
| Each GO annotation carries an evidence code. | Gene Ontology, [Guide to GO evidence codes](https://geneontology.org/docs/guide-go-evidence-codes/) | “Each annotation includes an evidence code to indicate how the annotation to a particular term is supported.” | The web page, opening paragraph |
| Script `F2_eggnog.sh` belongs to framework F1. | [`catalog/_namespaces.md`](../../catalog/_namespaces.md) (this repository) | “`F1_diamond.sh`, `F2_eggnog.sh`, `F3_interproscan.sh` are the **three steps of framework F1**” | The file at the current main branch |
| Errors in gene models carry into function labels. | Book chapter 1, section 1.5 (this repository), which cites [doi:10.1093/bioinformatics/btaf365](https://doi.org/10.1093/bioinformatics/btaf365) | “Function labels inherit every error in the gene models.” | The chapter text; the cited paper was not reopened for this page |

## 7. See also

- Book: [chapter 1, Concepts and principles](../../book/chapters/01-concepts.md); [appendix A, Glossary](../../book/chapters/appendix-a-glossary.md)
- Knowledge units: [Transferring function by homology and orthology](homology-transfer.md); [How far to trust a function table](credibility-criteria.md)
- Software by step: [`catalog/README.by-type.md`](../../catalog/README.by-type.md)
- Upstream: [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation)
