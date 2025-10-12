import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR.parent / ".env"

LOAD_DOTENV = os.getenv("LOAD_DOTENV", "false").lower() in {
    "1", "true", "yes", "on"
}

if LOAD_DOTENV and ENV_FILE.exists():
    with ENV_FILE.open() as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


def env_required(name: str) -> str:
    v = os.getenv(name)
    if not v:
        raise RuntimeError(f"{name} must be set")
    return v


def env_bool_required(name: str) -> bool:
    v = env_required(name).lower()
    return v in {"1", "true", "yes", "on"}


def env_list_required(name: str):
    v = env_required(name)
    return [x.strip() for x in v.split(",") if x.strip()]


SECRET_KEY = env_required("SECRET_KEY")
DEBUG = env_bool_required("DEBUG")
HOST = env_required("HOST")
ALLOWED_HOSTS = env_list_required("ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = env_list_required("CSRF_TRUSTED_ORIGINS")
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "techronomiblog",
    "markdownx",
    "markdownify",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "techronomicon.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "techronomicon.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": env_required("DB_HOST"),
        "PORT": env_required("DB_PORT"),
        "NAME": env_required("DB_NAME"),
        "USER": env_required("DB_USER"),
        "PASSWORD": env_required("DB_PASSWORD"),
    }
}

if not DEBUG and DATABASES["default"]["ENGINE"].endswith("sqlite3"):
    raise RuntimeError("SQLite not allowed in production")

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation."
        "MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation."
        "CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation."
        "NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "staticfiles": {
        "BACKEND": (
            "whitenoise.storage.CompressedManifestStaticFilesStorage"
        )
    },
}

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
