Estructura que utilizo para crear practicas con Django con una base ya hecha.

En prodcción requiere de `Nodejs` y `bower` por los recursos, pero los archivos que se generan
com `gulpfile.js` en dev, los pasa a prod, por lo que no require de "compilación".

De manera predeterminada utiliza django-apps, algunas apps que uso en varios proyectos.

# Instalación

Crear un entorno virtual con ``virtualenvwrapper`` y crear el proyecto.

    # Clonar.
    cd ~/projects
    git clone git@github.com:snicoper/django-boilerplate.git

    # Crear proyecto nuevo.
    django-admin.py startproject --template=https://github.com/snicoper/django-boilerplate/archive/master.zip nombre_proyecto
    cd nombre_proyecto/

    # requirements
    pip install -r requirements/(local|prod).txt

## Añadir postactivate y postdeactivate al env (opcional)

Esto es para comodidad, para los scripts dentro del directorio ``./bin/``

Activar el entorno virtual y editar ``postactivate`` y ``postdeactivate``.

**postactivate**

    workon nombre_proyecto

    vim $VIRTUAL_ENV/bin/postactivate

    # Añadir
    source ~/projects/nombre_proyecto/bin/postactivate.sh

    deactivate
    workon nombre_proyecto

**postdeactivate**

    vim $VIRTUAL_ENV/bin/postdeactivate

    # Añadir
    source ~/projects/nombre_proyecto/bin/postdeactivate.sh

Luego cualquier archivo de ``./bin/`` se podrá ejecutar desde cualquier ruta.

TODO: Poner lista de archivos ``./bin/``

A parte, una vez entrado al entorno, se podrá hacer ``cd_project`` para ir al directorio raíz del
proyecto o ``cd_apps`` para ir al directorio raíz de las **apps**.

## Migración y súper usuario (desarrollo)

Por defecto usa **SQLite**, editar ``./src/config/settings/local.py`` para editar los datos de conexión.

    ./manage.py migrate
    ./manage.py createsuperuser

## manage_prod.py y manage_test.py

Para no tener que estar cambiando con ``./manage.py command --settings=archivo.settings``, hay 3
archivos ``manage``, cada uno de ellos apunta al archivo ``settings`` que corresponde.

* ``manage.py``: Para desarrollo.
* ``prod_manage.py``: Para producción.
* ``test_manage.py``: Para tests.

## Node

Editar ``./.package.json`` para los paquetes de **nodejs**

    npm install

### gulpfile.js

* ``gulp``: Unifica y minifica los archivos ``.js`` y ``.scss``
* ``gulp watches``: Unifica, minifica y escucha archivos ``.js`` y ``.scss``
* ``gulp watch:styles``: Unifica, minifica y escucha archivos ``.scss``
* ``gulp watch:scripts``: Unifica, minifica y escucha archivos ``.js``

## Bower

    bower install

## Reinstalar en desarrollo.

Para una reinstalación rápida en la etapa de desarrollo (**solo PostgreSQL**).

Editar ``src/config/settings/local.py`` la conexión a **PostgreSQL**

Editar las variables del archivo ``bin/_variables.sh``.

Ejecutar ``reinstall_dev.sh``.

## Reload prod.

En desarrollo usar, ``reload_prod.sh``

TODO: Documentar mejor el README.md
