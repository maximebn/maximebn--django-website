"""
Django settings for maximebn project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/

Using Python Decouple for environment variables handling: cf. doc, config and settings.ini file
"""

import os
from os.path import abspath, basename, dirname, join, normpath
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# URL configuration
ROOT_URLCONF = 'maximebn.urls'

# Application definition

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'widget_tweaks',
    'blog',
    'stories',
    'contact',
    'annexes',
    'easy_thumbnails',
    'coverage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'csp.middleware.CSPMiddleware',
    ]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':  [
            # Cette ligne ajoute le dossier templates/ à la racine du projet
            os.path.join(DJANGO_ROOT, 'templates'),
        ],
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

# WebServer Gateway interface configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'maximebn.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 12,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#-----------------------------------------------------------------------
# ------------ STATIC FILES CONFIGURATION ------------------------------
# ----------------------------------------------------------------------

# Static files (CSS, JavaScript, Images) configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

#-----------------------------------------------------------------------
# ------------ STATIC FILES CONFIGURATION : END ------------------------
# ----------------------------------------------------------------------



# Media configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# Email backend configuration
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
SERVER_EMAIL = config('SERVER_EMAIL', default='')

# Manager configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
ADMINS = (
    (config('ADMIN_NAME', default=''), config('ADMIN_EMAIL', default='')),
)
MANAGERS = ADMINS

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = 'fr-FR'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Information: PyUp tracking and deploying dependencies vulerabilities fixes automatically.
# https://pyup.io/

FRAME_SRC=['openstreetmap.org']

