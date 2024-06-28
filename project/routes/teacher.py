from flask import session, render_template, redirect, request, url_for,Blueprint
from flask_session import Session
from project import Teacher
from project import login_user
from project import LoginForm

teacher_bp = Blueprint('teacher', __name__, url_prefix="/teacher")

@teacher_bp.route('/teacher', methods=['GET', 'POST'])
def teacher():
    return render_template('teacher.html')

@teacher_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        error = login_user(username, password, Teacher)
        if error['error']:
            return render_template('login.html', user_type="teacher", form = form, error=error)
        return redirect(url_for('index.index'))
    else:
        return render_template('login.html', user_type="teacher", form = form)