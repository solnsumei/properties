from .settings import Settings

settings = Settings.load_config()

# App db config
DB_CONFIG = {
        "connections": {"default": settings.DATABASE_URI},
        "apps": {
            "models": {
                "models": ["src.models.models"],
                "default_connection": "default"
            }
        }
    }
