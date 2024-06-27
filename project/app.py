from flask import Flask, session, render_template, redirect, request, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from .config import config
from .login_manager import login_manager , logout_user
from .db import db
from .models import *
from flask_bootstrap import Bootstrap
from .auth import login_user
from .forms import StudentLoginForm
from .routes import routes_bp
app = Flask(__name__)

# db config
app.config.from_object(config)
db.__init__(app)

# login config
login_manager.init_app(app)

# sesion config
Session(app)

#bootstrap config
Bootstrap(app)

'''
 / route is for student
 /admin route is for admin
 /teacher route is for teacher

'''
# routes

# import routes

app.register_blueprint(routes_bp)


if __name__ == '__main__':
    app.run(debug=True)