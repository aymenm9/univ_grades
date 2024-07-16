from .db import db
from .login_manager import login_manager, login_user
from werkzeug.security import check_password_hash
from flask import session , redirect , url_for
from .login_manager import current_user , unauthorized
from functools import wraps
from .apology import apology

def login(username, password, user_type):
    #to suport multple users 'admin', 'teacher', 'student'

    login_error = {
        'error': None,
        'username': None,
        'password': None
        }
    
    user = user_type.query.filter_by(username=username).first()
    if user is None:
        login_error['error'] = True
        login_error['username'] = True
        return login_error
    if not check_password_hash(user.password, password):
        login_error['error'] = True
        login_error['password'] = True
        return login_error
    
    login_error['error'] = False
    login_user(user)
    return login_error


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if require_role('admin'):
            return f(*args, **kwargs)
        return f(*args, **kwargs)
    return decorated_function

def teacher_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if require_role('teacher'):
            return f(*args, **kwargs)
        return f(*args, **kwargs)
    return decorated_function

def student_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if require_role('student'):
            return f(*args, **kwargs)
    return decorated_function


def require_role(user_type):
    if current_user.__class__.__name__ != user_type:
        if not current_user:
            return redirect(url_for('index.login'))
        return apology("You are not authorized to access this page.", 403)
    else:
        return True


