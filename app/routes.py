from flask import Flask, render_template, request, redirect, url_for, session
from database import process
from app import auth

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/", methods=["GET", "POST"])
def index():
    houses0 = process.houses()
    if len(houses0) == 0:
        return """
                <p>Sorry for this, but it looks like there’s no houses on the website just yet. 
                So we can’t render the main page. Do you want to add a house? 
                <a href="{}" role="button">Host house</a>
                </p>
                """.format(url_for('h_add'))
    houses = []
    for i in range(len(houses)):
        houses[i].append(houses0[0])
        houses[i].append(houses0[1])
        houses[i].append(houses0[2])
    print(houses0)
    if request.method == "POST":
        which = request.form.get("which")
        house_id = process.get_house_id(which)
        info = process.get_house_info(house_id)
        #info = [3, 'kazapobumbilka-4', "kazapobombilskiy region", 4, True, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoKG0WcrjaXp1vDSTyJNKm-NBj0_ybnnLi1Q&s", 999, False]
        return render_template("h_details.html", info=info, house_id=house_id)
    return render_template("index.html", houses=houses)

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
        print(f"{email, number, password, username}")
        if user_id:
            session["user_id"] = user_id
            return redirect(url_for("index"))
        else:
            return render_template("sign_in.html", error="Enrollment failed")
    return render_template("sign_in.html")

@app.route("/h_add", methods = ["POST", "GET"])
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
        image = request.form.get("image")
        print(appartament, adress, region, price, people, pets, image, booked)
        auth.insert_house(appartament, adress, region, price, people, pets, image, booked)
    return render_template("h_add.html")

@app.route("/house/<int:house_id>")
def house_details(house_id):
    house = process.get_house_id(house_id)
    if not house:
        return render_template("h_details.html", error="House not found")
    return render_template("h_details.html", house=house)