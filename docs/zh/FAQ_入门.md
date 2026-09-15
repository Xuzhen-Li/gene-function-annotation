# 入门 FAQ（功能仓）

配合 [README 今天最短路径](README.md)。先读完 **「F 编号别撞车」** 再跑任何脚本。

---

## F 编号别撞车（最重要）

仓库里同时有几套「F」，**不是同一套编号**：

| 你听到的 | 真正指什么 | 入门怎么记 |
|----------|------------|------------|
| **框架 F1** | 默认论文骨架：DIAMOND + eggNOG + InterProScan | **默认就认这个** |
| **框架 F2 / F3 / F5** | 快框 / EnTAP / Trinotate 等**替代整框** | 只有 `prefer_fast` 或 waiver 才走 |
| **脚本 `F1_diamond.sh` / `F2_eggnog.sh` / `F3_interproscan.sh`** | F1 骨架里的**三步文件名**（历史命名） | 按 diamond → eggnog → IPS 跑；**文件名里的 F2 ≠ 快框 F2** |
| **TOOLS 表 F1a / F1b / F1c** | 同上三步的素养页 | 与脚本三步一一对应 |
| **验收勾选 F1…F7** | 放行**硬门槛条目**（蛋白来源、BUSCO、三件套…） | 写 METHODS 时说「验收门 G/F1…」或直接抄勾选表原文，**不要说「做完了 F2」这种歧义句** |

**口诀：** 拿不准就宣称 **框架 F1**；动手顺序永远是 **diamond → emapper → InterProScan**；`bash pipeline/F2_eggnog.sh` = F1 里的 eggNOG 步。

**报告推荐口播：** 「功能注释采用框架 F1（DIAMOND + eggNOG-mapper + InterProScan），合并为 functional_master.tsv；脚本 F2_eggnog.sh 只是 F1 内第二步的历史文件名。验收按 F-L1 勾选表记录。」

---

## 和结构仓怎么接

**Q：结构 `proteins.faa` 填哪？**  
A：`config/local.env` 的 `PROTEINS_FA=`（先 `cp config/example.env config/local.env`）。首页「Three steps」第 3 步也会提到。

**Q：结构只有 L0，还能冲 F-L1 吗？**  
A：**不能诚实宣称 F-L1。** 勾 F-L0 / provisional，或先回结构仓升到 L1。`answers.yaml` 里的 `structure_grade` 是**你自己声明**，flow **不会**去读结构仓 release。

**Q：有 isoform，要「每基因一条」吗？**  
A：要。结构若吐出多 isoform，功能前先抽代表（与结构 METHODS 的 isoform 政策一致）。例（最长蛋白，需按你的 ID 规则改）：

```bash
# 若 ID 形如 GENE.t1 / GENE-isoform2，先与结构仓约定再抽；下面仅示意
seqkit fx2tab "$PROTEINS_MULTI" | awk -F '\t' '{
  id=$1; gsub(/ .*/,"",id); gene=id; sub(/\..*$/,"",gene); sub(/-.*$/,"",gene);
  if (length($2)>len[gene]) { len[gene]=length($2); seq[gene]=$2; keep[gene]=id }
} END { for (g in seq) print ">"keep[g]"\n"seq[g] }' > proteins.one_per_gene.faa
```

更稳：**默认要求结构放行时就给出 one-per-gene**（与结构 METHODS 的 isoform 政策一致）。  
若结构 ID 是 `xxx-mRNA-1` / `gene:ID` 等非 `GENE.t1` 形——**不要盲抄 awk**；先打开结构仓放行 METHODS / [结构 FAQ](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/zh/FAQ_入门.md) 的 isoform 句，按**同一套 gene 主键**再抽。FAQ 里的 awk 只是示意。

**Q：GO 不写回 GFF 第 9 列，下游怎么用？**  
A：本仓真相是 **`functional_master.tsv`**。浏览器/投稿需要列 9 时，**另做一步**（本仓暂不自动宣称）。METHODS 写「功能以 master TSV 为准」。

---

## flow / answers

**Q：plan 里默认挂了 AHRD/F4，必须做吗？**  
A：**不是。** 三件套过关仍可 F-L1；METHODS 写未跑 AHRD。或 want_ahrd: false 重出 plan。

**Q：宿舍盘不够 80GB，课程作业最低交付？**  
A：问老师。可约定：读懂 plan + FAQ 编号 + 列出库与磁盘预算；完整装库未必是课堂硬门槛。

**Q：`prefer_fast: true` 是什么？**  
A：框架走**快框 F2**（emapper 为主、IPS 可延期）→ 验收通常只能 **F-L0**，除非你另有完整 F1。默认请保持 `false`。

**Q：`proteins_provenance` 写啥？**  
A：结构仓 `RELEASE_TAG` 或蛋白文件路径+sha256，例如 `structure:species_ann.v0.1` 或 `sha256:abcd…`。不要留示例占位句。

**Q：两仓 flow 是接力吗？**  
A：是概念接力，不是自动读对方 plan。把结构 TAG/蛋白路径**手抄**进功能 `local.env` + answers。

**Q：中英文验收表都要勾吗？**  
A：勾一份即可；中文 `验收勾选表` ↔ 英文 `EVALUATION_CHECKLIST` 同级。写论文 METHODS 时英文细则更易引用。

---

## 装库（INSTALL）

**Q：Lane A conda 还是 Lane B Singularity？**  

| 你的情况 | 建议 |
|----------|------|
| 笔记本 / 小试 diamond+BUSCO | Lane A 即可 |
| 要跑 **eggNOG-mapper + InterProScan 全量** | **Lane B（或集群模块）**；IPS/eggNOG 数据体积大 |
| 共享 HPC、已有镜像 | Lane B |
| 计算节点无外网 | 登录节点先下好 DB/镜像再拷到 `$DB_ROOT` |

**Q：Swiss-Prot 下哪个？**  
A：只要 **Swiss-Prot**（`uniprot_sprot.fasta.gz`），不要误下 TrEMBL 全集。当前入口：UniProt → Download → Knowledgebase → *Reviewed (Swiss-Prot)* FASTA；或 FTP：  
`https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz`  
然后 `diamond makedb`（见 INSTALL §2.1）。

**Q：emapper 版本怎么查？DB 怎么配？**  
```bash
emapper.py --version
# 或：singularity exec "$EGGNOG_SIF" emapper.py --version
```
major v3 ↔ eggNOG **v7** 数据包；v2 二进制不要配 v5/v7 错代。错配常见症状：空注释、启动即报 data/DB incompatible。

**Q：磁盘要预留多少？**  
A：粗算 F1 三件套数据+安装：**约 80–150 GB**（Swiss-Prot 小；eggNOG 数据数十 GB；InterProScan 发行包+成员库常 **>50 GB**）。再加工作区与临时文件。

**Q：植物 `EGGNOG_TAX_SCOPE` / BUSCO？**  
A：`EGGNOG_TAX_SCOPE=Viridiplantae`（或 `auto` 让 emapper 猜，METHODS 仍建议写明）。`BUSCO_LINEAGE_PROTEIN` 常与结构蛋白 QC 一致，例如 `viridiplantae_odb12`——**同一谱系更好比**；不要混用完全不同的 odb 却不说明。

**Q：F0「灾难」有没有数字？**  
A：与结构仓一样，**不设全球阈值**。Completeness 相对同谱系的结构放行值断崖、或课题自定红线 → 停 FA 回结构。勾选表要的是「有记录 + 谱系名」。

**Q：master 行数「≈」？**  
A：目标与蛋白条数一致；差几条须在 METHODS/`merge` 日志说明（过滤、ID 对不上）。差 1% 也要说清楚，不要 silently。

---

## 执行顺序（默认 F1）

`FUN_PREFIX`、输出子目录在 [`../../config/example.env`](../../config/example.env) 已有默认（`FUN_PREFIX=ann` → `emapper/ann_fun.emapper.annotations`、`interpro/ann_ips.tsv`）。  
第一次：对照 `example.env` + 各脚本头注释；改了 `FUN_PREFIX` 就要改 merge 路径里的同名。

```bash
cp config/example.env config/local.env   # 填 PROTEINS_FA、DIAMOND_DB、EGGNOG_*、INTERPROSCAN_HOME…
set -a && source config/local.env && set +a
python3 pipeline/flow_tool/flow.py --answers my_answers.yaml -o my_fa_plan.md
# 按 plan 讲解理解后：
RUN=1 bash pipeline/F1_diamond.sh
RUN=1 bash pipeline/F2_eggnog.sh      # = F1 的 eggNOG 步
RUN=1 bash pipeline/F3_interproscan.sh
python3 pipeline/F_merge_tables.py --proteins "$PROTEINS_FA" \
  --emapper "$FUNCTION_DIR/emapper/${FUN_PREFIX}_fun.emapper.annotations" \
  --ips "$FUNCTION_DIR/interpro/${FUN_PREFIX}_ips.tsv" \
  --diamond "$FUNCTION_DIR/diamond/swissprot.tsv" \
  --out "$FUNCTION_DIR/merge/functional_master.tsv"
python3 pipeline/print_qc_commands.py   # 对照验收门
# 勾 docs/zh/验收勾选表.md
```
