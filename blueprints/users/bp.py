from flask import Blueprint, Flask, request

from blueprints.users.models import User
from ext.postgres import db

users_bp = Blueprint('users', __name__)


@users_bp.route('/new', methods=['POST'])
def new():
    name = request.form.get('name')[0]
    age = int(request.form.get('age')[0])
    user = User(name=name, age=age)
    db.session.add(user)
    db.session.commit()
    return ''


def init_app(app: Flask, url_prefix='/users'):
    app.register_blueprint(users_bp, url_prefix=url_prefix)
