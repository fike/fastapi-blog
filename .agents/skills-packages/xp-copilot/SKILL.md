---
name: xp-copilot
description: Skill for Extreme Programming (XP) practices and Test-Driven Development (TDD). Use when starting new features or fixing bugs to ensure a "Red-Green-Refactor" cycle.
---

# XP Copilot

## Overview

This skill guides the agent through the **Extreme Programming** workflow, prioritizing **TDD**, simple design, and continuous feedback.

## TDD Workflow (Red-Green-Refactor)

1.  **Red**: Create a failing test in `backend/tests/`. Run it using `scripts/run_test.sh`.
2.  **Green**: Write the minimum code in `backend/app/` to pass the test.
3.  **Refactor**: Clean up the code while keeping the tests green.

## Rules of Engagement

- **Test First**: Production code modification is forbidden without a corresponding test case.
- **Small Iterations**: Deliver small, functional increments.
- **Continuous Validation**: Use `scripts/run_test.sh` after every change.

## Reference Materials

- **[XP & TDD Guide](references/xp-tdd-guide.md)**: Detailed breakdown of the TDD phases and pair programming mindset.

## Resources

- `scripts/run_test.sh`: Executes pytest inside the project's Docker test environment.
