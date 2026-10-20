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
| eggNOG-mapper 2.1.x data (eggNOG 5.0.2) | tens of GB | tens of min–hours (I/O) |
| InterProScan distribution + member DBs | often **>50 GB** | hours first run / fetch |
| **Total F1 data+install** | **~80–150 GB** | plan overnight on shared FS |

Offline nodes: on a login/data node download Swiss-Prot, eggNOG data dir, InterProScan tree, and any `.sif`, then copy the whole `$DB_ROOT` to the compute filesystem.

Pinned versions (checked 2026-10-19): DIAMOND 2.2.8, eggNOG-mapper 2.1.14 (eggNOG 5.0.2 data), InterProScan 5.78-109.0.

This guide covers three installation options, including a package setup for DIAMOND and eggNOG-mapper, a setup for InterProScan, and an offline option where you copy `$DB_ROOT`. The total installation and F1 data require about 80 to 150 GB of disk space. Plan to run the downloads overnight. Record the exact software versions you use in your methods file.

### Lane A — conda/mamba (laptop / shared node)

```bash
mamba create -n gene_ann -c conda-forge -c bioconda \
  diamond=2.2.8 eggnog-mapper=2.1.14 busco seqkit gffread agat parallel pigz python=3.11 -y
mamba activate gene_ann
diamond version          # expect: diamond version 2.2.8
emapper.py --version     # expect: emapper-2.1.14
```

DIAMOND without conda (static Linux binary):

```bash
mkdir -p "$DB_ROOT/bin" && cd "$DB_ROOT/bin"
curl -LO https://github.com/bbuchfink/diamond/releases/download/v2.2.8/diamond-linux64.tar.gz
tar -xzf diamond-linux64.tar.gz
./diamond version
export PATH="$DB_ROOT/bin:$PATH"
```

### Lane B — InterProScan 5 (any lane; needs Java 11+)

InterProScan requires Java version 11 or newer to run. After downloading, verify the archive file, unpack it, and run `setup.py`. Link the unpacked folder to `$DB_ROOT/interproscan` so the pipeline can find it. The bundled member databases often take more than 50 GB of disk space.

```bash
# Java check (InterProScan 5.78-109.0 needs Java 11 or newer)
JAVA_MAJOR="$(java -version 2>&1 | sed -nE 's/.*version "([0-9]+).*/\1/p' | head -n1)"
if [ "${JAVA_MAJOR:-0}" -ge 11 ]; then echo "[OK] Java $JAVA_MAJOR"; else echo "[ERR] need Java 11+ (found: ${JAVA_MAJOR:-none}); install a JDK before continuing"; fi

IPS_V=5.78-109.0
mkdir -p "$DB_ROOT" && cd "$DB_ROOT"
curl -LO "https://ftp.ebi.ac.uk/pub/software/unix/iprscan/5/${IPS_V}/interproscan-${IPS_V}-64-bit.tar.gz"
curl -LO "https://ftp.ebi.ac.uk/pub/software/unix/iprscan/5/${IPS_V}/interproscan-${IPS_V}-64-bit.tar.gz.md5"
md5sum -c "interproscan-${IPS_V}-64-bit.tar.gz.md5"      # expect: OK
tar -pxzf "interproscan-${IPS_V}-64-bit.tar.gz"
(cd "interproscan-${IPS_V}" && python3 setup.py -f interproscan.properties)
ln -sfn "$DB_ROOT/interproscan-${IPS_V}" "$DB_ROOT/interproscan"
"$DB_ROOT/interproscan/interproscan.sh" -version         # expect: InterProScan version 5.78-109.0
```

KofamScan (optional): https://www.genome.jp/tools/kofamkoala/ → kofamscan + profiles + ko_list (see 2.4).

Record exact versions in METHODS when you install.

---

## 2. Databases (mandatory for F1)

### 2.1 SwissProt for DIAMOND

```bash
mkdir -p "$DB_ROOT/swissprot" && cd "$DB_ROOT/swissprot"
curl -LO https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
curl -L https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/reldate.txt -o reldate.txt
cat reldate.txt          # Swiss-Prot release for METHODS (e.g. 2026_03)
gunzip -c uniprot_sprot.fasta.gz > uniprot_sprot.fasta
diamond makedb --in uniprot_sprot.fasta -d swissprot
# then in local.env:
# DIAMOND_DB="$DB_ROOT/swissprot/swissprot"
```

### 2.2 eggNOG data

The script `download_eggnog_data.py` downloads `eggnog.db`, `eggnog.taxa`, and `eggnog_proteins.dmnd` for eggNOG-mapper. These database files require tens of GB of disk space. You can run `emapper.py --data_dir "$DB_ROOT/eggnog" --version` to print the software and database versions. Set `EGGNOG_DATA_DIR` in `local.env` when the download finishes.

```bash
mkdir -p "$DB_ROOT/eggnog"
download_eggnog_data.py --data_dir "$DB_ROOT/eggnog" -y   # eggnog.db, eggnog.taxa, eggnog_proteins.dmnd
ls -lh "$DB_ROOT/eggnog"
emapper.py --data_dir "$DB_ROOT/eggnog" --version        # prints emapper and eggNOG DB versions
# then in local.env:
# EGGNOG_DATA_DIR="$DB_ROOT/eggnog"
```

### 2.3 InterProScan data

Installed by Lane B above: `$DB_ROOT/interproscan/interproscan.sh` must exist and `-version` must print 5.78-109.0.

The script `F3_interproscan.sh` requires the `INTERPROSCAN_HOME` variable and runs when you set `RUN=1`. It runs InterProScan with the flags `-goterms -iprlookup -pa` and `-f tsv,gff3`. Without those lookup flags, the output table will have no InterPro entries, GO terms, or pathways. A pathway is a series of chemical reactions in a cell.

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
diamond version                                   # 2.2.8
busco -v || true
emapper.py --data_dir "$DB_ROOT/eggnog" --version # emapper-2.1.14
"$DB_ROOT/interproscan/interproscan.sh" -version  # 5.78-109.0
python3 "$REPO_ROOT/pipeline/F_aggregate.py" -h
```

---

## 4. Input protein rules

- One representative protein **per gene** (extract from a release GFF upstream in [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation), or bring your own).  
- FASTA headers = stable gene IDs (no spaces).  
- Soft-mask/TE junk cleaned upstream if gene count exploded.

Then open [`FUNCTIONAL_GUIDE.md`](FUNCTIONAL_GUIDE.md) and run **F0 → F1**.

Why this stack: [`RECENT_HIGH_QUALITY.md`](RECENT_HIGH_QUALITY.md) (allowlisted journals only: Cell/Nat/Sci + MP/PC/PBJ/HR/MBE/NAR/GB).
