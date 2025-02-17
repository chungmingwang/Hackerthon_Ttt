"""
Django settings for discussion_forum project.

Generated by 'django-admin startproject' using Django 2.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from decouple import config, Csv
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #added built-in app
    'django.contrib.humanize',

    #custom internal app
    'boards',   
    'user_account',

    #external app
    'mdeditor',
    'django_toggle_switch_widget',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'discussion_forum.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            #for template tags anf filter shared for all apps in projects
            'libraries':{
                'custom_tags_filters': 'templatetags.templatetags_filter',
            },
        },
    },
]

WSGI_APPLICATION = 'discussion_forum.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True  


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/' # url prefix where static files will be hosted

#where django will search for static files other than app directories
STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]

#where static files will be stored after collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'staticroot')

#adding default django authentication backend
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',]

#logout redirect url name
LOGOUT_REDIRECT_URL = 'home_url'

#login redirect url name i.e. after login
LOGIN_REDIRECT_URL = 'home_url'

#login url name for login required stuff
LOGIN_URL = 'login_url'

#email settings 
EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST', default='localhost')  #default as in docs
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)    #same
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='') #same
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='') #same
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)   #same
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='webmaster@localhost' ) #django default

#media root where all uploaded files will be stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

#media url to serve media files from media_root
MEDIA_URL = '/media/'

#paginate_by values
BOARD_PAGINATE_BY = 10
TOPIC_PAGINATE_BY = 10
POST_PAGINATE_BY = 10

#sendgrid api key
SENDGRID_API_KEY = config('SENDGRID_API_KEY', default='')