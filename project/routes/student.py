from flask import  session, render_template, redirect, request, url_for, Blueprint
from flask_session import Session
from project.login_manager import login_manager
from project.auth import login_user
from project.db import db
from project.models import Student
from project.forms import StudentLoginForm


student_bp = Blueprint('student', __name__,url_prefix="/student")


@student_bp.route('/student', methods=['GET', 'POST'])
def student():
    return render_template('student.html')


@student_bp.route("/login", methods=["GET", "POST"])
def login():
    form = StudentLoginForm()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = login_user(username, password, Student)
        if error['error']:
            return render_template("login.html",form = form, error=error)
        return redirect(url_for("index"))
    else:
        error = {'error': None, 'username': None, 'password': None}
        return render_template("login.html",form = form)