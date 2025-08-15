from decouple import config
from .common import MODE

if MODE == "dev":
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = config(
        "ALLOWED_HOSTS", default=None, cast=lambda v: [s.strip() for s in v.split(",")]
    )

# CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", default="*")

# CSRF_COOKIE_SECURE = config("CSRF_COOKIE_SECURE", default=False, cast=bool)

# SESSION_COOKIE_SECURE = config("SESSION_COOKIE_SECURE", default=False, cast=bool)

# SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", default=False, cast=bool)


AUTHENTICATION_BACKENDS = [
    "graphql_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
]
