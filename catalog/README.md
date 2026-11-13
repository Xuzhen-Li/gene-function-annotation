# Catalog — new functional tools, databases and ideas by stage (2026-11)

Entry cards for software, databases and ideas found in the 2026-11 survey, filed by **framework / stage + step name** (see [`_namespaces.md`](_namespaces.md) for the four numbering systems; script names, TOOLS cards and gates are separate fields in each card). Input: released `proteins.faa`; product: `merged_function_table.tsv`. Databases across stages: [`_databases.md`](_databases.md). Flat one-page list of the same survey: [`../docs/CATALOG_NEW_TOOLS_2026-11.md`](../docs/CATALOG_NEW_TOOLS_2026-11.md).

**Repo-wide boundary:** no gene finders, soft-masking, TE library construction or TE libraries, GFF editing (pointers go to gene-structure-annotation or vitis-te). The structure repo's A5c `pfam_scan` is structure QC, not a functional tool. F0 BUSCO is input QC. F7 annotates orthogroup representatives, not each gene. "Structure" in protein tools (Foldseek, DeepFRI, AlphaFold DB …) means protein 3D structure.

| Stage | Entries | Folder |
|---|---|---|
| F0 · protein input QC (BUSCO protein mode) | 0 | [`F0_protein_qc/`](F0_protein_qc/README.md) |
| F1 · default framework (DIAMOND, eggNOG-mapper, InterProScan, optional KofamScan and add-ons) | 28 | [`frame_F1/`](frame_F1/README.md) |
| F2 · fast framework (eggNOG-mapper alone ± Kofam; KEGGaNOG plots) | 0 | [`frame_F2/`](frame_F2/README.md) |
| F3 · EnTAP framework | 0 | [`frame_F3/`](frame_F3/README.md) |
| F5 · Trinotate framework (transcriptome CDS) | 1 | [`frame_F5/`](frame_F5/README.md) |
| F4 · readable names (AHRD, PANNZER2) | 3 | [`F4_readable_names/`](F4_readable_names/README.md) |
| F6 · MapMan BINs (Mercator4) and plant pathway views | 2 | [`F6_mapman/`](F6_mapman/README.md) |
| F7 · multi-genome orthogroups (OrthoFinder) | 6 | [`F7_multi_genome/`](F7_multi_genome/README.md) |
| F8 · NLR protein classification (IPS filter ± HRP) | 5 | [`F8_nlr/`](F8_nlr/README.md) |
| F9 · transcription factors / kinases (iTAK) | 2 | [`F9_tf_kinase/`](F9_tf_kinase/README.md) |
| F10 · function-table QC | 2 | [`F10_function_qc/`](F10_function_qc/README.md) |
| Merge / aggregate (`F_merge_tables.py`, `F_aggregate.py`) | 0 | [`Fmerge_aggregate/`](Fmerge_aggregate/README.md) |
| Release (`F_release.sh`, Gate-F1–F7) | 1 | [`Frelease/`](Frelease/README.md) |
| Cross-stage — whole pipelines, non-protein resources, downstream pointers, ideas | 18 | [`X_cross_stage/`](X_cross_stage/README.md) |

Stage-folder cards in this directory: 68 (first pass; table above). Combined inventory with the type catalog ([`docs/CATALOG_BY_TYPE_2026-11.md`](../docs/CATALOG_BY_TYPE_2026-11.md)): **129**. The repository homepage ([`README.md`](../README.md)) lists all 129 by type. Framework / step order stays in this folder and in [`docs/ROADMAP.md`](../docs/ROADMAP.md).

**Card fields:** entry_id (`GFA-<stage>-NNN`), type, stage, script, tools_card, gates, what it does, url, doi, venue / year, venue_label (Allowlisted / Below allowlist / Preprint per [`docs/RECENT_HIGH_QUALITY.md`](../docs/RECENT_HIGH_QUALITY.md)), latest release, license, plant_evidence, existing_doc, io, db_version_field, verdict (include / needs evidence / exclude), checked_at_CST, checked_by.

**How checked:** each DOI was resolved in Crossref (DataCite for Zenodo) and the title matched to the entry; GitHub repos, latest release and licence were read from the GitHub API on 2026-11-12 (CST). `[待确认]` = not verified. Website links that block automated checks are kept but not marked as verified. No entry was added from memory without a resolved record or official page. Machine-predicted GO/EC stays electronic evidence (IEA). Proposals only; framework F1 does not change until tested.
