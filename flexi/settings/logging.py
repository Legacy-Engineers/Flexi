from .common import BASE_DIR
import os

BASE_LOG_DIR = BASE_DIR / "logs"
os.makedirs(BASE_LOG_DIR, exist_ok=True)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "console",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_LOG_DIR / "flexi.log",
            "maxBytes": 1024 * 1024 * 10,  # 10MB
            "backupCount": 5,
            "level": "INFO",
            "formatter": "file",
        },
        "error_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_LOG_DIR / "error.log",
            "maxBytes": 1024 * 1024 * 10,  # 10MB
            "backupCount": 5,
            "level": "ERROR",
            "formatter": "file",
        },
        "security_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_LOG_DIR / "security.log",
            "maxBytes": 1024 * 1024 * 5,  # 5MB
            "backupCount": 3,
            "level": "WARNING",
            "formatter": "security",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["console", "file", "error_file"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.security": {
            "handlers": ["console", "security_file"],
            "level": "WARNING",
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": False,
        },
        "django.server": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "flexi": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
        "apps": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "console": {
            "format": "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s",
            "datefmt": "%H:%M:%S",
        },
        "file": {
            "format": "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] [%(funcName)s] - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "security": {
            "format": "%(asctime)s %(levelname)s [%(name)s] [%(ip)s] [%(user)s] - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {
            "format": "%(levelname)s %(message)s",
        },
    },
}
