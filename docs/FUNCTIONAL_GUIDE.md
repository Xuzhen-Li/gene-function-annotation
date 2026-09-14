# Functional annotation — complete copy-paste guide

**Goal:** from `PROTEINS_FA` to a released functional package without leaving this repo’s docs.  
**Install first:** [`INSTALL_FUNCTIONAL.md`](INSTALL_FUNCTIONAL.md).  
**Branches:** [`SCENARIOS_FUNCTIONAL.md`](SCENARIOS_FUNCTIONAL.md).  
**Main spine:** [`steps/FUNCTIONAL_MAIN.md`](steps/FUNCTIONAL_MAIN.md).

```bash
cd /path/to/gene-function-annotation
set -a && source config/local.env && set +a
mkdir -p "$FUNCTION_DIR"/{diamond,emapper,interpro,kofam,ahrd,mercator,merge,release,qc}
```

---

# F0 — Protein QC (always)

```bash
# set BUSCO_LINEAGE_PROTEIN to your clade (eukaryota / viridiplantae / metazoa / fungi / ...)
busco -i "$PROTEINS_FA" -l "${BUSCO_LINEAGE_PROTEIN:-eukaryota_odb10}" -m proteins \
  -o prot_busco --out_path "$FUNCTION_DIR/qc" -c "$THREADS"

seqkit stats "$PROTEINS_FA" | tee "$FUNCTION_DIR/qc/seqkit_stats.txt"
# Optional OMArk/compleasm: run upstream in gene-structure-annotation if needed
```

**Pass:** summary exists under `function/qc/`. If Completeness is catastrophic, fix structure upstream ([gene-structure-annotation MAIN](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/steps/MAIN.md)) before spending InterProScan time.

---

# F1 — Full default (copy all blocks)

## F1.1 DIAMOND → SwissProt

```bash
# Needs: DIAMOND_DB from INSTALL_FUNCTIONAL.md
diamond blastp --threads "$THREADS" \
  --query "$PROTEINS_FA" \
  --db "$DIAMOND_DB" \
  --out "$FUNCTION_DIR/diamond/swissprot.tsv" \
  --outfmt 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore stitle \
  --evalue 1e-5 --max-target-seqs 5

# Check
wc -l "$FUNCTION_DIR/diamond/swissprot.tsv"
head "$FUNCTION_DIR/diamond/swissprot.tsv"
```

Or: `bash pipeline/F1_diamond.sh` (prints the same; remove `[STOP]` by exporting `RUN=1` — see script).

## F1.2 eggNOG-mapper

**Conda/binary example (emapper v2-style flags; adjust for v3 per your install):**

```bash
emapper.py -i "$PROTEINS_FA" \
  --output ${FUN_PREFIX:-ann}_fun --output_dir "$FUNCTION_DIR/emapper" \
  --cpu "$THREADS" --type proteins -m diamond \
  --data_dir "${EGGNOG_DATA_DIR}" \
  --tax_scope "${EGGNOG_TAX_SCOPE:-auto}" \
  --go_evidence non-electronic \
  --pfam_realign realtime

ls "$FUNCTION_DIR/emapper"/*.emapper.annotations
head -20 "$FUNCTION_DIR/emapper"/*.emapper.annotations
```

**Singularity example:**

```bash
singularity exec "$EGGNOG_SIF" emapper.py -i "$PROTEINS_FA" \
  --output ${FUN_PREFIX:-ann}_fun --output_dir "$FUNCTION_DIR/emapper" \
  --cpu "$THREADS" --type proteins -m diamond \
  --data_dir "$EGGNOG_DATA_DIR" \
  --tax_scope "${EGGNOG_TAX_SCOPE:-auto}"
```

## F1.3 InterProScan

```bash
"$INTERPROSCAN_HOME/interproscan.sh" \
  -i "$PROTEINS_FA" -f tsv,gff3 -dp \
  -cpu "$THREADS" \
  -b "$FUNCTION_DIR/interpro/${FUN_PREFIX:-ann}_ips"

ls "$FUNCTION_DIR/interpro"/${FUN_PREFIX:-ann}_ips.tsv
wc -l "$FUNCTION_DIR/interpro"/${FUN_PREFIX:-ann}_ips.tsv
```

## F1.4 Optional — KofamScan (KEGG KO)

```bash
exec_annotation -o "$FUNCTION_DIR/kofam/kofam.tsv" \
  --profile "$KOFAM_PROFILE_DIR" \
  --ko-list "$KOFAM_KO_LIST" \
  --cpu "$THREADS" \
  "$PROTEINS_FA"
# Check threshold column per Kofam docs; keep significant hits only if you filter later
```

## F1.5 Merge → master TSV

```bash
python3 "$REPO_ROOT/pipeline/F_merge_tables.py" \
  --proteins "$PROTEINS_FA" \
  --emapper "$FUNCTION_DIR/emapper"/${FUN_PREFIX:-ann}_fun.emapper.annotations \
  --ips "$FUNCTION_DIR/interpro"/${FUN_PREFIX:-ann}_ips.tsv \
  --diamond "$FUNCTION_DIR/diamond/swissprot.tsv" \
  --out "$FUNCTION_DIR/merge/functional_master.tsv"

# Sanity
wc -l "$FUNCTION_DIR/merge/functional_master.tsv"
# header + N proteins; N should match protein count
python3 - <<'PY'
from pathlib import Path
p=Path("$FUNCTION_DIR/merge/functional_master.tsv".replace("$FUNCTION_DIR",__import__("os").environ["FUNCTION_DIR"]))
lines=p.read_text().splitlines()
print("rows", len(lines)-1, "cols", len(lines[0].split("\t")))
print("GO-nonempty", sum(1 for L in lines[1:] if "GO:" in L))
PY
```

## F1.6 Release package

```bash
bash "$REPO_ROOT/pipeline/F_release.sh"
```

---

# F2 — Fast (emapper only)

Run F0 + F1.2 + merge with only `--emapper`. Optional KEGGaNOG on the annotations file for pathway heatmaps ([`tools/kegganog.md`](tools/kegganog.md)).

---

# F3 — EnTAP

1. Install EnTAP from https://gitlab.com/PlantGenomicsLab/EnTAP (config.ini + databases).  
2. Run on `$PROTEINS_FA` (or CDS).  
3. Copy final annotation TSV into `$FUNCTION_DIR/entap/`.  
4. Join key columns into master TSV manually or extend `F_merge_tables.py`.  

Full flags live in EnTAP’s own config; this repo expects you to drop results under `function/entap/` and document versions in METHODS.

---

# F4 — AHRD readable names

After F1.1 (and ideally F1.3):

1. Configure AHRD YAML to read `$FUNCTION_DIR/diamond/swissprot.tsv` (+ InterPro if available).  
2. Run AHRD jar (see [`tools/ahrd.md`](tools/ahrd.md)).  
3. Save `ahrd_output.csv` under `$FUNCTION_DIR/ahrd/`.  
4. Join `Human-Readable-Description` onto `functional_master.tsv` by gene id:

```bash
python3 "$REPO_ROOT/pipeline/F4_join_ahrd.py" \
  --master "$FUNCTION_DIR/merge/functional_master.tsv" \
  --ahrd "$FUNCTION_DIR/ahrd/ahrd_output.csv" \
  --out "$FUNCTION_DIR/merge/functional_master.with_ahrd.tsv"
```

HPC wrapper alternative: [eifunannot](https://github.com/EI-CoreBioinformatics/eifunannot).

---

# F5 — Trinotate (transcriptome only)

If input is TransDecoder peptides (no genome GFF yet): run Trinotate SQLite workflow; export report → `$FUNCTION_DIR/trinotate/`; treat as provisional until genomic proteins exist. Commands: [`tools/trinotate.md`](tools/trinotate.md).

---

# F6 — Mercator4 / MapMan (plant BINs) — web step fully spelled out

Mercator4 has **no public CLI**. Do this once in a browser; then stay in-repo.

1. Open https://www.plabipd.de/mercator_main.html (Mercator4 protein annotation).  
2. Sequence type: **Protein**.  
3. Upload `$PROTEINS_FA` (split into &lt; chunks if the site rejects large files; e.g. 5k–10k proteins per job).  
4. Job name: `$GENOME_PREFIX` or accession.  
5. Submit; wait for email/UI completion.  
6. Download `mercator4_result.zip` → unpack into `$FUNCTION_DIR/mercator/`.  
7. Ingest:

```bash
python3 "$REPO_ROOT/pipeline/F6_ingest_mercator.py" \
  --mercator-dir "$FUNCTION_DIR/mercator" \
  --master "$FUNCTION_DIR/merge/functional_master.tsv" \
  --out "$FUNCTION_DIR/merge/functional_master.with_mapman.tsv"
```

8. Optional: load the mapping file into MapMan desktop for figures (local app from plabipd.de).

---

# F7 — OrthoFinder panel

```bash
# proteins/ with one FA per genome including yours
orthofinder -f "$WORK_DIR/orthofinder_in" -t "$THREADS" -a "$THREADS"
# Annotate OG representatives with F1; propagate labels — document majority rule in METHODS
```

---

# F8 — NLR / families

```bash
# After InterProScan: filter NLR domains OR run HRP (tools/hrp.md)
python3 "$REPO_ROOT/pipeline/F8_list_nlr_from_ips.py" \
  --ips "$FUNCTION_DIR/interpro"/${FUN_PREFIX:-ann}_ips.tsv \
  --out "$FUNCTION_DIR/merge/nlr_candidates.tsv"
```

Curate in GSAman if structure is uncertain; keep functional rows for these IDs even if expression is low.

---

# Understand your tables (no external tutorial needed)

| Column source | Meaning |
|---------------|---------|
| `emapper_GOs` | GO terms via eggNOG orthologs |
| `emapper_KEGG_ko` / `Pathway` | KEGG identifiers |
| `emapper_PFAMs` | PFAM from emapper |
| `ips_*` | Domains/GO from InterPro member DBs |
| `diamond_stitle` | Best SwissProt title (not always correct gene name) |
| `ahrd` (F4) | Chosen human-readable description |
| `mapman_bin` (F6) | Plant BIN from Mercator4 |

**Normal:** many genes lack GO. **Abnormal:** almost zero annotation with a high BUSCO proteome → wrong DB path or header mismatch (IDs must match FASTA).

---



---

# Journal-grade add-ons (HR HSE / MP Mercator)

After F1.5 merge, optionally:

## PANNZER2 (optional; not required by allowlisted standards)

Run PANNZER2 on `$PROTEINS_FA` → `$FUNCTION_DIR/pannzer/` · [`tools/pannzer2.md`](tools/pannzer2.md)

```bash
python3 "$REPO_ROOT/pipeline/F4b_join_pannzer.py" \
  --master "$FUNCTION_DIR/merge/functional_master.tsv" \
  --pannzer "$FUNCTION_DIR/pannzer/pannzer.out" \
  --out "$FUNCTION_DIR/merge/functional_master.with_pannzer.tsv"
```

## Mercator4

Already F6 — required for MapMan BINs (Molecular Plant Mercator4; HR-style pathway figures).

## Phobius / SignalP

Optional · [`tools/phobius_signalp.md`](tools/phobius_signalp.md)

Allowlisted journal sources only: [`RECENT_HIGH_QUALITY.md`](RECENT_HIGH_QUALITY.md).

# Release checklist (copy)

- [ ] `function/qc/` BUSCO (+ seqkit)  
- [ ] `functional_master.tsv` row count = protein count  
- [ ] Versions: diamond, emapper+DB, InterProScan, SwissProt release, optional Kofam/Mercator date  
- [ ] METHODS paragraph (template below)  
- [ ] No FASTQ/BAM in git; only TSVs/GFF attributes  

```bash
bash "$REPO_ROOT/pipeline/F_release.sh"
```

### METHODS template

```text
Representative proteins were functionally annotated with DIAMOND blastp against UniProt Swiss-Prot (release DATE),
eggNOG-mapper (version, database eggNOG X, tax scope …), and InterProScan (version).
Optional: KofamScan (KEGG KO); Mercator4 (MapMan4 BINs, web job DATE); AHRD descriptions.
Results were merged per gene into functional_master.tsv (gene-function-annotation pipeline).
```
