# AI-assisted functional annotation — prompts, data, order, checks

Use an AI assistant (Cursor / chat agent / lab bot) as a **runbook co-pilot**, not as a replacement for BUSCO, InterProScan, or METHODS. This page is the contract for the **function layer**.

Related: [`FUNCTIONAL_GUIDE.md`](FUNCTIONAL_GUIDE.md) · [`SCENARIOS_FUNCTIONAL.md`](SCENARIOS_FUNCTIONAL.md) · [`TOOLS.md`](TOOLS.md) · [`steps/FUNCTIONAL_MAIN.md`](steps/FUNCTIONAL_MAIN.md)

**Structural** gene-finding with AI (BRAKER / EVM / GSAman, …): use the sibling playbook  
[`gene-structure-annotation` docs/AI_ASSIST.md](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/AI_ASSIST.md)  
(or that repo's QUICKSTART / MAIN / PLAYBOOK).

---

## 1. What AI is good / bad at (FA)

| Good | Bad (do not trust alone) |
|------|---------------------------|
| Choosing F1–F9 from your evidence / goals | Inventing GO/KEGG counts or domain hits |
| Drafting `diamond` / emapper / InterProScan lines from this repo | Claiming "publication ready" without your QC files |
| Explaining emapper / IPS column meanings | Silent overwrites of `functional_master.tsv` |
| Drafting METHODS from **your** version list | Hallucinating DB paths or tool flags |

**Rule:** AI proposes; **you** run tools and keep the files. Every numeric claim must come from a file on disk.

---

## 2. Prepare data before you ask

Put a **manifest** in the chat (or `$FUNCTION_DIR/MANIFEST.md`). Minimum:

```text
Species / clade:
PROTEINS_FA: path + #sequences (seqkit stats)
Protein BUSCO (F0): C/D/F/M + lineage
DBs ready: Swiss-Prot .dmnd / eggNOG data_dir / InterProScan
Goal: paper F1 | fast F2 | names F4 | plant F6/F8/F9
Cluster: singularity|conda|modules; THREADS=
Upstream structure: release TAG or "bring your own"
```

**Do attach or paste:** F0 BUSCO short_summary, `head` of emapper/IPS, merge row counts.  
**Do not paste:** private FASTQ, license keys, passwords.

---

## 3. Prompt patterns (copy-paste)

### Pick F-branch

```text
Playbook: Xuzhen-Li/gene-function-annotation functional spine
(docs/SCENARIOS_FUNCTIONAL.md). Proteins: <path or BUSCO summary>.
Goal: paper|fast|names|NLR. Recommend F1–F9. No invented GO counts.
```

### Next functional command

```text
Branch F1. Done: F0. Next step only: eggNOG-mapper or InterProScan
using config/example.env. Point to pipeline/F*.sh.
```

### Interpret emapper/IPS

```text
I paste head -50 of emapper.annotations and IPS tsv.
Explain columns; how to merge with F_merge_tables.py;
what fraction unannotated is normal — only from my numbers.
```

### METHODS paragraph

```text
Draft a METHODS paragraph from this real tool/DB version list and F-branch.
Only use versions I list. Do not invent completeness %.
Versions:
<list>
```

### Anti-prompts

```text
Do not run cloud agents. Do not push to GitHub unless I say so.
One finished step at a time. Public files English. Talk to me in Chinese.
If unsure, say what file you need from me instead of guessing.
```

---

## 4. Order of work with AI (FA)

```text
0. You: qualified PROTEINS_FA (from structure sibling or own release)
1. You: F0 BUSCO proteins; AI: interpret only numbers you paste
2. You: F1 DIAMOND + eggNOG + InterProScan (or F2 fast path)
3. AI+You: merge with F_merge_tables.py — check one row/gene
4. Optional: F4 names · F6 Mercator · F8 NLR · F9 iTAK
5. You: F_release.sh; AI: draft METHODS from your versions
```

**Never** ask AI to "annotate all functions" in one shot. Chunk by F0–F9 in [`SCENARIOS_FUNCTIONAL.md`](SCENARIOS_FUNCTIONAL.md).

---

## 5. How to check AI output

- [ ] Paths are **your** `$FUNCTION_DIR` / env vars  
- [ ] Tool matches a [`TOOLS.md`](TOOLS.md) page or `pipeline/F*.sh`  
- [ ] Flags exist in `--help` / container docs (spot-check one)  
- [ ] No fabricated annotation rates  

If AI gives a metric you did not paste → **reject** that sentence.

---

## 6. Sign-off

1. Re-run F0 / spot-check merge yourself  
2. Fill [`METHODS_FUNCTIONAL.md`](METHODS_FUNCTIONAL.md) with **your** versions  
3. Tag `RELEASE_TAG`; never commit BAM/FASTQ  

AI chat is not the archive — `function/release/` + METHODS are.
