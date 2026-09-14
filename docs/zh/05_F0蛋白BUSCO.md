# F0：蛋白 BUSCO（开工前的急刹车）

英文：[`../STAGE_IO.md`](../STAGE_IO.md) · [`../FUNCTIONAL_GUIDE.md`](../FUNCTIONAL_GUIDE.md) · EVALUATION 门 F2

## 为什么

1. IPS 等步骤很贵 — F0 是**花费闸**。  
2. 灾难缺失/碎裂 → 先修结构，避免大规模错标签。  
3. 必须带**谱系全名**，否则百分比无意义。  
4. F0 **不替代**结构 QC（不看坐标/串联）。  
5. 结构暂定 → FA 也只能 provisional。

**反例：** 跳过 F0 直接全基因组 IPS，事后发现抽蛋白用了旧 GFF。  

深课：[14_为什么先结构后功能.md](14_为什么先结构后功能.md) · [15](15_为什么版本和谱系必须写清.md)

## 为什么功能仓还要再跑一次 BUSCO？

结构仓的蛋白 BUSCO（G6）证明「这套模型像完整基因集」。  
F0 是**功能侧的花费闸**：InterProScan 很贵；若输入蛋白集已经灾难性缺失/碎裂，先别烧 CPU 去贴 GO。

```text
PROTEINS_FA（带来源 TAG）
        │
        ▼
BUSCO -m proteins + 谱系名
        │
        ├─ 正常 → 进入 F1
        └─ 灾难（M/F 离谱）→ 停 FA，回结构 EVALUATION
```

## 教学要点

1. **必须写谱系全名**（如 `viridiplantae_odb12`），与 C/D/F/M 一起记在 `function/qc/`。  
2. F0 **不能替代**结构质控 — 它不看坐标、不看串联塌缩。  
3. 结构是 L0 暂定 → FA 也只能标 provisional。  
4. 可选：`seqkit stats` 记序列条数，与日后 master 行数对账。

## 和结构 G6 的关系

| | 结构 G6 | 功能 F0 |
|--|---------|---------|
| 目的 | 放行基因集 | 决定是否值得跑 FA |
| 失败 | 不达 L1 | 停 FA，回上游 |

下一页：[06_F1精讲_DIAMOND_eggNOG_IPS.md](06_F1精讲_DIAMOND_eggNOG_IPS.md)
