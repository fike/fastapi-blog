#!/bin/bash
set -e

sleep 2

export PYTHONPATH=/opt/blog/backend

alembic upgrade head

# Disabled opentelemetry-instrument with opentelemetry-instrumentation-sqlalchemy brake DefaultTraceProvider
# if [ $OTELE_TRACE = "True" ]
# then
#     echo "Running with OpenTelemetry"
    # opentelemetry-instrument -e none uvicorn app.main:app --host=0.0.0.0 $(test ${ENVIRONMENT} = "development" && echo "--reload")
# else
#     echo "OpenTelemetry isn't enable"
uvicorn app.main:app --host=0.0.0.0 $(test ${ENVIRONMENT} = "development" && echo "--reload")
# fi