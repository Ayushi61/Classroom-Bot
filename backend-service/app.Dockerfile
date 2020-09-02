FROM python:3.7.9-stretch

ARG BOT_SERVER_SECRET_KEY=${BOT_SERVER_SECRET_KEY}
ENV MYSQL_DATABASE=${MYSQL_DATABASE}
ENV MYSQL_USER=${MYSQL_USER}
ENV MYSQL_PASSWORD=${MYSQL_PASSWORD}
ENV MYSQL_HOST=${MYSQL_HOST}
ENV MYSQL_CONNECTION_PORT=${MYSQL_CONNECTION_PORT}
RUN echo ${MYSQL_CONNECTION_PORT}

RUN mkdir /bot_server
COPY bot_server/ bot_server/
WORKDIR /bot_server
RUN pip install --upgrade setuptools && \
    pip install -r requirements.txt

RUN python manage.py migrate && \
    python manage.py collectstatic --noinput
CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]
