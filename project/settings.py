"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os, locale
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$-cpsqf1!+sdxm9wyr^$2wzz1xg#d^$riv*&sdqd!cj@mz%fz2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'tinymce',
    'sorl.thumbnail',
    'accounts.apps.AccountsConfig',
    'company.apps.CompanyConfig',
    'homepage.apps.HomepageConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates/',],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Substituting a custom User model
# https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#substituting-a-custom-user-model

AUTH_USER_MODEL = 'accounts.User'


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'fa'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [BASE_DIR / 'locale/',]

locale.setlocale(locale.LC_ALL, 'fa_IR.UTF-8')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'assets/',]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Content Security Policy settings
# https://django-csp.readthedocs.io/en/latest/configuration.html

CSP_DEFAULT_SRC = ["'self'", "'unsafe-inline'"]
CSP_IMAGE_SRC = ["'self'", "'unsafe-inline'", "https://www.google-analytics.com"]
CSP_STYLE_SRC = ["'self'", "'unsafe-inline'"]
CSP_STYLE_SRC_ELEM = ["'self'", "'unsafe-inline'", "https://fonts.googleapis.com", "https://cdn.jsdelivr.net"]
CSP_SCRIPT_SRC = ["'self'", "'unsafe-inline'"]
CSP_SCRIPT_SRC_ELEM = ["'self'", "'unsafe-inline'", "https://cdn.jsdelivr.net"]
CSP_FONT_SRC = ["'self'", "data:", "https://fonts.googleapis.com", "https://fonts.gstatic.com"]
CSP_CONNECT_SRC = ["'self'", "https://www.google-analytics.com"]
CSP_FRAME_SRC = ["'self'"]


# Cors Headers settings
# https://pypi.org/project/django-cors-headers/

CORS_ALLOWED_ORIGINS = [
    'https://artanetwork.ir',
    'https://www.artanetwork.ir',
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]


# sorl-thumbnail settings
# https://sorl-thumbnail.readthedocs.io/en/latest/index.html

THUMBNAIL_PADDING_COLOR = 'rgba(0, 0, 0, 0)'


# django-filebrowser settings
# https://django-filebrowser.readthedocs.io/en/latest/

FILEBROWSER_MAX_UPLOAD_SIZE = 20971520


# django-tinymce settings
# https://django-tinymce.readthedocs.io/en/latest/

TINYMCE_FILEBROWSER = True
TINYMCE_DEFAULT_CONFIG = {
    'menubar': False,
    'width': '850',
    'skin': 'tinymce-5',
    'plugins': 'autolink directionality lists advlist media table image link',
    'toolbar1': '''
        styles fontfamily fontsize | forecolor backcolor | bold italic underline | outdent indent | removeformat
    ''',
    'toolbar2': '''
        rtl ltr | alignright aligncenter alignleft alignjustify | bullist numlist | link unlink | image media | table
    ''',
}


# Production settings

if os.getenv('DEBUG') == 'false':

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/5.0/howto/static-files/

    STATIC_ROOT = '/usr/src/app/staticfiles/'
    MEDIA_ROOT = '/usr/src/app/media/'

    # Database
    # https://docs.djangoproject.com/en/5.0/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASS'),
        }
    }

    # SSL/HTTPS settings
    # https://docs.djangoproject.com/en/5.0/topics/security/#ssl-https

    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
