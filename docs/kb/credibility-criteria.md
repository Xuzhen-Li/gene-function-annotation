# How far to trust a function table (criteria)

[中文](credibility-criteria.zh.md) · [Knowledge units](README.md)

This is a criteria unit. The grades F-L0 and F-L1, the gates and the fail rules are written once, in [`docs/EVALUATION.md`](../EVALUATION.md). This page explains the two levels of trust and points to them; it copies no thresholds.

## 1. What it is

Trust works at two levels. **Per label:** each GO term has an evidence code that says how it is supported; machine-made labels are electronic (IEA). **Per release:** the whole table gets a grade. In this repository F-L0 is a slim or fast frame and F-L1 is the qualified default frame F1 with all gates passed.

## 2. How the evidence is structured

| Level | What is judged | Where the rule is |
|---|---|---|
| Label | evidence code of each GO term; machine predictions stay IEA | [book chapter 19](../../book/chapters/19-pitfalls-and-qc.md); this page, claim 1 |
| Input | stable protein file and an upstream BUSCO check | [Gate-F1, Gate-F2](../EVALUATION.md#gate-f1--stable-protein-input) |
| Process | frame named, versions pinned, table rows complete | [Gate-F3 to Gate-F5](../EVALUATION.md#gate-f3--default-frame-or-waiver) |
| Release | grade, status and frame written; release pack; no databases in git | [Two finish grades](../EVALUATION.md#two-finish-grades); [Gate-F6, Gate-F7](../EVALUATION.md#gate-f6--release-pack) |

## 3. How to recognise a trustworthy table (field card)

- Predicted GO and EC terms are marked IEA.
- `grade=`, `status=` and `frame=` are written separately.
- No accuracy claim is made from similarity transfer alone.
- Plant add-ons are listed as modules, not as a higher grade.

## 4. Repository default and branches

The checklist is [`docs/EVALUATION_CHECKLIST.md`](../EVALUATION_CHECKLIST.md). QC and release steps are the catalog folders F10 and Frelease ([`catalog/README.md`](../../catalog/README.md)).

## 5. What is known in plants and in *Vitis*

- Community assessments show that GO prediction stays hard (book chapter 1, [section 1.4](../../book/chapters/01-concepts.md#14-why-errors-matter)).
- Plant add-ons (F4, F6, F8, F9) do not raise the grade by themselves (claim 4).
- The share of experimentally supported GO terms for grapevine proteins is not given here: **[待确认]**.

## 6. Claims and sources

| Claim | Source | Quoted sentence or figure | What was read |
|---|---|---|---|
| Electronic (IEA) annotations usually cannot be traced to an experiment. | Gene Ontology, [Guide to GO evidence codes](https://geneontology.org/docs/guide-go-evidence-codes/) | “IEA-supported annotations are ultimately based on either homology and/or other experimental or sequence information, but cannot generally be traced to an experimental source.” | The web page, section on electronic annotation |
| Each GO annotation carries an evidence code. | Gene Ontology, as above | “Each annotation includes an evidence code to indicate how the annotation to a particular term is supported.” | The web page, opening paragraph |
| The repository grades the process, not prediction accuracy. | [`docs/EVALUATION.md`](../EVALUATION.md#knowledge-frame-why-evaluation-looks-like-this) (this repository) | “This page therefore grades *process integrity*, not CAFA Fmax.” | The file at the current main branch |
| Plant add-ons are not a higher grade. | [`docs/EVALUATION.md`](../EVALUATION.md#two-finish-grades) (this repository) | “Plant add-ons (F4/F6/F8/F9) are **not** a higher grade by themselves” | The file at the current main branch |

## 7. See also

- Book: [chapter 19, Pitfalls and quality control](../../book/chapters/19-pitfalls-and-qc.md); [chapter 1, section 1.3](../../book/chapters/01-concepts.md#13-vocabularies-and-evidence)
- Knowledge units: [Functional labels and the four numbering schemes](function-concepts.md); [Transferring function by homology and orthology](homology-transfer.md)
- Upstream checks: [gene-structure-annotation `docs/EVALUATION.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/EVALUATION.md)
