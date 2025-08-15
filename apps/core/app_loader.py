from apps.core import APP_CONFIG_FILE, CONFIG_DIR
from django.urls import path, include
import logging
import importlib
import os
import yaml


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
    def get_app_config_data(cls):
        file_data = {}
        with open(APP_CONFIG_FILE, "r") as f:
            loaded_data = yaml.safe_load(f)
            if "apps" in loaded_data:
                file_data = loaded_data.get("apps", [])

        return file_data

    @classmethod
    def get_apps(cls):
        valid_apps = []
        try:
            apps = cls.get_app_config_data()
            for app in apps:
                app_module = importlib.import_module(app["path"])
                if app_module:
                    valid_apps.append(app["path"])
        except ImportError as ie:
            logging.error(f"Error loading app {app['path']}: {ie}")
        except AttributeError as ae:
            logging.error(f"Error loading app {app['path']}: {ae}")
        except Exception as e:
            logging.error(f"Error loading apps: {e}")

        # Fallback to default apps if no valid apps were loaded
        if not valid_apps:
            valid_apps = [app.path for app in FLEXI_APPS]

        return valid_apps

    @classmethod
    def get_app_urls(cls):
        app_urls = []
        try:
            apps = cls.get_apps()
            for app in apps:
                try:
                    app_url_module = importlib.import_module(f"{app}.urls")
                    if hasattr(app_url_module, "urlpatterns"):
                        app_urls.append(path("", include(app_url_module.urlpatterns)))
                except ImportError as ie:
                    logging.error(f"Error importing app {app}: {ie}")
                except AttributeError as ae:
                    logging.error(f"App {app} has no urls attribute: {ae}")
                except Exception as e:
                    logging.error(f"Error loading app {app}: {e}")
        except Exception as e:
            logging.error(f"Error in get_app_urls: {e}")
        return app_urls

    @classmethod
    def get_app_graphql_schema(cls):
        queries = []
        mutations = []
        try:
            apps = cls.get_apps()
            for app in apps:
                try:
                    app_schema_module = importlib.import_module(f"{app}.schema")
                    if app_schema_module:
                        if hasattr(app_schema_module, "Query"):
                            queries.append(app_schema_module.Query)
                        if hasattr(app_schema_module, "Mutation"):
                            mutations.append(app_schema_module.Mutation)
                except ImportError as ie:
                    logging.error(f"Error importing schema for app {app}: {ie}")
                except AttributeError as ae:
                    logging.error(f"App {app} has no schema module: {ae}")
                except Exception as e:
                    logging.error(f"Error loading schema for app {app}: {e}")
        except Exception as e:
            logging.error(f"Error in get_app_graphql_schema: {e}")
        return queries, mutations

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
    def reload_apps(cls):
        """Reload apps from config file"""
        cls._loaded_apps = cls.load_apps_from_config()
        return cls._loaded_apps
