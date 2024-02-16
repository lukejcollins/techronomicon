"""
Django settings for techronomicon project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import boto3
from botocore.exceptions import NoCredentialsError

def get_parameter(name):
    # Create a session
    session = boto3.Session()

    # Create SSM client
    ssm = session.client('ssm', region_name='eu-west-1')

    try:
        response = ssm.get_parameter(Name=name, WithDecryption=True)
    except NoCredentialsError:
        return None

    return response['Parameter']['Value']

# Load environment variables from .env file for local development
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
if os.path.exists(env_path):
    with open(env_path) as file:
        for line in file:
            key, value = line.strip().split('=', 1)
            os.environ[key] = value

# Use the environment variable for the secret key
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY') if os.path.exists(env_path) else get_parameter('DJANGO_SECRET_KEY')

# AWS static setup
AWS_ACCESS_KEY_ID = os.environ.get('TECHRONOMICON_ACCESS_KEY_ID') if os.path.exists(env_path) else get_parameter('TECHRONOMICON_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('TECHRONOMICON_SECRET_ACCESS_KEY') if os.path.exists(env_path) else get_parameter('TECHRONOMICON_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('TECHRONOMICON_STORAGE_BUCKET_NAME') if os.path.exists(env_path) else get_parameter('TECHRONOMICON_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
#AWS_DEFAULT_ACL = 'public-read'

# Static files (CSS, JavaScript, images)
AWS_STATIC_LOCATION = 'static'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Check if the .env file exists to determine if we're in a local development environment
DEBUG = os.path.exists(env_path)

# Get EC2 IP
TECHRONOMICON_IP = os.environ.get('TECHRONOMICON_IP') if os.path.exists(env_path) else get_parameter('TECHRONOMICON_IP')

ALLOWED_HOSTS = [TECHRONOMICON_IP, 'lukecollins.dev', 'preprod.lukecollins.dev']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'techronomiblog',
    'markdownx',
    'markdownify',
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

ROOT_URLCONF = 'techronomicon.urls'

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

WSGI_APPLICATION = 'techronomicon.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('TECHRONOMICON_RDS_DB_NAME') if os.path.exists(env_path) else get_parameter('TECHRONOMICON_RDS_DB_NAME'),
        'USER': os.environ.get('TECHRONOMICON_RDS_USERNAME') if os.path.exists(env_path) else get_parameter('TECHRONOMICON_RDS_USERNAME'),
        'PASSWORD': os.environ.get('TECHRONOMICON_RDS_PASSWORD') if os.path.exists(env_path) else get_parameter('TECHRONOMICON_RDS_PASSWORD'),
        'HOST': os.environ.get('TECHRONOMICON_RDS_HOST') if os.path.exists(env_path) else get_parameter('TECHRONOMICON_RDS_HOST'),
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Set SSL header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
