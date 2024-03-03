from flask import Flask, redirect, url_for, render_template, request, flash
# from flask_login import LoginManager
import os
import uuid
import datetime
from dataclasses import dataclass
from werkzeug.utils import secure_filename

## Constants
UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
super_secret = os.urandom(24)
# login_manager = LoginManager()

@dataclass
class Monster:
    id: uuid
    name:str
    size:int
    coordinates: str
    image_url: str
    date_added: str


@dataclass
class Character:
    level: int
    money: int
    picture: str


## Currently not using any of the email/password/authentication attributes
@dataclass
class User:
    id: uuid
    email: str
    name: str
    is_authenticated: bool
    is_active: bool
    is_anonymous: bool
    password: str
    profile_picture: str
    character: Character
    current_battles: []
    victories: []

    def get_id(self) -> str:
        return str(self.id)


@dataclass
class Quest:
    id: uuid
    active: bool
    party: []
    monster: Monster


def create_character() -> Character:
    return Character(level=0, money=0, picture="images/blankPFP.png")

def create_user(email:str, password_hash:str, name:str, image_url:str) -> User:
    return User(id=uuid.uuid4(),
                name=name,
                email=email,
                is_active=True,
                is_authenticated=True,
                is_anonymous=False,
                password=password_hash,
                profile_picture=image_url,
                character=create_character(),
                current_battles=[],
                victories=[]
                )


def create_monster(name:str, location:str, size:int, image_url:str) -> Monster:
    return Monster(id=uuid.uuid4(), name=name, coordinates=location, size=size, image_url=image_url, date_added=str(datetime.date.today()))


def create_quest(monster:Monster, user:User) -> Quest:
    return Quest(id=uuid.uuid4(), active=True, party=[user], monster=monster)

monsters = [Monster(uuid.uuid4(), "Gup", 5, "39.698488, -75.689280", "images/blankPFP.png", "02/03/2024"),
            Monster(uuid.uuid4(), "Gip", 2, "39.698488, -75.689280", "images/blankPFP.png", "02/02/2024"),
            Monster(uuid.uuid4(), "Geep", 3, "39.698488, -75.689280", "images/blankPFP.png", "03/31/2024")]

# This is the dummy user, representing the user that would normally have this browser session
users = [
    create_user(name="Lorem Ipsum", email="lorem@email.com", password_hash="XDFEAFAGAG45343", image_url="images/blankPFP.png")
]
users[0].current_battles.append(create_quest(monsters[0], users[0]))


def find_user_by_id(id:uuid, users:[]) -> User:
    for user in users:
        if id == user.id:
            return user
    return create_user(name="User Not Found", image_url=url_for('static', filename="images/blankPFP.png"))


def find_user_by_name(name:str, users:[]) -> User:
    for user in users:
        if name == user.name:
            return user
    return create_user(name="User Not Found", image_url=url_for('static', filename="images/blankPFP.png"))


def allowed_file(filename) -> bool:
    for extenstion in ALLOWED_EXTENSIONS:
        if filename.endswith(extenstion):
            return True
    else:
        return False


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html", monsters=monsters)

@app.route("/about")
def get_about():
    return render_template("about.html")

@app.route("/report", methods=["GET", "POST"])
def get_report():
    if request.method == "POST":
        print("A post request was made")
        print(request.files)
        if 'file' not in request.files:
            print("File not found")
            return redirect(request.url)
        file = request.files['file']
        print(file.filename)
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new_monster = create_monster(name=request.form['name'].title(),
                                         location=request.form['location'],
                                         size=int(request.form['size']),
                                         image_url="".join(['images/', filename])
                                         )
            monsters.append(new_monster)
            return redirect(url_for("home"))
        else:
            flash('File not found or file type not allowed.')
            return redirect(request.url)
    else:
        return render_template("report.html")

@app.route("/profile/<username>")
def get_profile(username):
    user = find_user_by_name(username, users)
    if user.name == "User Not Found":
        flash("User could not be found.")
        return redirect(url_for('home'))
    else:
        return render_template("profile.html",
                               username=user.name,
                               victories=len(user.victories),
                               quests= user.current_battles,
                               level=user.character.level,
                               profile=user.profile_picture,
                               character=user.character.picture
                               )

if __name__ == '__main__':
    app.secret_key = super_secret
    app.run()
