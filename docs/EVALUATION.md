# Final evaluation criteria — gene function

**What “done” means** for a functional release.  
Path choice: [`ROADMAP.md`](ROADMAP.md). **This page judges the finish.**

Upstream structure criteria: [gene-structure-annotation `EVALUATION.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/EVALUATION.md).

Journal-facing patterns: [`RECENT_HIGH_QUALITY.md`](RECENT_HIGH_QUALITY.md).  
Honesty / deferred items: [`SELF_AUDIT.md`](SELF_AUDIT.md).

---

## Two finish grades

| Grade | Label | When |
|-------|-------|------|
| **F-L0 Slim** | `status=provisional` or `frame=F2/F3/F5` | Fast frame only; IPS deferred; or incomplete merge |
| **F-L1 Qualified** | `status=qualified` | Hard gates below — default paper FA |

Plant add-ons (F4/F6/F8/F9) are **not** a higher grade by themselves; they are METHODS modules on top of F-L1.

---

## Hard gates (F-L1 — fail any ⇒ not qualified)

| # | Gate | Pass | Fail |
|---|------|------|------|
| F1 | Stable protein input | `PROTEINS_FA` source named (structure `RELEASE_TAG` or external hash/path) in METHODS | Anonymous `proteins.faa` with no provenance |
| F2 | Upstream sanity | F0 protein BUSCO: Completeness **+ lineage** recorded; if catastrophic, structure fixed first | Ignoring broken gene set and “annotating function” anyway |
| F3 | Default frame (or waiver) | **F1** run (DIAMOND + eggNOG-mapper + InterProScan) **or** written waiver naming F2/F3/F5 and why | Mystery pipeline; BLAST-only dump as master |
| F4 | Versions pinned | Tool + DB versions (Swiss-Prot / eggNOG / InterPro) in METHODS | Undated DBs |
| F5 | Master table integrity | `functional_master.tsv` gene count ≈ input proteins; drops documented | Silent row loss; duplicate gene IDs unexplained |
| F6 | Release pack | `F_release.sh` → `function/release/<TAG>/` with master TSV + proteins copy + METHODS stub | Only raw diamond/IPS folders |
| F7 | Hygiene | No private BAM/FASTQ / multi-GB DB files in the repo or release | Accidental DB commit |

---

## Soft metrics (report; clade-dependent)

| Metric | Use | Anti-pattern |
|--------|-----|--------------|
| F0 BUSCO-C | Sanity of the protein set | Treating FA BUSCO as structure QC replacement |
| Swiss-Prot / emapper hit rates | Coverage narrative in METHODS | Claiming “all genes annotated” from partial hits |
| IPS domain coverage | Domain evidence density | GO from homology alone without saying so |
| AHRD / Mercator / NLR / iTAK | Optional modules — list used or unused | Implying MapMan ran when it did not |
| Count match master↔proteins | F5 gate support | Padding rows with empty stubs to force 100% |

**Not claimed (automatic non-goal):** writing GO/KEGG into GFF column 9. Master TSV is the source of truth until that feature exists.

---

## Automatic fail

- Using EnTAP/Trinotate/TransAnnot output as “F1” without documenting the alternate frame  
- eggNOG v5 DB with emapper v3 (or mismatched mapper/DB) without saying so  
- Claiming CAFA-style GO accuracy from blast-transfer alone  
- FA release that depends on unpublished structure proteins with no tag/hash  

---

## Suggested METHODS tick list

```text
Grade: F-L0 / F-L1
F1 PROTEINS_FA provenance ________
F2 F0 BUSCO lineage + C/D/F/M ________
F3 Frame F1 / F2 / F3 / F5 ________
F4 Versions (diamond, emapper, IPS, DBs) ________
F5 master rows / protein n / drops ________
F6 release/<TAG>/ ________
Add-ons: F4[ ] F6[ ] F7[ ] F8[ ] F9[ ] unused[ ]
```

---

## Cross-layer rule

```text
Structure L1/L2  →  proteins.faa  →  FA F-L1
Structure L0     →  FA only as provisional (say so)
Catastrophic F0  →  stop FA; return to structure EVALUATION
```

Short checklist twin: [`PLAYBOOK.md`](PLAYBOOK.md). Stage pass column: [`STAGE_IO.md`](STAGE_IO.md).
