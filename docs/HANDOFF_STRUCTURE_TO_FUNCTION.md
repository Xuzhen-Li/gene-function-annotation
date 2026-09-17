# Handoff card — structure → function

Print-first. Paste into this repo’s `config/local.env`:

| Copy | Value |
|------|--------|
| `RELEASE_TAG` | Same tag as structure `release/<TAG>/` |
| `PROTEINS_FA` | `…/release/<TAG>/proteins.faa` (stable alias — **not** a stale structure `WORK_DIR/proteins.faa` root copy) |
| `structure_grade` | Honest L0 / L1 / L2 from structure — do **not** invent F-L1 from a provisional GFF |

```bash
# Example shape only — paths are yours
RELEASE_TAG="species_ann.v0.1"
PROTEINS_FA="/path/to/gene-structure-annotation/work/release/${RELEASE_TAG}/proteins.faa"
```

Upstream: [structure A6](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/pipeline/A6_functional_optional.md) · this repo [`POST_STRUCTURE.md`](POST_STRUCTURE.md) · [`zh/FAQ_入门.md`](zh/FAQ_入门.md).  
中文指针：[`zh/交接_结构到功能.md`](zh/交接_结构到功能.md).
