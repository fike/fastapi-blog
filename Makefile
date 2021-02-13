

DC_EXEC := docker-compose

DC_DIR := deployments

DC_APP := docker-compose.yaml

DC_APP_DEV := docker-compose-dev.yaml

DC_APP_TEST := docker-compose-test.yaml

export DOCKER_BUILDKIT := true
export COMPOSE_DOCKER_CLI_BUILD=true

logs:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP) logs -f


dev-up:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) up --remove-orphans --build

dev-down: 
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) down 

up-backend: up-db
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP) up --remove-orphans -d backend

up-db:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP) up --remove-orphans -d db-fapi-blog

down:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP) down --remove-orphans 

test-up-db:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_TEST) up --remove-orphans -d db-test

test-down:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_TEST) down --remove-orphans -v

test-commons:
export SQLALCHEMY_DATABASE_URI := postgresql://test:test@localhost:5433/test_app

								   
test-app:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_DEV) up --remove-orphans -d backend

test-local: test-up-db test-commons
	sleep 3
	coverage run -m pytest
	coverage report
	coverage html 
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP_TEST) down --remove-orphans -v --rmi local