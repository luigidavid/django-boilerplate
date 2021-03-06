Estructura que utilizo para crear practicas con Django con una base ya hecha.

Requiere Django >= 1.11 y Python 3.

# Instalación

Crear un entorno virtual con `virtualenvwrapper` y crear el proyecto.

Clonando el proyecto.

    cd ~/projects
    git clone git@github.com:snicoper/django-boilerplate.git

De esta manera se ha de generar [secret_key](http://www.miniwebtool.com/django-secret-key-generator/)
en los archivos `src/config/settings/(local,prod,test).py`

Usando `startproject --template=`.

    django-admin.py startproject --template=https://github.com/snicoper/django-boilerplate/archive/master.zip nombre_proyecto
    cd nombre_proyecto/

Requirements.

    # requirements
    pip install -r requirements/(local|prod).txt

Renombrar `src/apps/utils/templatetags/utils_tags.txt` a `src/apps/utils/templatetags/utils_tags.py`

    mv src/apps/utils/templatetags/utils_tags.txt src/apps/utils/templatetags/utils_tags.py

Al usar `startproject`, con `utils_tags.py` siempre me da el error `django.template.exceptions.TemplateSyntaxError: Invalid filter: 'markdown'`.
No he sabido solucionarlo y renombrarlo a `.txt` me ha solucionado el problema.

## Añadir postactivate y postdeactivate al env (opcional)

Esto es para comodidad, para los scripts dentro del directorio `bin`

Activar el entorno virtual y editar `postactivate` y `postdeactivate`.

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

Luego cualquier archivo de `bin` se podrá ejecutar desde cualquier ruta.

**TODO:** Poner lista de archivos `bin`

Una vez entrado al entorno, se podrá hacer `cd_project` para ir al directorio raíz del
proyecto o `cd_apps` para ir al directorio raíz de las **apps**.

## Migración y súper usuario (desarrollo)

Por defecto usa **SQLite**, editar `./src/config/settings/local.py` para editar los datos de conexión.

    ./manage.py migrate
    ./manage.py createsuperuser

## manage_prod.py y manage_test.py

Para no tener que estar cambiando con `./manage.py command --settings=archivo.settings`, hay 3
archivos `manage`, cada uno de ellos apunta al archivo `settings` que corresponde.

* `manage.py`: Para desarrollo.
* `prod_manage.py`: Para producción.
* `test_manage.py`: Para tests.

## Node

Editar `./package.json` para los paquetes de **nodejs**

    npm install

### gulpfile.js

* `gulp`: Unifica y minifica los archivos `.js` y `.scss` desarrollo y producción.
* `gulp watches`: Unifica, minifica y escucha archivos `.js` y `.scss` en desarrollo locales.
* `gulp watch:styles`: Unifica, minifica y escucha archivos `.scss` en desarrollo locales.
* `gulp watch:scripts`: Unifica, minifica y escucha archivos `.js` en desarrollo locales.

## Reinstalar en desarrollo.

Para una reinstalación rápida en la etapa de desarrollo (**solo PostgreSQL**).

Editar `src/config/settings/local.py` la conexión a **PostgreSQL**

Editar las variables del archivo `bin/_variables.sh`.

Ejecutar `reinstall_dev.sh`.

## Reload prod.

En desarrollo usar, `reload_prod.sh`

**TODO:** Documentar mejor el README.md
