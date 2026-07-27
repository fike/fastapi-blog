# Skill: API Tester

Validates API endpoint responses against expected status codes and JSON schemas by curling the running backend.

## 📖 Description

This skill tests the health and correctness of all public API endpoints. It checks that endpoints return HTTP 200 (or 401 for protected routes) and that responses are valid JSON. Essential to run after any backend changes to ensure the API surface remains functional.

## 🛠 Usage

Agents should invoke this skill after implementing new endpoints or modifying existing ones.

**Command**:
```bash
./.agents/skills/test_api.sh
```

## 🎯 Expected Outcome

- **Success**: All endpoints return expected status codes and valid JSON responses.
- **Failure**: Specific endpoint failures are reported with HTTP status codes, indicating connectivity issues or broken endpoints.

## ⚠️ Requirements

- The backend must be running (e.g., `make dev-up` or `docker compose -f deployments/docker-compose-dev.yaml up -d backend`).
- Environment variable `API_BASE_URL` can override the default `http://localhost:8000`.
