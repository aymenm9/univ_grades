from flask import Flask, session, render_template, redirect, request
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# db config
db = SQLAlchemy()
app.config.from_file("config.py")
db.__init__(app)

# sesion config
Session(app)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "admin":
            session["username"] = username
            return redirect("/")
    return render_template("login.html")


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)