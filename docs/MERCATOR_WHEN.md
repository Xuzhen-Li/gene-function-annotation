# Mercator4 — when to use the web (F6)

**F6 in this repo** = **local ingest** of MapMan-style BINs **after** you already have Mercator4 output (`F6_ingest_mercator.py`).  
This page answers when to open the **plabipd Mercator4 web** vs when to skip it.

Tool card: [`tools/mercator.md`](tools/mercator.md) · Branch map: [`ROADMAP.md`](ROADMAP.md) · Plant add-ons: wiki [Plant-addons](https://github.com/Xuzhen-Li/gene-function-annotation/wiki/Plant-addons) · Scenario: [`SCENARIOS_FUNCTIONAL.md`](SCENARIOS_FUNCTIONAL.md) (F6).

---

## When the **web** is the right door

Use [Mercator4 (plabipd)](https://www.plabipd.de/mercator_main.html) when:

- You have a **small** gene / protein set (subset, candidate list, or classroom demo) — not a multi-hour whole-proteome upload if you can avoid it
- You need **exploration** / MapMan figures and have **no local plant MapMan DB** or CLI
- You already finished (or will finish) the **F1 spine** and only need BIN labels as an **optional add-on**

Then: download results → `$FUNCTION_DIR/mercator/` → run `F6_ingest_mercator.py` into the master TSV. Record the **job date** in METHODS.

---

## When **not** to use Mercator (or not to claim it)

| Do not | Why |
|--------|-----|
| Treat Mercator / MapMan as raising the **F-L** grade | Add-ons are METHODS modules — grades are in [`EVALUATION.md`](EVALUATION.md); F6 alone ≠ higher F-L |
| Substitute Mercator for **F1** (DIAMOND + eggNOG + InterProScan) | F1 is the gene-centric spine; MapMan BINs decorate it |
| Write “MapMan done” with an empty `mercator/` folder | Provenance fail |
| Expect a public Mercator **CLI** in this playbook | F6 is **ingest of web (or pre-existing) output** |

Default if unsure: **F1 only** — skip F6 until a figure or species story needs MapMan language ([`ROADMAP.md`](ROADMAP.md) §B).

---

## One-line chooser

```text
Need MapMan BINs for a plant figure, have proteins, no local plant DB?
  → Mercator4 web → F6 ingest (after F1)
Just labeling proteins for a qualified release?
  → F1 → merge → release (skip F6)
```
