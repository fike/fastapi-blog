#!/bin/bash
# .agents/skills-packages/clean-code-refactorer/scripts/check_quality.sh
# Runs linters and tests to ensure refactoring didn't break anything or violate style.

set -e

FILE_PATH=$1

if [ -z "$FILE_PATH" ]; then
    echo "Usage: ./check_quality.sh <file_path>"
    exit 1
fi

echo "🧪 Running quality checks for $FILE_PATH..."

# 1. Lint with Ruff
echo "🔸 Checking with Ruff..."
docker run --rm -v "$(pwd)/backend":/app -w /app python:3.13-slim bash -c "pip install ruff && ruff check $FILE_PATH"

# 2. Format check with Black
echo "🔸 Checking formatting with Black..."
docker run --rm -v "$(pwd)/backend":/app -w /app python:3.13-slim bash -c "pip install black && black --check $FILE_PATH"

# 3. Run tests related to the file (heuristic: same name in tests folder)
# This is a simplified version; real XP would use a test watcher.
echo "🔸 Running tests..."
# Assuming we use the Makefile's test-app logic or similar
# For this script, we'll just try to run pytest on the file's corresponding test if it exists
TEST_FILE=$(echo $FILE_PATH | sed 's|app/|tests/test_|' | sed 's|/|_|g')
# This heuristic is complex, let's just run all tests for safety in this simple script
make test-app

echo "✅ Quality checks passed!"
