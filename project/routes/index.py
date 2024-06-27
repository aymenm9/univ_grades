from flask import session, render_template, redirect, request, url_for, Blueprint
from flask_session import Session
from project.login_manager import login_manager, logout_user


index_bp = Blueprint('index', __name__, url_prefix="/")





@index_bp.route("/logout")
def logout():
    logout_user()
    session.clear()
    return redirect("/")


@index_bp.route("/", methods=["GET", "POST"])
def index():
    #return render_template("index.html")
    return 'hello world!'
