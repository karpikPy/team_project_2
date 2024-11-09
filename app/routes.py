from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    items = [1, 2, "3"]
    return render_template("index.html", items=items)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    password = request.form['age']
    email = request.form['']
    return