# Reviews & benchmarks — function layer

This repo is the **function** layer (GO / domains / names / pathways). Structure evidence-chooser reviews live upstream.

## Where to read what

| Need | Doc |
|------|-----|
| Structure chooser (Ji *NRG* 2026, Freedman *GR* 2025, Helixer/ANNEVO/EviAnn, Haul 2026-09-14) | [gene-structure-annotation `docs/REVIEWS.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/REVIEWS.md) |
| Allowlisted FA journal patterns (eggNOG *MBE/NAR*, InterPro *NAR*, HR HSE, MapMan *MP*) | [`RECENT_HIGH_QUALITY.md`](RECENT_HIGH_QUALITY.md) |
| Below-allowlist FA peers (TransAnnot, IPS6, CAFA4 preprint) | [`RELATED_SOFTWARE.md`](RELATED_SOFTWARE.md) § Haul 2026-09-14 |
| Gap table (this audit) | [`SELF_AUDIT.md`](SELF_AUDIT.md) |
| Branch map F0–F9 | [`ROADMAP.md`](ROADMAP.md) |

## FA-specific haul snapshot (2026-09-14)

1. **Cite InterPro 2025** (*NAR* doi:10.1093/nar/gkae1082) beside InterProScan in METHODS.  
2. **TransAnnot** / **InterProScan 6** are useful speed/engineering peers — keep in RELATED_SOFTWARE; do **not** redefine F1 standards (allowlist discipline).  
3. **CAFA4** preprint (doi:10.64898/2026.05.06.722942): electronic GO still imperfect — F1 outputs remain transferable hypotheses.  
4. Structure peers with FA hooks (GenePAL eggNOG step, funannotate2-addons) do **not** replace this repo’s merge/release spine.

**Default unchanged:** F0 → F1 (DIAMOND + eggNOG-mapper + InterProScan) → merge → release.
