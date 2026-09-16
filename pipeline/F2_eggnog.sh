#!/usr/bin/env bash
# eggNOG-mapper (frame F1 step / TOOLS F1b). Set RUN=1 to execute.
# Needs emapper.py on PATH or EGGNOG_SIF.
# Canonical flags (also documented in docs/FUNCTIONAL_GUIDE.md F1.2):
#   --go_evidence non-electronic
#   --pfam_realign realtime   # slower/heavier; override with EGGNOG_PFAM_REALIGN=none if cost-constrained
set -euo pipefail
: "${PROTEINS_FA:?}"
: "${WORK_DIR:?}"
# shellcheck source=pipeline/_env_guards.sh
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_env_guards.sh"
_gfa_reject_placeholder_path WORK_DIR "$WORK_DIR" || exit 1
_gfa_reject_placeholder_path PROTEINS_FA "$PROTEINS_FA" || exit 1
THREADS="${THREADS:-32}"
FUNCTION_DIR="${FUNCTION_DIR:-$WORK_DIR/function}"
OUT="$FUNCTION_DIR/emapper"
TAX="${EGGNOG_TAX_SCOPE:-auto}"
FUN_PREFIX="${FUN_PREFIX:-ann}"
GO_EVIDENCE="${EGGNOG_GO_EVIDENCE:-non-electronic}"
PFAM_REALIGN="${EGGNOG_PFAM_REALIGN:-realtime}"
DATA_ARGS=()
[[ -n "${EGGNOG_DATA_DIR:-}" ]] && DATA_ARGS=(--data_dir "$EGGNOG_DATA_DIR")

if [[ -n "${EGGNOG_SIF:-}" ]]; then
  PRE=(singularity exec "$EGGNOG_SIF")
else
  PRE=()
fi

CMD=("${PRE[@]}" emapper.py -i "$PROTEINS_FA" --output "${FUN_PREFIX}_fun" --output_dir "$OUT"
  --cpu "$THREADS" --type proteins -m diamond --tax_scope "$TAX"
  --go_evidence "$GO_EVIDENCE" --pfam_realign "$PFAM_REALIGN"
  "${DATA_ARGS[@]}")
printf '[CMD] '; printf '%q ' "${CMD[@]}"; echo
if [[ "${RUN:-0}" == "1" ]]; then
  mkdir -p "$OUT"
  "${CMD[@]}"
  ls -1 "$OUT"/*.emapper.annotations
else
  echo "[DRY] export RUN=1 to execute (no mkdir on DRY)"
fi
