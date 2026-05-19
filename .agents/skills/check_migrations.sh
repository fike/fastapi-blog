#!/bin/bash
# .agents/skills/check_migrations.sh
# Validates if SQLAlchemy models are in sync with Alembic migrations.

set -e

# Path to the backend directory relative to project root
BACKEND_DIR="backend"

echo "🔍 Checking migration status..."

# Use the test docker-compose to run the check in an isolated environment
docker compose -f deployments/docker-compose-test.yaml run --rm \
    -e PYTHONPATH=/opt/blog/backend \
    backend \
    bash -c "alembic upgrade head && alembic check"

if [ $? -eq 0 ]; then
    echo "✅ Models and migrations are in sync."
else
    echo "❌ Drift detected between models and migrations!"
    exit 1
fi
