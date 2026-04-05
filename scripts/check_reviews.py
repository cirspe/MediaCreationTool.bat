#!/usr/bin/env python3
"""Daily cron script: flags decisions whose review date has arrived."""

import csv
import sys
from datetime import date, datetime
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "decisions.csv"
TODAY = date.today()


def main():
    if not CSV_PATH.exists():
        print(f"[ERROR] decisions.csv not found at {CSV_PATH}", file=sys.stderr)
        sys.exit(1)

    rows = []
    flagged = []

    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            try:
                review_date = datetime.strptime(row["review_date"], "%Y-%m-%d").date()
            except (ValueError, KeyError):
                rows.append(row)
                continue

            if review_date <= TODAY and row.get("status", "").strip() == "PENDING":
                row["status"] = "REVIEW DUE"
                flagged.append(row["decision"])

            rows.append(row)

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    if flagged:
        print(f"[{TODAY}] Flagged {len(flagged)} decision(s) as REVIEW DUE:")
        for d in flagged:
            print(f"  - {d}")
    else:
        print(f"[{TODAY}] No new reviews due.")


if __name__ == "__main__":
    main()
