# Instructions to run Django Proxy Service

## Requirements

1. Python 3.7.3
2. IDE that supports `pycodestyle`
3. We use a `.pyenv` file if you use [PyEnv](https://github.com/pyenv/pyenv) to manage multiple python environments
4. Docker
5. [Ngrok](https://ngrok.com/)

### Python Dependencies

First, create a virtual environment as a `./venv` directory
```
python -m venv ./venv
```

Then install all dependencies
```
./venv/bin/pip install -r requirements.txt
```
       
### Running the Proxy Service

If you want to run outside of the Docker container, you can manually start the server. 

First, you will need to export the local environment for running the 
```
source local.env
```

Second, you will need to create a super-user to access all of the Django resources. This user will be used for both the proxy service and the backend service, so you will only need to create it once.

When you run this command, you will be prompted for a username, email, and a password. Use whatever you want, just remember them as this is now the super-user for your local development environment.

```
./venv/bin/python manage.py createsuperuser
```

```
./venv/bin/python manage.py makemigrations
./venv/bin/python manage.py migrate
./venv/bin/python manage.py runserver 0.0.0.0:8001
```

### Running w/Docker

To run via Docker, use the `Makefile`

```
make backend-proxy.app
```

This will run the MySQL database, the backend service, and the backend proxy service.