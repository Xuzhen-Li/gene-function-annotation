# Install everything for functional annotation (copy this)

**Tick list (disk + METHODS fields):** [`DB_INSTALL_CHECKLIST.md`](DB_INSTALL_CHECKLIST.md)

Biology-general install. Clone [`gene-function-annotation`](https://github.com/Xuzhen-Li/gene-function-annotation); set `FUN_PREFIX`, BUSCO lineage, and `EGGNOG_TAX_SCOPE` for your species/clade.

You only need this file + `config/example.env` + `pipeline/F*.sh` to run **F1**.  
No other websites are required for the default path except downloading the databases listed below (URLs are included).

Assumes Linux + bash. Prefer **conda/mamba** or **Singularity** on HPC.

---

## 0. Workspace

```bash
git clone https://github.com/Xuzhen-Li/gene-function-annotation.git
cd gene-function-annotation
cp config/example.env config/local.env
# edit: WORK_DIR, PROTEINS_FA, THREADS, REPO_ROOT, DIAMOND_DB paths
mkdir -p "$HOME/annot_dbs"   # or a shared scratch
```

Set in `config/local.env`:

```bash
REPO_ROOT="$(pwd)"
WORK_DIR="/path/to/work"
PROTEINS_FA="/path/to/proteins.one_per_gene.faa"
THREADS=32
FUNCTION_DIR="$WORK_DIR/function"
DB_ROOT="$HOME/annot_dbs"
```

```bash
set -a && source config/local.env && set +a
mkdir -p "$FUNCTION_DIR"/{diamond,emapper,interpro,kofam,ahrd,mercator,merge,release,qc}
```

---

## 1. Core binaries (pick one lane)

### F1 minimum install (read this first)

| Goal | What you need | Lane |
|------|---------------|------|
| Read plan / BUSCO F0 / DIAMOND only | `diamond`, `busco`, `seqkit` | **A** enough |
| Full **frame F1** (emapper + InterProScan) | + emapper image/data + InterProScan home | **B** (or site modules) |
| Claim F-L1 | Full F1 + merge + release pack | **B** for emapper/IPS |

Shortest-path “run F1 scripts” assumes you can reach Lane B (or equivalent modules). Lane A alone is **not** a complete F1 install.

### Which lane?

| Situation | Pick |
|-----------|------|
| Laptop / try DIAMOND+BUSCO only | **A** |
| Full F1 (eggNOG + InterProScan) on HPC | **B** (or site modules) |
| Compute nodes without internet | Download DBs/images on login node → copy to `$DB_ROOT` |

Disk budget (rough, plus workdir):

| Component | Download / unpack (order of magnitude) | Typical wall-clock (once) |
|-----------|------------------------------------------|---------------------------|
| Swiss-Prot FASTA + DIAMOND DB | ~0.5–1 GB | minutes |
| eggNOG-mapper data (v7 pack) | tens of GB | tens of min–hours (I/O) |
| InterProScan distribution + member DBs | often **>50 GB** | hours first run / fetch |
| **Total F1 data+install** | **~80–150 GB** | plan overnight on shared FS |

Offline nodes: on a login/data node download Swiss-Prot, eggNOG data dir, InterProScan tree, and any `.sif`, then copy the whole `$DB_ROOT` to the compute filesystem.

### Lane A — conda/mamba (laptop / shared node)

```bash
mamba create -n gene_ann -c bioconda -c conda-forge \
  diamond busco seqkit gffread agat parallel pigz python=3.11 -y
mamba activate gene_ann
# eggNOG-mapper and InterProScan are LARGE — often better as containers (Lane B)
```

### Lane B — Singularity/Apptainer (recommended on HPC)

```bash
# eggNOG-mapper v3 image + data: follow https://data.cgmlab.org/eggnog-mapper/
# (download .sif + eggNOG7 data into $DB_ROOT/eggnog)
# InterProScan: download tarball from EBI FTP into $DB_ROOT/interproscan
# KofamScan: https://www.genome.jp/tools/kofamkoala/ → kofamscan + profiles + ko_list
```

Record exact versions in METHODS when you install.

---

## 2. Databases (mandatory for F1)

### 2.1 SwissProt for DIAMOND

```bash
mkdir -p "$DB_ROOT/swissprot" && cd "$DB_ROOT/swissprot"
# UniProt Swiss-Prot FASTA (release URL changes — use current uniprot.org download)
# Example pattern:
# wget https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
gunzip -c uniprot_sprot.fasta.gz > uniprot_sprot.fasta
diamond makedb --in uniprot_sprot.fasta -d swissprot
# then in local.env:
# DIAMOND_DB="$DB_ROOT/swissprot/swissprot"
```

### 2.2 eggNOG data

Download the **eggNOG-mapper data pack matching your emapper major version** into `$DB_ROOT/eggnog`  
(official: eggnog-mapper docs / data.cgmlab.org).  
Set `EGGNOG_DATA_DIR="$DB_ROOT/eggnog"`.

### 2.3 InterProScan data

Unpack InterProScan distribution under `$DB_ROOT/interproscan` so `interproscan.sh` exists.  
First run may download member DBs; keep disk quota large (tens of GB).

In `config/local.env` set:

```bash
INTERPROSCAN_HOME="$DB_ROOT/interproscan"   # required by pipeline/F3_interproscan.sh
```

### 2.4 KofamScan (optional F1+/F2)

```bash
mkdir -p "$DB_ROOT/kofam" && cd "$DB_ROOT/kofam"
# From KEGG KofamKOALA download page get:
#   ko_list, profiles.tar.gz, kofamscan executable
# tar xf profiles.tar.gz
# KOFAM_PROFILE_DIR="$DB_ROOT/kofam/profiles"
# KOFAM_KO_LIST="$DB_ROOT/kofam/ko_list"
```

---

## 3. Verify installs

```bash
diamond version
busco -v || true
python3 "$REPO_ROOT/pipeline/F_merge_tables.py" -h
# emapper.py --version   OR singularity exec eggnog.sif emapper.py --version
# "$DB_ROOT/interproscan/interproscan.sh" -version
```

---

## 4. Input protein rules

- One representative protein **per gene** (extract from a release GFF upstream in [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation), or bring your own).  
- FASTA headers = stable gene IDs (no spaces).  
- Soft-mask/TE junk cleaned upstream if gene count exploded.

Then open [`FUNCTIONAL_GUIDE.md`](FUNCTIONAL_GUIDE.md) and run **F0 → F1**.

Why this stack: [`RECENT_HIGH_QUALITY.md`](RECENT_HIGH_QUALITY.md) (allowlisted journals only: Cell/Nat/Sci + MP/PC/PBJ/HR/MBE/NAR/GB).
