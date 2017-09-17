import os

from settings import *

DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')

ALLOWED_HOSTS = ALLOWED_HOSTS.append(os.environ.get('ALLOWED_HOST'))

DEBUG = False