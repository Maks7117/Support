#!/bin/sh


python /usr/src/djangoInnowise/manage.py runserver 0.0.0.0:8000 &
python /usr/src/djangoInnowise/manage.py migrate --noinput &


celery -A djangoInnowise worker -l info &
celery -A djangoInnowise beat -l info &
celery -A djangoInnowise flower --adress=192.168.99.100 --port=5566


exec "$@"

