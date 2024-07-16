from flask import  session, render_template, redirect, request, url_for, Blueprint, flash
from flask_session import Session
from project import login_manager, current_user
from project import login as login_user
from project import db
from project import Student
from project import LoginForm
from project import student_required

student_bp = Blueprint('student', __name__,url_prefix="/student")

student = Student.__name__


@student_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('student.html')


@student_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = login_user(username, password, Student)
        if error['error']:
            return render_template("login.html", user_type= student,form = form, error=error)
        return redirect(url_for('student.index'))
    else:
        return render_template('login_form.html', user_type= student, form = form)

@student_bp.route("/profile")
def profile():
    return render_template("profile.html", user=current_user)
