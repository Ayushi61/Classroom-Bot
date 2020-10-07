# Instructions to run Django Proxy Service

## Requirements

1. Python 3.7.3
2. IDE that supports `pycodestyle`
3. We use a `.pyenv` file if you use [PyEnv](https://github.com/pyenv/pyenv) to manage multiple python environments
4. Docker

#### Standalone setup (Without docker)

This is the way most of the development has happened for the proxy service. Now that we tried docker I 
feel we should have used docker from the start (I'm just talking about the proxy service).

Let' start:

1. We need mysql to be installed on your machine. That's the toughest part of the whole setup I feel.

2. Next we need to setup a bunch of environment variables. Let's do that quickly:

    Here is what I would copy into my ~/.bash_profile or ~/.bash_rc: 
        
        # classroom bot proxy
        export BOT_PROXY_SERVER_SECRET_KEY="you can find this key in the bitwarden, never expose it"
        export MYSQL_BOT_PROXY_DB_NAME=classroom_db
        export MYSQL_BOT_PROXY_USER=root
        export MYSQL_BOT_PROXY_PASSWORD=root
        export MYSQL_BOT_PROXY_HOST=localhost
        export MYSQL_BOT_PROXY_CONNECTION_PORT=3306
        export BOT_PROXY_SERVER_API_VERSION=v0.1
        export BOT_SERVER_COURSE_URL=http://localhost:8001/api/course/
        export BOT_SERVER_ASSIGNMENT_URL=http://localhost:8001/api/assignment/
        export BOT_SERVER_STUDENT_URL=http://localhost:8001/api/student/

    Quick explanation of each of the fields:
    
        1. BOT_PROXY_SERVER_SECRET_KEY: This is the secret key required by Django to encrypt request. 
           Currently they are stored in a bitwarden account. Reach out to atrived@ncsu.edu for account
           details.
            
        2. MYSQL_BOT_PROXY_DB_NAME: DB that the proxy services uses. You can give any db name, just 
           make sure to create the db in mysql before starting the application.
           
        3. MYSQL_BOT_PROXY_USER: Self explanatory
        
        4. MYSQL_BOT_PROXY_PASSWORD: Self explanatory
        
        5. MYSQL_BOT_PROXY_HOST: Self explanatory
        
        6. MYSQL_BOT_PROXY_CONNECTION_PORT: Self explanatory
        
        7. BOT_PROXY_SERVER_API_VERSION: This is used to version the proxy server apis. If this version
           is changed then make sure you change the URL's in Command Configuration of the slack apps.
           That has api version in it.
           
           If possible remove this api version from the URL since changing it would need all the workspaces
           to change their command configuration of the slack apps.
           Instead just use it for internal purpose.
           
        8. BOT_SERVER_COURSE_URL: Course endpoint of the backend service.
        
        9. BOT_SERVER_ASSIGNMENT_URL: Assignment endpoint of the backend service.
        
        10. BOT_SERVER_STUDENT_URL: Student endpoint of the backend service.
       
3. 
    
4. Migrate: `python manage.py migrate`

5. Run server: python manage.py runserver (this by default runs the server on port 8000)

6. Use ngrok to make this server accessible to the world (over exaggeration). Ngrok helps in configuring 
    request urls in command configurations of the app. Now the slack can post command request to the configured
    request url since it is accessible to everyone via ngrok.
    
**Hurray, the standalone setup is finished.**


#### Containerized setup

The author is really tired and stress with so much documentation. We will finish this section of the doc
ASAP. Meanwhile you can have a look at docker-compose.yml to checkout how it works. If it's really urgent
reach out to (atrived@ncsu.edu).