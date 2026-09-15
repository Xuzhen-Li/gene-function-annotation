# Functional annotation quality — methods, papers, repos

Grades: [`EVALUATION.md`](EVALUATION.md) / [`EVALUATION_CHECKLIST.md`](EVALUATION_CHECKLIST.md).  
This page lists **extra** ways peers discuss FA quality — without turning CAFA into a lab gate.

Chinese: [`zh/验收勾选表.md`](zh/验收勾选表.md)

---

## Spine we already require

| Need | Role |
|------|------|
| Protein provenance + F0 BUSCO | Structure hand-off sanity |
| F1 frame (DIAMOND + eggNOG + InterPro) or waiver | Process integrity |
| Versions + master TSV + release pack | Reproducibility |

---

## Soft add-ons (report; clade-dependent)

| Method | What it adds | Caution |
|--------|--------------|---------|
| Swiss-Prot / emapper / IPS **coverage %** | METHODS coverage narrative | Low plant hit rates ≠ automatic fail |
| Domain-only vs GO-empty genes | Honest evidence mix | Domains ≠ gene names |
| AHRD / Mercator / NLR / iTAK modules | Plant community languages | Optional modules, not higher grade |
| Upstream structure RNA/OMArk story | Two-layer audit | FA cannot fix bad structure |

## Papers / benchmarks (cite, do not overclaim)

| Source | Use |
|--------|-----|
| CAFA4 / CAFA community | Reminds GO transfer is imperfect — **not** our F-L1 score |
| InterPro *NAR* DB issues | Version pins matter (gate F4) |
| eggNOG-mapper / eggNOG v7 pairing | Mapper–DB mismatch = auto-fail risk |
| Journal METHODS patterns | [`RECENT_HIGH_QUALITY.md`](RECENT_HIGH_QUALITY.md) |

Upstream structure QC shelf: [gene-structure-annotation `QUALITY_SOURCES.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/QUALITY_SOURCES.md).

## Print recommended commands

```bash
set -a && source config/local.env && set +a
python3 pipeline/print_qc_commands.py
```
