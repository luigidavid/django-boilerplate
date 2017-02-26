#!/usr/bin/env bash

NAME="EXAMPLE.COM" # Name of the application
DJANGODIR=/var/webapps/EXAMPLE.COM/src/ # Django project directory
LOGFILE=/var/log/gunicorn/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
USER=TU_USER # the user to run as
GROUP=TU_GROUP # the group to run as
ADDRESS=127.0.0.1:8001
NUM_WORKERS=3 # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=config.settings.prod # which settings file should Django use
DJANGO_WSGI_MODULE=config.wsgi # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/TU_USER/.virtualenvs/EXAMPLE.COM/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
    --workers $NUM_WORKERS \
    --bind=$ADDRESS \
    --user=$USER --group=$GROUP \
    --log-level=debug \
    --log-file=$LOGFILE 2>>$LOGFILE
