from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT', cast=int)
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_DATABASE = config('DB_DATABASE')
SQLALCHEMY_DATABASE_URI = (
    f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?client_encoding=utf8'
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
