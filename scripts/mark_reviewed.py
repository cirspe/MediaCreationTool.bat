#!/usr/bin/env python3
"""Mark a REVIEW DUE decision as REVIEWED (closes the review loop)."""

import csv
import sys
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "decisions.csv"

rows = []
due = []

with open(CSV_PATH, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        if row.get("status", "").strip() == "REVIEW DUE":
            due.append(row)
        rows.append(row)

if not due:
    print("No decisions pending review.")
    sys.exit(0)

print("Decisions due for review:\n")
for i, r in enumerate(due, 1):
    print(f"  [{i}] {r['date']} — {r['decision']}")

print()
try:
    raw = input("Enter number(s) to mark reviewed (e.g. 1 or 1,2,3), or 'all': ").strip()
except (EOFError, KeyboardInterrupt):
    print("\nAborted.")
    sys.exit(0)

if raw.lower() == "all":
    targets = set(r["decision"] for r in due)
else:
    indices = [int(x.strip()) for x in raw.split(",") if x.strip().isdigit()]
    targets = {due[i - 1]["decision"] for i in indices if 1 <= i <= len(due)}

updated = 0
for row in rows:
    if row["decision"] in targets and row["status"] == "REVIEW DUE":
        row["status"] = "REVIEWED"
        updated += 1

with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"\n[OK] Marked {updated} decision(s) as REVIEWED.")
