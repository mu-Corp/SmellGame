#-*- coding: utf-8 -*-
"""
Django settings for SmellGame project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.translation import gettext_lazy as _
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_!tech41)94ulwd0e+o^bcf&0#bjj3b*=zixxm2q8ha(&1nnzm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

ADMINS = (
    ('Arnaud',  'arnaud.ferre.pro@gmail.com'),
    ('Florian', 'florian.thonier@gmail.com'),
    ('Jean',    'coquet.jean@gmail.com'),
    ('Lucas',   'lucas.lelann@gmail.com'),
    ('Nathan',  'nathan.foulquier.pro@gmail.com'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'SmellGuess',
    'SmellGift',
    'SmellGalaxy',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware', 
)

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.contrib.auth.context_processors.auth",
	"django.core.context_processors.i18n",
)

ROOT_URLCONF = 'SmellGame.urls'

WSGI_APPLICATION = 'SmellGame.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.sqlite3',
        'NAME'     : os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER'     : 'smellgame',
        'PASSWORD' : 'smellgame',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr-fr'
USE_I18N = True
USE_L10N = True
gettext = lambda x: x
LANGUAGES = (
    ('fr', _('Français')),
    ('en', _('Anglais')),
)
DEFAULT_LANGUAGE = 1

absoluteLocalePath = BASE_DIR + "/locale/"
LOCALE_PATHS = (
	absoluteLocalePath,
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
# Read the tuto !!! (http://fr.openclassrooms.com/informatique/cours/developpez-votre-site-web-avec-le-framework-django/les-templates-3)

STATIC_URL = '/assets/'
#STATIC_URL = '/static/'

absoluteStaticPath = BASE_DIR + "/assets/" #effective for everybody (see / or \ maybe...)
STATICFILES_DIRS = (
        absoluteStaticPath,
        #'/home/cridev/webapps/smellofus_static/',
)
STATIC_ROOT = '/home/cridev/webapps/smellofus_static/' # modify for webfactional static app


# Directory of templates
relativeTemplatePath = BASE_DIR + "/templates/" #effective for everybody (see / or \ maybe...)
TEMPLATE_DIRS = (
                 relativeTemplatePath,
)


APPEND_SLASH = True  # Ajoute un slash en fin d'URL

