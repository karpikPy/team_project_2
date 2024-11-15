from flask import Flask, render_template, request, redirect, url_for, session
#from database import process
#from app import auth

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def index():
    #houses = process.houses()
    houses = [["A"], ["b"], ["c"], ["d"]]
    if request.method == "POST":
        which = request.form.get("which")
        #info = "" KIRIL day tut infu from house z zminnoyi "which"
        info = [3, 'kazapobumbilka-4', "kazapobombilskiy region", 4, True, "https://i.natgeofe.com/n/4cebbf38-5df4-4ed0-864a-4ebeb64d33a4/NationalGeographic_1468962_3x4.jpg", 999, False]
        return render_template("h_details.html", info = info)
    return render_template("index.html", houses=houses)
"""
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
"""
@app.route("/h_add")
def h_add():
    return render_template("h_add.html")