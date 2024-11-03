from flask import Flask, render_template, request
import auth

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

