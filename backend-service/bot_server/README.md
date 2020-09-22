# Instructions to run the Django Bot Server

## Requirements

1. `python --version` <br/>
   Python 3.7.3
2. `mysql --version` <br/>
   [mysql Ver 14.14 Distrib 5.7.31](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/), for Linux (x86_64) using  EditLine wrapper
3. [Django and code base requirements](./requirements.txt)
4. Linter, which adheres to PEP8 standards:
   `pycodestyle==2.6.0`
5. We have used PyCharm and VSCode as Editors with pycodestyle as linter in Python Environment
Note: We recommend using virtualenv

## Note for a developer

1. Always makemigrations and commit those new migration files to respository to keep track of changes to Database. Use the steps without Docker option for that.

## Steps to follow for local development without docker

1. Install MySQL Client, Use user `root` and assign password `group18`
2. Set up local environment variables as given [here](./../sample.env)
3. Install all the other requirements which were mentioned above.
4. Give executable permissions to `backend-service/execute.sh`
5. From the directory Classroom-Bot, go to bot_server: `cd backend-service/bot_server/`
6. Run `../execute.sh`
7. Your server is running on port number 8000.

## Steps to follow for local development with docker

1. Install Docker
2. Modify the Docker compose version in [`docker-compose.yml`](../../docker-compose.yml), if you have different version.
3. Use make commands: `make backend.app` to run the bot_server application.
4. Check docker logs `docker container logs backend-service`, if there are errors of connection with mysql, use `make restart.backend` to rerun the bot_server application.
5. Your server is running on port number 8000.
