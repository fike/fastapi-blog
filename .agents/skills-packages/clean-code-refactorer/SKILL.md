---
name: clean-code-refactorer
description: Skill for identifying code smells and refactoring code using Clean Code, SOLID, and DRY principles. Use when requested to "clean up", "refactor", or "improve quality" of backend code.
---

# Clean Code Refactorer

## Overview

This skill provides a systematic approach to improving code quality without changing external behavior. It enforces SOLID principles and project-specific FastAPI standards.

## Refactoring Workflow

Follow this cycle for every refactoring task:

1.  **Observe**: Identify *code smells* (long functions, duplication, tight coupling).
2.  **Orient**: Read the **[Clean Code Rules](references/clean-code-rules.md)** to determine the best pattern to apply.
3.  **Validate (Pre)**: Run existing tests to ensure the current state is stable.
4.  **Act**: Apply surgical changes (extract method, rename variable, etc.).
5.  **Validate (Post)**: Execute the **`scripts/check_quality.sh`** to verify linters and tests.

## Standards & Principles

Refer to the following for detailed guidance:

-   **[Clean Code & SOLID Reference](references/clean-code-rules.md)**: Mandatory rules for naming, function size, and architectural layers.

## Examples

-   **User**: "This service function is too long, can you refactor it?"
-   **Agent**: *Reads the function, identifies logic that can be extracted to a helper, verifies tests pass, refactors, and runs quality checks.*

## Resources

-   `scripts/check_quality.sh`: Automates Ruff, Black, and Pytest validation.
-   `references/clean-code-rules.md`: Comprehensive guide for SOLID and Clean Code.
