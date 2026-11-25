# Chapter 17. Visualization tools

*This chapter reproduces [README section Visualization tools](../../README.md#visualization): the section notes, the full tool table with paper, lab, tier and evaluation, and the benchmark notes. Links point back into the repository.*

Tools for looking at gene models and for figures. Rows marked general-purpose are not specific to annotation. Rows that already appear in a type section are listed again here with a pointer and are not counted twice.

<a id="viz-1"></a>
## Domain and motif diagrams

| Tool | Role | What it does / when to use | Paper | Lab (corresponding author, institution) | Tier · citations | Evaluation (source) |
|---|---|---|---|---|---|---|
| [IBS 2.0](https://ibs.renlab.org/) | alternative, general-purpose | Draws protein domain and motif diagrams for figures. | [Nucleic Acids Research 2022](https://doi.org/10.1093/nar/gkac373) | Jian Min Ren (Sun Yat-sen University) | established · 279 | Paper: “Here, we present a professional tool called IBS 2.0 for illustrating the organization of both protein and nucleotide sequences.” |
| [drawProteins](https://bioconductor.org/packages/drawProteins/) | alternative | R/Bioconductor domain-architecture diagrams from UniProt features. | [F1000Research 2018](https://doi.org/10.12688/f1000research.14541.1) | Paul Brennan (Cardiff University) | niche · 66 | no abstract or repo text available; see paper |

<a id="viz-2"></a>
## GO and enrichment plots

| Tool | Role | What it does / when to use | Paper | Lab (corresponding author, institution) | Tier · citations | Evaluation (source) |
|---|---|---|---|---|---|---|
| [enrichplot](https://github.com/YuLab-SMU/enrichplot) | alternative | Dot, bar, cnet and emap plots for clusterProfiler results (no separate paper). | no paper | — | no paper | Repo description: “Visualization of Functional Enrichment Result”; GitHub last push 2026-11 |
| [GOplot](https://github.com/wencke/wencke.github.io) | alternative | R package combining enrichment results with expression (chord, circle plots). | [Bioinformatics 2015](https://doi.org/10.1093/bioinformatics/btv300) | Fátima Sánchez‐Cabo (Spanish National Centre for Cardiovascular Research) +1 | standard · 2053 | Paper: “Here we present an R package called GOplot, based on ggplot2, for enhanced graphical representation.”; GitHub last push 2016-12 |
| [Revigo](http://revigo.irb.hr/) | alternative | Summarises long lists of enriched GO terms into non-redundant groups by semantic similarity. (see section 14) | [PLoS ONE 2011](https://doi.org/10.1371/journal.pone.0021800) | Fran Supek (Universitat Pompeu Fabra) | standard · 7068 | Authors: “Furthermore, REVIGO visualizes this non-redundant GO term set in multiple ways to assist in interpretation: multidimensional scaling and graph-based visualizations accurately render the subdivisions and the semantic relationships in the data, while treemaps …” |
| [simplifyEnrichment](https://github.com/jokergoo/simplifyEnrichment) | alternative | Clusters enriched GO terms by semantic similarity and displays word-cloud summaries for each cluster. (see section 14) | [Genomics Proteomics & Bioinformatics 2022](https://doi.org/10.1016/j.gpb.2022.04.008) | Zuguang Gu (National Center for Tumor Diseases) +1 | established · 348 | GitHub last push 2026-01 |
| [clusterProfiler 4.0](https://github.com/YuLab-SMU/clusterProfiler) | alternative | R enrichment with custom TERM2GENE from merged_function_table.tsv. (see section 14) | [The Innovation 2021](https://doi.org/10.1016/j.xinn.2021.100141) | Xiaochen Bo (Beijing Radiation Center) +1 | standard · 17017 | Paper: “To meet these requirements, we present here an updated version of our popular Bioconductor package, clusterProfiler 4.0.”; GitHub last push 2026-11 |
| [ClueGO](https://apps.cytoscape.org/apps/cluego) | alternative | Cytoscape app that groups enriched GO terms and pathways into networks. (see section 14) | [Bioinformatics 2009](https://doi.org/10.1093/bioinformatics/btp101) | Jérôme Galon (Inserm) | standard · 6926 | Authors: “We have developed ClueGO, an easy to use Cytoscape plug-in that strongly improves biological interpretation of large lists of genes.” |

<a id="viz-3"></a>
## Pathway maps

| Tool | Role | What it does / when to use | Paper | Lab (corresponding author, institution) | Tier · citations | Evaluation (source) |
|---|---|---|---|---|---|---|
| [Pathview](https://bioconductor.org/packages/pathview/) | alternative | Paints gene or compound data onto KEGG pathway maps. | [Bioinformatics 2013](https://doi.org/10.1093/bioinformatics/btt285) | Weijun Luo (University of North Carolina at Charlotte) | standard · 2671 | no abstract or repo text available; see paper |
| [iPath3.0](https://pathways.embl.de/) | alternative | Interactive overview maps of metabolism for coloring KO/EC sets. | [Nucleic Acids Research 2018](https://doi.org/10.1093/nar/gky299) | Peer Bork (Max Delbrück Center) +1 | established · 343 | no abstract or repo text available; see paper |
| [MapMan (viewer)](https://mapman.gabipd.org/) | alternative | Paints plant omics data onto MapMan pathway diagrams; pairs with Mercator4 bins. | [The Plant Journal 2004](https://doi.org/10.1111/j.1365-313X.2004.02016.x) | Mark Stitt (Max Planck Society) | standard · 3804 | no abstract or repo text available; see paper |
| [KEGG Mapper](https://www.kegg.jp/kegg/mapper/) | alternative | Maps KO lists onto KEGG pathways, BRITE and modules. (see section 6) | [Protein Science 2019](https://doi.org/10.1002/pro.3711) | Minoru I. Kanehisa (Kyoto University Institute for Chemical Research) | standard · 1339 | Paper: “Here we report a new version of KEGG Mapper, a suite of KEGG mapping tools available at the KEGG website (https://www.kegg.jp/ or https://www.genome.jp/kegg/), together with the KOALA family tools for automatic assignment of KO (KEGG Orthology) identifiers …” |

<a id="viz-4"></a>
## Networks

| Tool | Role | What it does / when to use | Paper | Lab (corresponding author, institution) | Tier · citations | Evaluation (source) |
|---|---|---|---|---|---|---|
| [Cytoscape](https://cytoscape.org/) | alternative, general-purpose | Network visualization platform for co-expression, PPI and enrichment maps. | [Genome Research 2003](https://doi.org/10.1101/gr.1239303) | Trey Ideker (University of California San Diego) | standard · 57947 | no abstract or repo text available; see paper |
| [ClueGO](https://apps.cytoscape.org/apps/cluego) | alternative | Cytoscape app that groups enriched GO terms and pathways into networks. (see section 14) | [Bioinformatics 2009](https://doi.org/10.1093/bioinformatics/btp101) | Jérôme Galon (Inserm) | standard · 6926 | Authors: “We have developed ClueGO, an easy to use Cytoscape plug-in that strongly improves biological interpretation of large lists of genes.” |

<a id="viz-5"></a>
## 3D structure viewers

| Tool | Role | What it does / when to use | Paper | Lab (corresponding author, institution) | Tier · citations | Evaluation (source) |
|---|---|---|---|---|---|---|
| [UCSF ChimeraX](https://www.cgl.ucsf.edu/chimerax/) | alternative, general-purpose | Desktop 3D structure viewer for predicted models (pLDDT coloring, superposition). | [Protein Science 2020](https://doi.org/10.1002/pro.3943) | Thomas E. Ferrin (University of California, San Francisco) | standard · 10274 | Authors: “ChimeraX brings (a) significant performance and graphics enhancements; (b) new implementations of Chimera's most highly used tools, many with further improvements; (c) several entirely new analysis features; (d) support for new areas such as virtual reality, …” |
| [Mol* Viewer](https://molstar.org/) | alternative, general-purpose | Web 3D structure viewer used by RCSB PDB and the AlphaFold DB. | [Nucleic Acids Research 2021](https://doi.org/10.1093/nar/gkab314) | Alexander Rose (San Diego Supercomputer Center) | standard · 1333 | no abstract or repo text available; see paper |
