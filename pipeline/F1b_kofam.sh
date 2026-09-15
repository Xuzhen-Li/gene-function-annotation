#!/usr/bin/env bash
# KofamScan KEGG KO = F1+ optional KO (NOT TOOLS F1b; F1b = eggNOG). Set RUN=1.
set -euo pipefail
: "${PROTEINS_FA:?}"
: "${WORK_DIR:?}"
: "${KOFAM_PROFILE_DIR:?}"
: "${KOFAM_KO_LIST:?}"
THREADS="${THREADS:-32}"
FUNCTION_DIR="${FUNCTION_DIR:-$WORK_DIR/function}"
OUT="$FUNCTION_DIR/kofam"
mkdir -p "$OUT"
# executable may be named exec_annotation or kofamscan
EXE="${KOFAM_BIN:-exec_annotation}"
CMD=("$EXE" -o "$OUT/kofam.tsv" --profile "$KOFAM_PROFILE_DIR" --ko-list "$KOFAM_KO_LIST" --cpu "$THREADS" "$PROTEINS_FA")
printf '[CMD] '; printf '%q ' "${CMD[@]}"; echo
if [[ "${RUN:-0}" == "1" ]]; then
  "${CMD[@]}"
  echo "[OK] $OUT/kofam.tsv"
else
  echo "[DRY] export RUN=1 to execute"
fi
