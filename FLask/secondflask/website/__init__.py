from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "IFP"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/blog")
    app.register_blueprint(auth, url_prefix="/blog")

    return app
