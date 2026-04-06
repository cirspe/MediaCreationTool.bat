# Decisions

Architectural, technical, and project decisions made during sessions.

<!-- Format:
## YYYY-MM-DD: Decision Title
**Context:** Why this decision was needed
**Decision:** What was decided
**Rationale:** Why this option was chosen
**Consequences:** What this affects going forward
-->

## 2026-04-06: Persistent memory system via markdown files
**Context:** Claude has no native memory between sessions.
**Decision:** Use a `memory/` directory with four markdown files (decisions, people, preferences, user). CLAUDE.md instructs reading them at session start and updating at session end.
**Rationale:** File-based memory is versioned in git, human-readable, and easy to edit manually.
**Consequences:** Claude must always read these files at session start; updates happen at session end or when significant info arises.

## 2026-04-06: Decision log in CSV with 30-day review cycle
**Context:** Decisions made in sessions were not being tracked or revisited.
**Decision:** Use `decisions.csv` (pipe-safe, Python-managed) with a daily cron job (`check_reviews.py`) and `review.sh` surfacing `REVIEW DUE` rows.
**Rationale:** CSV is queryable and diff-friendly; Python handles quoting reliably; 30-day cycle creates accountability.
**Consequences:** `log_decision.sh` must be run whenever a decision is described. Cron installed via `scripts/install_cron.sh`.

## 2026-04-06: Python for CSV manipulation, shell wrappers for UX
**Context:** Bash CSV parsing is brittle with embedded commas/quotes.
**Decision:** All CSV logic lives in Python scripts under `scripts/`; shell scripts (`log_decision.sh`, `review.sh`) are thin wrappers.
**Rationale:** Python's `csv` module handles edge cases correctly. Shell wrappers keep the user-facing API simple.
**Consequences:** Python 3 is a runtime dependency.
