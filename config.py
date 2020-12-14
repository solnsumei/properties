import os
from os.path import join, dirname
from dotenv import load_dotenv


class Config:
    APP_ENVIRONMENT = None
    SECRET_KEY = None
    PORT = None
    DATABASE_URI = None
    API_URL = None
    ALGORITHM = None
    ACCESS_TOKEN_EXPIRE_MINUTES = None

    @classmethod
    def load_config(cls):
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)

        cls.APP_ENVIRONMENT = os.environ.get('ENVIRONMENT')
        cls.SECRET_KEY = os.environ.get('APP_SECRET')
        cls.PORT = int(os.environ.get('PORT'))
        cls.API_URL = os.environ.get('API_URL')

        cls.ALGORITHM = os.environ.get('ALGORITHM')
        cls.ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES')

        if cls.APP_ENVIRONMENT == 'development':
            cls.DATABASE_URI = os.environ.get("DATABASE_URI")

        if cls.APP_ENVIRONMENT == 'production':
            cls.DATABASE_URI = os.environ.get("PRODUCTION_DATABASE_URI")

        return cls
