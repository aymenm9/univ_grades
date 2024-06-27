from flask import session, render_template, redirect, request, url_for,Blueprint
from flask_session import Session


teacher_bp = Blueprint('teacher', __name__, url_prefix="/teacher")

@teacher_bp.route('/teacher', methods=['GET', 'POST'])
def teacher():
    return render_template('teacher.html')