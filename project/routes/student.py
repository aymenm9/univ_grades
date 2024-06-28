from flask import  session, render_template, redirect, request, url_for, Blueprint
from flask_session import Session
from project import login_manager
from project import login_user
from project import db
from project import Student
from project import LoginForm


student_bp = Blueprint('student', __name__,url_prefix="/student")


@student_bp.route('/student', methods=['GET', 'POST'])
def student():
    return render_template('student.html')


@student_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = login_user(username, password, Student)
        if error['error']:
            return render_template("login.html", user_type="student",form = form, error=error)
        return redirect(url_for('index.index'))
    else:
        error = {'error': None, 'username': None, 'password': None}
        return render_template("login.html",user_type="student",form = form)