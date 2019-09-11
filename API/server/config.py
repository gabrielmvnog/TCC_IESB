class BaseConfig():
    SECRET_KEY = 'asdjahdjka84561s2651hdajsdhsad'
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False

class ProductionConfig(BaseConfig):
    DEBUG = False