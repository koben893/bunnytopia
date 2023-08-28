from random import randint, choice as rc
from faker import Faker
from flask_bcrypt import Bcrypt
from flask import Flask
from models import db, Bunny, Log, User, Review
from flask_login import LoginManager, login_user, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

fake = Faker()


def clear_database():
    with app.app_context():
        Bunny.query.delete()
        User.query.delete()
        Log.query.delete()
        Review.query.delete()
        db.session.commit()


def seed_bunnies(bunny_data):
    with app.app_context():
        bunny_objects = []
        for bunny_id, bunny_name in bunny_data.items():
            bunny = Bunny(id=bunny_id, name=bunny_name)
            bunny_objects.append(bunny)
        db.session.add_all(bunny_objects)
        db.session.commit()
        return bunny_objects


def create_users():
    users_data = [
        {
            "name": "John Doe",
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password": "secretpassword"  # Replace with the actual password
        },
        # ... Other user data ...
    ]

    users = []
    for user_data in users_data:
        user = User(
            name=user_data["name"],
            username=user_data["username"],
            email=user_data["email"]
        )
        user.password_hash = bcrypt.generate_password_hash(user_data["password"]).decode('utf-8')  # Hash and set the password
        users.append(user)
        db.session.add(user)
    db.session.commit()
    return users

for user_data in users_data:
    user = User(
        name=user_data["name"],
        username=user_data["username"],
        email=user_data["email"]
    )
    user.password_hash = user_data["password"]  # Hash and set the password
    db.session.add(user)

db.session.commit()


def create_logs(bunnies, users):
    logs = []
    for _ in range(20):
        r = Log(
            user_id=rc([user.id for user in users]),
            bunny_id=rc([bunny.id for bunny in bunnies]),
            log=randint(1, 5)
        )
        logs.append(r)

    return logs

def reviews():
    with app.app_context():
        V1 = Review(name = '')
        V2 = Review(name = '')
        V3 = Review(name = '')
        V4 = Review(name = '')
        V5 = Review(name = '')
        V6 = Review(name = '')
        V7 = Review(name = '')
        V8 = Review(name = '')
        V9 = Review(name = '')
        V10 = Review(name = '')
        V11 = Review(name = '')
        V12 = Review(name = '')
        V13 = Review(name = '')
        V14 = Review(name = '')
        V15 = Review(name = '')
        V16 = Review(name = '')
        V17 = Review(name = '')
        V18 = Review(name = '')
        V19 = Review(name = '')
        V20 = Review(name = '')
        V21 = Review(name = '')
        V22 = Review(name = '')
        V23 = Review(name = '')
        V24 = Review(name = '')
        V25 = Review(name = '')
        V26 = Review(name = '')
        V27 = Review(name = '')
        V28 = Review(name = '')
        V29 = Review(name = '')
        V30 = Review(name = '')

        allreviews = [V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, V29, V30]
        return allreviews

if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        clear_database()

        print("Seeding bunnies...")
        bunny_data = {
            1: "Patches",
            2: "Bugs",
            3: "Marble",
            4: "Boots",
            5: "Buttercup",
            6: "Diamond",
            7: "Recces",
            8: "Nigella",
            9: "Fluff",
            10: "Bambi",
            11: "Elsa",
            12: "Bernadette",
            13: "Tillie",
            14: "Pumpkin",
            15: "Jasmine",
            16: "Paloma",
            17: "Delilah",
            18: "Louise",
            19: "Abbi",
            20: "Djali",
            21: "Dolores",
            22: "Anja",
            23: "Daphne",
            24: "Nala",
            25: "Serena",
            26: "White Spot",
            27: "Boots",
            28: "Twin",
            29: "Dark Ear",
            30: "Abby"
        }
    
    bunny_objects = seed_bunnies(bunny_data)
    print("Bunnies objects seeded successfully!")



    print("Creating users...")
    users = create_users()
    print("Users objects created successfully!")

    print("Seeding logs...")
    logs = create_logs(bunny_objects, users)
    db.session.add_all(logs)
    db.session.commit()

    reviews = reviews()
    db.session.add_all(reviews)
    db.session.commit()

    print("Seeding users, logs, and reviews...")
    print("Done seeding!")