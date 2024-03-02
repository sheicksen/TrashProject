from flask import Flask, redirect, url_for, render_template, request
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# Replace the placeholder with your Atlas connection string
# uri = "<connection string>"
# Set the Stable API version when creating a new client
# client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/profile/<username>")
def get_profile(username):
    return render_template("profile.html", username=username)


if __name__ == '__main__':
    app.run()
