from flask import session, render_template, redirect, request, url_for, Blueprint
from flask_session import Session


admin_bp = Blueprint('admin', __name__, url_prefix="/admin")


@admin_bp.route("/admin")
def admin():
    return render_template('admin.html')