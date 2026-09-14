# F1 精讲：DIAMOND + eggNOG + InterProScan

默认论文骨架。英文逐步：[`../QUICKSTART.md`](../QUICKSTART.md) · [`../FUNCTIONAL_GUIDE.md`](../FUNCTIONAL_GUIDE.md)

## 三根柱子各回答什么

| 步 | 工具 | 回答 | 典型输出 |
|----|------|------|----------|
| F1a | **DIAMOND × Swiss-Prot** | 最像哪条高质量蛋白？ | `diamond/swissprot.tsv` |
| F1b | **eggNOG-mapper** | 偏直系同源的功能转移（GO/KEGG-ish/COG…） | `eggnog/*` 或 `emapper/*` |
| F1c | **InterProScan** | 有哪些结构域/签名？ | `interpro/*.tsv` |

然后 `F_merge_tables.py` → **`functional_master.tsv`**（基因一行；本仓真相来源）。

```text
F0 通过
  → DIAMOND
  → eggNOG-mapper
  → InterProScan（可与前两步重叠排队）
  → merge
  → （可选加件）
  → F_release.sh
```

## 教学要点

1. **同源命中 ≠ 基因正式名。** `diamond_stitle` 是线索；可读名用 F4 AHRD 等另做。  
2. **直系同源转移 ≠ 实验验证。** eggNOG 降低「BLAST 最佳命中乱贴 GO」的经典翻车，但仍非 CAFA 冠军声明。  
3. **结构域是机制证据，不是名字。** InterPro 有域、GO 可空（反过来也常见）。  
4. **版本钉死：** Swiss-Prot release、eggNOG DB 主版本、emapper 主版本、InterProScan 版本全部进 METHODS。  
5. **emapper v3 ↔ eggNOG v7**（不要用 v5 库配 v3 而不声明）。

## 助手怎么跑（print-first）

```bash
RUN=1 bash pipeline/F1_diamond.sh
RUN=1 bash pipeline/F2_eggnog.sh      # 注意：脚本名 F2 = F1 内 eggNOG 步
RUN=1 bash pipeline/F3_interproscan.sh
python3 pipeline/F_merge_tables.py …  # 见 FUNCTIONAL_GUIDE
bash pipeline/F_release.sh
```

不设 `RUN=1` 时脚本通常只打印命令 — 方便你改路径/module。

## 合并后自检

- master 行数 ≈ 输入蛋白数（掉行写进 METHODS）  
- 抽查对照基因：Swiss-Prot 标题、emapper GO、IPS 域是否合理  
- 许多基因无 GO 是**正常**的；高 BUSCO 蛋白集却几乎零注释 → 查 DB 路径或 ID 对不齐

下一页：[07_替代框架_F2F3F5.md](07_替代框架_F2F3F5.md)
