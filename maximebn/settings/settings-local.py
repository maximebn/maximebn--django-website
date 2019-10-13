from .settings import *
from decouple import config


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY_LOCAL')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG_LOCAL', default=False, cast=bool)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE_LOCAL'),         # Database engine
        'NAME': config('DB_NAME_LOCAL'),             # Database name
        'USER': config('DB_USER_LOCAL'),
        'PASSWORD': config('DB_PASSWORD_LOCAL'),        
    }
}


# Cache configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Information: PyUp tracking and deploying dependencies vulerabilities fixes automatically.
# https://pyup.io/