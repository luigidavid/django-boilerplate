#!/usr/bin/env bash

# Para ejecutar el servidor en desarrollo.
# Los argumentos seran pasados despues de ./manage.py runserver *args

source _variables.sh

$PROJECT_ROOT/manage.py runserver $*
