from flask_login import UserMixin, login_user, logout_user, LoginManager
from .db import db
from .models import Admin, Teacher, Student

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    #to suport multple users 'admin', 'teacher', 'student' user['user_type] = the class of user
    user = user_id['usr_type']
    return user.query.get(user_id['user_id'])