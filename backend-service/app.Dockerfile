FROM python:3.7.9-stretch

ENV BOT_SERVER_SECRET_KEY=${BOT_SERVER_SECRET_KEY}
ENV MYSQL_DATABASE=${MYSQL_DATABASE}
ENV MYSQL_USER=${MYSQL_USER}
ENV MYSQL_PASSWORD=${MYSQL_PASSWORD}
ENV MYSQL_HOST=${MYSQL_HOST}
ENV MYSQL_CONNECTION_PORT=${MYSQL_CONNECTION_PORT}

RUN mkdir /bot_server
COPY bot_server/ bot_server/
COPY execute.sh /bot_server/execute.sh
WORKDIR /bot_server
RUN chmod +x execute.sh
RUN pip install -r requirements.txt
CMD ["./execute.sh"]
