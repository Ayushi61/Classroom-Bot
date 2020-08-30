# lint:
# 	ui.lint
# 	core.lint

# ui.lint:
# 	docker build ...
# 	docker run ...

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
	docker build --file='ui/lint.Dockerfile' ui  --tag=node-lint:local
	docker run -it --name=node-lint node-lint:local
	docker rm node-lint

ui.docker.build:
	docker build ui/ --tag=bot-ui

ui.docker.run:
	docker-compose rm -f ui
	docker-compose up ui

ui.docker.build.all: ui.build
	docker build ui/ --tag=bot-ui

ui.docker.run.all: ui.docker.build.all
	docker-compose rm -f ui
	docker-compose up ui

ui.docker.down:
	docker-compose stop ui




