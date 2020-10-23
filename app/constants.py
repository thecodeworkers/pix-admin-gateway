import os
from os.path import join, dirname
from dotenv import load_dotenv

path = os.path.dirname(dirname(__file__))
dotenv_path = join(path, '.env')

load_dotenv(dotenv_path)

SECRET_KEY = os.getenv('SECRET_KEY', '')
SECURE_SERVER = os.getenv('SECURE_SERVER', 'False')

HOST = os.getenv('HOST', '127.0.0.1')
PORT = os.getenv('PORT', 5000)

DEBUG = os.getenv('DEBUG', False)
ENVIRONMENT = os.getenv('ENVIRONMENT', 'production')

DATABASE_NAME = os.getenv('DATABASE_NAME', 'pix_gateway')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_PORT = os.getenv('DATABASE_PORT', 27017)

RESOURCES_HOST = os.getenv('RESOURCES_HOST', 'localhost:50051')
AUTHENTICATION_HOST = os.getenv('AUTHENTICATION_HOST', 'localhost:50050')
BANKS_HOST = os.getenv('BANKS_HOST', 'localhost:50054')
COUNTRIES_HOST = os.getenv('COUNTRIES_HOST', 'localhost:50053')

APP_NAME = os.getenv('APP_NAME', "ADMIN_GATEWAY")
APP_KEY = os.getenv('APP_KEY', "")

