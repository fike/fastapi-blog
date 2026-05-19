# Clean Code & SOLID Rules

Follow these rules strictly when refactoring or creating new code in this project.

## 🧱 SOLID Principles

1.  **Single Responsibility (SRP)**: A class/function should have only one reason to change.
2.  **Open/Closed (OCP)**: Software entities should be open for extension, but closed for modification.
3.  **Liskov Substitution (LSP)**: Objects of a superclass shall be replaceable with objects of its subclasses without affecting the correctness of the program.
4.  **Interface Segregation (ISP)**: No client should be forced to depend on methods it does not use.
5.  **Dependency Inversion (DIP)**: Depend on abstractions, not concretions. (Use FastAPI `Depends`).

## 🧼 Clean Code Practices

-   **Meaningful Names**: Variables, functions, and classes should reveal intent. Avoid `data`, `info`, `item`.
-   **Small Functions**: Functions should do one thing and do it well. Target < 20 lines.
-   **No Comments (mostly)**: Code should explain itself. Use comments only for "why", not "what".
-   **DRY (Don't Repeat Yourself)**: Abstract duplicated logic into reusable functions or services.
-   **KISS (Keep It Simple, Stupid)**: Avoid over-engineering.

## 🐍 Project Specific (FastAPI / SQLAlchemy)

-   **Schema vs Model**: Always use Pydantic for input/output and SQLAlchemy for DB. Never leak Models to the API.
-   **Service Layer**: Business logic lives in `app/services/`. Routers only handle requests and call services.
-   **Type Annotations**: Use Python type hints everywhere.
-   **Async/Await**: Use async for DB calls and external requests.
