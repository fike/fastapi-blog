#!/bin/bash
# .agents/skills/test_api.sh
# Validates API endpoint responses against expected status codes and schemas.

set -e

BASE_URL="${API_BASE_URL:-http://localhost:8000}"

echo "🔌 Testing API Endpoints..."
echo "   Base URL: $BASE_URL"

FAILED=0

# Test 1: Health check / root endpoint
echo ""
echo "📍 Testing GET / ..."
RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/" 2>/dev/null || echo "000")
if [ "$RESPONSE" = "200" ]; then
    echo "   ✅ GET / → 200 OK"
else
    echo "   ❌ GET / → $RESPONSE (expected 200)"
    FAILED=1
fi

# Test 2: Posts listing
echo ""
echo "📍 Testing GET /api/posts ..."
RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/api/posts" 2>/dev/null || echo "000")
if [ "$RESPONSE" = "200" ] || [ "$RESPONSE" = "401" ]; then
    echo "   ✅ GET /api/posts → $RESPONSE"
    BODY=$(curl -s "$BASE_URL/api/posts" 2>/dev/null || echo "{}")
    if echo "$BODY" | python3 -c "import sys,json; json.load(sys.stdin)" 2>/dev/null; then
        echo "   ✅ Response is valid JSON"
    else
        echo "   ⚠️  Response is not valid JSON"
    fi
else
    echo "   ❌ GET /api/posts → $RESPONSE (expected 200 or 401)"
    FAILED=1
fi

# Test 3: Users listing
echo ""
echo "📍 Testing GET /api/users ..."
RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/api/users" 2>/dev/null || echo "000")
if [ "$RESPONSE" = "200" ] || [ "$RESPONSE" = "401" ]; then
    echo "   ✅ GET /api/users → $RESPONSE"
else
    echo "   ❌ GET /api/users → $RESPONSE (expected 200 or 401)"
    FAILED=1
fi

# Test 4: OpenAPI schema
echo ""
echo "📍 Testing GET /docs (OpenAPI) ..."
RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/docs" 2>/dev/null || echo "000")
if [ "$RESPONSE" = "200" ]; then
    echo "   ✅ GET /docs → 200 OK"
else
    echo "   ⚠️  GET /docs → $RESPONSE (expected 200)"
fi

echo ""
if [ $FAILED -eq 0 ]; then
    echo "🚀 All API tests passed!"
    exit 0
else
    echo "❌ Some API tests failed. Is the backend running?"
    echo "   Start with: make dev-up"
    exit 1
fi
