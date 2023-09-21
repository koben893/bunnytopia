#library imports
from random import randint, choice as rc

#remote library imports
from faker import Faker
from flask_bcrypt import Bcrypt
from flask import Flask
from models import Bunny, Log, User, Review, Breeding
from flask_login import LoginManager, login_user, current_user
from config import app, db, bcrypt
from sqlalchemy.orm.exc import UnmappedInstanceError


fake = Faker()


def clear_database():
    with app.app_context():
        Bunny.query.delete()
        User.query.delete()
        Log.query.delete()
        Review.query.delete()
        Breeding.query.delete()
        db.session.commit()

def seed_bunnies(bunny_data):
    with app.app_context():
        bunny_objects = []
        for bunny_id, (bunny_name, bunny_user) in bunny_data.items():
            bunny = Bunny(name=bunny_name, user=bunny_user)
            bunny_objects.append(bunny)
        db.session.add_all(bunny_objects)
        db.session.commit()
        return bunny_objects

def create_logs(bunnies, users):
    logs = []
    for _ in range(30):
        random_bunny = rc(bunnies)
        random_user = rc(users)
        r = Log(
            bunny=random_bunny,
            user=random_user,
            log=randint(1, 1825)
        )
        logs.append(r)

    return logs

def reviews():
    with app.app_context():
        V1 = Review(name = 'Dolores had 8 kits')
        V2 = Review(name = 'Nigella and Bernadette bread same date')
        V3 = Review(name = 'Elsa and White Spot bread same date')
        V4 = Review(name = 'South Paw usually has 6-8 kits')
        V5 = Review(name = 'Farfalla and Bernadette have 8 kits')
        V6 = Review(name = 'Djali had 8 kits')
        V7 = Review(name = 'Nigella has 10 kits but not heat tolerant')
        V8 = Review(name = 'Diamond has 8 kits')
        V9 = Review(name = 'Buttercup has 8 kits')
        V10 = Review(name = "Reece's has 6 heat tolerant babies")
        V11 = Review(name = "Nigella's babies are not heat tolerant")
        V12 = Review(name = 'Abbi and Thelma have 7-8 kits each')
        V13 = Review(name = 'Elsa and Louise have 8 kits')
        V14 = Review(name = "Elsa and Louise' kits gain good weight")
        V15 = Review(name = 'Pumkin needs to be bread with South Paw')
        V16 = Review(name = 'Marble, Bugs, Boots, Patches need to be bread immediately')
        V17 = Review(name = 'FLuff, Bambi, Jasmine need to be bread')
        V18 = Review(name = 'Nigella has lots of kits but is mean mom')
        V19 = Review(name = "Paloma great mom but kits aren't as heat tolerant")
        V20 = Review(name = 'Paloma has lost 3 kits')
        V21 = Review(name = 'Nigella has 3 kits left')
        V22 = Review(name = 'White Spot has soft fur')
        V23 = Review(name = 'Igor is cuddly, soft and plump')
        V24 = Review(name = 'Igor had heat stroke but recovering')
        V25 = Review(name = 'Lynx, Ember, and Luna need to bread')
        V26 = Review(name = 'One of Diamonds kit is named Hei Hei or Wiley')
        V27 = Review(name = 'Possible name for kits Nala or Duchess')
        V28 = Review(name = "Need to wean Reece's kits")
        V29 = Review(name = 'Need to wean Buttercup')
        V30 = Review(name = 'Need to wean Diamond')

        allreviews = [V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, V29, V30]
        return allreviews

if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        clear_database()

        print("Creating users...")
        andrew = User(name="Andrew O'Brien", username="aobrien", email="andrew@gmail.com", password_hash='123456')
        erin = User(name="Erin O'Brien", username="eobrien", email="erin@gmail.com", password_hash='789456')
        david = User(name="David O'Brien", username="dobrien", email="david@gmail.com", password_hash='abcdef')

        users_to_add = [andrew, erin, david]

        for user in users_to_add:
            try:
                db.session.add(user)
            except UnmappedInstanceError:
                pass

        db.session.commit()  # Commit users first

        # Now, detach the user objects from the session
        for user in users_to_add:
            db.session.expunge(user)

        print("Seeding bunnies...")
        bunny_data = {
            1: ("Patches", erin),
            2: ("Bugs", erin),
            3: ("Marble", david),
            4: ("Boots", david),
            5: ("Buttercup", erin),
            6: ("Diamond", erin),
            7: ("Recces", erin),
            8: ("Nigella", erin),
            9: ("Fluff", erin),
            10: ("Bambi", erin),
            11: ("Elsa", erin),
            12: ("Bernadette", erin),
            13: ("Tillie", erin),
            14: ("Pumpkin", david),
            15: ("Jasmine", david),
            16: ("Paloma", david),
            17: ("Delilah", david),
            18: ("Louise", david),
            19: ("Abbi", david),
            20: ("Djali", andrew),
            21: ("Dolores", andrew),
            22: ("Anja", andrew),
            23: ("Daphne", andrew),
            24: ("Nala", andrew),
            25: ("Serena", andrew),
            26: ("White Spot", andrew),
            27: ("Boots", erin),
            28: ("Twin", erin),
            29: ("Dark Ear", david),
            30: ("Abby", andrew)
        }
    
        bunny_objects = seed_bunnies(bunny_data)
        db.session.add_all(bunny_objects)
        db.session.commit()
        print("Bunnies objects seeded successfully!")

        print("Seeding logs...")
        logs = create_logs(bunny_objects, [andrew, erin, david])
        db.session.add_all(logs)
        db.session.commit()

        reviews_list = reviews()
        db.session.add_all(reviews_list)
        
        db.session.commit()

        print("Seeding users, logs, and reviews...")
        print("Done seeding!")