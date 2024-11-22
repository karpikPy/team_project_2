from flask import Flask, render_template, request, redirect, url_for, session
from database import process
from app import auth
import base64
#import os
#from werkzeug.utils import secure_filename

#UPLOAD_FOLDER = 'static/uploads'  # Define where uploaded files will be stored
#ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}



#app = Flask(__name__, static_folder='static')
app = Flask(__name__)
app.secret_key = "your_secret_key"
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    houses0 = process.houses()
    if not houses0:
        return """
                <p>Sorry for this, but it looks like there’s no houses on the website just yet. 
                So we can’t render the main page. Do you want to add a house? 
                <a href="{}" role="button">Host house</a>
                </p>
                """.format(url_for('h_add'))

    houses = houses0
    all_houses = list()
    for house in houses:
        home = list(house)
        home[6] = base64.b64encode(house[6]).decode("utf-8")
        all_houses.append(home)
    #print(houses)

    if request.method == "POST":
        which = request.form.get("which")
        house_id = process.get_house_id(which)
        if house_id:
            info = process.get_house_info(house_id["id"])
            return render_template("h_details.html", info=info, house_id=house_id)
        else:
            return "House not found", 404

    return render_template("index.html", houses=all_houses)
@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = auth.verify_us(email, password)
        if user:
            session["user_id"] = user[0]
            return redirect(url_for("profile"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@app.route("/profile")
def profile():
    u_id = session.get("user_id")
    if not u_id:
        return redirect(url_for("login"))
    user = process.id_user(u_id)
    return render_template("profile.html",
                           info=user)

@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        number = request.form["number"]
        password = request.form["password"]
        user_id = auth.insert_users(username, email, number, password)
        #print(f"{email, number, password, username}")
        if user_id:
            session["user_id"] = user_id
            return redirect(url_for("index"))
        else:
            return render_template("sign_in.html", error="Enrollment failed")
    return render_template("sign_in.html")

#def allowed_file(filename):
#    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/h_add", methods=["POST", "GET"])
def h_add():
    if request.method == "POST":
        if request.form.get("appartament") == "": appartament = None
        else: appartament = request.form.get("appartament")



        adress = request.form.get("adress")
        region = request.form.get("region")
        people = request.form.get("people")
        pets = request.form.get("pets")
        price = request.form.get("price")
        booked = False
        image = request.files["image"]
        image_data = image.read()
        print(appartament, adress, region, price, people, pets, image, booked)
        auth.insert_house(appartament, adress, region, price, people, pets, image_data, booked)
    return render_template("h_add.html")

@app.route("/house/<int:house_id>")
def house_details(house_id):
    house_fix = process.get_house_id(house_id)
    house = list(house_fix)
    print(house)
    house[6] = base64.b64encode(house[6]).decode("utf-8")
    if not house:
        return render_template("h_details.html", error="House not found")
    return render_template("h_details.html", info=house)