# Skill: Telemetry Tester

Validates the end-to-end health of the OpenTelemetry (OTLP) pipeline by emitting a test span and checking connectivity to the Collector and Jaeger.

## 📖 Description

This skill verifies that the observability stack is correctly configured and that the Backend can communicate with the `otel-collector`. It ensures that `OTEL_EXPORTER_OTLP_ENDPOINT` settings are working as expected before deep-diving into complex tracing bugs.

## 🛠 Usage

Agents should invoke this skill when troubleshooting missing traces in Jaeger or after modifying observability configurations.

**Command**:
```bash
./.agents/skills/test_telemetry.sh
```

## 🎯 Expected Outcome

- **Success**: Script prints "✅ Span created and sent to Collector." and provides a link to Jaeger.
- **Failure**: Errors indicating connection timeouts to the collector or missing OpenTelemetry libraries in the backend container.

## ⚠️ Requirements

- Docker and Docker Compose must be installed.
- The `otel-collector` and `jaeger` services must be defined in `deployments/docker-compose-dev.yaml`.
