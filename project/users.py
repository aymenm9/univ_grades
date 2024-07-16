
from .models import Admin, Student, Teacher

def get_obj(user : str):
    id, user_type = user.split(',')
    user_id = int(id)
    if user_type == 'admin':
        return user_id, Admin
    elif user_type == 'student':
        return user_id, Student
    elif user_type == 'teacher':
        return user_id, Teacher
    else:
        return None, None