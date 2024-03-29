"""
Django settings for rbscience project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xb6$@(*o1q#+^*fxfzs4!@of9(#x627_5m4+q(7jf!9*)w!36r'

# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = False
import os
print(os.environ.get('enviorment'))
if os.environ.get('enviorment') == 'production':
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    'home',
    'about',
    'artical',
    'blogs',
    'services',
    'team',
    'research',
    'superuser',
    'livereload',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'superuser.middleware.simple_middleware',
    'livereload.middleware.LiveReloadScript',
]

ROOT_URLCONF = 'rbscience.urls'

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
                'home.context_processors.regfunc'
            ],
        },
    },
]

WSGI_APPLICATION = 'rbscience.wsgi.application'
CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
    },
}
CKEDITOR_UPLOAD_PATH = 'content/ckeditor/'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db1.sqlite3',
    },
    # 'default':{
    #     'ENGINE': 'mysql.connector.django',
    #     'NAME': 'rbscience',
    #     'USER': 'root',
    #     'PASSWORD': '',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    # }
    # 'default':{
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'Rbscience',
    #     'USER': 'rbscience',
    #     'PASSWORD': 'Flax@2021',
    #     'HOST': '184.168.112.236',
    #     'PORT': '3306',
    # }
}
if os.environ.get('enviorment') == 'production':
    DATABASES['default'] = {
        
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Rbscience',
        'USER': 'rbscience',
        'PASSWORD': 'Flax@2021',
        'HOST': 'localhost',
        'PORT': '3306',
    
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

import socket

try:
    HOSTNAME = socket.gethostname()
except:pass

# if 'desktop' in HOSTNAME.lower():
#     HOST_ADDR = 'http://localhost:8000'
#     EMAIL_USE_TLS = True
#     EMAIL_HOST = 'smtp.gmail.com'
#     EMAIL_PORT = 587
#     EMAIL_HOST_USER = 'ritik.cyberflax@gmail.com'
#     EMAIL_HOST_PASSWORD = 'cqhmcpmptleeeqqz'
# else:
#     HOST_ADDR = 'http://'+HOSTNAME
#     EMAIL_HOST_USER = 'sales@rbscience.co.in'
#     EMAIL_HOST_PASSWORD = 'Flax@2021'
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT =  BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
CKEDITOR_UPLOAD_PATH = 'uploads/' 

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
