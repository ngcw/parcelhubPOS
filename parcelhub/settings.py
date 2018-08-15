"""
Django settings for parcelhub project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.conf import settings
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*w1#s!3=20hitaq2@$cf_$83ge41u7pf!$%p4v4p@!rxm2#nad'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'parcelhubPOS.apps.ParcelhubposConfig',
    'parcelhubWeb.apps.ParcelhubwebConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'menu',
    'django_tables2',
    'import_export',
]

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': [os.path.join(BASE_DIR, 'var/backups'), ]}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'parcelhub.urls'
LOGIN_URL = '/parcelhubPOS/'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'parcelhubPOS/templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'parcelhub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
import dj_database_url
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'parcelhubPOS',
        'USER': 'postgres',#'USER': 'admin',#'USER': 'ngcw',
        'PASSWORD': 'bakayar00',#'PASSWORD': 'admin1234',#'PASSWORD': 'bakayar00',
        'HOST': '127.0.0.1',#'HOST': 'localhost',#'HOST': '127.0.0.1',
        'PORT': '5433',#'PORT': '',#'PORT': '5432',
        'CONN_MAX_AGE': 500,
    },
  
    'remote': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dd5rr9lejh7scj',
        'USER': 'clrfmpcbsyagpe',
        'PASSWORD': '4e3a445b90fa2a83fb3176f04508e8398f0dca737b649ca83d411a5aae3ca538',
        'HOST': 'ec2-54-235-210-115.compute-1.amazonaws.com',
        'PORT': '5432',
        'CONN_MAX_AGE': 500,
    }
}
db_from_env = dj_database_url.config(conn_max_age=500)

DATABASES['default'].update(db_from_env)
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#Session engine
SESSION_ENGINE = "django.contrib.sessions.backends.file"
#Excel file upload
FILE_UPLOAD_HANDLERS = ("django_excel.ExcelMemoryFileUploadHandler",
                        "django_excel.TemporaryExcelFileUploadHandler")

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kuala_Lumpur'

USE_I18N = True

USE_L10N = False

USE_TZ = False
SHORT_DATETIME_FORMAT = 'd/m/Y P'
DATETIME_FORMAT = 'd/m/Y P'
DATE_FORMAT = 'd/m/Y'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

IMPORT_EXPORT_USE_TRANSACTIONS = True
LOGIN_REDIRECT_URL = 'parcelhubPOS/login'
DATA_UPLOAD_MAX_NUMBER_FIELDS = 100000000
