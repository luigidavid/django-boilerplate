# flake8: noqa
from .base import *

# Añadir ~/tests a PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(BASE_DIR), 'tests'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

ALLOWED_HOSTS = ['127.0.0.1']

INTERNAL_IPS = ['127.0.0.1']

# Application definition
THIRD_PARTY_APPS += ()

LOCAL_APPS += ()

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.test.sqlite3'),
    }
}

# Media
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-MEDIA_ROOT

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/test')

# Emails
DEFAULT_FROM_EMAIL = 'snicoper@snicoper.local'

# Admins
ADMINS = (
    ('snicoper', 'snicoper@snicoper.local'),
)

# Grupos de email.
GROUP_EMAILS = {
    "NO-REPLY": 'no-responder@snicoper.local <snicoper@snicoper.local>',
    'CONTACTS': (
        'Salvador Nicolas <snicoper@snicoper.local>',
    ),
}

# SMTP
EMAIL_USE_TLS = True
EMAIL_HOST = 'mail.snicoper.local'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'snicoper'
EMAIL_HOST_PASSWORD = '123456'
