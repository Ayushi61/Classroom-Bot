BACKEND-SERVICE-CONTAINER=backend-service
MYSQL-CONTAINER=mysql

.PHONY : help
help :
	@echo "backend.lint		: Run static code analyis for backend"
	@echo "backend.app		: Build and run backend service alongwith mysql server"
	@echo "clean			: Remove docker containers."

# core.lint:
# 	docker build ..
# 	docker run  ...


# UI management commands
ui.install:
	cd ui/classroom-bot-ui && npm install

ui.build:
	cd ui/classroom-bot-ui && npm run-script build

ui.local.start:
	cd ui/classroom-bot-ui && npm start

ui.docker.lint:
	docker build --file='ui/lint.dockerfile' ui  --tag=node-lint:local
	docker run -it --name=node-lint node-lint:local
	docker rm node-lint

ui.docker.build:
	docker build --file='ui/deploy.dockerfile' ui --tag=bot-ui:local

ui.docker.run:
	docker-compose rm -f ui
	docker-compose up ui

ui.docker.run.all: ui.docker.build
	docker-compose rm -f ui
	docker-compose up ui

ui.docker.down:
	docker-compose stop ui


.PHONY : backend.lint
backend.lint:
	docker build -t backendlinter -f backend-service/lint.Dockerfile ./backend-service/
	docker run --rm backendlinter

.PHONY : backend.app
backend.app:
	- docker-compose build
	- docker-compose up -d

# temporary hack: run make backend.app twice and finally restart.backend
.PHONY : restart.backend
restart.backend:
	docker rm -f ${BACKEND-SERVICE-CONTAINER}
	docker-compose up -d

.PHONY : clean
clean:
	docker rm -f ${BACKEND-SERVICE-CONTAINER}
	docker rm -f ${MYSQL-CONTAINER}

