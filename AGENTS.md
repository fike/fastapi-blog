# Agents

This file and the `.agents/` directory define the operational framework for AI agents interacting with the **fastapi-blog** project.

## 🤖 Framework Structure

- **`.agents/skills/`**: Contains specialized tool definitions, scripts, and executable logic that extend the agent's core capabilities.
- **`.agents/subagents/`**: Defines specialized agent personas with focused system prompts and tailored toolsets for specific domains (e.g., Backend, Frontend, DevOps).

## 🛠 Project Blueprint

### Backend (Python/FastAPI)
- **Stack**: Python 3.13, Poetry, SQLAlchemy, Alembic, Pydantic.
- **Key Files**: `backend/app/main.py`, `backend/pyproject.toml`.
- **Database**: PostgreSQL (managed via SQLAlchemy models in `backend/app/models/`).

### Frontend (Next.js/React)
- **Stack**: React, Next.js, Yarn, Vanilla CSS.
- **Key Files**: `frontend/pages/index.js`, `frontend/package.json`.

### Infrastructure & Observability
- **Containerization**: Docker & Docker Compose (`deployments/`).
- **Telemetry**: OpenTelemetry (OTLP), Jaeger, Zipkin, Prometheus.

## 📜 Agent Guidelines

1. **Empirical Research**: Before any implementation, use `grep_search` and `read_file` to confirm current logic. Do not rely solely on memory.
2. **Atomic Changes**: Keep PRs and commits focused. One feature or fix per cycle.
3. **Validation Mandatory**: Every code change must be followed by a verification step (test execution or manual verification script).
4. **Dependency Management**: Use the provided Docker environments to run commands like `poetry lock` or `npm install` if local tools are missing.

## 🧩 Custom Skills (Coming Soon)

Custom skills located in `.agents/skills/` allow for project-specific automation:
- **`migration-check`**: Validates Alembic migration integrity.
- **`telemetry-verify`**: Checks if OTLP exporters are correctly configured.

## 👥 Subagents (Coming Soon)

Invoke specialized agents for complex investigations:
- **`backend-specialist`**: Expert in FastAPI performance and DB schema design.
- **`frontend-specialist`**: Expert in React state management and responsive design.

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:7510c1e2 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
<!-- END BEADS INTEGRATION -->
