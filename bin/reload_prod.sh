#!/bin/bash

# Cuando se hace un commit desde producción, con este archivo automatizara
# procesos típicos para implementar los cambios.
#
# Nodejs y Bower se requiren para recursos como las fuentes

source _variables.sh

cd $PROJECT_ROOT

# Ejecutar git pull origin prod.
read -p "${GREEN}git pull origin ${BRANCH_PROD}? ${YELLOW}(y/[N]) ${RESTORE}" yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  git pull origin $BRANCH_PROD
fi

# Backup database
read -p "${GREEN}¿Backup database? ${YELLOW}(y/[N]) ${RESTORE}" yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  $CRON_ROOT/postgres_db_backup.sh
fi

# Ejecutar migrate.
read -p "${GREEN}¿Ejecutar migrate? ${YELLOW}(y/[N]) ${RESTORE}" yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  $PROJECT_ROOT/prod_manage.py migrate
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

# Eliminar directorio de collectstatic.
read -p "${GREEN}¿Eliminar directorio de collectstatic? ${YELLOW}(y/[N]) ${RESTORE}" yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  if [ -d $SRC_ROOT/staticfiles ]
  then
    rm -rf $SRC_ROOT/staticfiles
  fi
fi

# Ejecutar collectstatic.
read -p "${GREEN}¿Ejecutar collectstatic? ${YELLOW}(y/[N]) ${RESTORE}" yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  $PYTHON_EXEC $PROJECT_ROOT/prod_manage.py collectstatic
fi

# Reiniciar gunicorn.
read -p "${GREEN}¿Reiniciar gunicorn? ${YELLOW}(y/[N]) ${RESTORE}" yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  sudo systemctl restart gunicorn
fi
