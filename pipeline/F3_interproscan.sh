#!/usr/bin/env bash
# InterProScan. Set RUN=1. Needs INTERPROSCAN_HOME pointing at install dir.
set -euo pipefail
: "${PROTEINS_FA:?}"
: "${WORK_DIR:?}"
: "${INTERPROSCAN_HOME:?set INTERPROSCAN_HOME to directory containing interproscan.sh}"
# shellcheck source=pipeline/_env_guards.sh
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_env_guards.sh"
_gfa_reject_placeholder_path WORK_DIR "$WORK_DIR" || exit 1
_gfa_reject_placeholder_path PROTEINS_FA "$PROTEINS_FA" || exit 1
_gfa_reject_placeholder_path INTERPROSCAN_HOME "$INTERPROSCAN_HOME" || exit 1
THREADS="${THREADS:-32}"
FUNCTION_DIR="${FUNCTION_DIR:-$WORK_DIR/function}"
OUT="$FUNCTION_DIR/interpro"
FUN_PREFIX="${FUN_PREFIX:-ann}"
IPS="$INTERPROSCAN_HOME/interproscan.sh"
CMD=("$IPS" -i "$PROTEINS_FA" -f tsv,gff3 -dp -cpu "$THREADS" -b "$OUT/${FUN_PREFIX}_ips")
printf '[CMD] '; printf '%q ' "${CMD[@]}"; echo
if [[ "${RUN:-0}" == "1" ]]; then
  mkdir -p "$OUT"
  "${CMD[@]}"
  echo "[OK] InterProScan outputs under $OUT"
else
  echo "[DRY] export RUN=1 to execute (no mkdir on DRY)"
fi
