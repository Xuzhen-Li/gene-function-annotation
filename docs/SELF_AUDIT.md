# Self-audit — gene-function-annotation

**Date:** 2026-09-14 (UTC+8 / Asia/Shanghai)  
**Scope:** Functional annotation reviews / peers vs F1 spine and allowlist.  
**Upstream structure audit:** [gene-structure-annotation `docs/SELF_AUDIT.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/SELF_AUDIT.md).

## Gap table

| Gap | Evidence from lit / peer | Action taken or deferred |
|-----|--------------------------|---------------------------|
| InterPro citation stale / generic | Blum et al. *NAR* 2025 doi:10.1093/nar/gkae1082 | **Taken:** row in RECENT_HIGH_QUALITY + RELATED |
| Fast FA pipeline vs EnTAP/Trinotate/emapper | TransAnnot *Bioinf Adv* 2024 doi:10.1093/bioadv/vbae152 | **Taken:** RELATED (below allowlist); **deferred:** not an F-frame — speed peer only |
| InterProScan Nextflow rewrite | IPS6 *Bioinf Adv* 2026 doi:10.1093/bioadv/vbag141 | **Taken:** RELATED watch; **deferred:** keep current IPS runner until lab adopts v6 |
| GO prediction state of the art | CAFA4 bioRxiv doi:10.64898/2026.05.06.722942 | **Taken:** RELATED caveat; **not** allowlist standard |
| Structure+FA Nextflow with eggNOG | GenePAL Zenodo doi:10.5281/zenodo.14195006 | **Taken:** RELATED pointer; structure PEER has full entry |
| REVIEWS.md was a stub | Mission request | **Taken:** pointer page → structure REVIEWS + RECENT_HIGH_QUALITY + haul |
| EnTAP / Trinotate already alternate frames | Existing ROADMAP F3/F5 | **Already covered** |
| eggNOG v7 DB | Already in RECENT_HIGH_QUALITY | **Already covered** |
| HR HortGenome Search Engine pattern | Already B2 | **Already covered** |
| DL GO (NetGO / DeepFRI / ProteInfer) | Already RELATED peers | **Already covered** — optional post-F1 |
| Write GO into GFF column 9 | User/roadmap explicit non-claim | **Deferred** (honest gap) |

## ROADMAP

**No rewrite.** One documentation honesty item only: REVIEWS pointer + SELF_AUDIT link from README. F1 remains default.

## Chooser honesty (unchanged)

```text
Publication proteins → F1
Need speed today     → F2 (IPS later)
Lab on EnTAP         → F3
Transcriptome only   → F5
Plant paper extras   → F4 / F6 / F8 / F9 after F1
```
