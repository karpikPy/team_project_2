from flask import Flask, render_template, request
from flask import Flask, render_template, request, redirect, url_for, session
from database import process
import auth

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    houses = process.houses()
    return render_template("index.html", houses=houses)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["email"]
        user = auth.verify_us(email, password)
        if user:
            session["user_id"] = user["id"]
            return redirect(url_for("profile"))
        else:
            return render_template("login.html")

    return render_template("login.html")

@app.route("/profile")
def profile():
    u_id = session.get("user_id")
    if not u_id:
        return redirect(url_for("login"))
    user = process.id_user(id)
    return render_template("profile.html", user=user)

@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        number = request.form["number"]
        password = request.form["password"]
        user_id = auth.insert_users(username, email, number, password)
        if user_id:
            session["user_id"] = user_id
            return redirect(url_for("profile"))
        else:
            return render_template("sign_in.html", error="Enrolment failed")
    return render_template("sign_in.html")

