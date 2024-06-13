import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PORT = int(os.getenv('DB_PORT'))
DB_HOST = os.getenv('DB_HOST')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USER_PASSWORD = os.getenv('DB_USER_PASSWORD')

SECRET_AUTH_KEY = os.getenv('SECRET_AUTH_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

ADMIN_MANAGER_USERNAME = os.getenv('ADMIN_MANAGER_USERNAME')
ADMIN_MANAGER_PASSWORD = os.getenv('ADMIN_MANAGER_PASSWORD')
