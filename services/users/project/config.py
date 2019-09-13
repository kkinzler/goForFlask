import os


class BaseConfig:
    """this be the base configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """this be the development configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestingConfig(BaseConfig):
    """this be the testing configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')
    TESTING = True

class ProductionConfig(BaseConfig):
    """this be the production configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

