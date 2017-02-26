#!/bin/bash

source _variables.sh

# Eliminar todos los directorios 'migrations' y luego ejecuta
# makemigrations en cada app en bin/_variables.APPS
for app in "${APPS[@]}"
do
  if [ -d "$APPS_ROOT/$app/migrations" ]
  then
    rm -rf "$APPS_ROOT/$app/migrations"
  fi
done

for app in "${APPS[@]}"
do
  $PROJECT_ROOT/manage.py makemigrations $app
done
