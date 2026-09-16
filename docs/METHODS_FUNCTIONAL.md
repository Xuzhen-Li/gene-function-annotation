# METHODS template — functional annotation

Copy into `work/function/release/<TAG>/METHODS.md` and fill FILLs.  
Cite only venues you actually used ([`CITATIONS.md`](CITATIONS.md); journal allowlist in [`RECENT_HIGH_QUALITY.md`](RECENT_HIGH_QUALITY.md)).

Align Gate-F4 (versions) and Gate-F1/F2 (provenance / BUSCO lineage) with [`zh/15_为什么版本和谱系必须写清.md`](zh/15_为什么版本和谱系必须写清.md).

```text
Functional annotation. Representative protein sequences (one translation per
gene model; structure RELEASE_TAG or protein provenance FILL) were compared
with DIAMOND vFILL blastp to UniProt Swiss-Prot (release FILL) and annotated
with eggNOG-mapper vFILL (eggNOG database FILL; taxonomic scope FILL) and
InterProScan vFILL (InterPro / member-DB data release FILL). Gene ontology and
KEGG orthology terms were taken from eggNOG-mapper (and/or KofamScan / F1+
optional KO, FILL). Domain architectures were taken from InterProScan. Optional
human-readable descriptions were assigned with AHRD (FILL). When applicable
(e.g. plants), optional MapMan4 BINs were assigned with Mercator4 (job date FILL;
Schwacke et al. Mol. Plant 2019); optional transcription-factor / kinase families
with iTAK (Zheng et al. Mol. Plant 2016); optional NLR candidates from
InterProScan domain hits and/or HRP (FILL). Per-gene tables were merged with this
repository’s functional-annotation pipeline (functional_master.tsv). Protein-set
completeness was summarized with BUSCO (lineage FILL; mode proteins).
```

**Do not** claim this repository mirrors another lab’s private pipeline; cite the
tools and papers above.


## Gate-F5 — table accounting (fill before claiming F-L1)

Record numbers from `F_merge_tables.py` stderr / summary (do not invent):

- Input protein count (from `PROTEINS_FA`): FILL
- Master row count (`functional_master.tsv`): FILL
- Per-source hit counts (DIAMOND / eggNOG / IPS / …): FILL
- Genes with ≥1 annotation vs all-empty: FILL / FILL
- Rows dropped or duplicate `gene_id` rejected: FILL (must be 0 duplicates)

Empty-all or duplicate gene_id must not pass (script exits non-zero).

