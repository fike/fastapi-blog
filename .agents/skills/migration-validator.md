# Skill: Migration Validator

Ensures that the database schema (Alembic migrations) and the application models (SQLAlchemy) are perfectly synchronized.

## 📖 Description

This skill runs a deep comparison between the current declarative models in `backend/app/models/` and the migration scripts in `backend/migrations/versions/`. It is essential to run this before committing any changes to backend models.

## 🛠 Usage

Agents should invoke this skill whenever a model is modified or a new migration is created.

**Command**:
```bash
./.agents/skills/check_migrations.sh
```

## 🎯 Expected Outcome

- **Success**: Output confirms "Models and migrations are in sync."
- **Failure**: Detailed drift information is provided by Alembic, indicating that a new migration needs to be generated (e.g., via `make migrate`).

## ⚠️ Requirements

- Docker and Docker Compose must be running.
- The `deployments/docker-compose-test.yaml` must be valid.
