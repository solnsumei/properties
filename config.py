import os
from os.path import join, dirname
from dotenv import load_dotenv


class Config:
    APP_ENVIRONMENT = None
    SECRET_KEY = None
    PORT = None
    DATABASE_URI = None

    @classmethod
    def load_config(cls):
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)

        cls.APP_ENVIRONMENT = os.environ.get('ENVIRONMENT')
        cls.SECRET_KEY = os.environ.get('APP_SECRET')
        cls.PORT = int(os.environ.get('PORT'))

        if cls.APP_ENVIRONMENT == 'development':
            cls.DATABASE_URI = os.environ.get("DATABASE_URI")

        if cls.APP_ENVIRONMENT == 'production':
            cls.DATABASE_URI = os.environ.get("PRODUCTION_DATABASE_URI")

        return cls
