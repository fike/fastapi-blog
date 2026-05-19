# Skill: Dependencies Sync

Automates the synchronization and update of lockfiles for both Backend (Poetry) and Frontend (Yarn) using isolated Docker containers.

## 📖 Description

This skill ensures that `poetry.lock` and `yarn.lock` are always consistent with their respective configuration files (`pyproject.toml` and `package.json`). By using Docker, it eliminates "tool not found" errors on the host machine and ensures the correct versions of Poetry and Node/Yarn are used.

## 🛠 Usage

Agents should invoke this skill after any modification to `pyproject.toml` or `package.json`.

**Command**:
```bash
./.agents/skills/sync_deps.sh
```

## 🎯 Expected Outcome

- **Success**: Both `backend/poetry.lock` and `frontend/yarn.lock` are updated and consistent.
- **Failure**: An error message indicating which environment failed to synchronize.

## ⚠️ Requirements

- Docker must be installed and running.
- Internet access (within the container) to download Poetry or Yarn packages if not cached.
