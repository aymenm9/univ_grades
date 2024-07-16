from flask_login import UserMixin, login_user, logout_user, LoginManager, login_required, current_user
from .apology import apology
from .users import get_obj
from flask import url_for, redirect
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    #to suport multple users 'admin', 'teacher', 'student' user = id,the class of user
    id, user  = get_obj(user_id) 
    if user is None or id is None:
        return None
    return user.query.get(id)

@login_manager.unauthorized_handler
def unauthorized():
    if current_user is None:
        return redirect(url_for('index.login'))
    return apology("You are not authorized to access this page.", 403)

