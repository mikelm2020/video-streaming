from .common import *
import os
from django.conf import settings
import dj_database_url

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = "RENDER" not in os.environ

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

DATABASES = {
    "default": dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default="postgres://test_database_ei4z_user:Bde0xNAr6z71bZvnFLpyvnsL8ieoo8Ka@dpg-ce54s7g2i3mjq974rsrg-a/test_database_ei4z",
        conn_max_age=600,
    )
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Tell Django to copy statics to the `staticfiles` directory
# in your application directory on Render.
STATIC_ROOT = os.path.join(settings.BASE_DIR, "staticfiles")

# Turn on WhiteNoise storage backend that takes care of compressing static files
# and creating unique names for each version so they can safely be cached forever.
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True