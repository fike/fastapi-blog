# Extreme Programming (XP) & TDD Guide

Core practices for rapid, high-quality development in the **fastapi-blog** project.

## 🔴 Phase 1: RED (Test First)
- **Rule**: Never write production code without a failing test first.
- **Action**: Create a new test file in `backend/tests/` or add a case to an existing one.
- **Verify**: Run the test and ensure it fails with the expected error (e.g., `ImportError` or `AssertionError`).

## 🟢 Phase 2: GREEN (Make it Pass)
- **Rule**: Write the minimum amount of code to make the test pass.
- **Action**: Implement the logic in `app/`. Don't worry about perfection yet.
- **Verify**: Run the test again. It must pass.

## 🔵 Phase 3: REFACTOR (Clean Up)
- **Rule**: Improve the code structure while keeping tests green.
- **Action**: Apply **Clean Code** principles. Remove duplication.
- **Verify**: Ensure tests stay green.

## 🤝 Pair Programming Workflow
- **Continuous Feedback**: Share thoughts and architectural decisions before large edits.
- **Small Commits**: Aim for atomic commits that represent a single Red-Green-Refactor cycle.
- **Simple Design**: Build only what is needed *now* (YAGNI - You Ain't Gonna Need It).
