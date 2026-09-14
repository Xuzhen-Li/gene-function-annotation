# High-quality annotation sources — journal allowlist only

**Allowed venues only** (user rule): Cell / Cell Press sister journals and above, plus  
**MP** (*Molecular Plant*), **PC** (*The Plant Cell*), **PBJ** (*Plant Biotechnology Journal*),  
**HR** (*Horticulture Research*), **MBE** (*Molecular Biology and Evolution*),  
**NAR** (*Nucleic Acids Research*), **GB** (*Genome Biology* / *Genome Research*),  
and Nature / Science family research journals.

**Excluded from standards here:** *Scientific Data*, *G3*, *Frontiers*, preprints, Zenodo-only, unreviewed GitHub pipelines.

---

## A. Tool / method papers (cite these for METHODS)

| Tool | Venue | Citation | Role in our FA spine |
|------|--------|----------|----------------------|
| eggNOG-mapper v2 | **MBE** 2021 | Cantalapiedra et al. doi:10.1093/molbev/msab293 | F1/F2 core |
| eggNOG v7 DB | **NAR** 2026 | Hernández-Plaza et al. doi:10.1093/nar/gkaf1249 | emapper DB |
| eggNOG 5/6 DBs | **NAR** | Huerta-Cepas et al. | legacy DB notes |
| InterPro / InterProScan | **NAR** (resource issues) | Blum / Paysan-Lafosse et al. InterPro updates | F1 domains/GO |
| InterPro 2025 resource | **NAR** 2025 | Blum et al. doi:10.1093/nar/gkae1082 | Cite current InterPro DB for F1 IPS |
| MapMan4 + Mercator4 | **MP** 2019 | Schwacke et al. doi:10.1016/j.molp.2019.01.003 | F6 plant BINs |
| BRAKER3 | **Genome Research** 2024 | Gabriel et al. doi:10.1101/gr.278090.123 | upstream structure |
| GSAman last-mile | **The Innovation** (Cell Press partner) 2026 | Chen, Chen & Xia doi:10.1016/j.xinn.2026.101537 | upstream curation |
| iTAK (TF/kinase) | **MP** 2016 | Zheng et al. doi:10.1016/j.molp.2016.09.014 | optional TF call |
| quarTeT (T2T toolkit) | **HR** 2023 | Lin et al. doi:10.1093/hr/uhad127 | upstream Asm only |
| T2T-Hub | **NAR** 2026 | doi:10.1093/nar/gkag423 | optional online FA check |

---

## B. How top journals actually annotate function (recent)

### B1. *Horticulture Research* T2T / genome papers (pattern)

Repeated FA pattern across recent HR T2T/genome articles (e.g. broccoli uhag110; monk fruit uhag103):

```text
proteins → search multiple DBs:
  eggNOG (± COG/KOG)
  PFAM
  Swiss-Prot / UniProt
  NR
  GO
  KEGG
→ report % genes hitting ≥1 DB
```

**Our mapping:** F1 = DIAMOND SwissProt + eggNOG-mapper + InterProScan (PFAM/GO); KEGG from emapper (± KofamScan). NR optional (heavy).

### B2. HortGenome Search Engine — **HR** 2024 (uhae100)

Documented FA recipe for 500+ horticultural genomes:

1. BLAST vs NR, UniProt (TrEMBL+SwissProt), Arabidopsis  
2. **AHRD** descriptions  
3. **InterProScan** domains  
4. **eggNOG-mapper** → GO / KEGG  
5. **iTAK** TF / TR / kinases  

**Our mapping:** F1 + F4 (AHRD) + optional iTAK (add if needed). This is the **primary horticulture-journal template** for this repo.

### B3. *Molecular Plant* — MapMan4 / Mercator4

Schwacke et al. **MP** 2019: plant-specific BIN ontology + Mercator4 web annotation.  
**Our mapping:** F6 (required for plant-pathway figures in MP/HR-style papers).

### B4. Cell / Cell Genomics T2T collection

Assembly-first (Verkko-Fillet, TTT, …). Gene models often **CAT + Liftoff / LiftOn** (CHM13 lineage).  
**Functional:** not a new FA standard — use A/B1–B3 above after proteins exist.  
**Our mapping:** LiftOn → upstream S4/S11 only ([LiftOn (structure repo)](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/tools/lifton.md)).

### B5. *Nature Genetics* — Garg et al. 2024 plant T2T review

doi:10.1038/s41588-024-01830-7 — assembly / pangenome / breeding impact.  
Does **not** replace FA METHODS; cite for T2T assembly context only.

### B6. *Genome Research* — BRAKER3

Upstream structural default (with BRAKER4 runner). Not an FA paper.

### B7. *The Innovation* — GSAman

Upstream last-mile structure before FA.

---

## C. Standardized “journal-grade” FA (this repo)

Biology-general core (*Vitis*/horticulture papers are one evidence lane). Core aligned to **MBE/NAR eggNOG + NAR InterPro + Swiss-Prot**; plant extras (Mercator4 / iTAK / HR HSE) are optional:

```text
F0  BUSCO proteins (lineage = your clade)
F1  DIAMOND SwissProt (+ optional NR)
    eggNOG-mapper (MBE/NAR; tax scope = your clade)
    InterProScan (NAR InterPro)
F4  AHRD descriptions (optional; HR HSE-style)
±   F6 Mercator4 MapMan BINs (plants / MP)
±   F8/F9 NLR / iTAK (plants)
±   KofamScan KO (optional KEGG depth)
→ merge → release
```

Copy-paste: [`INSTALL_FUNCTIONAL.md`](INSTALL_FUNCTIONAL.md) → [`SCENARIOS_FUNCTIONAL.md`](SCENARIOS_FUNCTIONAL.md) **F1** then F4 (± F6 for plants).

**PANNZER2:** useful in some pipelines but **not** retained as a tier-defining citation under this allowlist unless/until a listed journal METHODS block is added; keep tool page optional only.

---

## D. Do not use as standards (below allowlist)

| Source | Why dropped as standard |
|--------|-------------------------|
| *Scientific Data* Camellia FA stack | Below allowlist (was previous draft reference) |
| GeneForge GitHub | No allowlisted paper attached here |
| zgtools marketing claims | Not a listed journal METHODS |
| G3 / Frontiers genome notes | Below allowlist |

---

## E. Haul 2026-09-14 (allowlist-compatible only)

New **NAR** InterPro 2025 resource paper folded into table A above (doi:10.1093/nar/gkae1082).

**Does not change F1 spine:** DIAMOND Swiss-Prot + eggNOG-mapper + InterProScan remains journal-grade default (HR HSE / MBE-NAR pattern).

Below-allowlist but useful FA peers (TransAnnot, InterProScan 6, CAFA4 preprint, EnTAP/Trinotate speed notes) → [`RELATED_SOFTWARE.md`](RELATED_SOFTWARE.md) § Haul 2026-09-14 — **not** standards here.
