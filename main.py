from flask import Flask, redirect, url_for, render_template, request
from dataclasses import dataclass

@dataclass
class Monster:
    name:str
    size:int
    coordinates: str
    image_url: str
    date_added: str;

monsters = [Monster("Gup", 2, "39.698488, -75.689280", "images/blankPFP.png", "02/03/2024"),
            Monster("Sludge", 8, "40.698488, -73.689280", "images/blankPFP.png", "03/01/2024"),
            Monster("Sludge", 8, "40.698488, -73.689280", "images/blankPFP.png", "03/01/2024")]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", monsters=monsters)

@app.route("/profile/<username>")
def get_profile(username):
    return render_template("profile.html", username=username)

if __name__ == '__main__':
    app.run()
