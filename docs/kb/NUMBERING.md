# Numbering schemes

[中文](NUMBERING.zh.md) · [Knowledge units](README.md)

Several numbering schemes are used in this repository. The current ones are used in new pages; the legacy ones are kept in older pages and are not renumbered. This page maps them.

| Scheme | Labels | Status | Defined in |
|---|---|---|---|
| Catalogue type sections | 1–15 and visualization | current | [`catalog/METHODS_CATALOG.md`](../../catalog/METHODS_CATALOG.md); `section` column of the TSV |
| Book chapters | 1–20 and appendix A; chapter *n* + 1 covers type section *n*, chapter 17 covers visualization | current | [`book/`](../../book/README.md) |
| Frameworks and add-on stages | F1 (default), F2, F3, F5; add-ons F0, F4, F6–F10 | current | [`catalog/_namespaces.md`](../../catalog/_namespaces.md) |
| Script files | `F1_diamond.sh`, `F2_eggnog.sh`, `F3_interproscan.sh` = the three steps of framework F1; `F1b_kofam.sh` = the Kofam step of F1 | current; never a stage name | [`catalog/_namespaces.md`](../../catalog/_namespaces.md) |
| TOOLS cards | F1a, F1b, F1c; F1+, F2+ | current; card labels only | [`docs/TOOLS.md`](../TOOLS.md) |
| Finish grades and gates | F-L0, F-L1; Gate-F1–Gate-F7 | current | [`docs/EVALUATION.md`](../EVALUATION.md) |
| Stage folders of initial cards | `F0_protein_qc/`, `frame_F1/` … `Frelease/` | legacy view (2026-11 initial) | [`catalog/README.md`](../../catalog/README.md) |
| Type-class keys | `homology-search` … `idea` | legacy (2026-11 survey) | [`docs/CATALOG_BY_TYPE_2026-11.md`](../CATALOG_BY_TYPE_2026-11.md) |

## Type sections, legacy keys and book chapters

| Type section (current) | Type-class key (legacy) | Book chapter |
|---|---|---|
| [1. Homology search](../../catalog/METHODS_CATALOG.md#section-1) | `homology-search` | [Chapter 2. Homology search](../../book/chapters/02-homology-search.md) |
| [2. Reference sequence and ontology databases](../../catalog/METHODS_CATALOG.md#section-2) | `reference-db` | [Chapter 3. Reference sequence and ontology databases](../../book/chapters/03-reference-sequence-and-ontology-databases.md) |
| [3. Domain and family annotation](../../catalog/METHODS_CATALOG.md#section-3) | `domain` | [Chapter 4. Domain and family annotation](../../book/chapters/04-domain-and-family-annotation.md) |
| [4. Orthology-based names, GO and KEGG](../../catalog/METHODS_CATALOG.md#section-4) | `orthology-go` | [Chapter 5. Orthology-based names, GO and KEGG](../../book/chapters/05-orthology-based-names-go-and-kegg.md) |
| [5. Machine-learning GO prediction](../../catalog/METHODS_CATALOG.md#section-5) | `ml-go` | [Chapter 6. Machine-learning GO prediction](../../book/chapters/06-machine-learning-go-prediction.md) |
| [6. Pathways, KO and EC](../../catalog/METHODS_CATALOG.md#section-6) | `pathway-enzyme` | [Chapter 7. Pathways, KO and EC](../../book/chapters/07-pathways-ko-and-ec.md) |
| [7. Multi-genome orthology](../../catalog/METHODS_CATALOG.md#section-7) | `multi-genome-orthology` | [Chapter 8. Multi-genome orthology](../../book/chapters/08-multi-genome-orthology.md) |
| [8. Localization and topology](../../catalog/METHODS_CATALOG.md#section-8) | `localization` | [Chapter 9. Localization and topology](../../book/chapters/09-localization-and-topology.md) |
| [9. Plant gene families](../../catalog/METHODS_CATALOG.md#section-9) | `plant-family` | [Chapter 10. Plant gene families](../../book/chapters/10-plant-gene-families.md) |
| [10. Non-coding RNA function resources](../../catalog/METHODS_CATALOG.md#section-10) | `ncrna-function` | [Chapter 11. Non-coding RNA function resources](../../book/chapters/11-non-coding-rna-function-resources.md) |
| [11. Expression-supported function](../../catalog/METHODS_CATALOG.md#section-11) | `expression` | [Chapter 12. Expression-supported function](../../book/chapters/12-expression-supported-function.md) |
| [12. Community catalogues and naming](../../catalog/METHODS_CATALOG.md#section-12) | `community-db` | [Chapter 13. Community catalogues and naming](../../book/chapters/13-community-catalogues-and-naming.md) |
| [13. Protein 3D structure](../../catalog/METHODS_CATALOG.md#section-13) | `protein-3d` | [Chapter 14. Protein 3D structure](../../book/chapters/14-protein-3d-structure.md) |
| [14. Downstream enrichment](../../catalog/METHODS_CATALOG.md#section-14) | `enrichment` | [Chapter 15. Downstream enrichment](../../book/chapters/15-downstream-enrichment.md) |
| [15. Ideas, formats and merge rules](../../catalog/METHODS_CATALOG.md#section-15) | `idea` | [Chapter 16. Ideas, formats and merge rules](../../book/chapters/16-ideas-formats-and-merge-rules.md) |
