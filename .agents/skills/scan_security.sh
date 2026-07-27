#!/bin/bash
# .agents/skills/scan_security.sh
# Runs pre-commit security hooks and security-focused tests.

set -e

echo "🔒 Running Security Scan..."

# 1. Run pre-commit security hooks on backend
echo ""
echo "📍 Running pre-commit hooks..."
cd backend && poetry run pre-commit run --all-files --show-diff-on-failure

if [ $? -eq 0 ]; then
    echo "✅ Pre-commit hooks passed."
else
    echo "❌ Pre-commit hooks failed!"
    exit 1
fi

# 2. Run security-specific tests
echo ""
echo "📍 Running security tests..."
make test-app || {
    echo "❌ Security tests failed!"
    exit 1
}

echo ""
echo "🚀 Security scan completed successfully!"
