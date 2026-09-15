#!/usr/bin/env bash
# Package functional release + METHODS stub (Gate-F4 / Gate-F1 / Gate-F2 prompts).
set -euo pipefail
: "${WORK_DIR:?}"
: "${RELEASE_TAG:?}"
FUNCTION_DIR="${FUNCTION_DIR:-$WORK_DIR/function}"
REL="$FUNCTION_DIR/release/${RELEASE_TAG}"
mkdir -p "$REL"
MASTER="$FUNCTION_DIR/merge/functional_master.tsv"
[[ -f "$MASTER" ]] || MASTER="$FUNCTION_DIR/merge/functional_master.with_mapman.tsv"
[[ -f "$MASTER" ]] || MASTER="$FUNCTION_DIR/merge/functional_master.with_ahrd.tsv"
if [[ ! -f "$MASTER" ]]; then
  echo "[ERR] no functional_master*.tsv under $FUNCTION_DIR/merge" >&2
  exit 1
fi
cp -L "$MASTER" "$REL/functional_master.tsv"
cp -L "$PROTEINS_FA" "$REL/proteins.faa" 2>/dev/null || true
[[ -d "$FUNCTION_DIR/qc" ]] && cp -r "$FUNCTION_DIR/qc" "$REL/" || true
# Prefer copying filled template if present; else emit stub with Gate-aligned FILLs.
if [[ -f "${REPO_ROOT:-}/docs/METHODS_FUNCTIONAL.md" ]]; then
  echo "[hint] Fill FILLs from docs/METHODS_FUNCTIONAL.md (Gate-F1/F2/F4)." >&2
fi
cat > "$REL/METHODS.md" << MTX
# Functional annotation METHODS (${RELEASE_TAG})

Fill every FILL before claiming F-L1 (see docs/METHODS_FUNCTIONAL.md; Gate-F1/F2/F4).

- Protein provenance (Gate-F1): structure RELEASE_TAG or hash/path = FILL
- DIAMOND software version: FILL ; Swiss-Prot DB release: FILL
- eggNOG-mapper version: FILL ; eggNOG database: FILL ; tax_scope: FILL
- InterProScan software version: FILL ; InterPro / member-DB data release: FILL
- Optional: KofamScan (F1+ optional KO) / Mercator4 / AHRD — FILL or unused
- Merge: this repo pipeline/F_merge_tables.py → functional_master.tsv
- QC (Gate-F2): BUSCO protein Completeness + lineage FILL (summary under qc/)

Do not distribute private BAM/FASTQ with this release.
MTX
echo "[OK] release at $REL"
ls -la "$REL"
