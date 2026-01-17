"""
Django settings for gss_scheme project.

Based on 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import posixpath
from pathlib import Path
import environ

env = environ.Env()
environ.Env.read_env()  # reads from a .env file if present

BASE_DIR = Path(__file__).resolve().parent.parent
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY", default="unsafe-dev-key")
DEBUG = env.bool("DJANGO_DEBUG", default=True)
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["127.0.0.1", "localhost"])

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
   


    # Add your apps here to enable them
    "jazzmin",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'institutions',
    'applications',
    'finance',

    'crispy_forms',
    'crispy_bootstrap5',

    'widget_tweaks',

#Authentication
'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.linkedin_oauth2',
   # 'allauth.socialaccount.providers.facebook',
]
# --- Allauth ---
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = env.int("SITE_ID", default=1)

# django-allauth (NEW settings format)

ACCOUNT_LOGIN_METHODS = {"email", "username"}

ACCOUNT_SIGNUP_FIELDS = [
    "email*",
    "username*",
    "password1*",
    "password2*",
]
# Require verification before login
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

# Send email confirmation email on signup
ACCOUNT_EMAIL_REQUIRED = True

# Auto-confirm immediately when user clicks the link (no extra "Confirm" button page)
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

# After confirming email, redirect here (login page)
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "/login/"
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "/login/"


LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
SITE_URL = env("SITE_URL", default="http://127.0.0.1:8000")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="noreply@gsss.com")
# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

ROOT_URLCONF = 'gss_scheme.urls'



WSGI_APPLICATION = 'gss_scheme.wsgi.application'
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Add this line
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'applications.context_processors.user_context',
                'applications.context_processors.application_status',

            ],
        },
    },
]

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
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

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
    }
}

# Default Django email settings (development)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "no-reply@example.com"

# AWS SES SMTP endpoint (region-specific)
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'   # change to your SES region
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Credentials from AWS SES (SMTP username & password)
EMAIL_HOST_USER = 'AKIAZD3ZOJ6U4FHL6LP4'
EMAIL_HOST_PASSWORD = 'BMmpMkFMRadufGfjV9WEqM1hBSzp0tLn1lbbQMmDAtTx'

# Default sender
DEFAULT_FROM_EMAIL = 'noreply@mpgss.org'


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True

TIME_ZONE = "Pacific/Port_Moresby"
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = "/apply/"
LOGOUT_REDIRECT_URL = "/"


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

TWO_PDF_API_KEY = env('TWO_PDF_API_KEY', default='')
TWO_PDF_API_URL = env('TWO_PDF_API_URL', default='https://api.2pdf.com/fill')

DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
#GS_BUCKET_NAME = env("gssstorage")

# settings.py

JAZZMIN_SETTINGS = {
    "site_title": "Gerson Solulu Scholarship Admin",
    "site_header": "GSSS Administration",
    "site_brand": "GSSS",
    "welcome_sign": "Welcome to the Gerson Solulu Scholarship Dashboard",
    "copyright": "2025 Gerson Solulu Scholarship Scheme",

    "site_icon": "img/logo.png",

    # Global search across key models
    "search_model": [
        "applications.ApplicantProfile",
        "applications.Application",
        "applications.ApplicationReview",
        "applications.News",
    ],

    # Top menu links
    "topmenu_links": [
        {"name": "Home", "url": "applications:home", "permissions": ["auth.view_user"]},
        {"name": "Apply", "url": "applications:apply"},
        {"name": "About", "url": "applications:about"},
    ],

    # User menu links
    "usermenu_links": [
        {"name": "Profile", "url": "admin:auth_user_change", "permissions": ["auth.change_user"]},
    ],

    "show_sidebar": True,
    "navigation_expanded": True,

    # Icons for apps and models
    "icons": {
        "auth": "fas fa-users-cog",
        "applications.ApplicantProfile": "fas fa-id-card",
        "applications.Application": "fas fa-file-signature",
        "applications.ApplicationReview": "fas fa-clipboard-check",
        "applications.News": "fas fa-newspaper",
        "applications.FAQ": "fas fa-question-circle",
        "applications.PolicyPage": "fas fa-balance-scale",
             # Authentication & Authorization
        "auth.User": "fas fa-user",              # 👤 individual user
        "auth.Group": "fas fa-users",            # 👥 groups of users

        # Finance app
        "finance.Payment": "fas fa-money-check-alt",  # 💳 payments

        # Institutions app
        "institutions.Course": "fas fa-book-open",    # 📖 courses
        "institutions.Institution": "fas fa-university",  # 🎓 institution name

        # Social accounts
        "socialaccount.SocialAccount": "fas fa-share-alt",       # 🔗 linked social accounts
        "socialaccount.SocialApp": "fas fa-plug",                # 🔌 social applications
        "socialaccount.SocialToken": "fas fa-key",
    },

    # Theme and customization
    "theme": "default",
    "custom_css": "css/gss_admin.css",
    "custom_js": "js/gss_admin.js",
    "show_ui_builder": True,
}


JAZZMIN_UI_TWEAKS = {
    "navbar": "navbar-dark bg-primary",
    "sidebar": "sidebar-dark-primary",
    "theme": "cosmo",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn btn-primary",
        "secondary": "btn btn-secondary",
    },
}

# Celery (recommended using Redis)
CELERY_BROKER_URL = env("CELERY_BROKER_URL", default="redis://127.0.0.1:6379/0")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND", default="redis://127.0.0.1:6379/0")

CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

CELERY_TIMEZONE = TIME_ZONE
CELERY_ENABLE_UTC = True


