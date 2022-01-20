#!/bin/sh 

python manage.py migrate --noinput
python manage.py loaddata fixtures.json

gunicorn -b 0.0.0.0:8000 social.wsgi
