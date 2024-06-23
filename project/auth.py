from db import db
from login_manager import login_manager, login_user
from werkzeug.security import check_password_hash, generate_password_hash 

def login(username, password, user_type):
    user = user_type.query.filter_by(username=username).first()
    if user is None:
        return False
    if not check_password_hash(user.password, password):
        return False
    login_user(user)
    return True
