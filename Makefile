BACKEND-SERVICE-CONTAINER=backend-service
MYSQL-CONTAINER=mysql

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
	docker-compose up -d

# temporary hack: run make backend.app twice and finally restart.backend
.PHONY : restart.backend
restart.backend:
	- docker rm -f ${BACKEND-SERVICE-CONTAINER}
	- docker-compose up -d

.PHONY : clean
clean:
	- docker rm -f ${BACKEND-SERVICE-CONTAINER}
	- docker rm -f ${MYSQL-CONTAINER}