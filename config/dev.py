from config_common import *

ENVIRONMENT = "dev"

DEBUG = True

SECRET_KEY = 'super-secret'

# Database choice
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost:5432'
SQLALCHEMY_TRACK_MODIFICATIONS = True

MAIL_SEND = False

LOG_LEVEL = logging.DEBUG
