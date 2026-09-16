#!/usr/bin/env bash
# DIAMOND blastp vs SwissProt. Set RUN=1 to execute.
set -euo pipefail
: "${PROTEINS_FA:?}"
: "${WORK_DIR:?}"
: "${DIAMOND_DB:?set DIAMOND_DB in config/local.env}"
# shellcheck source=pipeline/_env_guards.sh
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_env_guards.sh"
_gfa_reject_placeholder_path WORK_DIR "$WORK_DIR" || exit 1
_gfa_reject_placeholder_path PROTEINS_FA "$PROTEINS_FA" || exit 1
_gfa_reject_placeholder_path DIAMOND_DB "$DIAMOND_DB" || exit 1
THREADS="${THREADS:-32}"
FUNCTION_DIR="${FUNCTION_DIR:-$WORK_DIR/function}"
OUT="$FUNCTION_DIR/diamond"
CMD=(diamond blastp --threads "$THREADS" --query "$PROTEINS_FA" --db "$DIAMOND_DB"
  --out "$OUT/swissprot.tsv"
  --outfmt 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore stitle
  --evalue 1e-5 --max-target-seqs 5)
printf '[CMD] '; printf '%q ' "${CMD[@]}"; echo
if [[ "${RUN:-0}" == "1" ]]; then
  mkdir -p "$OUT"
  "${CMD[@]}"
  echo "[OK] $OUT/swissprot.tsv ($(wc -l <"$OUT/swissprot.tsv") lines)"
else
  echo "[DRY] export RUN=1 to execute (no mkdir on DRY)"
fi
