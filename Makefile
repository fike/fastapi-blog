

DC_EXEC := docker-compose

DC_DIR := deployments

DC_APP := docker-compose.yaml


up-db:
	$(DC_EXEC) -f $(DC_DIR)/$(DC_APP) up -d db


test-local:
	coverage run -m pytest
	coverage report
	coverage html