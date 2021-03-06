import os
from datetime import timedelta


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=3)
    JWT_SECRET_KEY = os.getenv('SECRET', 'AsGeNgIoJeRTUu1VQDbpbg')

    JSON_SORT_KEYS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
    BASE_URL = os.getenv('DEV_BASE_URL')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
    BASE_URL = os.getenv('PROD_BASE_URL')


config_selector = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
