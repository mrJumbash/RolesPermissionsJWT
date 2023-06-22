# Imports
import os
from pathlib import Path
from .env_reader import env

# BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# PROJECT_ROOT
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Production
PRODUCTION = env("PRODUCTION", default=False, cast=bool)


# Application definition

# COMMON_APPS
COMMON_APPS = [
    "common.apps.AuthAdminConfig",
]

# LOCAL_APPS
LOCAL_APPS = ["common", "service"]

THIRD_PARTY_APPS = ["rest_framework", "chartjs"]

THEME_APPS = [
    "jazzmin",
]


INSTALLED_APPS = [
    *THEME_APPS,
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
    *COMMON_APPS,
]

# MIDDLEWARE
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

LANGUAGE_CODE = "ru-RU"


TIME_ZONE = "Asia/Bishkek"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files
STATIC_URL = "/back_static/"
STATIC_ROOT = os.path.join(BASE_DIR, "back_static")


# Media files
MEDIA_URL = "/back_media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "back_media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# rest_framework
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
}


# jazzmin settings importing
from .theme import *

if not PRODUCTION:
    from .local import *
else:
    from .production import *
