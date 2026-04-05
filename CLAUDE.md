# Claude Instructions

## Persistent Memory

At the **start of every session**, read all files in the `memory/` directory:

- `memory/decisions.md` — past architectural and technical decisions
- `memory/people.md` — collaborators, maintainers, and relevant people
- `memory/preferences.md` — project conventions and user preferences
- `memory/user.md` — information about the user

Use this context to maintain continuity across sessions.

At the **end of every session** (or when significant new information arises), update the relevant memory files:

- Record any new technical or architectural decisions in `decisions.md`
- Add or update people information in `people.md`
- Capture any new preferences or conventions learned in `preferences.md`
- Update user context in `user.md`

Keep entries concise, dated where appropriate, and remove outdated information.

## Decision Logging

Whenever the user describes a decision — architectural, technical, process, or otherwise — log it immediately using:

```bash
./log_decision.sh
```

This appends a row to `decisions.csv` with today's date and a 30-day review date.

**What counts as a decision:** any choice between alternatives where the reasoning matters — e.g. "we'll use X instead of Y", "we decided to drop feature Z", "we'll prioritise A over B".

When logging, capture:
- **Decision** — the choice made (concise, action-oriented)
- **Reasoning** — why this option was chosen
- **Expected outcome** — what success looks like in 30 days

To see decisions due for review at any time:

```bash
./review.sh
```

The daily cron job (installed via `bash scripts/install_cron.sh`) automatically flags rows as `REVIEW DUE` when their 30-day date arrives. Logs are written to `logs/review_check.log`.

## Project Overview

This is the [MediaCreationTool.bat](https://github.com/AveYo/MediaCreationTool.bat) project — a Windows batch script for downloading and creating Windows 10/11 installation media.
