# lint:
# 	ui.lint
# 	core.lint

# ui.lint:
# 	docker build ...
# 	docker run ...

# core.lint:
# 	docker build ..
# 	docker run  ...
BACKEND-SERVICE-CONTAINER=backend-service
MYSQL-CONTAINER=mysql

backend.lint:
	- docker build -t backendlinter -f backend-service/lint.Dockerfile ./backend-service/
	- docker run --rm backendlinter

backend.app:
	- docker-compose build
	- docker-compose up -d

clean:
	- docker rm -f ${BACKEND-SERVICE-CONTAINER}
	- docker rm -f ${MYSQL-CONTAINER}