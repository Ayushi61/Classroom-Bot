FROM python:3.7.9-stretch

ARG BOT_SERVER_SECRET_KEY=${BOT_SERVER_SECRET_KEY}
RUN echo $BOT_SERVER_SECRET_KEY

RUN mkdir /bot_server
COPY bot_server/ bot_server/
WORKDIR /bot_server
RUN pip install --upgrade setuptools && \
    pip install -r requirements.txt

RUN python manage.py migrate && \
    python manage.py collectstatic --noinput
CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]
