#!/bin/bash

# Comando para crear una app, añadir/modificar segun gustos.

source _variables.sh

APPNAME=$1
APPDIR="${APPS_ROOT}/${APPNAME}"

cd $APPS_ROOT
django-admin startapp $APPNAME

cd $APPNAME
rm -rf "${APPDIR}/tests.py"
touch "${APPDIR}/urls.py"

cd $SRC_ROOT

echo "Creada APP ${APPNAME} en ${APPDIR}"
