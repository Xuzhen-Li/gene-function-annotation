# Main process — functional annotation

Biology-general. **Goal:** attach function to a stable gene set.  
**Input:** representative `PROTEINS_FA` (+ optional `CURATED_GFF`).  
**Output:** `$WORK_DIR/function/merge/functional_master.tsv` (+ optional AHRD/MapMan/NLR/iTAK tables), then `$WORK_DIR/function/release/<TAG>/`.

**Downstream:** METHODS text, enrichment / MapMan figures, curated gene lists — not automatic GFF attribute write-back.

**Upstream:** sibling [`gene-structure-annotation`](https://github.com/Xuzhen-Li/gene-structure-annotation) evidence chooser → S1–S14 *or* bring your own GFF+proteins. Structure and function are separate layers (Ji *NRG* 2026).

```text
curated proteins (+ GFF)
  → F0 protein QC (BUSCO proteins)
  → F1 default (DIAMOND + eggNOG-mapper + InterProScan)
       or F2 / F3 / F5 alternate frames
  → optional F4 AHRD · F6 Mercator4 · F8 NLR · F9 iTAK
  → merge tables → F_release.sh
```

No proteins yet? Upstream structural spine: [`gene-structure-annotation` MAIN](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/steps/MAIN.md) (S1–S14), then return here.

## Default order (paper)

1. [`../INSTALL_FUNCTIONAL.md`](../INSTALL_FUNCTIONAL.md)  
2. [`../SCENARIOS_FUNCTIONAL.md`](../SCENARIOS_FUNCTIONAL.md) **F1**  
3. **F4** for readable names; **F6/F8/F9** when doing plant HR/MP-style METHODS  
4. `bash pipeline/F_release.sh`  
5. Fill [`../METHODS_FUNCTIONAL.md`](../METHODS_FUNCTIONAL.md)

## Branch table

| ID | When | Core tools | In-repo runner |
|----|------|------------|----------------|
| **F0** | Always | BUSCO proteins | inline in scenarios |
| **F1** | Default / paper | DIAMOND + emapper + InterProScan | `F1_diamond.sh` `F2_eggnog.sh` `F3_interproscan.sh` |
| **F2** | Fast | emapper (± Kofam) | `F2_eggnog.sh` `F1b_kofam.sh` |
| **F3** | EnTAP frame | EnTAP | docs + copy TSV |
| **F4** | Readable names | AHRD | `F4_join_ahrd.py` · `F4_run_ahrd.md` |
| **F5** | Transcriptome CDS | Trinotate (± F1) | docs/tools/trinotate.md |
| **F6** | Plant MapMan BINs (optional) | Mercator4 | `F6_ingest_mercator.py` |
| **F7** | Multi-genome | OrthoFinder → F1 on reps | `F7_orthofinder.sh` |
| **F8** | Plant NLR (optional) | IPS filter ± HRP | `F8_run.sh` `F8_list_nlr_from_ips.py` |
| **F9** | Plant TF / kinase (optional) | iTAK | `F9_itak.sh` |

Commands: [`../FUNCTIONAL_GUIDE.md`](../FUNCTIONAL_GUIDE.md).  
Standards: [`../RECENT_HIGH_QUALITY.md`](../RECENT_HIGH_QUALITY.md).  
Citations: [`../CITATIONS.md`](../CITATIONS.md).
