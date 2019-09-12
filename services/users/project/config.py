class BaseConfig:
    """this be the base configuration"""
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """this be the development configuration"""
    pass

class TestingConfig(BaseConfig):
    """this be the testing configuration"""
    TESTING = True

class ProductionConfig(BaseConfig):
    """this be the production configuration"""
    pass

