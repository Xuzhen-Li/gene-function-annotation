# F0：蛋白 BUSCO（开工前的急刹车）

英文：[`../STAGE_IO.md`](../STAGE_IO.md) · [`../FUNCTIONAL_GUIDE.md`](../FUNCTIONAL_GUIDE.md) · EVALUATION 门 F2

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
