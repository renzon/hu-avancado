import pytest
import sqlalchemy
from sqlalchemy.exc import OperationalError, ProgrammingError

import settings
from app_factory import create_app
from ext.postgres import db


@pytest.fixture(scope='session')
def database():
    test_database = 'test_db'
    test_db_uri = (
        f'postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:'
        f'{settings.DB_PORT}/postgres?client_encoding=utf8'
    )
    engine = sqlalchemy.create_engine(test_db_uri)
    try:
        conn = engine.connect()
    except OperationalError:
        print(f'Not able to connect with {test_db_uri}')
    else:
        try:
            conn.execute('commit')
            conn.execute(f'DROP DATABASE {test_database}')
        except ProgrammingError:
            print("Database already cleaned")
        conn.execute('commit')
        conn.execute(f'CREATE DATABASE {test_database}')
        conn.close()
    return (
        f'postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:'
        f'{settings.DB_PORT}/{test_database}?client_encoding=utf8'
    )


@pytest.fixture(scope='session')
def _db(app):
    db.create_all()
    return db


@pytest.fixture(scope='session')
def app(database):
    settings.SQLALCHEMY_DATABASE_URI = database
    app_obj = create_app(settings)
    app_obj.testing = True
    with app_obj.test_request_context() as _:
        yield app_obj


@pytest.fixture
def client(app):
    client_obj = app.test_client()
    return client_obj
