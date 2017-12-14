import logging
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# For running locally
DEBUG = True

TIMEZONE = 'America/Los_Angeles'

# Secret key for generating tokens
SECRET_KEY = 'houdini'

# Database choice
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Configuration of a Gmail account for sending mails
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ['EMAIL_USER']
MAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
ADMIN = "{}@gmail.com".format(MAIL_USERNAME)

# Number of times a password is hashed
BCRYPT_LOG_ROUNDS = 12

LOG_LEVEL = logging.DEBUG
LOG_FILENAME = 'activity.log'
