#!/usr/bin/env bash
# Log a new decision to decisions.csv
# Usage: ./log_decision.sh
set -euo pipefail
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "${REPO_DIR}/scripts/log_decision.py"
