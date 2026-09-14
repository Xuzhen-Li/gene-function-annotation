# External tutorials & meetings — gene function

Hands-on **functional** annotation tutorials. Structure GTN / JOBIM → sibling  
[gene-structure-annotation `TUTORIALS_AND_MEETINGS.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TUTORIALS_AND_MEETINGS.md).

Chinese: [`zh/17_外部教程与会议.md`](zh/17_外部教程与会议.md).

---

## Software flow tutorials

| Tutorial | Practice | Maps to us | URL |
|----------|----------|------------|-----|
| **Galaxy — Functional annotation of protein sequences** | eggNOG-mapper + InterProScan on proteins | **F1** core (emapper + IPS); add DIAMOND Swiss-Prot in our spine | https://training.galaxyproject.org/training-material/topics/genome-annotation/tutorials/functional/tutorial.html |
| **WorkflowHub / IWC — functional annotation of protein sequences** | Portable emapper + IPS workflow | F1 lab demo | https://www.workflowhub.eu/workflows/2118 · https://github.com/iwc-workflows/functional-annotation-protein-sequences |
| **EnTAP documentation** | Transcriptome-oriented FA frame | **F3** | https://entap.readthedocs.io/ |
| **eggNOG-mapper GitHub / wiki** | Orthology transfer; v3 ↔ eggNOG v7 pairing | F1/F2 | https://github.com/eggnogdb/eggnog-mapper |
| **InterPro / InterProScan docs** | Domains & member DBs | F1c | https://www.ebi.ac.uk/interpro/ |

**Honesty:** GTN functional tutorial often starts from **already predicted proteins** — same assumption as this repo. It may not run DIAMOND Swiss-Prot; our **F1** still recommends it for METHODS.

---

## Meetings

JOBIM 2026 mini-symposium was primarily about **structural** AI/ab initio (Helixer/Tiberius) — read it before trusting DL gene calls that feed FA.  
Hub: https://pepi-ibis.inrae.fr/node/136  

CAFA challenges (GO prediction benchmarks) are **research competitions**, not a substitute for F1 process integrity — see [`EVALUATION.md`](EVALUATION.md).

---

## See also

[`RECENT_HIGH_QUALITY.md`](RECENT_HIGH_QUALITY.md) · [`ROADMAP.md`](ROADMAP.md) · structure tutorials page above.
