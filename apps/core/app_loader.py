import os
import yaml
from apps.core import APP_CONFIG_FILE, CONFIG_DIR


class AppDefinination:
    def __init__(self, name, path, description: str = ""):
        self.name = name
        self.path = path
        self.description = description

    def __str__(self):
        return f"{self.name} - {self.path}"

    def __repr__(self):
        return f"{self.name} - {self.path}"

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.path == other.path
            and self.description == other.description
        )

    def to_dict(self):
        """Convert to dictionary for clean YAML serialization"""
        return {"name": self.name, "path": self.path, "description": self.description}

    @classmethod
    def from_dict(cls, data):
        """Create instance from dictionary"""
        return cls(
            name=data["name"],
            path=data["path"],
            description=data.get("description", ""),
        )


FLEXI_APPS = [
    AppDefinination(
        name="account",
        path="apps.account",
        description="Authentication and authorization app",
    ),
    AppDefinination(
        name="library",
        path="apps.library",
        description="Library app for the project",
    ),
]


class AppLoader:
    _loaded_apps = None

    @classmethod
    def initialize(cls):
        if not os.path.exists(APP_CONFIG_FILE):
            os.makedirs(CONFIG_DIR, exist_ok=True)
            cls.generate_app_config()
        cls._loaded_apps = cls.load_apps_from_config()

    @classmethod
    def generate_app_config(cls):
        """Generate clean YAML config file"""
        config_data = {"apps": [app.to_dict() for app in FLEXI_APPS]}

        with open(APP_CONFIG_FILE, "w") as f:
            yaml.dump(
                config_data, f, default_flow_style=False, indent=2, sort_keys=False
            )

    @classmethod
    def load_apps_from_config(cls):
        """Load apps from the YAML config file"""
        if not os.path.exists(APP_CONFIG_FILE):
            return FLEXI_APPS

        with open(APP_CONFIG_FILE, "r") as f:
            config_data = yaml.safe_load(f)

        if not config_data or "apps" not in config_data:
            return FLEXI_APPS

        return [AppDefinination.from_dict(app_data) for app_data in config_data["apps"]]

    @classmethod
    def get_apps(cls):
        """Get the currently loaded apps"""
        if cls._loaded_apps is None:
            cls.initialize()
        return cls._loaded_apps

    @classmethod
    def reload_apps(cls):
        """Reload apps from config file"""
        cls._loaded_apps = cls.load_apps_from_config()
        return cls._loaded_apps
