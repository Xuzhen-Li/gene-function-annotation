#!/usr/bin/env bash
# Package functional release + METHODS (Gate-F1/F2/F4/F5 prompts).
# No RUN=1 dry mode — fails closed if master/proteins missing.
set -euo pipefail
: "${WORK_DIR:?}"
: "${RELEASE_TAG:?}"
: "${PROTEINS_FA:?set PROTEINS_FA to the structure release proteins.faa}"
# shellcheck source=pipeline/_env_guards.sh
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_env_guards.sh"
_gfa_reject_placeholder_path WORK_DIR "$WORK_DIR" || exit 1
_gfa_reject_placeholder_path PROTEINS_FA "$PROTEINS_FA" || exit 1
FUNCTION_DIR="${FUNCTION_DIR:-$WORK_DIR/function}"
_gfa_reject_placeholder_path FUNCTION_DIR "$FUNCTION_DIR" || exit 1
REPO_ROOT="${REPO_ROOT:-}"
REL="$FUNCTION_DIR/release/${RELEASE_TAG}"
M="$FUNCTION_DIR/merge"

# Merged table: first existing file wins (enriched tables first). The legacy
# functional_master*.tsv names are still accepted, with a warning.
MASTER=""
for cand in merged_function_table.with_mapman.tsv merged_function_table.with_ahrd.tsv merged_function_table.with_pannzer.tsv \
            merged_function_table.tsv \
            functional_master.with_mapman.tsv functional_master.with_ahrd.tsv functional_master.with_pannzer.tsv functional_master.tsv; do
  if [[ -f "$M/$cand" ]]; then MASTER="$M/$cand"; break; fi
done
if [[ -z "$MASTER" ]]; then
  echo "[ERR] no merged_function_table*.tsv under $M (run pipeline/F_aggregate.py first)" >&2
  exit 1
fi
case "$MASTER" in
  */functional_master*) echo "[WARN] using legacy name $MASTER; new runs write merged_function_table.tsv" >&2 ;;
esac
echo "[release] merged table: $MASTER" >&2
if [[ ! -f "$PROTEINS_FA" ]]; then
  echo "[ERR] PROTEINS_FA missing: $PROTEINS_FA" >&2
  exit 1
fi
mkdir -p "$REL"
cp -L "$MASTER" "$REL/merged_function_table.tsv"

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
- Merge: pipeline/F_aggregate.py → merged_function_table.tsv
- QC (Gate-F2): BUSCO Completeness + lineage FILL
- Table accounting (Gate-F5): protein_n=FILL; master_rows=FILL; per-source hits FILL; annotated/empty FILL; duplicates/drops FILL

Do not distribute private BAM/FASTQ with this release.
MTX
  echo "[hint] Wrote METHODS stub with Gate-F1/F2/F4/F5 FILLs." >&2
fi

echo "[OK] release at $REL"
ls -la "$REL"
