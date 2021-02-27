

DC_EXEC := docker-compose

DC_DIR := deployments

DC_APP := docker-compose.yaml

DC_APP_DEV := docker-compose-dev.yaml

DC_APP_TEST := docker-compose-test.yaml

export DOCKER_BUILDKIT := true
export COMPOSE_DOCKER_CLI_BUILD=true


dev-up:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) up -d --remove-orphans --build
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP) logs -f

dev-down: 
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) down 

dev-db-kill:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) kill db-fapi-blog

dev-db-start:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) up --remove-orphans -d db-fapi-blog

dev-logs:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP) logs -f

backend-up: db-up
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) kill backend
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) up --remove-orphans -d backend
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
	PYTHONPATH=$${PWD} alembic upgrade head
	PYTHONPATH=$${PWD} alembic revision --autogenerate

pre-commint: 
	poetry run pre-commit run --all-files --show-diff-on-failure

test-populate:
	opentelemetry-instrument tests/populate_posts.py

test-db-up:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_TEST) up --remove-orphans -d db-test

test-down:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_TEST) down --remove-orphans -v

test-commons:
export SQLALCHEMY_DATABASE_URI := postgresql://test:test@localhost:5433/test_app

								   
test-app:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) up --remove-orphans -d backend

test-local: test-down clean test-db-up test-commons
	sleep 3
	poetry run coverage run -m pytest -vv
	poetry run coverage report
	poetry run coverage xml
	poetry run coverage html 
	# $(DC_EXEC) -f $(DC_DIR)/$(DC_APP_TEST) down --remove-orphans -v --rmi local
