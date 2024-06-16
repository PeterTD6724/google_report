from pathlib import Path
import os
from corsheaders.defaults import default_headers
from corsheaders.defaults import default_methods

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6w=7tbh5*!d4si=vidlnt9^si*%=hj8x@@s1_=d44tf4g+$%-8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'whitefreport.apps.WhitefreportConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'gcpdjreport.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "whitefreport/whitefreport/templates")],
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

WSGI_APPLICATION = 'gcpdjreport.wsgi.application'

CORS_ALLOW_HEADERS = (
    *default_headers,
    'accept',
    'authorization',
    'content-type',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'X-Content-Type-Options',
)

CORS_ALLOW_METHODS = (
    *default_methods,
    'GET',
    'HEAD',
    'POST',
    'PUT',
    'DELETE',
    'TRACE',
    'OPTIONS', 
    'PATCH',
)

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

SESSION_FILE_PATH = './whitef-data-b8eff.json'

CORS_ALLOW_ALL_ORIGINS = True

ACCESS_CONTROL_ALLOW_CREDENTIALS = True
ACCESS_CONTROL_ALLOW = True

ACCESS_CONTROL_ALLOW_ORIGIN = [
   'gs://whitefeather-json.appspot.com', 
   'https://whitefeather-json-default-rtdb.europe-west1.firebasedatabase.app'
]

CORS_ORIGIN_WHITELIST = [
    'gs://whitefeather-json.appspot.com', 
    'https://whitefeather-json-default-rtdb.europe-west1.firebasedatabase.app' 
]

CORS_ALLOWED_ORIGINS = [
   'gs://whitefeather-json.appspot.com',  
   'https://whitefeather-json-default-rtdb.europe-west1.firebasedatabase.app'
]

CORS_ORIGIN_ALLOW = [
   'gs://whitefeather-json.appspot.com',  
   'https://whitefeather-json-default-rtdb.europe-west1.firebasedatabase.app'
]

CSRF_TRUSTED_ORIGINS = [
    'gs://whitefeather-json.appspot.com',
    'https://whitefeather-json-default-rtdb.europe-west1.firebasedatabase.app'
    ]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "whitefreport/static")
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
