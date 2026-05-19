#!/bin/bash
# .agents/skills/sync_deps.sh
# Synchronizes backend (Poetry) and frontend (Yarn) dependencies using Docker.

set -e

PROJECT_ROOT=$(pwd)

echo "📦 Synchronizing dependencies..."

# 1. Backend (Poetry)
if [ -d "backend" ]; then
    echo "🐍 Updating backend (Poetry)..."
    docker run --rm \
        -v "$PROJECT_ROOT/backend":/app \
        -w /app \
        python:3.13-slim \
        bash -c "pip install poetry && poetry lock --no-update"
    echo "✅ Backend lockfile synchronized."
fi

# 2. Frontend (Yarn)
if [ -d "frontend" ]; then
    echo "⚛️ Updating frontend (Yarn)..."
    docker run --rm \
        -v "$PROJECT_ROOT/frontend":/app \
        -w /app \
        node:16-slim \
        bash -c "yarn install --mode update-lockfile"
    echo "✅ Frontend lockfile synchronized."
fi

echo "🚀 All dependencies are in sync!"
