# shellcheck shell=bash
_gfa_reject_placeholder_path() {
  local label="$1" val="${2:-}"
  case "$val" in
    /path/to*|*/path/to*|"")
      echo "[ERR] $label is missing or still /path/to — edit config/local.env" >&2
      return 1
      ;;
  esac
  return 0
}
_gfa_reject_busco_lineage() {
  local val="${1:-}"
  if [[ -z "$val" ]]; then
    echo "[ERR] BUSCO_LINEAGE_PROTEIN unset" >&2
    return 1
  fi
  case "$val" in
    YOUR_*|*YOUR_*)
      echo "[ERR] BUSCO_LINEAGE_PROTEIN still placeholder ($val)" >&2
      return 1
      ;;
  esac
  if [[ "$val" == eukaryota* || "$val" == *eukaryota_odb* ]]; then
    echo "[ERR] BUSCO_LINEAGE_PROTEIN=$val bare eukaryota anti-pattern" >&2
    return 1
  fi
  return 0
}
