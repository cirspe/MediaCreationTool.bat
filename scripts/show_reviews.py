#!/usr/bin/env python3
"""Print all decisions with status REVIEW DUE in a readable format."""

import csv
import sys
from pathlib import Path

CSV_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "decisions.csv"

due = []
with open(CSV_PATH, newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if row.get("status", "").strip() == "REVIEW DUE":
            due.append(row)

if not due:
    print("No decisions pending review.")
    sys.exit(0)

W = 60
print("=" * W)
print(f"  DECISIONS DUE FOR REVIEW  ({len(due)} item(s))")
print("=" * W)
for r in due:
    print(f"\n  Date logged : {r['date']}")
    print(f"  Review due  : {r['review_date']}")
    print(f"  Decision    : {r['decision']}")
    print(f"  Reasoning   : {r['reasoning']}")
    print(f"  Expected    : {r['expected_outcome']}")
    print("-" * W)
