FROM python:3.7.9-stretch
COPY webapp/ .
RUN pip install -r requirements.txt

RUN python manage.py migrate && \
    python manage.py collectstatic --noinput
CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]
