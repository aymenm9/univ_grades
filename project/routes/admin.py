from flask import session, render_template, redirect, request, url_for, Blueprint
from flask_session import Session
from project import Admin
from project import login_user
from project import LoginForm
admin_bp = Blueprint('admin', __name__, url_prefix="/admin")


@admin_bp.route("/admin")
def admin():
    return render_template('admin.html')

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        error = login_user(username, password, Admin)
        if error['error']:
            return render_template('login.html', user_type="admin", form = form, error=error)
        return redirect(url_for('index.index'))
    else:
        return render_template('login.html', user_type="admin", form = form)