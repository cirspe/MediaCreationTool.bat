# MediaCreationTool.bat — Project Information

## Project Overview

A Windows batch script for downloading and creating Windows 10/11 installation media.
Based on [AveYo/MediaCreationTool.bat](https://github.com/AveYo/MediaCreationTool.bat).
The repo also hosts a decision logging system and persistent memory infrastructure for Claude.

## Essential Commands

```bash
# Log a decision
./log_decision.sh

# Review decisions due for review
./review.sh

# Mark reviewed decisions as done
./mark_reviewed.sh

# Install daily review cron (run once)
bash scripts/install_cron.sh
```

## Directory Structure

```
MediaCreationTool.bat/
├── MediaCreationTool.bat   # Main Windows batch script
├── bypass11/               # Windows 11 bypass scripts
├── memory/                 # Claude persistent memory
│   ├── decisions.md
│   ├── people.md
│   ├── preferences.md
│   └── user.md
├── decisions.csv           # Decision log with 30-day review dates
├── log_decision.sh         # Log a new decision
├── review.sh               # Show REVIEW DUE decisions
├── mark_reviewed.sh        # Close out reviewed decisions
├── scripts/
│   ├── log_decision.py
│   ├── check_reviews.py    # Daily cron script
│   ├── show_reviews.py
│   ├── mark_reviewed.py
│   └── install_cron.sh
├── .claude/
│   ├── agents/             # RIPER agents
│   ├── commands/           # RIPER + memory slash commands
│   ├── memory-bank/        # RIPER session memory
│   └── skills/             # 181 installed skills (symlinks)
└── CLAUDE.md               # Claude session instructions
```

## Technology Stack

- Windows Batch Script (.bat)
- PowerShell (embedded in .bat)
- Python 3 (decision logging, CSV management)
- Bash (helper scripts)

## RIPER Workflow

### Available Commands
- `/riper:strict` — Enable strict RIPER protocol enforcement
- `/riper:research` — Research mode (read-only)
- `/riper:innovate` — Brainstorm approaches (optional)
- `/riper:plan` — Create technical specifications
- `/riper:execute` — Implement approved plan
- `/riper:execute <substep>` — Execute a specific substep
- `/riper:review` — Validate implementation against plan
- `/memory:save` — Save context to memory bank
- `/memory:recall` — Retrieve from memory bank
- `/memory:list` — List all memories

### Workflow Phases
1. **Research** — Understand the codebase and requirements
2. **Innovate** — Brainstorm approaches (optional)
3. **Plan** — Create detailed specs saved to memory bank
4. **Execute** — Implement exactly what the plan specifies
5. **Review** — Validate against the plan

## Memory Bank Policy

- Location: `.claude/memory-bank/` at repo root
- Branch-aware: each branch gets its own subdirectory
- Persists across sessions

```
.claude/memory-bank/
└── main/
    ├── plans/      # Technical specifications
    ├── reviews/    # Code review reports
    └── sessions/   # Session context
```

## Development Guidelines

- All logic in Python; shell scripts are thin wrappers
- Commit messages end with the Claude Code session URL
- Work on feature branches; push after each logical unit
- Log any decision made during a session via `./log_decision.sh`
- Read `memory/` files at session start; update at session end
