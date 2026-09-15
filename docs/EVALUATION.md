# Final evaluation criteria — gene function

**What “done” means** for a functional release.  
Path choice: [`ROADMAP.md`](ROADMAP.md). **This page judges the finish.**

Upstream structure criteria: [gene-structure-annotation `EVALUATION.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/EVALUATION.md).

Journal patterns: [`RECENT_HIGH_QUALITY.md`](RECENT_HIGH_QUALITY.md) · peers: [`RELATED_SOFTWARE.md`](RELATED_SOFTWARE.md) · gaps: [`SELF_AUDIT.md`](SELF_AUDIT.md).
QC methods shelf: [`QUALITY_SOURCES.md`](QUALITY_SOURCES.md).

---

## Knowledge frame (why evaluation looks like this)

Functional annotation asks what proteins *resemble* and which domains/pathways they carry — not where exons sit. Reviews and community practice converge on:

1. **Second layer** (Ji *NRG* 2026) — attach function only to a stable gene set; do not use FA to paper over structure errors.
2. **Orthology ≠ BLAST best hit** (eggNOG-mapper line; Huerta-Cepas et al.) — fine-grained orthologs beat raw homology for GO/KEGG transfer; still not ground truth.
3. **Domains are evidence, not names** (InterPro *NAR* 2025; InterProScan) — signatures support mechanism claims; readable gene names need a separate naming step (AHRD / PANNZER).
4. **Journal METHODS are modular** (HR / MP patterns in [`RECENT_HIGH_QUALITY.md`](RECENT_HIGH_QUALITY.md)) — DIAMOND + emapper + IPS is the common spine; MapMan/NLR/iTAK are optional plant modules, not a higher “truth.”

CAFA-style GO accuracy is a research benchmark (CAFA4 preprint) — **not** what a DIAMOND dump proves. This page therefore grades *process integrity*, not CAFA Fmax.

---

## Two finish grades

| Grade | Label | When |
|-------|-------|------|
| **F-L0 Slim** | `status=provisional` or `frame=F2/F3/F5` | Fast frame only; IPS deferred; or incomplete merge |
| **F-L1 Qualified** | `status=qualified` | Hard gates below — default paper FA |

Plant add-ons (F4/F6/F8/F9) are **not** a higher grade by themselves; they are METHODS modules on top of F-L1.

### Background — grades

- **F-L0** covers legitimate speed paths (emapper-first, EnTAP, Trinotate) used in transcriptome or triage work — EnTAP docs even treat IPS as optional. They must be labelled so readers do not assume full F1 depth.
- **F-L1** matches what recent genome papers usually mean by “functional annotation”: homology + orthology + domains, merged to a gene-centric table, with versions and provenance. Plant extras decorate that table for MapMan/HR figures; they do not replace it.

---

## Hard gates (Gate-F*) (F-L1 — fail any ⇒ not qualified)

### Gate-F1 — Stable protein input

| | |
|--|--|
| **Pass** | `PROTEINS_FA` source named (structure `RELEASE_TAG` or external hash/path) in METHODS |
| **Fail** | Anonymous `proteins.faa` with no provenance |

**Background:** Function tables are worthless without knowing *which* gene models they describe. Structure releases change after GSAman; a tag/hash is the join key between layers (Ji two-layer model).

### Gate-F2 — Upstream sanity (F0)

| | |
|--|--|
| **Pass** | Protein BUSCO: Completeness **+ lineage** recorded; if catastrophic, structure fixed first |
| **Fail** | Decorating a broken proteome with GO-looking columns |

**Background:** F0 reuses the same ortholog-completeness idea as structure G6, but here it is a **sanity brake** for FA spend (InterProScan is expensive). Catastrophic M/F means the input set is not ready — same logic as “don’t annotate a genome that fails Asm1.”

### Gate-F3 — Default frame (or waiver)

| | |
|--|--|
| **Pass** | **F1** (DIAMOND Swiss-Prot + eggNOG-mapper + InterProScan) **or** written waiver naming F2/F3/F5 and why |
| **Fail** | Mystery pipeline; BLAST-only dump branded as master |

**Background:** F1 mirrors high-quality genome METHODS: curated homology (Swiss-Prot), orthology-aware transfer (eggNOG v7 / emapper), and integrative domains (InterPro). Alternates exist — EnTAP (F3) wraps similar ideas for transcriptomes; Trinotate (F5) for Trinity; TransAnnot for speed — but each has different error modes and must be named (see RELATED_SOFTWARE). BLAST-only best-hit is the classic over-annotation failure eggNOG-mapper was built to reduce.

### Gate-F4 — Versions pinned

| | |
|--|--|
| **Pass** | Tool + DB versions (Swiss-Prot / eggNOG / InterPro) in METHODS |
| **Fail** | Undated databases |

**Background:** Orthology DBs and InterPro member signatures change coverage year to year (*NAR* DB issues). eggNOG-mapper **v3** expects eggNOG **v7** (not v5). Undated FA is not reproducible and fails review checklists.

### Gate-F5 — Master table integrity

| | |
|--|--|
| **Pass** | `functional_master.tsv` gene count ≈ input proteins; drops documented |
| **Fail** | Silent row loss; unexplained duplicate gene IDs |

**Background:** The master TSV is the lab’s source of truth (GFF column-9 write-back is explicitly **not** claimed yet — [`SELF_AUDIT.md`](SELF_AUDIT.md)). Count drift means join bugs or ID mismaps — the same class of error as stale proteins in structure G5.

### Gate-F6 — Release pack

| | |
|--|--|
| **Pass** | `F_release.sh` → `function/release/<TAG>/` with master TSV + proteins copy + METHODS stub |
| **Fail** | Only raw `diamond/` / `interpro/` folders pointed at as “the release” |

**Background:** Same contract as structure G8: a tag, a frozen table, METHODS. Raw tool outputs are intermediates; journals and collaborators cite the merged product.

### Gate-F7 — Hygiene

| | |
|--|--|
| **Pass** | No private BAM/FASTQ / multi-GB DB files in repo or release |
| **Fail** | Accidental Swiss-Prot / eggNOG DB commit |

**Background:** FA workstations hold huge DBs by design. Releases must stay thin; DBs are cited by version/URL, not copied into GitHub.

---

## Soft metrics (report; clade-dependent)

| Metric | Use | Anti-pattern |
|--------|-----|--------------|
| F0 BUSCO-C | Sanity of the protein set | Treating FA BUSCO as structure QC replacement |
| Swiss-Prot / emapper hit rates | Coverage narrative in METHODS | Claiming “all genes annotated” from partial hits |
| IPS domain coverage | Domain evidence density | GO from homology alone without saying so |
| AHRD / Mercator / NLR / iTAK | Optional modules — list used or unused | Implying MapMan ran when it did not |
| Count match master↔proteins | Supports Gate-F5 | Padding empty stubs to force 100% |
| Domain-only / GO-empty split | Honest evidence mix in METHODS | Treating empty GO as “unannotated failure” |
| Upstream structure OMArk/RNA story | Two-layer audit trail | Using FA hit rates to excuse bad structure |

**Not claimed (automatic non-goal):** writing GO/KEGG into GFF column 9.

### Background — soft metrics

Hit rates depend on clade distance to Swiss-Prot / eggNOG taxa — plants and protists look “worse” than mammals without being failed runs. InterPro can assign domains where GO is empty (and vice versa). MapMan4/Mercator4 (*Mol Plant*) and iTAK (*Mol Plant*) are **plant community languages** for pathways/TFs — valuable in HR/MP papers, irrelevant as universal grades for fungi/animals. CAFA4 reminds that GO prediction quality is hard; do not equate emapper GO with competition-winning accuracy.

---

## Automatic fail

- Using EnTAP/Trinotate/TransAnnot output as “F1” without documenting the alternate frame  
- eggNOG v5 DB with emapper v3 (or mismatched mapper/DB) without saying so  
- Claiming CAFA-style GO accuracy from blast-transfer alone  
- FA release that depends on unpublished structure proteins with no tag/hash  

### Background — automatic fails

Mis-labelling frames confuses meta-analyses and METHODS. Mapper/DB mismatch yields empty or wrong annotations silently. CAFA claims from blast-transfer overstate evidence (CAFA community standards). Untagged proteins break the two-layer audit trail.

---

## Cross-layer rule

```text
Structure L1/L2  →  proteins.faa  →  FA F-L1
Structure L0     →  FA only as provisional (say so)
Catastrophic F0  →  stop FA; return to structure EVALUATION
```

### Background — cross-layer

Function cannot rescue wrong loci, merged tandems, or TE-captured ORFs; it can only decorate them. Provisional structure ⇒ provisional FA. This is the operational reading of Ji’s two-layer figure for lab releases.

---

## Suggested METHODS tick list

```text
Grade: F-L0 / F-L1
Gate-F1 PROTEINS_FA provenance ________
Gate-F2 F0 BUSCO lineage + C/D/F/M ________
Gate-F3 Frame F1 / F2 / F3 / F5 ________
Gate-F4 Versions (diamond, emapper, IPS, DBs) ________
Gate-F5 master rows / protein n / drops ________
Gate-F6 release/<TAG>/ ________
Gate-F7 hygiene (no private reads / multi-GB DBs) ________
Add-ons: F4[ ] F6[ ] F7[ ] F8[ ] F9[ ] unused[ ]
```

Short checklist twin: [`PLAYBOOK.md`](PLAYBOOK.md). Stage pass column: [`STAGE_IO.md`](STAGE_IO.md).
