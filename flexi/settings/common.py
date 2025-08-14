from decouple import config
from pathlib import Path
from django.core.management.utils import get_random_secret_key
import logging

logger = logging.getLogger(__name__)

DEBUG = config("DEBUG", default=True, cast=bool)
SECRET_KEY = config("SECRET_KEY", default=None)
MODE = config("MODE", default="dev")

if DEBUG:
    # if developer mode, generate a random secret key from django
    logger.info("Generating random secret key for development")
    SECRET_KEY = get_random_secret_key()
    MODE = "dev"

BASE_DIR = Path(__file__).resolve().parent.parent.parent
