#!/usr/bin/env bash
#
# template.sh - Description of what this script does
#
# Usage: ./template.sh [options] <arg>
#
set -euo pipefail
IFS=$'\n\t'

# ---- Constants ----
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC2034  # SCRIPT_DIR is provided for use in main logic below
readonly SCRIPT_DIR
SCRIPT_NAME="$(basename "${BASH_SOURCE[0]}")"
readonly SCRIPT_NAME

# ---- Logging ----
log()   { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >&2; }
info()  { log "INFO:  $*"; }
warn()  { log "WARN:  $*"; }
error() { log "ERROR: $*"; }
die()   { error "$*"; exit 1; }

# ---- Cleanup on exit (temp files, etc.) ----
TMP_DIR="$(mktemp -d)"
cleanup() {
    rm -rf "${TMP_DIR}"
}
trap cleanup EXIT INT TERM

# ---- Usage ----
usage() {
    cat <<EOF
Usage: ${SCRIPT_NAME} [-v] [-h] <required_arg>

Options:
  -v          Verbose output
  -h          Show this help message

Arguments:
  required_arg   Description here
EOF
}

# ---- Argument parsing ----
VERBOSE=0
while getopts ":vh" opt; do
    case "${opt}" in
        v) VERBOSE=1 ;;
        h) usage; exit 0 ;;
        \?) die "Invalid option: -${OPTARG}" ;;
    esac
done
shift $((OPTIND - 1))

if [[ $# -lt 1 ]]; then
    usage
    die "Missing required argument"
fi

REQUIRED_ARG="$1"

# ---- Dependency checks ----
require_cmd() {
    command -v "$1" >/dev/null 2>&1 || die "Required command not found: $1"
}
# require_cmd jq
# require_cmd curl

# ---- Main logic ----
main() {
    info "Starting ${SCRIPT_NAME}"
    [[ "${VERBOSE}" -eq 1 ]] && info "Verbose mode enabled"

    info "Working with arg: ${REQUIRED_ARG}"

    # Your actual work goes here

    info "Done"
}

main "$@"
