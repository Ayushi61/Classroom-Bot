BACKEND-SERVICE-CONTAINER=backend-service
MYSQL-CONTAINER=mysql
BACKEND-TEST-CONTAINER=test-backend
TEST-NETWORK=test-network

.PHONY : help
help :
	@echo "backend.lint		: Run static code analyis for backend"
	@echo "backend.app		: Build and run backend service alongwith mysql server"
	@echo "clean			: Remove docker containers."

.PHONY : backend.lint
backend.lint:
	docker build -t backendlinter -f backend-service/lint.Dockerfile ./backend-service/
	docker run --rm backendlinter

.PHONY : backend.app
backend.app:
	docker-compose build
	docker-compose up -d ${MYSQL-CONTAINER}
	docker-compose up -d ${BACKEND-SERVICE-CONTAINER}

# temporary hack: run make backend.app twice and finally restart.backend
.PHONY : restart.backend
restart.backend:
	- docker rm -f ${BACKEND-SERVICE-CONTAINER}
	- docker-compose up -d ${BACKEND-SERVICE-CONTAINER}

.PHONY : run-mysql
run-mysql:
	- docker run --name ${MYSQL-CONTAINER} --network ${TEST-NETWORK} -e MYSQL_ROOT_PASSWORD=group18 \
     -e MYSQL_DATABASE=classroom_db -e MYSQL_USER=user \
     -e MYSQL_PASSWORD=group18 -p 52000:3306 -d mysql:5.7
	- sleep 60

.PHONY : create-network
create-network:
	- docker network create ${TEST-NETWORK}

.PHONY : backend.test
backend.test:
	docker build -t backendtest -f backend-service/test.Dockerfile ./backend-service/
	docker run --rm --name ${BACKEND-TEST-CONTAINER} --network ${TEST-NETWORK} \
	 -p 8002:8002 --env-file backend-service/sample.env -e MYSQL_HOST=${MYSQL-CONTAINER} \
	 -e MYSQL_USER=root -e MYSQL_ROOT_PASSWORD=group18 backendtest

.PHONY : run-tests
run-tests: create-network run-mysql backend.test clean

.PHONY : test.backend
test.backend:
	- docker-compose build ${MYSQL-CONTAINER}
	- docker-compose build ${BACKEND-TEST-CONTAINER}
	- docker-compose up -d ${MYSQL-CONTAINER}
	- sleep 60
	- docker-compose up --abort-on-container-exit ${BACKEND-TEST-CONTAINER}
	- make clean

.PHONY : clean
clean:
	- docker rm -f ${BACKEND-SERVICE-CONTAINER}
	- docker rm -f ${MYSQL-CONTAINER}
	- docker rm -f ${BACKEND-TEST-CONTAINER}
	- docker network rm ${TEST-NETWORK}