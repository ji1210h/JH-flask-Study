from flask import Blueprint, render_template, redirect

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return redirect("views.blog_home")  # 로그아웃하면 views의 blog_home으로 리다이렉트됨


@auth.route("/sign-up")
def sign_up():
    return render_template("signup.html")
