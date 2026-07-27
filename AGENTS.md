# Agents

This file and the `.agents/` directory define the operational framework for AI agents interacting with the **fastapi-blog** project.

## Framework Structure

- **`.agents/skills/`**: Project-specific automation skills with executable scripts.
- **`.agents/skills-packages/`**: Agent Skills Open Standard packages (distributable).
- **`.agents/subagents/`**: Specialized agent personas with restricted tool access.

## Project Blueprint

### Backend (Python/FastAPI)
- **Stack**: Python 3.13, Poetry, SQLAlchemy 2.0, Alembic, Pydantic v2.
- **Key Files**: `backend/app/main.py`, `backend/pyproject.toml`.
- **Models**: `backend/app/models/` — SQLAlchemy entities.
- **Schemas**: `backend/app/schemas/` — Pydantic DTOs.
- **Services**: `backend/app/services/` — Business logic.
- **Routers**: `backend/app/routers/` — API endpoints.

### Frontend (Next.js/React)
- **Stack**: React, Next.js (v12), Yarn, Chakra UI, Vanilla CSS.
- **Key Files**: `frontend/pages/index.js`, `frontend/package.json`.
- **Linting**: ESLint + Prettier (`frontend/.eslintrc.json`).

### Infrastructure & Observability
- **Containerization**: Docker & Docker Compose (`deployments/`).
- **Telemetry**: OpenTelemetry (OTLP), Jaeger, Zipkin, Prometheus.
- **CI/CD**: GitHub Actions (`.github/workflows/`).

## Agent Guidelines

1. **Empirical Research**: Before any implementation, use `grep` and `read_file` to confirm current logic. Do not rely solely on memory.
2. **Atomic Changes**: Keep PRs and commits focused. One feature or fix per cycle.
3. **Validation Mandatory**: Every code change must be followed by a verification step (tests, linters, or manual verification script).
4. **Dependency Management**: Use Docker environments to run `poetry lock` or `yarn install` if local tools are missing.
5. **Read-Only Subagents**: Subagents analyze and validate but do not write code. The main agent handles all code modifications.

## Skills

### `.agents/skills/` (Executable Scripts)
- **`migration-validator`** — Validates Alembic migration integrity (`check_migrations.sh`).
- **`telemetry-tester`** — Verifies OTLP exporter connectivity (`test_telemetry.sh`).
- **`dependencies-sync`** — Synchronizes Poetry and Yarn lockfiles (`sync_deps.sh`).
- **`api-tester`** — Validates API endpoint responses (`test_api.sh`).
- **`security-scan`** — Runs security hooks and tests (`scan_security.sh`).

### `.agents/skills-packages/` (Open Standard)
- **`clean-code-refactorer`** — Refactoring with SOLID/DRY principles.
- **`xp-copilot`** — TDD and Extreme Programming workflow.

## Subagents

Invoke specialized agents for complex investigations. All subagents have **restricted tool access** (read-only + specific commands):

- **`backend-architect`** — FastAPI architecture, SQLAlchemy models, Alembic migrations.
- **`frontend-specialist`** — Next.js components, Chakra UI, responsive design.
- **`devops-infra`** — Docker, Docker Compose, CI/CD pipelines, Makefile automation.
- **`observability-expert`** — OpenTelemetry, Jaeger, Zipkin, Prometheus.
- **`fullstack-integrator`** — Cross-cutting changes spanning backend and frontend.

## Verification Commands

```bash
make pre-commit    # Run ruff, black, and pre-commit hooks on backend
make test-app      # Run pytest with coverage in Docker test environment
```

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
