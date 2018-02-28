import logging
import os

from config_common import *

ENVIRONMENT = "prod"

DEBUG = False

SECRET_KEY = '4xkcukK7QBkdfZxBSk355'

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuration of a Gmail account for sending mails
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ['EMAIL_USER']
MAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
MAIL_SENDER = os.environ['EMAIL_SENDER_ADDRESS']

LOG_LEVEL = logging.WARN
