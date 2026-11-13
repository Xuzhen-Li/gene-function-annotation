# Figures

| File | Role |
|------|------|
| `functional_spine.svg` / `.png` | **Beginner** one-glance spine (zh + root README) |
| `functional_overview.*` | Advanced playbook (keep; fold on zh entry) |
| `plant_sim_three_lines.*` | Copy of structure classroom crop lines |

Do not edit the `.svg` or `.png` image files by hand (`plant_sim_three_lines.*` is copied from the structure repo and has no script here). Edit the Python script that holds the layout and box lists. Open a terminal (Mac: Terminal app; Linux: a terminal window; cluster: your login shell) inside the `gene-function-annotation` folder (the repo root). Run `python3 docs/figures/src/functional_spine.py` or `python3 docs/figures/src/functional_overview.py`. Each script writes the `.svg` and uses `rsvg-convert` (librsvg) to export the `.png` at 200 dpi (dots per inch). Without `rsvg-convert`, it prints `"rsvg-convert not found: PNG not updated"`. Text-fit checks use Pillow and an Arial font via `FONT_DIR`, and are skipped when either is missing.

## Catalog figures (added 2026-11-13)

Software-output figures from CC BY papers (Europe PMC `license` field `cc by`, checked 2026-11-13). No NC/ND. Original JPEGs, not redrawn. Credits are repeated under each figure on the homepage and in the README figure-credits table.

| File | Tool | Section | Credit |
|---|---|---|---|
| `catalog/01_eggnogmapper_v2_runtime.jpg` | eggNOG-mapper v2 runtime | orthology-go | Cantalapiedra et al. 2021, Mol. Biol. Evol., Fig. 2, doi:10.1093/molbev/msab293, PMC8662613, CC BY. |
| `catalog/02_eggnogmapper_vs_interproscan.jpg` | eggNOG-mapper versus InterProScan | orthology-go | Huerta-Cepas et al. 2017, Mol. Biol. Evol., Fig. 3, doi:10.1093/molbev/msx148, PMC5850834, CC BY. |
| `catalog/03_eggnogmapper_rhogap1_go.jpg` | eggNOG-mapper GO example | orthology-go | Huerta-Cepas et al. 2017, Mol. Biol. Evol., Fig. 4, doi:10.1093/molbev/msx148, PMC5850834, CC BY. |
| `catalog/04_interpro_pik3ca_domains.jpg` | InterPro PIK3CA domains | domain | Blum, Andreeva, Florentino et al. 2025, Nucleic Acids Res., Fig. 4, doi:10.1093/nar/gkae1082, PMC11701551, CC BY. |
| `catalog/05_interproscan_human_runtime.jpg` | InterProScan human runtime | domain | Blum, Andreeva, Florentino et al. 2025, Nucleic Acids Res., Fig. 6, doi:10.1093/nar/gkae1082, PMC11701551, CC BY. |
| `catalog/06_orthofinder_chordata_summary.jpg` | OrthoFinder Chordata | multi-genome-orthology | Emms and Kelly 2019, Genome Biol., Fig. 3, doi:10.1186/s13059-019-1832-y, PMC6857279, CC BY. |
| `catalog/07_omark_vs_busco_proteomes.jpg` | OMArk versus BUSCO proteomes | data-needs | Nevers et al. 2025, Nat. Biotechnol. 43(1):124-133, Fig. 5, doi:10.1038/s41587-024-02147-w (online 2024-02-21), PMC11738984, CC BY. |

