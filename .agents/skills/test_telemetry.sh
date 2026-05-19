#!/bin/bash
# .agents/skills/test_telemetry.sh
# Validates if the application can successfully send traces to the OTLP Collector.

set -e

echo "📡 Testing Telemetry Pipeline..."

# 1. Check if the Collector is reachable (checking the gRPC port 4317)
# We use the dev-up stack or similar. If services are down, we warn the user.
if ! docker compose -f deployments/docker-compose-dev.yaml ps | grep -q "otel-collector"; then
    echo "⚠️  OTel Collector is not running. Starting observability stack..."
    docker compose -f deployments/docker-compose-dev.yaml up -d otel-collector jaeger-all-in-one
    sleep 5
fi

echo "🚀 Sending test span via Backend container..."

# Run a one-off python script inside the backend container to emit a manual span
docker compose -f deployments/docker-compose-dev.yaml run --rm \
    -e OTEL_EXPORTER_OTLP_ENDPOINT="http://otel-collector:4317" \
    -e OTEL_SERVICE_NAME="telemetry-test-skill" \
    backend \
    python3 -c "
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

resource = Resource(attributes={SERVICE_NAME: 'telemetry-test-skill'})
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint='http://otel-collector:4317', insecure=True))
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)
with tracer.start_as_current_span('manual-test-span') as span:
    span.set_attribute('test.status', 'success')
    print('✅ Span created and sent to Collector.')
"

echo "🔎 Check Jaeger at http://localhost:16686 to verify the 'telemetry-test-skill' service traces."
