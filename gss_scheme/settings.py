import os
from pathlib import Path
import environ
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = 'a14fcabb-36a9-4bb1-bf3c-e7d78f2dfc21'
DEBUG = True

# Render provides RENDER_EXTERNAL_HOSTNAME automatically


RENDER_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "mpgss-ycle.onrender.com",
    "mpgss.org",
    "www.mpgss.org",
]

if RENDER_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_HOSTNAME)


# APPLICATIONS
INSTALLED_APPS = [
   # "jazzmin",
    "storages",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "institutions",
    "applications",
    "finance",

    "crispy_forms",
    "crispy_bootstrap5",
    "widget_tweaks",

    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.linkedin_oauth2",
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)


# Cloudflare R2 credentials (store securely in environment variables!)
AWS_ACCESS_KEY_ID = "f0a97eed388f189a31045f485e7cef9d"
AWS_SECRET_ACCESS_KEY = "R8240559df5b6f847bbee214393b782583b7b84a229577b421b59b4a1573de7b1"

# Your Cloudflare account ID (from R2 dashboard)
CLOUDFLARE_ACCOUNT_ID = "0f71abb008d0d253aaca4b2507969384"

# R2 endpoint (S3-compatible)
AWS_S3_ENDPOINT_URL = f"https://https://0f71abb008d0d253aaca4b2507969384.r2.cloudflarestorage.com"

# Bucket name
AWS_STORAGE_BUCKET_NAME = "mpgss-docs"


# Optional: make uploaded files public
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH = False

MEDIA_URL = f"https://0f71abb008d0d253aaca4b2507969384.r2.cloudflarestorage.com/mpgss-docs/"


SITE_ID =1

CSRF_TRUSTED_ORIGINS = [
    "https://mpgss-ycle.onrender.com",
    "https://mpgss.org",
    "https://www.mpgss.org",
]


# ALLAUTH
ACCOUNT_LOGIN_METHODS = {"email", "username"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "username*", "password1*", "password2*"]
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "/login/"
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "/login/"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
SITE_URL = "https://mpgss-ycle.onrender.com"

# MIDDLEWARE
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "gss_scheme.urls"
WSGI_APPLICATION = "gss_scheme.wsgi.application"

# DATABASE (Render PostgreSQL)
DATABASES = {
    "default": dj_database_url.config(
        default="postgresql://mpgss_admin:ZPMatQoubfADwKXEYbJhK0NdRKPVrhKn@dpg-d5lgobh4tr6s73bulvrg-a/mpgss_db",
        conn_max_age=600,
        ssl_require=True,
    )
}

# TEMPLATES
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "applications.context_processors.user_context",
                "applications.context_processors.application_status",
            ],
        },
    },
]

# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# REDIS CACHE (Render Redis)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
    }
}

STORAGES = {
    "staticfiles": {
        "BACKEND": "applications.storage.NonStrictManifestStaticFilesStorage",
    },
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
}



EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "mail.privateemail.com"
EMAIL_PORT = 587

# TLS recommended for Namecheap
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

EMAIL_HOST_USER = "notification@mpgss.org"         # full email address
EMAIL_HOST_PASSWORD = "admin@2026"  # mailbox password

# INTERNATIONALIZATION
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Pacific/Port_Moresby"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# STATIC FILES
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = []
if (BASE_DIR / "static").exists():
    STATICFILES_DIRS = [BASE_DIR / "static"]




# MEDIA
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/apply/"
LOGOUT_REDIRECT_URL = "/"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# PDF API
#TWO_PDF_API_KEY = env("TWO_PDF_API_KEY", default="")
#TWO_PDF_API_URL = env("TWO_PDF_API_URL", default="https://api.2pdf.com/fill")

# CELERY
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE
CELERY_ENABLE_UTC = True


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