BACKEND-SERVICE-CONTAINER=backend-service
MYSQL-CONTAINER=mysql
BACKEND-TEST-CONTAINER=test-backend

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