from flask import Flask, session, render_template, redirect, request, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from config import config
from login_manager import login_manager , logout_user
from db import db
from models import *
from flask_bootstrap import Bootstrap
from auth import login_user
from forms import StudentLoginForm


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

# login student
@app.route("/login", methods=["GET", "POST"])
def login():
    form = StudentLoginForm()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = login_user(username, password, Student)
        if error['error']:
            return render_template("login.html",form = form, error=error)
        return redirect(url_for("index"))
    else:
        error = {'error': None, 'username': None, 'password': None}
        return render_template("login.html",form = form)

@app.route("/logout")
def logout():
    logout_user()
    session.clear()
    return redirect("/")

@app.route("/", methods=["GET", "POST"])
def index():
    #return render_template("index.html")
    return 'hello world!'
if __name__ == '__main__':
    app.run(debug=True)