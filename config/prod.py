import logging
import os

from config_common import *

ENVIRONMENT = "prod"

DEBUG = False

SECRET_KEY = '4xkcukK7QBkdfZxBSk355'

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False

LOG_LEVEL = logging.WARN
