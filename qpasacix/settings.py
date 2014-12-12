"""
Django settings for qpasacix project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import dj_database_url#heroku

import dj_database_url#heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8j73$!$)@3m5ivnu!_y98j*^4#p7=rz=74twe+hh$*%7m1ogpu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'templates/'),
    )

ALLOWED_HOSTS = [
<<<<<<< HEAD
    '.herokuapps.com',
    '.heroku.com',
=======
    '*.heroku.com',
>>>>>>> 17b7d2d61d21dfe3f4a2748b9071af114d772ab0
    ]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fotos',
    'index',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'qpasacix.urls'

WSGI_APPLICATION = 'qpasacix.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}
DATABASES = {
      'default' : {
         'ENGINE' : 'django.db.backends.postgresql_psycopg2',
         'NAME' : 'db_name',
      }
}
#DATABASES = {
#      'default' : {
#         'ENGINE' : 'django.db.backends.postgresql_psycopg2',
#         'NAME' : 'db_name',
#      }
#}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-PE'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

##############################################################################
###para Heroku
#
import dj_database_url
#import os
#
if bool(os.environ.get('LOCAL_DEV', False)): 
  DATABASES = {
      'default' : {
         'ENGINE' : 'django.db.backends.postgresql_psycopg2',
         'NAME' : 'db_name',
         #setear USERNAME Y PASS si necesitan.
      }
  } 
else: 
  DATABASES = {
      'default' : dj_database_url.config(default='postrgres://localhost')
  }
#############################################################################