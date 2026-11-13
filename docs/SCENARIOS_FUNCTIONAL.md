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
  --out "$FUNCTION_DIR/merge/merged_function_table.tsv"

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
  --out "$FUNCTION_DIR/merge/merged_function_table.tsv"
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
#   $FUNCTION_DIR/merge/merged_function_table.tsv
# and DIAMOND (+ ideally IPS) outputs.

# 1) Run AHRD using DIAMOND (+ IPS) — see docs/tools/ahrd.md
#    Write: $FUNCTION_DIR/ahrd/ahrd_output.csv

python3 "$REPO_ROOT/pipeline/F4_join_ahrd.py" \
  --master "$FUNCTION_DIR/merge/merged_function_table.tsv" \
  --ahrd "$FUNCTION_DIR/ahrd/ahrd_output.csv" \
  --out "$FUNCTION_DIR/merge/merged_function_table.with_ahrd.tsv"

# F_release prefers *.with_ahrd.tsv when master is absent; or:
cp "$FUNCTION_DIR/merge/merged_function_table.with_ahrd.tsv" \
   "$FUNCTION_DIR/merge/merged_function_table.tsv"
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
  --out "$FUNCTION_DIR/merge/merged_function_table.tsv"
bash "$REPO_ROOT/pipeline/F_release.sh"
echo "Keep Trinotate_report.tsv beside merged_function_table in the release folder."
```

---

## F6 — Mercator4 / MapMan BINs

```bash
# 1) Browser: https://www.plabipd.de/mercator_main.html
#    Upload $PROTEINS_FA → download result table → save as:
#    $FUNCTION_DIR/mercator/mercator_results.txt  (or .tsv)

python3 "$REPO_ROOT/pipeline/F6_ingest_mercator.py" \
  --master "$FUNCTION_DIR/merge/merged_function_table.tsv" \
  --mercator-dir "$FUNCTION_DIR/mercator" \
  --out "$FUNCTION_DIR/merge/merged_function_table.with_mapman.tsv"

cp "$FUNCTION_DIR/merge/merged_function_table.with_mapman.tsv" \
   "$FUNCTION_DIR/merge/merged_function_table.tsv"
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
# Needs WORK_DIR + REPO_ROOT. No RUN=1 dry mode — missing IPS fails closed.
bash "$REPO_ROOT/pipeline/F8_run.sh"
```

### F8 vs structure S7 families (timing — do not conflate)

1. **Structure S7a (optional, before/during curation):** build `curate/families.tsv` (`gene_id\tNLR`) from HRP / curated lists → `02_priority_loci.py --families` for G9.
2. **FA F8 (after InterProScan):** `bash pipeline/F8_run.sh` → `function/nlr/nlr_candidates.tsv` (gene_id + IPS signatures) for the FA release.
3. **Loop-back (optional):** convert FA NLR hits for a later structure re-priority:

```bash
python3 pipeline/F8b_nlr_to_families.py \
  --nlr "$FUNCTION_DIR/nlr/nlr_candidates.tsv" \
  --out /path/to/structure/curate/families_from_f8.tsv \
  --family NLR
# then on structure side:
# python3 pipeline/02_priority_loci.py -i "$PSAURON_TSV" -o curate/priority.tsv --families curate/families_from_f8.tsv
```

Optional full-length NB-LRR refinement: [HRP](tools/hrp.md) → `$FUNCTION_DIR/nlr/hrp/`.  
Optional: prioritize NLR loci in curated GFF upstream (gene-structure-annotation helpers — not mirrored here).

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
  --out /tmp/toy_out/merged_function_table.tsv
diff /tmp/toy_out/merged_function_table.tsv "$REPO_ROOT/testdata/function/expected/merged_function_table.tsv" && echo "[OK] matches expected"
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

---

<a id="data-needs-details"></a>

## Data needed alongside the proteins

The main input is `proteins.faa` from a structure release (one representative sequence per gene). The notes below say what else each step usually needs. They do not change default frame F1 until a change is tested.

### Summary

| Situation | Minimum | Recommended | Typical tools in this repo | Common pitfall |
|---|---|---|---|---|
| Input QC (F0) | `PROTEINS_FA` + protein-mode BUSCO lineage | OMArk as an extra consistency check | BUSCO protein, OMArk (optional) | Treating F0 as a source of functional labels; trying to "fix" a bad proteome here instead of going back to structure |
| Default frame F1 | Local DIAMOND DB, eggNOG-mapper data, InterProScan data (versions in METHODS) | Swiss-Prot (or documented equivalent) for DIAMOND | `F1_diamond.sh`, `F2_eggnog.sh`, `F3_interproscan.sh` | Confusing script `F2_eggnog.sh` with alternate frame F2 |
| Fast frame F2 | eggNOG-mapper data only | Add Kofam later into merge | eggNOG-mapper ± Kofam | Shipping F2 as if IPS had been run |
| Names (F4, optional) | Blast/DIAMOND-style outputs that AHRD expects | A documented name source | AHRD, optional PANNZER (`[待确认]` site check in the 2026-11 catalog) | Treating names as a higher F-L grade by themselves |
| MapMan (F6, optional) | Mercator4 result (web or local) | Follow `docs/MERCATOR_WHEN.md` | `F6_ingest_mercator.py` | Running Mercator "because it is a plant" with no MapMan figure planned |
| Multi-genome (F7) | Proteins from every genome in the panel | Annotate orthogroup representatives, then merge | OrthoFinder, then F1 on representatives | Writing labels as if every gene had been through F1 |
| NLR (F8, optional) | InterProScan output; optional HRP windows from the structure overlay | Only if there is a disease / NLR story | `F8_run.sh` | Calling an IPS+HRP screen a curated NLR set |
| TF / kinase (F9, optional) | iTAK (or a documented equivalent) | Only if that family is needed | `F9_itak.sh` | Adding F9 as a plant-genome checklist item |
| Enrichment (downstream) | `merged_function_table.tsv` + a defined background | The full release gene set as background | clusterProfiler and similar are catalogued; some licenses are NC/ND and are not used for figures | Using a convenience subset as the background without saying so |
| Pathways / KO | Kofam HMM set and thresholds, or eggNOG KO fields | Record the library version | KofamScan, eggNOG | Assuming KEGG data can be redistributed (`[待确认]`) |

### Cross-cutting pitfalls

- No gene finding, soft-mask, TE library, or GFF editing happens here. Those belong to gene-structure-annotation or vitis-te.
- Four ID sets must stay distinct in METHODS: frame (F1/F2/F3/F5), script file (`F2_eggnog.sh` is a step inside frame F1), tool card (F1a/F1b/F1c), and gate (Gate-F1…F7).
- The merge product is `merged_function_table.tsv`. Machine-predicted GO/EC stays IEA.
- Frame F7 annotates orthogroup representatives, not each gene.
- "Structure" in Foldseek, DeepFRI or AlphaFold DB means protein 3D structure.
- InterProScan is part of default F1 but is slow; F-L1 is an acceptance bar, not a requirement to finish IPS tonight.
- Optional plant add-ons (F4/F6/F8/F9) are not a higher grade by themselves.

Catalog rows still marked `[待确认]` (HMMER 3, eggNOG 6, PANNZER2, MetaCyc, PRGdb 4.0, psRobot, DALI, ShinyGO — site checks on 2026-11-13) stay marked until a person opens the page. This text does not re-check those sites.

---

<a id="data-needs-zh"></a>

## 蛋白序列之外还需要的数据

主输入是结构库发布的 `proteins.faa`（每个基因一条代表序列）。下表说明各步骤通常还要什么。未实测前不改变默认框架 F1。

### 摘要

| 场景 | 最低要求 | 建议再加 | 本库常用工具 | 常见陷阱 |
|---|---|---|---|---|
| 输入质控（F0） | `PROTEINS_FA` + 蛋白模式 BUSCO lineage | 再用 OMArk 做一致性检查 | BUSCO 蛋白模式、OMArk（可选） | 把 F0 当成功能标签来源；想在这里“修好”差的蛋白组，而不是回到结构库 |
| 默认框架 F1 | 本地 DIAMOND 库、eggNOG-mapper 数据、InterProScan 数据（版本写入 METHODS） | DIAMOND 用 Swiss-Prot（或书面指定的等效库） | `F1_diamond.sh`、`F2_eggnog.sh`、`F3_interproscan.sh` | 把脚本 `F2_eggnog.sh` 和备用框架 F2 搞混 |
| 快速框架 F2 | 只需 eggNOG-mapper 数据 | 随后把 Kofam 并入合并表 | eggNOG-mapper ± Kofam | 把 F2 结果当成已经跑过 IPS 来发布 |
| 名称（F4，可选） | AHRD 所需的 Blast/DIAMOND 类输出 | 书面指定的名称来源 | AHRD，可选 PANNZER（2026-11 目录中网站检查为 `[待确认]`） | 仅凭名称就当作更高的 F-L 等级 |
| MapMan（F6，可选） | Mercator4 结果（网页或本地） | 按 `docs/MERCATOR_WHEN.md` 操作 | `F6_ingest_mercator.py` | 只因为“这是植物”就跑 Mercator，并无 MapMan 图计划 |
| 多基因组（F7） | 面板中每个基因组的蛋白 | 注释直系同源组代表序列，再合并 | OrthoFinder，然后对代表序列跑 F1 | 写成好像每个基因都跑过 F1 |
| NLR（F8，可选） | InterProScan 输出；可选结构叠加层给出的 HRP 窗口 | 仅在有病害 / NLR 故事时使用 | `F8_run.sh` | 把 IPS+HRP 筛查当成已审定的 NLR 集 |
| TF / 激酶（F9，可选） | iTAK（或书面指定的等效工具） | 仅在需要该家族时使用 | `F9_itak.sh` | 把 F9 当成植物基因组的检查清单项目 |
| 富集（下游） | `merged_function_table.tsv` + 定义清楚的背景 | 以该次发布的全部基因为背景 | 目录收录了 clusterProfiler 等；部分许可为 NC/ND，不用于配图 | 用方便的子集当背景却不说明 |
| 通路 / KO | Kofam HMM 库和阈值，或 eggNOG 的 KO 字段 | 记录库版本 | KofamScan、eggNOG | 假定 KEGG 数据可以再分发（`[待确认]`） |

### 跨切陷阱

- 这里不做基因预测、soft-mask、TE 库或 GFF 编辑。那些在结构库或 vitis-te。
- METHODS 里四套编号不要混：框架（F1/F2/F3/F5）、脚本（`F2_eggnog.sh` 是框架 F1 里的一步）、工具卡片（F1a/F1b/F1c）、门控（Gate-F1…F7）。
- 合并产物是 `merged_function_table.tsv`。机器预测的 GO/EC 仍是 IEA。
- 框架 F7 注释直系同源组代表序列，不是每个基因。
- Foldseek、DeepFRI、AlphaFold DB 里的 “structure” 指蛋白三维结构。
- InterProScan 属于默认 F1，但很慢；F-L1 是验收标准，不是今晚必须做完 IPS。
- F4/F6/F8/F9 这些植物可选步骤本身不会提高等级。

目录中仍标 `[待确认]` 的条目（HMMER 3、eggNOG 6、PANNZER2、MetaCyc、PRGdb 4.0、psRobot、DALI、ShinyGO — 2026-11-13 网站检查）保持原标记，直到有人打开页面。本文未重新检查那些网站。
