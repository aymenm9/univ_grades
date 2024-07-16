from flask import session, render_template, redirect, request, url_for,Blueprint
from flask_session import Session
from project import Teacher
from project import login as login_user
from project import LoginForm
from project import teacher_required

teacher_bp = Blueprint('teacher', __name__, url_prefix="/teacher")

teacher = Teacher.__name__

@teacher_bp.route('/')
def index():
    return render_template('teacher.html')

@teacher_bp.route('/dashboard', methods=['GET', 'POST'])
def teacher():
    return render_template('teacher_dashboard.html')



@teacher_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        error = login_user(username, password, Teacher)
        if error['error']:
            return render_template('login.html', user_type= teacher, form = form, error=error)
        return redirect(url_for('teacher.index'))
    else:
        return render_template('login_form.html', user_type= teacher, form = form)