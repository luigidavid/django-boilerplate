#!/bin/bash

# Cuando se hace un commit desde producción, con este archivo automatizara
# procesos típicos para implementar los cambios.
#
# Nodejs y Bower se requiren para recursos como las fuentes

source _variables.sh

# Probar que se esta en el entorno de producción.
if [ $VIRTUALENV != $VIRTUAL_ENV_PROD ]
then
  echo "reinstall_dev.sh es solo para en entorno '$VIRTUAL_ENV_PROD'"
  exit
fi

cd $PROJECT_ROOT

# Ejecutar git pull origin prod.
read -p "git pull origin ${BRANCH_PROD}? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  git pull origin $BRANCH_PROD
fi

# Backup database
read -p "¿Backup database? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  $CRON_ROOT/postgres_db_backup.sh
fi

# Ejecutar migrate.
read -p "¿Ejecutar migrate? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  $PROJECT_ROOT/prod_manage.py migrate
fi

# Reinstalar node_modules.
read -p "¿Reinstalar Node? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  if [ -d $PROJECT_ROOT/node_modules ]
  then
    rm -rf $PROJECT_ROOT/node_modules
  fi
  npm install
fi

# Reinstalar bower.
read -p "¿Reinstalar Bower? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  if [ -d $SRC_ROOT/static/bower_components ]
  then
    rm -rf $SRC_ROOT/static/bower_components
    echo "Eliminado directorio ${SRC_ROOT}/static/bower_components"
  fi
  bower install
fi

# Eliminar directorio de collectstatic.
read -p "¿Eliminar directorio de collectstatic? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  if [ -d $SRC_ROOT/staticfiles ]
  then
    rm -rf $SRC_ROOT/staticfiles
  fi
fi

# Ejecutar collectstatic.
read -p "¿Ejecutar collectstatic? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  $PYTHON_EXEC $PROJECT_ROOT/prod_manage.py collectstatic
fi

# Reiniciar gunicorn.
read -p "¿Reiniciar gunicorn? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  sudo systemctl restart gunicorn
fi
