import logging
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

TIMEZONE = 'America/Los_Angeles'

# Number of times a password is hashed
BCRYPT_LOG_ROUNDS = 12

# Configuration of a Gmail account for sending mails
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ['EMAIL_USER']
MAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
MAIL_SENDER = os.environ['EMAIL_SENDER']

LOG_LEVEL = logging.DEBUG
LOG_FILENAME = 'activity.log'

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = True






DEBUG = os.environ['DEBUG_LEVEL']
SECRET_KEY = os.environ['SECRET_KEY']





DEBUG = True

SECRET_KEY = 'super-secret'

# Database choice
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost:5432'
SQLALCHEMY_TRACK_MODIFICATIONS = True

MAIL_SEND = False

LOG_LEVEL = logging.DEBUG
