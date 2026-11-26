# Catalogue counts

Checked on 2026-11-26 (CST). [中文](#中文)

## Current count

The catalogue has **194 entries**: one row each in [`SOFTWARE_AUTHORITY.tsv`](SOFTWARE_AUTHORITY.tsv). This is the number to cite. It was counted from the repository root with:

```bash
python3 -B -c "import csv;print(sum(1 for _ in csv.DictReader(open('catalog/SOFTWARE_AUTHORITY.tsv',encoding='utf-8'),delimiter='\t')))"
```

Output: `194`. The breakdown below was counted with:

```bash
python3 -B -c "import csv,collections;r=list(csv.DictReader(open('catalog/SOFTWARE_AUTHORITY.tsv',encoding='utf-8'),delimiter='\t'));[print(k,v) for c in ('section','tier','added_2026_11_25') for k,v in collections.Counter(x[c] for x in r).items()]"
```

| Section | Title in the TSV | Entries |
|---|---|---|
| 1 | Homology search | 8 |
| 2 | Reference sequence and ontology databases | 11 |
| 3 | Domain and family annotation | 6 |
| 4 | Orthology-based names, GO and KEGG | 12 |
| 5 | Machine-learning GO prediction | 11 |
| 6 | Pathways, KO and EC | 18 |
| 7 | Multi-genome orthology | 16 |
| 8 | Localization and topology | 11 |
| 9 | Plant gene families | 20 |
| 10 | Non-coding RNA function resources | 11 |
| 11 | Expression-supported function | 9 |
| 12 | Community catalogues and naming | 4 |
| 13 | Protein 3D structure | 23 |
| 14 | Downstream enrichment | 15 |
| 15 | Ideas, formats and merge rules | 9 |
| viz | Visualization tools | 10 |
| | **Total** | **194** |

| Tier | Entries |
|---|---|
| standard | 90 |
| established | 51 |
| newer | 30 |
| niche | 13 |
| no paper | 10 |

## Why older pages show other numbers

Three totals appear in the repository. They are not in conflict: each is the total at a different date.

| Total | Date | What it counted | Can it be recounted from the TSV? |
|---|---|---|---|
| 129 | 2026-11 survey | 68 stage-folder cards in `catalog/` plus 61 entries in `docs/CATALOG_BY_TYPE_2026-11.md` | no; the survey files are kept as written |
| 167 | after 2026-11-14 | 129 − 3 older-version entries merged + 41 added | yes: rows with `added_2026_11_25 = no` (167) |
| 194 | after 2026-11-25 | 167 + 27 added | yes: all rows (194); rows with `added_2026_11_25 = yes`: 27 |

Pages that still show the older totals have a dated **Counts updated** note added at the end; their text was not changed:

- [`catalog/README.md`](../catalog/README.md) line 24
- [`docs/CATALOG_BY_TYPE_2026-11.md`](../docs/CATALOG_BY_TYPE_2026-11.md) line 33
- [`docs/CATALOG_BY_TYPE_2026-11.md`](../docs/CATALOG_BY_TYPE_2026-11.md) line 353
- [`docs/ROADMAP.md`](../docs/ROADMAP.md) line 133
- [`docs/ROADMAP.md`](../docs/ROADMAP.md) line 145
- [`docs/ROADMAP.md`](../docs/ROADMAP.md) line 214

## 中文

目录共 **194 条**，即 [`SOFTWARE_AUTHORITY.tsv`](SOFTWARE_AUTHORITY.tsv) 的行数，引用时以此为准。统计命令和分项见上文。
仓库里出现的 129、167、194 三个总数并不矛盾，分别是 2026-11 调研、2026-11-14 更新后和 2026-11-25 更新后的总数。仍写旧总数的页面已在文末追加一条带日期的“Counts updated”说明，正文未改。
