# Gene **function** playbook — proteins to master TSV

Biology-general. Structure (GFF) is upstream; this repo is the **second layer**.

**Branch map:** [`ROADMAP.md`](ROADMAP.md) · **Start:** [`QUICKSTART.md`](QUICKSTART.md) · **I/O:** [`STAGE_IO.md`](STAGE_IO.md).  
**Process:** [`steps/FUNCTIONAL_MAIN.md`](steps/FUNCTIONAL_MAIN.md) · **Recipes:** [`SCENARIOS_FUNCTIONAL.md`](SCENARIOS_FUNCTIONAL.md).

Upstream structure checklist: [gene-structure-annotation PLAYBOOK](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/PLAYBOOK.md).

---

## End-to-end spine

```text
PROTEINS_FA
  → F0 protein BUSCO
  → F1 DIAMOND + eggNOG + InterProScan   (or alternate frame F2/F3/F5)
  → optional F4 / F6 / F7 / F8 / F9
  → merge → functional_master.tsv
  → F_release.sh → release/<TAG>/
```

Full draft-vs-add-on map: [`ROADMAP.md`](ROADMAP.md).

---

## Qualification checklist (FA release)

A functional release is **qualified** here when:

- [ ] `PROTEINS_FA` source named (structure `RELEASE_TAG` or external) in METHODS
- [ ] F0 protein BUSCO lineage + Completeness recorded (or explicitly skipped with reason)
- [ ] F1 (or documented alternate frame) versions in METHODS
- [ ] `functional_master.tsv` gene count ≈ input protein count (document drops)
- [ ] Optional add-ons listed (F4/F6/F8/F9) or marked unused
- [ ] Packaged with `pipeline/F_release.sh` under `RELEASE_TAG`
- [ ] No private BAM/FASTQ / huge DBs committed

---

## How to use the branches

1. Point `PROTEINS_FA` at a stable representative set.  
2. Open [`ROADMAP.md`](ROADMAP.md): default **F1**; use F2/F3/F5 only with a reason.  
3. Add plant extras (F4/F6/F8/F9) only if METHODS needs them.  
4. Merge → release → fill [`METHODS_FUNCTIONAL.md`](METHODS_FUNCTIONAL.md).
