#!/usr/bin/env python3
"""Append a new decision to decisions.csv with a 30-day review date."""

import csv
import sys
from datetime import date, timedelta
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "decisions.csv"
FIELDNAMES = ["date", "decision", "reasoning", "expected_outcome", "review_date", "status"]


def prompt(label: str) -> str:
    try:
        value = input(f"{label}: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nAborted.", file=sys.stderr)
        sys.exit(1)
    if not value:
        print(f"[ERROR] {label} cannot be empty.", file=sys.stderr)
        sys.exit(1)
    return value


def main():
    today = date.today()
    review_date = today + timedelta(days=30)

    print("=== Log a Decision ===")
    decision = prompt("Decision")
    reasoning = prompt("Reasoning")
    outcome = prompt("Expected outcome")

    row = {
        "date": today.isoformat(),
        "decision": decision,
        "reasoning": reasoning,
        "expected_outcome": outcome,
        "review_date": review_date.isoformat(),
        "status": "PENDING",
    }

    # Create file with header if it doesn't exist
    write_header = not CSV_PATH.exists() or CSV_PATH.stat().st_size == 0
    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerow(row)

    print(f"\n[OK] Decision logged. Review due: {review_date.isoformat()}")


if __name__ == "__main__":
    main()
