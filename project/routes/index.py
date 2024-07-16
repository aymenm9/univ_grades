from flask import session, render_template, redirect, request, url_for, Blueprint
from flask_session import Session
from project import login_manager, logout_user, login_required, current_user, Admin, db
from werkzeug.security import generate_password_hash

index_bp = Blueprint('index', __name__, url_prefix="")


@index_bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    if request.method == "POST":
        logout_user()
        return redirect("/")
    else:
        return render_template("logout.html")


@index_bp.route("/", methods=["GET", "POST"])
#@login_required
def index():
    #user = current_user.__class__.__name__
    # temp creat admin user

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        admin = Admin(username="admin", password=generate_password_hash("admin"))
        db.session.add(admin)
        db.session.commit()
        return 'added'

    return render_template('index.html')

@index_bp.route("/login")
def login():
    logout_user()
    return render_template("login.html")
