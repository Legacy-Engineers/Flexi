import os
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_DIR = os.path.join(PROJECT_DIR, "config")

APP_CONFIG_FILE = os.path.join(CONFIG_DIR, "apps.yaml")
