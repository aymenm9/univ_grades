from .db import db
from .login_manager import login_manager, login_user
from werkzeug.security import check_password_hash, generate_password_hash 
from flask import session

def login_user(username, password, user_type):
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
    session['user_type'] = user_type.__name__
    return login_error


