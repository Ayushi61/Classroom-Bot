BACKEND-SERVICE-CONTAINER=backend-service
BACKEND-PROXY-SERVICE-CONTAINER=backend-proxy-service
MYSQL-CONTAINER=mysql

BACKEND-TEST-CONTAINER=test-backend
TEST-NETWORK=test-network

.PHONY : help
help :
	@echo "backend.lint			: Run static code analyis for backend"
	@echo "backend-proxy.lint	: Run static code analysis for the slack proxy backend service"
	@echo "backend.app			: Build and run backend service alongwith mysql server"
	@echo "backend.test			: Build and Run the tests for backend service"
	@echo "clean				: Remove docker containers."

start.all:
	docker-compose build
	docker-compose up -d

ui.install:
	cd ui/classroom-bot-ui && npm install

ui.build: ui.install
	cd ui/classroom-bot-ui && npm run-script build

ui.docker.build: ui.build
	docker build -f ui/app.Dockerfile ui --tag=bot-ui:local

ui.docker.run: ui.build ui.docker.build 
	docker-compose up ui

ui.docker.test:
	docker build --file='ui/test.Dockerfile' ui  --tag=node-test:local
	docker run -it --name=node-test node-test:local
	docker rm node-test

ui.app: ui.docker.run

.PHONY : backend.app
backend.app:
	docker-compose build
	docker-compose up -d ${MYSQL-CONTAINER}
	docker-compose up -d ${BACKEND-SERVICE-CONTAINER}

.PHONY : backend.app
backend-proxy.app:
	docker-compose build
	docker-compose up -d ${MYSQL-CONTAINER}
	docker-compose up -d ${BACKEND-PROXY-SERVICE-CONTAINER}

.PHONY : restart.backend
restart.backend:
	- docker rm -f ${BACKEND-SERVICE-CONTAINER}
	- docker-compose up -d ${BACKEND-SERVICE-CONTAINER}

.PHONY : run.mysql
run.mysql:
	- docker-compose build
	- docker-compose up -d ${MYSQL-CONTAINER}

.PHONY : run.all
run.all: run.mysql backend.app backend-proxy.app ui.app

.PHONY : clean
clean:
	- docker-compose stop
	- docker-compose rm

## LINTERS ##

.PHONY : backend.lint
backend.lint:
	docker build -t backendlinter -f backend-service/lint.Dockerfile ./backend-service/
	docker run --rm backendlinter

.PHONY : backend-proxy.lint
backend-proxy.lint:
	docker build -t backendproxylinter -f backend-service/lint-bot-proxy.Dockerfile ./backend-service/
	docker run --rm backendproxylinter

ui.lint:
	docker build -f ui/lint.Dockerfile ui --tag=node-lint:local
	docker run -it --name=node-lint node-lint:local
	docker rm node-lint

## TESTS ##

.PHONY : build.run.backend-test
build.run.backend.test:
	docker build -t ${BACKEND-TEST-CONTAINER} -f backend-service/test.Dockerfile ./backend-service/
	docker run --rm --name ${BACKEND-TEST-CONTAINER} --network ${TEST-NETWORK} \
	 -p 8002:8002 --env-file backend-service/bot_server/.env ${BACKEND-TEST-CONTAINER}

.PHONY : backend.test
backend.test: run.mysql build.run.backend.test