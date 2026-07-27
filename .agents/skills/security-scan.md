# Skill: Security Scan

Runs pre-commit security hooks and security-focused tests to ensure the codebase meets security standards.

## 📖 Description

This skill performs a security audit of the codebase by running pre-commit hooks (trailing whitespace, YAML validation, large file checks) and executing security-specific pytest suites. Essential to run before committing changes or before CI/CD pipeline execution.

## 🛠 Usage

Agents should invoke this skill before committing any code changes or when security is a concern.

**Command**:
```bash
./.agents/skills/scan_security.sh
```

## 🎯 Expected Outcome

- **Success**: Pre-commit hooks pass and security tests (`test_security.py`) return green.
- **Failure**: Specific hook or test failures are reported, indicating security concerns or code quality issues.

## ⚠️ Requirements

- Docker must be installed and running.
- Poetry must be configured in `backend/pyproject.toml`.
- The test database must be available (`make test-db-up`).
