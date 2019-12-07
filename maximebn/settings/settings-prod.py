from .settings import *
from decouple import config
import re


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY_PROD')
DEBUG = config('DEBUG_PROD', default=False, cast=bool)

INSTALLED_APPS += [
    'gunicorn',
]

STATIC_ROOT = normpath(join(SITE_ROOT, 'static'))

# Allowed hosts for production environment, must be suitable value
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
ALLOWED_HOSTS = ['51.15.140.89', 'maximebn.com', 'www.maximebn.com']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE_PROD'),         # Database engine
        'NAME': config('DB_NAME_PROD'),             # Database name
        'USER': config('DB_USER_PROD'),
        'PASSWORD': config('DB_PASSWORD_PROD'),    
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'TEST': {
            'NAME': 'test_maximebnProject',
        },
    }
}

# Cache configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND':  'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 600,
        'OPTIONS': {
            'MAX_ENTRIES': 100
        }
    }
}

#-------------------------------------------------------------------------------
# Additionnal security settings
# ------------------------------------------------------------------------------

# Sensitive data exposure
# https://docs.djangoproject.com/en/2.1/ref/middleware/#http-strict-transport-security

# SECURE_HSTS_SECONDS = 3600 # 1 heure,to me modified after validation
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SECURE_SSL_REDIRECT= True

# Click-jacking protection : X-frame middleware setting header option to deny loading resource within a frame
# https://docs.djangoproject.com/en/2.1/ref/clickjacking/

# X_FRAME_OPTIONS = 'DENY'

# XSS filtering protection enabled on web browsers (+ Django templates escaping specific characters)
# https://docs.djangoproject.com/en/2.1/ref/clickjacking/

# SECURE_BROWSER_XSS_FILTER  = True

# Cookie sessions protection, forcing cookies to be shared by HTTPS
# https://docs.djangoproject.com/en/2.1/topics/http/sessions/

# to activate SESSION_COOKIE_SECURE = True
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# Information: PyUp tracking and deploying dependencies vulerabilities fixes automatically.
# https://pyup.io/

IGNORABLE_404_URLS = (
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
)