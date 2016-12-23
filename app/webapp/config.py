
class Config(object):
    SECRET_KEY = '44W0ECXJL4UDHDIF6DCA'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/flask-bb-notecard'
    #SQLALCHEMY_ECHO = True
    