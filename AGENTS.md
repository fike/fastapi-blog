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
