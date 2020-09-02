# lint:
# 	ui.lint
# 	core.lint

# ui.lint:
# 	docker build ...
# 	docker run ...

# core.lint:
# 	docker build ..
# 	docker run  ...

backend.lint:
	- docker build -t backendlinter -f backend-service/lint.Dockerfile ./backend-service/
	- docker run --rm backendlinter

backend.app:
	- docker-compose build
	- docker-compose up -d