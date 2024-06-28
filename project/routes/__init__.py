from .admin import admin_bp
from .teacher import teacher_bp
from .student import student_bp
from .index import index_bp
from flask import Blueprint


routes_bp = Blueprint('routes', __name__)

routes_bp.register_blueprint(admin_bp)
routes_bp.register_blueprint(teacher_bp)
routes_bp.register_blueprint(student_bp)
routes_bp.register_blueprint(index_bp)

__all__ = [
    'admin_bp',
    'teacher_bp',
    'student_bp',
    'index_bp',
    'routes_bp']