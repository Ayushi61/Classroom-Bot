# Instructions to run the Django Bot Server

## Requirements

1. Python 3.7.3
2. IDE that supports `pycodestyle`
3. We use a `.pyenv` file if you use [PyEnv] to manage multiple python environments
4. Docker

## Setting Up

### MySQL or MySQL Client

This project requires a MySQL client driver to work. You can install this by either installing mysql in full, or just the mysql client. Follow the instructions on the official [MySQL Documentation site](https://dev.mysql.com/doc/refman/8.0/en/installing.html).

**We reccomend installing just the `mysql-client` and not the entire database!**

### Python Dependencies

First, create a virtual environment as a `./venv` directory
```
python -m venv ./venv
```

Then install all dependencies
```
./venv/bin/pip install -r requirements.txt
```

## Note for a developer

1. Always makemigrations and commit those new migration files to respository to keep track of changes to Database. Use the steps without Docker option for that.

## Steps to follow for local development with docker

1. Install Docker
2. Modify the Docker compose version in [`docker-compose.yml`](../../docker-compose.yml), if you have different version.
3. Use make commands: `make backend.app` to run the bot_server application.
4. Check docker logs `docker container logs backend-service`, if there are errors of connection with mysql, use `make restart.backend` to rerun the bot_server application.
5. Your server is running on port number 8000.
