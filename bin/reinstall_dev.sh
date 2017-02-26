#!/bin/bash

# Elimina una instalacion y la reinstala en un entorno de desarrollo.
# Elimina la base de datos y la restaura.

source _variables.sh

cd $PROJECT_ROOT

# Restaurar permisos de directorios y archivos.
read -p "${GREEN}¿Restaurar permisos? ${YELLOW}(y/[N]) ${RESTORE}" yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  $BIN_ROOT/permissions.sh
fi

# Reinstalar node_modules.
read -p "${GREEN}¿Reinstalar Node? ${YELLOW}(y/[N]) ${RESTORE}" yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  if [ -d $PROJECT_ROOT/node_modules ]
  then
    rm -rf $PROJECT_ROOT/node_modules
  fi
  npm install
fi

# Reinstalar bower.
read -p "${GREEN}¿Reinstalar Bower? ${YELLOW}(y/[N]) ${RESTORE}" yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  if [ -d $SRC_ROOT/static/bower_components ]
  then
    rm -rf $SRC_ROOT/static/bower_components
    echo "${RED}Eliminado directorio ${SRC_ROOT}/static/bower_components${RESTORE}"
  fi
  bower install
fi

# Ejecutar Gulp?
read -p "${GREEN}¿Ejecutar Gulp? ${YELLOW}(y/[N]) ${RESTORE}" yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  gulp
fi

# Reinstalar la base de datos, requiere ~/.pgpass
read -p "${GREEN}¿Restaurar la base de datos? ${YELLOW}(y/[N]) ${RESTORE}" yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  # Eliminar directorios migrations, quitar cuando se pasa a prod.
  read -p "${GREEN}¿Eliminar directorios migrations? ${YELLOW}(y/[N]) " yn
  if [ "$yn" == "y" -o "$yn" == "Y" ]
  then
    source $BIN_ROOT/delete_migrations.sh
  fi

  psql -U postgres -c "DROP DATABASE IF EXISTS $DATABASE_NAME"
  echo "${RED}Eliminada base de datos $DATABASE_NAME${RESTORE}"
  psql -U postgres -c "CREATE DATABASE $DATABASE_NAME WITH OWNER $DATABASE_USER"
  echo "${GREEN}Creada base de datos ${YELLOW}$DATABASE_NAME ${GREEN}WITH OWNER ${YELLOW}$DATABASE_USER${RESTORE}"

  $PROJECT_ROOT/manage.py makemigrations
  $PROJECT_ROOT/manage.py migrate
fi

# Load fixtures
read -p "${GREEN}¿Load Fixtures? ${YELLOW}(y/[N]) ${RESTORE}" yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  source django_loaddata.sh
fi

# Restore Media?
read -p "${GREEN}¿Restaurar Media local? ${YELLOW}(y/[N]) ${RESTORE}" yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  rm -rf $SRC_ROOT/media/local
  cp -r $PROJECT_ROOT/compose/media/local $SRC_ROOT/media/local

  # Test pone los mismos que los de local
  rm -rf $SRC_ROOT/media/test
  cp -r $PROJECT_ROOT/compose/media/local $SRC_ROOT/media/test
fi

# Eliminar logs
read -p "${GREEN}¿Eliminar logs? ${YELLOW}(y/[N]) ${RESTORE}" yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  find $PROJECT_ROOT/logs/* ! -name ".keep" -exec rm -r {} \;
fi

# Comprueba si hay algun print() en el codigo.
grep --exclude=*.pyc -rnw $PROJECT_ROOT/src/apps $PROJECT_ROOT/tests -e 'print'

# Iniciar el servidor
read -p "${GREEN}¿Iniciar el servidor? ${YELLOW}(y/[N]) ${RESTORE}" yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  $PROJECT_ROOT/manage.py runserver $SITE_DOMAIN
fi
