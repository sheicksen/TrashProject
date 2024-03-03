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
    id: str
    name:str
    size:int
    coordinates: str
    image_url: str
    date_added: str
    quest_id: str


@dataclass
class Character:
    level: int
    money: int
    picture: str


## Currently not using any of the email/password/authentication attributes
@dataclass
class User:
    id: str
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
        return self.id


@dataclass
class Quest:
    id: str
    active: bool
    date_started: str
    party: []
    monster: Monster


def create_character() -> Character:
    return Character(level=0, money=0, picture="images/blankPFP.png")

def create_user(email:str, password_hash:str, name:str, image_url:str) -> User:
    return User(id=str(uuid.uuid4()),
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
    return Monster(id=str(uuid.uuid4()), quest_id="None", name=name, coordinates=location, size=size, image_url=image_url, date_added=str(datetime.date.today()))


def create_quest(monster:Monster, user:User) -> Quest:
    return Quest(id=str(uuid.uuid4()), active=True, party=[user], monster=monster, date_started=str(datetime.date.today()))

# FAKE DB


monsters = [Monster(str(uuid.uuid4()), "Gup", 5, "39.698488, -75.689280", "images/blankPFP.png", "02/03/2024", "None"),
            Monster(str(uuid.uuid4()), "Gip", 2, "39.698488, -75.689280", "images/blankPFP.png", "02/02/2024", "None"),
            Monster(str(uuid.uuid4()), "Geep", 3, "39.698488, -75.689280", "images/blankPFP.png", "03/31/2024", "None")]

## This is the dummy user, representing the user that would normally have this browser session
users = [
    create_user(name="Lorem Ipsum", email="lorem@email.com", password_hash="XDFEAFAGAG45343", image_url="images/blankPFP.png")
]

quests = []

def find_user_by_id(id:str, users:[]) -> User:
    found_user = create_user(name="User Not Found", email="", password_hash="", image_url=url_for('static', filename="images/blankPFP.png"))
    for user in users:
        if (id == user.id):
            found_user=user
    return found_user


def find_user_by_name(name:str, users:[]) -> User:
    for user in users:
        if name == user.name:
            return user
    return create_user(name="Not Found", image_url=url_for('static', filename="images/blankPFP.png"))


def find_monster_by_id(id:str, monsters:[]) -> Monster:
    found_monster = create_monster(name="Not Found", location="Nowhere", size=0, image_url=url_for('static', filename="images/blankPFP.png"))
    for monster in monsters:
        if id == monster.id:
            found_monster = monster
    return found_monster

def find_quest_by_id(id:str, quests:[]) -> Quest:
    found_quest = Quest(id="0", party=[], date_started="",  monster=create_monster(name="Not Found", location="Nowhere", size=0, image_url=url_for('static', filename="images/blankPFP.png")), active=False )
    for quest in quests:
        if id == quest.id:
            found_quest = quest
    return found_quest


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
    unclaimed_monsters = []
    active_quests = []
    for monster in monsters:
        if monster.quest_id == "None":
            unclaimed_monsters.append(monster)
        else:
            quest = find_quest_by_id(monster.quest_id, quests)
            if quest.id != "0" and quest.active:
                active_quests.append(quest)

    return render_template("index.html", monsters=unclaimed_monsters, quests=active_quests,user=users[0])

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
                               user_id=user.id,
                               victories=user.victories,
                               monsters_def = len(user.victories),
                               quests= user.current_battles,
                               level=user.character.level,
                               profile=user.profile_picture,
                               character=user.character.picture
                               )

@app.route("/add_quest")
def add_quest():
    query = request.args.getlist('ids')
    monster= find_monster_by_id(query[0], monsters)
    user = find_user_by_id(query[1], users)

    if monster.name == "Not Found" or user.name == "Not Found":
        print("Either user or monster does not exist")
        return redirect(url_for("home"))
    else:
        for quest in user.current_battles:
            if quest.monster.id == monster.id:
                print("User already created quest")
                return redirect(url_for('get_profile', username=user.name))
        new_quest = create_quest(monster=monster, user=user)
        quests.append(new_quest)
        user.current_battles.append(new_quest)
        monster.quest_id = new_quest.id
        return redirect(url_for('get_profile', username=user.name))

@app.route("/claim_xp")
def mark_complete():
    query = request.args.getlist('ids')
    quest= find_quest_by_id(query[0], quests)
    user = find_user_by_id(query[1], users)
    if user.name == "Not Found" or quest.id == 0:
        return redirect(url_for("home", user=users[0]))
    else:
        quest.active = False
        user.character.level += 5 * quest.monster.size
        user.current_battles.remove(quest)
        user.victories.append(quest)
        return redirect(url_for("get_profile", username=user.name))


if __name__ == '__main__':
    app.secret_key = super_secret
    app.run()
