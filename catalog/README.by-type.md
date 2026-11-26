# Catalogue by type

[中文](README.by-type.zh.md) · [Full catalogue](METHODS_CATALOG.md) · [Counts](COUNTS.md) · [Index by stage](README.md)

One row per type section of the methods catalogue. Entry counts come from [`SOFTWARE_AUTHORITY.tsv`](SOFTWARE_AUTHORITY.tsv) (194 entries, 2026-11-26). The type-class key is the label used in the 2026-11 survey file [`docs/CATALOG_BY_TYPE_2026-11.md`](../docs/CATALOG_BY_TYPE_2026-11.md), which is kept as a legacy record. The folders in this directory sort the first-pass cards by stage; that index ([`README.md`](README.md)) is kept unchanged as a second view.

| # | Type section | Type-class key (legacy) | Entries | Default and branch tools | Book chapter | Knowledge unit |
|---|---|---|---|---|---|---|
| 1 | [1. Homology search](METHODS_CATALOG.md#section-1) | `homology-search` | 8 | DIAMOND (v2) | [ch. 2](../book/chapters/02-homology-search.md) | [homology-transfer](../docs/kb/homology-transfer.md) |
| 2 | [2. Reference sequence and ontology databases](METHODS_CATALOG.md#section-2) | `reference-db` | 11 | — | [ch. 3](../book/chapters/03-reference-sequence-and-ontology-databases.md) | [homology-transfer](../docs/kb/homology-transfer.md) |
| 3 | [3. Domain and family annotation](METHODS_CATALOG.md#section-3) | `domain` | 6 | InterProScan 6 | [ch. 4](../book/chapters/04-domain-and-family-annotation.md) | [homology-transfer](../docs/kb/homology-transfer.md) |
| 4 | [4. Orthology-based names, GO and KEGG](METHODS_CATALOG.md#section-4) | `orthology-go` | 12 | eggNOG-mapper v2, AHRD, Trinotate | [ch. 5](../book/chapters/05-orthology-based-names-go-and-kegg.md) | [homology-transfer](../docs/kb/homology-transfer.md) |
| 5 | [5. Machine-learning GO prediction](METHODS_CATALOG.md#section-5) | `ml-go` | 11 | — | [ch. 6](../book/chapters/06-machine-learning-go-prediction.md) | [credibility-criteria](../docs/kb/credibility-criteria.md) |
| 6 | [6. Pathways, KO and EC](METHODS_CATALOG.md#section-6) | `pathway-enzyme` | 18 | — | [ch. 7](../book/chapters/07-pathways-ko-and-ec.md) | — |
| 7 | [7. Multi-genome orthology](METHODS_CATALOG.md#section-7) | `multi-genome-orthology` | 16 | OrthoFinder 3 | [ch. 8](../book/chapters/08-multi-genome-orthology.md) | — |
| 8 | [8. Localization and topology](METHODS_CATALOG.md#section-8) | `localization` | 11 | SignalP 6.0, DeepTMHMM, TMbed | [ch. 9](../book/chapters/09-localization-and-topology.md) | — |
| 9 | [9. Plant gene families](METHODS_CATALOG.md#section-9) | `plant-family` | 20 | — | [ch. 10](../book/chapters/10-plant-gene-families.md) | — |
| 10 | [10. Non-coding RNA function resources](METHODS_CATALOG.md#section-10) | `ncrna-function` | 11 | — | [ch. 11](../book/chapters/11-non-coding-rna-function-resources.md) | — |
| 11 | [11. Expression-supported function](METHODS_CATALOG.md#section-11) | `expression` | 9 | — | [ch. 12](../book/chapters/12-expression-supported-function.md) | — |
| 12 | [12. Community catalogues and naming](METHODS_CATALOG.md#section-12) | `community-db` | 4 | — | [ch. 13](../book/chapters/13-community-catalogues-and-naming.md) | — |
| 13 | [13. Protein 3D structure](METHODS_CATALOG.md#section-13) | `protein-3d` | 23 | Foldseek | [ch. 14](../book/chapters/14-protein-3d-structure.md) | — |
| 14 | [14. Downstream enrichment](METHODS_CATALOG.md#section-14) | `enrichment` | 15 | — | [ch. 15](../book/chapters/15-downstream-enrichment.md) | — |
| 15 | [15. Ideas, formats and merge rules](METHODS_CATALOG.md#section-15) | `idea` | 9 | — | [ch. 16](../book/chapters/16-ideas-formats-and-merge-rules.md) | [function-concepts](../docs/kb/function-concepts.md) |
| viz | [Visualization tools](METHODS_CATALOG.md#visualization) | — | 10 | — | [ch. 17](../book/chapters/17-visualization-tools.md) | — |

**Total: 194**

## Stage folders with no cards

These stage folders hold no first-pass card. They are kept so that stage links still resolve; the tools for these steps are in the type sections above.

- F0 · protein input QC (BUSCO protein mode): [`F0_protein_qc/`](F0_protein_qc/README.md)
- F2 · fast framework (eggNOG-mapper alone ± Kofam; KEGGaNOG plots): [`frame_F2/`](frame_F2/README.md)
- F3 · EnTAP framework: [`frame_F3/`](frame_F3/README.md)
- Merge / aggregate (`F_merge_tables.py`, `F_aggregate.py`): [`Fmerge_aggregate/`](Fmerge_aggregate/README.md)
