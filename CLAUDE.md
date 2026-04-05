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

## Project Overview

This is the [MediaCreationTool.bat](https://github.com/AveYo/MediaCreationTool.bat) project — a Windows batch script for downloading and creating Windows 10/11 installation media.
