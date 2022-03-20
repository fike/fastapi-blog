

DC_EXEC := docker-compose

DC_DIR := deployments

DC_APP := docker-compose.yaml

DC_APP_DEV := docker-compose-dev.yaml

DC_APP_TEST := docker-compose-test.yaml

export DOCKER_BUILDKIT := false
export COMPOSE_DOCKER_CLI_BUILD := false

dev-up:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) up -d --remove-orphans --build backend db-fapi-blog jaeger-all-in-one zipkin-all-in-one
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) up -d --remove-orphans --build frontend otel-collector
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) logs -f

dev-down:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) down

dev-db-kill:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) kill db-fapi-blog

dev-backend-kill:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) kill backend

dev-db-start:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) up --remove-orphans -d db-fapi-blog

dev-logs:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP) logs -f

backend-up: clean db-up
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) up --remove-orphans -d backend jaeger-all-in-one zipkin-all-in-one otel-collector
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) logs -f

clean:
	docker system prune -f
	docker volume prune -f

db-up:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP) up --remove-orphans -d db-fapi-blog

down:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP) down --remove-orphans

migrate: test-commons test-db-up
	sleep 3
	cd backend && PYTHONPATH=$${PWD} alembic upgrade head
	cd backend && PYTHONPATH=$${PWD} alembic revision --autogenerate

pre-commit:
	cd backend &&  \
	poetry run pre-commit run -a --show-diff-on-failure

test-populate:
	opentelemetry-instrument backend/tests/populate_posts.py

test-db-up:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_TEST) up --remove-orphans -d db-test

test-down:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_TEST) down --remove-orphans -v

test-app: test-down test-db-up
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_TEST) run -w /opt/blog/backend --entrypoint "poetry run coverage run -m pytest -vv" backend
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_TEST) run -w /opt/blog/backend --entrypoint "poetry run coverage report" backend
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_TEST) run -w /opt/blog/backend --entrypoint "poetry run coverage xml" backend
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_TEST) run -w /opt/blog/backend --entrypoint "poetry run coverage html" backend

test-local: test-down clean test-db-up
	sleep 3
	cd backend && poetry run coverage run -m pytest -vv
	cd backend && poetry run coverage report
	cd backend && poetry run coverage xml
	cd backend && poetry run coverage html
	# $(DC_EXEC) -f $(DC_DIR)/$(DC_APP_TEST) down --remove-orphans -v --rmi local
