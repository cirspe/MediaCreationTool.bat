#!/usr/bin/env bash
# Surface all decisions flagged as REVIEW DUE.
# Usage: ./review.sh
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CSV="${REPO_DIR}/decisions.csv"

if [[ ! -f "$CSV" ]]; then
    echo "[ERROR] decisions.csv not found." >&2
    exit 1
fi

python3 "${REPO_DIR}/scripts/show_reviews.py" "$CSV"
