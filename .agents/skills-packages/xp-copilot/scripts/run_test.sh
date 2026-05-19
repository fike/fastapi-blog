#!/bin/bash
# .agents/skills-packages/xp-copilot/scripts/run_test.sh
# Runs a specific test file or directory inside the Docker environment.

set -e

TARGET=$1

if [ -z "$TARGET" ]; then
    echo "Usage: ./.agents/skills-packages/xp-copilot/scripts/run_test.sh <path_to_test_file>"
    exit 1
fi

echo "🧪 Running test: $TARGET..."

# Use the test docker-compose to run pytest
docker compose -f deployments/docker-compose-test.yaml run --rm \
    -w /opt/blog/backend \
    -e PYTHONPATH=/opt/blog/backend \
    backend \
    pytest -vv "$TARGET"
