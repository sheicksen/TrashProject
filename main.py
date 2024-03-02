from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/profile/<username>")
def get_profile(username):
    return render_template("profile.html", username=username)


if __name__ == '__main__':
    app.run()
