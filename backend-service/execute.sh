#!/bin/bash
python3 manage.py migrate --fake queue zero
python3 manage.py migrate --fake routingslip zero
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
python3 manage.py makemigrations
python3 manage.py migrate --fake-initial
python3 manage.py collectstatic --noinput
python3 manage.py runserver 0.0.0.0:8000
