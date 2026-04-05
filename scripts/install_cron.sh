#!/usr/bin/env bash
# Installs a daily cron job to check for decisions due for review.
# Run once: bash scripts/install_cron.sh

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CRON_CMD="0 8 * * * python3 ${REPO_DIR}/scripts/check_reviews.py >> ${REPO_DIR}/logs/review_check.log 2>&1"

# Ensure log directory exists
mkdir -p "${REPO_DIR}/logs"

# Check if already installed
if crontab -l 2>/dev/null | grep -qF "check_reviews.py"; then
    echo "[INFO] Cron job already installed."
    crontab -l | grep "check_reviews.py"
    exit 0
fi

# Add to crontab
(crontab -l 2>/dev/null; echo "${CRON_CMD}") | crontab -
echo "[OK] Cron job installed (runs daily at 08:00):"
echo "     ${CRON_CMD}"
