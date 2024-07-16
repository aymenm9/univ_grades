from flask import session, render_template, redirect, request, url_for, Blueprint
from project import Admin
from project import login as login_user
from project import LoginForm
from project import admin_required

admin_bp = Blueprint('admin', __name__, url_prefix="/admin")

admin = Admin.__name__


@admin_bp.route('/')
@admin_required
def admin_index():
    return render_template('admin.html')

@admin_bp.route("/dashboard")
@admin_required
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
            return render_template('login_form.html', user_type= 'admin', form = form, error=error)
        return redirect('/admin/')
    else:
        return render_template('login_form.html', user_type= 'admin', form = form)