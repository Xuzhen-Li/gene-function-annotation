# Quickstart — functional annotation (second layer)

**Audience:** you already have a **representative protein FASTA** (one sequence per gene).  
**Goal:** run **F1**, understand each table, package a release.  
**Upstream structure:** [`gene-structure-annotation` QUICKSTART](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/QUICKSTART.md).

| Need | Doc |
|------|-----|
| Branch map | [`ROADMAP.md`](ROADMAP.md) |
| Stage I/O | [`STAGE_IO.md`](STAGE_IO.md) |
| Install DBs/tools | [`INSTALL_FUNCTIONAL.md`](INSTALL_FUNCTIONAL.md) |
| Main process | [`steps/FUNCTIONAL_MAIN.md`](steps/FUNCTIONAL_MAIN.md) |
| Situations F1–F9 | [`SCENARIOS_FUNCTIONAL.md`](SCENARIOS_FUNCTIONAL.md) |

---

## 1. What this project is

**Structure** found *where* genes are. **This repo** asks *what the proteins look like functionally*:

- homology hits (Swiss-Prot via DIAMOND),  
- orthology / COG / KEGG-ish maps (eggNOG-mapper),  
- domains (InterProScan),  
- merged into one **gene-centric** table: `functional_master.tsv`.

Plant extras (AHRD names, Mercator, NLR, iTAK) are **optional add-ons after F1**.

```text
proteins.faa  →  F0 QC  →  F1 (DIAMOND + eggNOG + InterPro)
                      →  optional F4/F6/F8/F9
                      →  merge  →  release/<TAG>/
```

---

## 2. Setup

```bash
git clone https://github.com/Xuzhen-Li/gene-function-annotation.git
cd gene-function-annotation
cp config/example.env config/local.env
```

**Minimum variables:**

| Variable | Meaning |
|----------|---------|
| `REPO_ROOT` | This clone |
| `WORK_DIR` | Work directory |
| `PROTEINS_FA` | Input proteins (from structure release) |
| `DIAMOND_DB` | Swiss-Prot `.dmnd` |
| `FUNCTION_DIR` | Usually `$WORK_DIR/function` |
| `FUN_PREFIX` | Short label for output files |
| `EGGNOG_DATA_DIR` | eggNOG-mapper data pack (required for local/SIF runs) |
| `EGGNOG_TAX_SCOPE` | `auto` or your clade |
| `INTERPROSCAN_HOME` | Dir containing `interproscan.sh` (for F1c / `F3_interproscan.sh`) |
| `BUSCO_LINEAGE_PROTEIN` | For F0 |
| `RELEASE_TAG` | Release folder name |
| `THREADS` | Cores |

```bash
# Edit every /path/to in local.env first (PROTEINS_FA, WORK_DIR, DBs…).
set -a && source config/local.env && set +a
case "$WORK_DIR" in /path/to*|*/path/to*) echo "edit WORK_DIR before mkdir"; exit 1;; esac
case "$FUNCTION_DIR" in /path/to*|*/path/to*) echo "edit FUNCTION_DIR before mkdir"; exit 1;; esac
mkdir -p "$FUNCTION_DIR"/{diamond,emapper,interpro,merge,qc,release}
```

Follow [`INSTALL_FUNCTIONAL.md`](INSTALL_FUNCTIONAL.md) for databases.

---

## 3. Walkthrough F1 (with products)

### F0 — protein QC

Run BUSCO on `$PROTEINS_FA` (see scenarios).  
**Produces:** QC under `$FUNCTION_DIR/qc`.  
**Check:** completeness reported with lineage name.

### F1a — DIAMOND

```bash
# dry-run prints the command; RUN=1 executes
RUN=1 bash pipeline/F1_diamond.sh
```

**Produces:** `$FUNCTION_DIR/diamond/swissprot.tsv`.  
**Check:** non-empty; top hits look like real proteins.

### F1b — eggNOG-mapper

```bash
RUN=1 bash pipeline/F2_eggnog.sh
```

**Produces:** emapper annotations under `$FUNCTION_DIR/emapper/` (exact names depend on emapper version).  
**Check:** preferred names / GOs present for a sample of genes.

### F1c — InterProScan

```bash
RUN=1 bash pipeline/F3_interproscan.sh
```

**Produces:** InterPro TSV under `$FUNCTION_DIR/interpro/`.  
**Check:** domains for known control genes.

### Merge

```bash
python3 "$REPO_ROOT/pipeline/F_merge_tables.py" \
  --proteins "$PROTEINS_FA" \
  --emapper "$FUNCTION_DIR/emapper"/${FUN_PREFIX:-ann}_fun.emapper.annotations \
  --ips "$FUNCTION_DIR/interpro"/${FUN_PREFIX:-ann}_ips.tsv \
  --diamond "$FUNCTION_DIR/diamond/swissprot.tsv" \
  --out "$FUNCTION_DIR/merge/functional_master.tsv"
```

**Produces:** `$FUNCTION_DIR/merge/functional_master.tsv` — **source of truth**.  
**Check:** one row per gene; columns documented in guide.

### Release

```bash
bash pipeline/F_release.sh
```

**Produces:** `$FUNCTION_DIR/release/$RELEASE_TAG/` with TSV + proteins + METHODS stub.  
**Fill:** DB versions in `METHODS.md`.

---

## 4. What success looks like

- You can point to **one master TSV** and explain each major column.  
- METHODS lists tool + database versions.  
- You did **not** claim automatic GFF attribute write-back unless you built that yourself.

Optional plant papers: F4 AHRD → F6 Mercator → F8/F9 after F1 ([`SCENARIOS_FUNCTIONAL.md`](SCENARIOS_FUNCTIONAL.md)).
