# Transferring function by homology and orthology

[中文](homology-transfer.zh.md) · [Knowledge units](README.md)

## 1. What it is

Most labels on a new proteome are transferred, not measured. A protein is compared with proteins whose function is known, and the label of a match is carried over. **Homology** means the two sequences share an ancestor; a best hit in a similarity search is evidence of homology. **Orthology** is a narrower relation: genes separated by speciation. Orthologs are more likely to keep the same function than paralogs, which is why orthology-based transfer is preferred for GO and KEGG.

## 2. How the evidence is structured

| Step in frame F1 | Tool (default) | What it adds | Catalogue |
|---|---|---|---|
| Similarity search against a curated set | DIAMOND v2 against Swiss-Prot | best curated matches | [section 1](../../catalog/METHODS_CATALOG.md#section-1) |
| Orthology assignment | eggNOG-mapper | ortholog groups, names, GO, KO | [section 4](../../catalog/METHODS_CATALOG.md#section-4) |
| Domains and families | InterProScan | domain evidence that supports, but does not replace, a name | [section 3](../../catalog/METHODS_CATALOG.md#section-3) |

The databases behind these steps (Swiss-Prot, eggNOG, InterPro) are listed in [catalogue section 2](../../catalog/METHODS_CATALOG.md#section-2).

## 3. How to recognise a sound transfer (field card)

- The database and its version are given for every transfer.
- Mapper and database versions match (for example the eggNOG-mapper release and the eggNOG release).
- A label from a best hit alone is not called an ortholog assignment.
- A domain hit is not turned into a gene name without a naming step.

## 4. Repository default and branches

Frame F1 is the default; F2 (eggNOG-mapper alone), F3 (EnTAP) and F5 (Trinotate) are faster frames with a lower grade ([`catalog/_namespaces.md`](../../catalog/_namespaces.md); [`docs/EVALUATION.md`](../EVALUATION.md#gate-f3--default-frame-or-waiver)). Readable names are an add-on (F4, AHRD). The step order is in [`docs/workflow/README.md`](../workflow/README.md).

## 5. What is known in plants and in *Vitis*

- Misannotation is common in databases built without manual curation; book chapter 1 gives the enzyme-family study and its numbers ([section 1.4](../../book/chapters/01-concepts.md#14-why-errors-matter)).
- Plant gene families such as NLRs need their own tools; see [catalogue section 9](../../catalog/METHODS_CATALOG.md#section-9).
- A measured transfer accuracy for grapevine proteins is not given here: **[待确认]**.

## 6. Claims and sources

| Claim | Source | Quoted sentence or figure | What was read |
|---|---|---|---|
| DIAMOND v2 reaches BLASTP sensitivity at tree-of-life scale. | Buchfink, Reuter and Drost 2021, *Nat Methods* 18:366, [doi:10.1038/s41592-021-01101-x](https://doi.org/10.1038/s41592-021-01101-x) | “harnesses supercomputing to perform tree-of-life scale protein alignments in hours, while matching the sensitivity of the gold standard BLASTP” | Abstract (PubMed 33828273) |
| eggNOG-mapper transfers function through precomputed orthology. | Cantalapiedra et al. 2021, *Mol Biol Evol* 38:5825, [doi:10.1093/molbev/msab293](https://doi.org/10.1093/molbev/msab293) | “a tool for functional annotation based on precomputed orthology assignments” | Abstract (PubMed 34597405) |
| Orthology is preferred to a raw best hit, but is still not ground truth. | [`docs/EVALUATION.md`](../EVALUATION.md#knowledge-frame-why-evaluation-looks-like-this), knowledge frame (this repository) | “fine-grained orthologs beat raw homology for GO/KEGG transfer; still not ground truth” | The file at the current main branch |
| Domains are evidence, not names. | [`docs/EVALUATION.md`](../EVALUATION.md#knowledge-frame-why-evaluation-looks-like-this), as above | “**Domains are evidence, not names**” | The file at the current main branch |

## 7. See also

- Book: [chapter 2, Homology search](../../book/chapters/02-homology-search.md); [chapter 5, Orthology-based names, GO and KEGG](../../book/chapters/05-orthology-based-names-go-and-kegg.md); [chapter 8, Multi-genome orthology](../../book/chapters/08-multi-genome-orthology.md)
- Knowledge units: [Functional labels and the four numbering schemes](function-concepts.md); [How far to trust a function table](credibility-criteria.md)
