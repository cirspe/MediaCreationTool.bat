#!/usr/bin/env bash
# Interactively mark REVIEW DUE decisions as REVIEWED.
# Usage: ./mark_reviewed.sh
set -euo pipefail
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "${REPO_DIR}/scripts/mark_reviewed.py"
