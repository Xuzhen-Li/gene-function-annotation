# Function release checklist (pass / fail)

Full rules: [`EVALUATION.md`](EVALUATION.md). Chinese tick sheet: [`zh/验收勾选表.md`](zh/验收勾选表.md).

**Target:** [ ] F-L0 slim [ ] F-L1 qualified (default)

## F-L1 hard gates (any fail ⇒ not F-L1)

- [ ] F1 Protein provenance (structure TAG or hash)
- [ ] F2 F0 protein BUSCO Completeness **+ lineage**
- [ ] F3 F1 frame (DIAMOND + eggNOG + IPS) or written waiver
- [ ] F4 Tool + DB versions pinned
- [ ] F5 Master TSV count ≈ proteins; drops documented
- [ ] F6 `function/release/<TAG>/` pack
- [ ] F7 No private reads / multi-GB DBs in release

## Soft (report)

- [ ] Hit / domain coverage narrative (clade-aware)
- [ ] Domain-only vs GO-empty noted if relevant
- [ ] Upstream structure grade / TAG recorded

Shelf: [`QUALITY_SOURCES.md`](QUALITY_SOURCES.md).

## Auto-fail

- [ ] No alternate frame branded as F1 without waiver
- [ ] No silent mapper/DB mismatch
- [ ] No CAFA-grade GO claims from BLAST-only
- [ ] No anonymous proteins without TAG/hash

**Verdict:** status=________ TAG=________ structure TAG=________

## Pack smoke (optional)

```bash
python3 pipeline/check_release_pack.py path/to/release/TAG
```

Checks files exist; does **not** replace the gates above.
