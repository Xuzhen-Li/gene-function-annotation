# Functional scenarios F1–F8 (every command in-repo)

Install: [`INSTALL_FUNCTIONAL.md`](INSTALL_FUNCTIONAL.md) · Detail: [`FUNCTIONAL_GUIDE.md`](FUNCTIONAL_GUIDE.md) · Cite: [`CITATIONS.md`](CITATIONS.md)

```bash
set -a && source config/local.env && set +a
# need: REPO_ROOT, WORK_DIR, FUNCTION_DIR, PROTEINS_FA, THREADS, RELEASE_TAG
FUNCTION_DIR="${FUNCTION_DIR:-$WORK_DIR/function}"
mkdir -p "$FUNCTION_DIR"/{qc,diamond,emapper,interpro,merge,release,ahrd,mercator,nlr,orthofinder,itak,trinotate,entap,kofam}
```

---

## F1 — Full (default, paper)

```bash
# F0
busco -i "$PROTEINS_FA" -l "${BUSCO_LINEAGE_PROTEIN:-eukaryota_odb10}" -m proteins -o prot_busco --out_path "$FUNCTION_DIR/qc" -c "$THREADS"

# DIAMOND
RUN=1 bash "$REPO_ROOT/pipeline/F1_diamond.sh"

# eggNOG
RUN=1 bash "$REPO_ROOT/pipeline/F2_eggnog.sh"

# InterProScan
RUN=1 bash "$REPO_ROOT/pipeline/F3_interproscan.sh"

# optional Kofam (F1+ optional KO; script filename historical)
# RUN=1 bash "$REPO_ROOT/pipeline/F1b_kofam.sh"

python3 "$REPO_ROOT/pipeline/F_merge_tables.py" \
  --proteins "$PROTEINS_FA" \
  --emapper "$FUNCTION_DIR/emapper"/${FUN_PREFIX:-ann}_fun.emapper.annotations \
  --ips "$FUNCTION_DIR/interpro"/${FUN_PREFIX:-ann}_ips.tsv \
  --diamond "$FUNCTION_DIR/diamond/swissprot.tsv" \
  --out "$FUNCTION_DIR/merge/functional_master.tsv"

bash "$REPO_ROOT/pipeline/F_release.sh"

# Journal-grade extras (HR HSE / MP):
# 1) AHRD → pipeline/F4_run_ahrd.md
# 2) Mercator4 web → F6 below
# 3) optional iTAK: RUN=1 bash pipeline/F9_itak.sh
# Allowlist: docs/RECENT_HIGH_QUALITY.md
```

---

## F2 — Fast

```bash
busco -i "$PROTEINS_FA" -l "${BUSCO_LINEAGE_PROTEIN:-eukaryota_odb10}" -m proteins -o prot_busco --out_path "$FUNCTION_DIR/qc" -c "$THREADS"
RUN=1 bash "$REPO_ROOT/pipeline/F2_eggnog.sh"
# optional F1+ Kofam: RUN=1 bash "$REPO_ROOT/pipeline/F1b_kofam.sh"
python3 "$REPO_ROOT/pipeline/F_merge_tables.py" \
  --proteins "$PROTEINS_FA" \
  --emapper "$FUNCTION_DIR/emapper"/${FUN_PREFIX:-ann}_fun.emapper.annotations \
  --out "$FUNCTION_DIR/merge/functional_master.tsv"
bash "$REPO_ROOT/pipeline/F_release.sh"
```

---

## F3 — EnTAP

```bash
# Install EnTAP per docs/tools/entap.md (GitLab PlantGenomicsLab/EnTAP).
# Typical: configure databases once, then:

EnTAP --runP \
  -i "$PROTEINS_FA" \
  -d /path/to/entap_out \
  --threads "$THREADS"
  # plus your lab’s DIAMOND/SQLite DB flags — see EnTAP wiki

mkdir -p "$FUNCTION_DIR/entap"
cp -L /path/to/entap_out/final_results/*.tsv "$FUNCTION_DIR/entap/" 2>/dev/null || \
  cp -L /path/to/entap_out/**/*final*.tsv "$FUNCTION_DIR/entap/" 2>/dev/null || true
ls -la "$FUNCTION_DIR/entap/"

# Document versions in METHODS. Optional: merge selected columns into master
# with a one-off join, or keep EnTAP TSV as the primary FA table for F3 releases.
RELEASE_TAG="${RELEASE_TAG:-entap1}"
mkdir -p "$FUNCTION_DIR/release/${RELEASE_TAG}"
cp -L "$FUNCTION_DIR/entap/"*.tsv "$FUNCTION_DIR/release/${RELEASE_TAG}/" || true
cp -L "$PROTEINS_FA" "$FUNCTION_DIR/release/${RELEASE_TAG}/proteins.faa"
cp "$REPO_ROOT/docs/METHODS_FUNCTIONAL.md" "$FUNCTION_DIR/release/${RELEASE_TAG}/METHODS.md"
```

---

## F4 — Readable names (after F1)

```bash
# Requires F1 merge already at:
#   $FUNCTION_DIR/merge/functional_master.tsv
# and DIAMOND (+ ideally IPS) outputs.

# 1) Run AHRD using DIAMOND (+ IPS) — see docs/tools/ahrd.md
#    Write: $FUNCTION_DIR/ahrd/ahrd_output.csv

python3 "$REPO_ROOT/pipeline/F4_join_ahrd.py" \
  --master "$FUNCTION_DIR/merge/functional_master.tsv" \
  --ahrd "$FUNCTION_DIR/ahrd/ahrd_output.csv" \
  --out "$FUNCTION_DIR/merge/functional_master.with_ahrd.tsv"

# F_release prefers *.with_ahrd.tsv when master is absent; or:
cp "$FUNCTION_DIR/merge/functional_master.with_ahrd.tsv" \
   "$FUNCTION_DIR/merge/functional_master.tsv"
bash "$REPO_ROOT/pipeline/F_release.sh"
```

Full checklist: [`../pipeline/F4_run_ahrd.md`](../pipeline/F4_run_ahrd.md).

---

## F5 — Trinotate (transcriptome CDS)

```bash
# Input: TransDecoder peptides (not genome gene models)
# PROTEINS_FA=/path/to/longest_orfs.pep

busco -i "$PROTEINS_FA" -l viridiplantae_odb12 -m proteins -o prot_busco --out_path "$FUNCTION_DIR/qc" -c "$THREADS"

# Follow docs/tools/trinotate.md (BLAST/SQLite load → report)
# Copy final annotation report:
mkdir -p "$FUNCTION_DIR/trinotate"
cp -L /path/to/Trinotate_report.tsv "$FUNCTION_DIR/trinotate/"

# Often still run F1 on the same peptides for GO/KEGG/domains:
RUN=1 bash "$REPO_ROOT/pipeline/F1_diamond.sh"
RUN=1 bash "$REPO_ROOT/pipeline/F2_eggnog.sh"
RUN=1 bash "$REPO_ROOT/pipeline/F3_interproscan.sh"
python3 "$REPO_ROOT/pipeline/F_merge_tables.py" \
  --proteins "$PROTEINS_FA" \
  --emapper "$FUNCTION_DIR/emapper"/${FUN_PREFIX:-ann}_fun.emapper.annotations \
  --ips "$FUNCTION_DIR/interpro"/${FUN_PREFIX:-ann}_ips.tsv \
  --diamond "$FUNCTION_DIR/diamond/swissprot.tsv" \
  --out "$FUNCTION_DIR/merge/functional_master.tsv"
bash "$REPO_ROOT/pipeline/F_release.sh"
echo "Keep Trinotate_report.tsv beside functional_master in the release folder."
```

---

## F6 — Mercator4 / MapMan BINs

```bash
# 1) Browser: https://www.plabipd.de/mercator_main.html
#    Upload $PROTEINS_FA → download result table → save as:
#    $FUNCTION_DIR/mercator/mercator_results.txt  (or .tsv)

python3 "$REPO_ROOT/pipeline/F6_ingest_mercator.py" \
  --master "$FUNCTION_DIR/merge/functional_master.tsv" \
  --mercator-dir "$FUNCTION_DIR/mercator" \
  --out "$FUNCTION_DIR/merge/functional_master.with_mapman.tsv"

cp "$FUNCTION_DIR/merge/functional_master.with_mapman.tsv" \
   "$FUNCTION_DIR/merge/functional_master.tsv"
bash "$REPO_ROOT/pipeline/F_release.sh"
# Cite: Schwacke et al. Molecular Plant 2019 (MapMan4 / Mercator4)
```

---

## F7 — OrthoFinder panel → annotate OG reps

```bash
# Put ≥2 species proteomes as *.faa into:
mkdir -p "$FUNCTION_DIR/orthofinder/input"
# cp speciesA.faa speciesB.faa ... "$FUNCTION_DIR/orthofinder/input/"

RUN=1 bash "$REPO_ROOT/pipeline/F7_orthofinder.sh"

# Pick one representative protein per OG (your script / OrthoFinder tables),
# write reps.faa, then:
export PROTEINS_FA="$FUNCTION_DIR/orthofinder/reps.faa"
# run F1 (or F2) on reps — same commands as above
```

---

## F8 — NLR / resistance-gene focus

```bash
# Need InterProScan TSV from F1.3:
#   $FUNCTION_DIR/interpro/${FUN_PREFIX:-ann}_ips.tsv

bash "$REPO_ROOT/pipeline/F8_run.sh"

# Optional full-length NB-LRR refinement (HRP):
# see docs/tools/hrp.md → outputs under $FUNCTION_DIR/nlr/hrp/

# Optional: prioritize NLR loci in curated GFF upstream
# (gene-structure-annotation pipeline helpers — not mirrored here)
```

---

## F9 — iTAK (optional TF / kinase; HR HSE-style)

```bash
RUN=1 bash "$REPO_ROOT/pipeline/F9_itak.sh"
# Cite Zheng et al. Molecular Plant 2016; keep tables under $FUNCTION_DIR/itak/
```

---

## Dry-run merge (no DBs)

```bash
python3 "$REPO_ROOT/pipeline/F_merge_tables.py" \
  --proteins "$REPO_ROOT/testdata/function/toy.faa" \
  --emapper "$REPO_ROOT/testdata/function/toy.emapper.annotations" \
  --ips "$REPO_ROOT/testdata/function/toy.ips.tsv" \
  --diamond "$REPO_ROOT/testdata/function/toy.diamond.tsv" \
  --out /tmp/vga_toy_master.tsv
wc -l /tmp/vga_toy_master.tsv
```

---

## Chooser

| Goal | Branch |
|------|--------|
| Paper-ready (general) | **F1** (+ F4) |
| Paper-ready (plant / HR–MP) | **F1** (+ F4 + F6) |
| Quick | **F2** |
| EnTAP lab | **F3** |
| Readable names | **F1 → F4** |
| MapMan BINs (plants) | **F1 → F6** |
| Transcriptome only | **F5** |
| Multi-genome panel | **F7 → F1** |
| NLR focus (plants) | **F1 → F8** |
| TF / kinase table (plants) | **F9** |
| Extra KO (KEGG) | **F1+** Kofam / DeepKOALA / BlastKOALA |
| Extra GO DL | DeepGOPlus / ProteInfer / DeepFRI / NetGO3 after F1 (optional) |
| CAZyme / secretome | dbCAN3 · SignalP6 · DeepLoc2 after F1 |
| Isoform FA | SQANTI3 → IsoAnnot/FIT (after LR structure) |
