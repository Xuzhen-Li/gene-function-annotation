#!/usr/bin/env bash
# Package functional release + METHODS (Gate-F1/F2/F4/F5 prompts).
# No RUN=1 dry mode — fails closed if master/proteins missing.
set -euo pipefail
: "${WORK_DIR:?}"
: "${RELEASE_TAG:?}"
: "${PROTEINS_FA:?set PROTEINS_FA to the structure release proteins.faa}"
FUNCTION_DIR="${FUNCTION_DIR:-$WORK_DIR/function}"
REPO_ROOT="${REPO_ROOT:-}"
REL="$FUNCTION_DIR/release/${RELEASE_TAG}"
mkdir -p "$REL"

MASTER="$FUNCTION_DIR/merge/functional_master.tsv"
# Prefer MapMan/AHRD-enriched masters when present
[[ -f "$FUNCTION_DIR/merge/functional_master.with_mapman.tsv" ]] && MASTER="$FUNCTION_DIR/merge/functional_master.with_mapman.tsv"
[[ -f "$FUNCTION_DIR/merge/functional_master.with_ahrd.tsv" ]] && MASTER="$FUNCTION_DIR/merge/functional_master.with_ahrd.tsv"
# If both enriched exist, prefer with_mapman then allow override by copying ahd last — pick mapman if set:
if [[ -f "$FUNCTION_DIR/merge/functional_master.with_mapman.tsv" ]]; then
  MASTER="$FUNCTION_DIR/merge/functional_master.with_mapman.tsv"
fi
if [[ ! -f "$MASTER" ]]; then
  echo "[ERR] no functional_master*.tsv under $FUNCTION_DIR/merge" >&2
  exit 1
fi
cp -L "$MASTER" "$REL/functional_master.tsv"

if [[ ! -f "$PROTEINS_FA" ]]; then
  echo "[ERR] PROTEINS_FA missing: $PROTEINS_FA" >&2
  exit 1
fi
cp -L "$PROTEINS_FA" "$REL/proteins.faa"

[[ -d "$FUNCTION_DIR/qc" ]] && cp -r "$FUNCTION_DIR/qc" "$REL/" || true

# Prefer a user-filled METHODS if present; else seed from template FILLs
if [[ -f "$FUNCTION_DIR/METHODS.md" ]]; then
  cp -L "$FUNCTION_DIR/METHODS.md" "$REL/METHODS.md"
elif [[ -n "$REPO_ROOT" && -f "$REPO_ROOT/docs/METHODS_FUNCTIONAL.md" ]]; then
  cp -L "$REPO_ROOT/docs/METHODS_FUNCTIONAL.md" "$REL/METHODS.md"
  echo "[hint] Copied docs/METHODS_FUNCTIONAL.md — replace every FILL (incl. Gate-F5)." >&2
else
  cat > "$REL/METHODS.md" << MTX
# Functional annotation METHODS (${RELEASE_TAG})

Fill every FILL before claiming F-L1 (see docs/METHODS_FUNCTIONAL.md).

grade=F-L0
status=provisional
frame=F1
# Never write status=F-L1 (status is only provisional or qualified).
# Do not bump grade=F-L1 until EVALUATION gates pass.

- Protein provenance (Gate-F1): structure RELEASE_TAG or hash/path = FILL
- DIAMOND software version: FILL ; Swiss-Prot DB release: FILL
- eggNOG-mapper version: FILL ; eggNOG database: FILL ; tax_scope: FILL ; GO evidence flags: FILL
- InterProScan software version: FILL ; InterPro / member-DB data release: FILL
- Optional: KofamScan (F1+) / Mercator4 / AHRD — FILL or unused
- Merge: pipeline/F_merge_tables.py → functional_master.tsv
- QC (Gate-F2): BUSCO Completeness + lineage FILL
- Table accounting (Gate-F5): protein_n=FILL; master_rows=FILL; per-source hits FILL; annotated/empty FILL; duplicates/drops FILL

Do not distribute private BAM/FASTQ with this release.
MTX
  echo "[hint] Wrote METHODS stub with Gate-F1/F2/F4/F5 FILLs." >&2
fi

echo "[OK] release at $REL"
ls -la "$REL"
