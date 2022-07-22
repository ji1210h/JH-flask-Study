from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    # id : 유일 키, Integer
    id = db.Column(db.Integer, primary_key=True)
    # email : 이메일 (unique), String
    email = db.Column(db.String(150), unique=True)
    # username : 유저이름 (unique), String
    username = db.Column(db.String(150), unique=True)
    # password : 비밀번호, String
    password = db.Column(db.String(150))
    # 생성일자, 기본적으로 현재가 저장되도록 함
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
