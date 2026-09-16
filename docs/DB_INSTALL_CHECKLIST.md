# F1 database install checklist

Tick before claiming framework **F1** / F-L1. Narrative install: [`INSTALL_FUNCTIONAL.md`](INSTALL_FUNCTIONAL.md).  
METHODS versions: [`METHODS_FUNCTIONAL.md`](METHODS_FUNCTIONAL.md).

**Print-first:** download on a login/data node if compute nodes lack internet; copy `$DB_ROOT` to the shared filesystem.

---

## Disk estimates (order of magnitude)

| Component | Download / unpack | Typical once-cost |
|-----------|-------------------|-------------------|
| Swiss-Prot FASTA + DIAMOND `.dmnd` | ~0.5–1 GB | minutes |
| eggNOG-mapper data (v7 / match emapper major) | tens of GB | tens of min–hours (I/O) |
| InterProScan tarball + member DBs | often **>50 GB** | hours first fetch/run |
| **Total F1 data + install** | **~80–150 GB** | plan overnight on shared FS |
| Workdir (per genome) | extra tens of GB | depends on proteome size / threads |

Offline: mirror Swiss-Prot, eggNOG data dir, InterProScan tree, and any `.sif` into `$DB_ROOT`, then sync to compute FS.

---

## Checklist

### Workspace

- [ ] `git clone` this repo; `cp config/example.env config/local.env`
- [ ] `DB_ROOT` set (e.g. `$HOME/annot_dbs` or shared scratch)
- [ ] `FUNCTION_DIR` / `PROTEINS_FA` / `THREADS` / `REPO_ROOT` set
- [ ] `mkdir -p "$FUNCTION_DIR"/{diamond,emapper,interpro,kofam,ahrd,mercator,merge,release,qc}`

### Swiss-Prot → DIAMOND DB

- [ ] Downloaded UniProt Swiss-Prot FASTA (current release URL from uniprot.org / FTP)
- [ ] `diamond makedb --in uniprot_sprot.fasta -d "$DB_ROOT/swissprot/swissprot"`
- [ ] `DIAMOND_DB="$DB_ROOT/swissprot/swissprot"` in `local.env` (no `.dmnd` suffix in some setups — match your diamond version)
- [ ] `diamond version` recorded

```bash
mkdir -p "$DB_ROOT/swissprot" && cd "$DB_ROOT/swissprot"
# wget/curl current uniprot_sprot.fasta.gz — URL changes; use UniProt current_release
gunzip -c uniprot_sprot.fasta.gz > uniprot_sprot.fasta
diamond makedb --in uniprot_sprot.fasta -d swissprot
```

### eggNOG data

- [ ] eggNOG-mapper **data pack matches emapper major version**
- [ ] Unpacked under `$DB_ROOT/eggnog` (or site module path)
- [ ] `EGGNOG_DATA_DIR` set; `EGGNOG_TAX_SCOPE` set for **your** clade
- [ ] emapper binary or Singularity image on `PATH` / documented

### InterProScan

- [ ] InterProScan distribution tarball unpacked; `interproscan.sh` exists
- [ ] `INTERPROSCAN_HOME="$DB_ROOT/interproscan"` (or real path) in `local.env`
- [ ] Disk quota OK for member DBs (first run may fetch more)
- [ ] InterPro / IPS **version + data release date** noted for METHODS

### Optional (F1+ / add-ons)

- [ ] KofamScan profiles + `ko_list` (F1b / F2-ish KO)
- [ ] AHRD / Mercator / iTAK only if that plant module is in scope

### Verify

```bash
diamond version
busco -v || true
# emapper.py --version   OR  singularity exec eggnog.sif emapper.py --version
# "$INTERPROSCAN_HOME/interproscan.sh" -version
python3 "$REPO_ROOT/pipeline/F_merge_tables.py" -h
```

- [ ] Smoke commands above succeed on the node you will use for `RUN=1`

---

## METHODS version / date fields (copy)

Fill in `release/<TAG>/METHODS.md` (see [`METHODS_FUNCTIONAL.md`](METHODS_FUNCTIONAL.md)):

```text
DIAMOND vFILL ; UniProt Swiss-Prot release FILL (download date FILL)
eggNOG-mapper vFILL ; eggNOG DB FILL ; tax scope FILL
InterProScan vFILL ; InterPro / member-DB data release FILL
BUSCO lineage (protein F0) FILL
proteins provenance: structure RELEASE_TAG FILL (or external hash)
```

Gate-F4: tool + DB versions required for F-L1. Do not leave `FILL` in a qualified pack.

---

## Not in this checklist

- Gene finding / GFF / soft-mask → [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation)
- Committing Swiss-Prot / eggNOG / IPS data into git → **forbidden** (Gate hygiene)
