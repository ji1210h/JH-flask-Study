from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager  # 로그인 기능을 쉽게 구현하도록 돕는 라이브러리

from pprint import pprint

# DB 설정하기
db = SQLAlchemy()
DB_NAME = "blog.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "IFP"

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # blueprint 등록
    from .views import views
    app.register_blueprint(views, url_prefix="/blog")

    from .auth import auth
    app.register_blueprint(auth, url_prefix="/auth")

    from .models import User
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"  # 가입하지 않은 유저가 접근했다면 로그인창으로 리다이렉트
    login_manager.init_app(app)

    # 받은 id로부터, DB에 있는 유저 테이블의 정보에 접근하도록 해줌
    # login manager는 유저 테이블의 정보에 접근해 저장된 세션을 바탕으로 로그인되어 있다면 로그인 페이지로 안 가도 되게끔 해줌...
    @login_manager.user_loader
    def load_user_by_id(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists("blog/" + DB_NAME):  # DB 경로가 존재하지 않는다면,
        # DB를 하나 만들어냄, create_all 함수는 SQLAlchemy에 구현되어있음
        db.create_all(app=app)
        print('Created database!')
