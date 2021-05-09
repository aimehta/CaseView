"""
Django settings for cv project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import datetime
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p7f=wdh0eoo2m=!o0uf3#ton!_36dn=jkl3+0(4a$9z(#kr%fu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = (
    'cv_api',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'cv.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'cv.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
REST_FRAMEWORK = {
'DEFAULT_PERMISSION_CLASSES': (
'rest_framework.permissions.IsAuthenticated',
),
'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
'DEFAULT_AUTHENTICATION_CLASSES': (
'rest_framework.authentication.SessionAuthentication',
'rest_framework.authentication.BasicAuthentication',
'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
),
'DEFAULT_RENDERER_CLASSES': (
'rest_framework.renderers.JSONRenderer',
),
}

# Dangerous to expose all headers but for interview ok to do and make it simple for intervier
CORS_EXPOSE_HEADERS = (
#'Access-Control-Allow-Origin: *',
#'CORS_ORIGIN_ALLOW_ALL = True',
'Access-Control-Allow-Methods: GET, POST, PUT, DELETE',
'Access-Control-Allow-Headers": "Content-Type,X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Date, X-Api-Version, X-File-Name, Authorization',
)

LOGGING = {
'version': 1,
'formatters': {
'verbose': {
'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
},
'simple': {
'format': '%(levelname)s %(message)s'
},
},
'handlers': {
'console': {
'level': 'DEBUG',
'class': 'logging.StreamHandler',
'formatter': 'simple'
},
'file': {
'level': 'ERROR',
'class': 'logging.FileHandler',
'filename': '/var/log/cv.log',
'formatter': 'simple'
},
},
'loggers': {
'django': {
'handlers': ['file'],
'level': 'DEBUG',
'propagate': True,
},
}
}

JWT_AUTH = {
# 'JWT_ENCODE_HANDLER' : 'jwt_auth.utils.jwt_encode_handler',
# 'JWT_DECODE_HANDLER' : 'jwt_auth.utils.jwt_decode_handler',
# 'JWT_PAYLOAD_HANDLER' : 'jwt_auth.utils.jwt_payload_handler',
# 'JWT_PAYLOAD_GET_USER_ID_HANDLER' : 'jwt_auth.utils.jwt_get_user_id_from_payload_handler',
'JWT_SECRET_KEY' : 'SECRET_KEY',
'JWT_ALGORITHM' : 'HS256',
'JWT_VERIFY' : True,
'JWT_VERIFY_EXPIRATION' : True,
'JWT_LEEWAY' : 0,
'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=1),
'JWT_ALLOW_REFRESH' : False,
'JWT_REFRESH_EXPIRATION_DELTA' : datetime.timedelta(days=1),
'JWT_AUTH_HEADER_PREFIX' : 'JWT',
'JWT_RESPONSE_PAYLOAD_HANDLER' : 'cv_api.jwtresponse.jwt_response_payload_handler'
}

