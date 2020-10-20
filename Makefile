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

ui.build:
	cd ui/classroom-bot-ui && npm run-script build

ui.local.test:
	cd ui/classroom-bot-ui && npm test

ui.local.start:
	cd ui/classroom-bot-ui && npm start


ui.docker.build:
	docker build -f ui/app.Dockerfile ui --tag=bot-ui:local

ui.docker.run:
	docker-compose rm -f ui
	docker-compose up ui

ui.docker.test:
	docker build --file='ui/test.Dockerfile' ui  --tag=node-test:local
	docker run -it --name=node-test node-test:local
	docker rm node-test

ui.docker.run.all: ui.docker.build
	docker-compose rm -f ui
	docker-compose up ui

ui.docker.down:
	docker-compose stop ui

backend.down:
	docker-compose stop backend-service
	docker-compose rm backend-service



.PHONY : project.lint
project.lint :
	pip install pycodestyle --user
	pycodestyle --max-line-length=200 --exclude=python3.8 .


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

.PHONY : create-network
create-network:
	- docker network create ${TEST-NETWORK}

.PHONY : run-mysql
run-mysql:
	- docker run --name ${MYSQL-CONTAINER} --network ${TEST-NETWORK} \
	 -p 52000:3306 \
	 -e MYSQL_ROOT_PASSWORD=group18 \
	 -d mysql:5.7

.PHONY : build-run-backend-test
build-run-backend-test:
	docker build -t ${BACKEND-TEST-CONTAINER} -f backend-service/test.Dockerfile ./backend-service/
	docker run --rm --name ${BACKEND-TEST-CONTAINER} --network ${TEST-NETWORK} \
	 -p 8002:8002 --env-file backend-service/bot_server/.env ${BACKEND-TEST-CONTAINER}

.PHONY : backend.test
backend.test: create-network run-mysql build-run-backend-test

.PHONY : clean
clean:
	- docker rm -f ${BACKEND-SERVICE-CONTAINER}
	- docker rm -f ${BACKEND-PROXY-SERVICE-CONTAINER}
	- docker rm -f ${BACKEND-TEST-CONTAINER}
	- docker rm -f ${MYSQL-CONTAINER}
	- docker network rm ${TEST-NETWORK} 
