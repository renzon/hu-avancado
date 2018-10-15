from flask import url_for

from blueprints.users.models import User


def test_status_code(client, db_session):
    resp = client.post(url_for('users.new'), data={'name': 'Renzo', 'age': '35'})
    assert resp.status_code == 200


def test_user_creation(client, db_session):
    client.post(url_for('users.new'), data={'name': 'Renzo', 'age': '35'})
    assert 1 == User.query.count()
