from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Bunny, Log, User, Review

fake = Faker()


def clear_database():
    with app.app_context():
        Bunny.query.delete()
        User.query.delete()
        Log.query.delete()
        Review.query.delete()
        db.session.commit()


def bunnies():
    with app.app_context():
        R1= Bunny(name = 'Als Burger Joint')
        R2= Bunny(name = 'Connies Drive Through')
        R3= Bunny(name = 'Hole in the Wall')
        R4= Bunny(name = 'Bella Sera')
        R5= Bunny(name = 'Mario and Luigi')
        R6= Bunny(name = 'Mamma Mias')
        R7= Bunny(name = 'Jeffs Pancake House')
        R8= Bunny(name = 'MCdonalds Waffles')
        R9= Bunny(name = 'The V Cafe')
        R10= Bunny(name = 'Bobs Gator Shack')

        allbunnies = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10]


        return allbunnies


def create_users():
    users = []
    for _ in range(20):
        u = User(
            name=fake.name(),
            email= fake.email(),
            username= fake.user_name(),

        )
        u.password_hash = fake.password()
        users.append(u)

    return users


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
        Bunny.query.delete()
        Log.query.delete()
        User.query.delete()
        Review.query.delete()

        print("Seeding bunnies...")
        bunnies = bunnies()
        db.session.add_all(bunnies)
        db.session.commit()

        print("Seeding users...")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        print("Seeding logs...")
        logs = create_logs(bunnies, users)
        db.session.add_all(logs)
        db.session.commit()

        print("Seeding reviews...")
        reviews = reviews()
        db.session.add_all(reviews)
        db.session.commit()

        print("Done seeding!")