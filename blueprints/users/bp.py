from flask import Blueprint, Flask, request

from blueprints.users.models import User
from ext.postgres import db

users_bp = Blueprint('users', __name__)


@users_bp.route('/new', methods=['POST'])
def new():
    data = {k: v[0] for k, v in request.form.items()}
    data['age'] = int(data['age'])
    db.session.add(User(**data))
    db.session.commit()
    return ''


def init_app(app: Flask, url_prefix='/users'):
    app.register_blueprint(users_bp, url_prefix=url_prefix)
