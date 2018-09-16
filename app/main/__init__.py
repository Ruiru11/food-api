from flask import Flask

from .config import config_by_name
from app.main.views.users_view import mod_users
from app.main.views.orders_view import mod_orders


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_blueprint(mod_users)
    app.register_blueprint(mod_orders)
    return app
