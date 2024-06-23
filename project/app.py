from flask import Flask, session, render_template, redirect, request, url_for
from flask_session import Session
from db import db
from login_manager import login_manager
from auth import login
app = Flask(__name__)

# db config
app.config.from_file("config.py")
db.__init__(app)

# login config
login_manager.init_app(app)

# sesion config
Session(app)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        login(username, password, "Admin")
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")

@app.route("/", methods=["GET", "POST"])
def index():
    #return render_template("index.html")
    return 'hello world!'
if __name__ == '__main__':
    app.run(debug=True)