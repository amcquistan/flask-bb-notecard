
import os

class Config(object):
    SECRET_KEY = '44W0ECXJL4UDHDIF6DCA'
    ALLOWED_UPLOAD_EXT = ['png', 'jpg', 'jpeg', 'gif']
    UPLOAD_DIR = os.path.dirname(__file__) + '/static/images'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/flask-bb-notecard'
    