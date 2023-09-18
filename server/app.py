# Remote library imports
from flask import make_response, jsonify, request, session
from flask_restful import Resource

# Local imports
from config import app, db, api

# Add your model imports
from models import Bunny, User, Log, Review

# Views go here!

@app.route('/')
def index():
    return '<h1>Bunnytopia</h1>'

class Bunnies(Resource):
    def get(self):
        bunnies = Bunny.query.all()
        bunnies_dict_list = [bunny.to_dict( rules= ('-logs',)) for bunny in bunnies]
        return make_response (bunnies_dict_list)
    
    def post(self):
        data = request.get_json()
        new_bunny = Bunny(name = data['name'])
        db.session.add(new_bunny)
        db.session.commit()
        return make_response(new_bunny.to_dict(), 201)

class BunnyByID(Resource):
    def get(self, id):
        bunny = Bunny.query.filter_by(id=id).first()
        if not bunny:
            return make_response({"error": "Bunny not found"}, 404)
        return make_response(bunny.to_dict())

    def delete(self, id):
        bunny = Bunny.query.filter_by(id=id).first()
        if not bunny:
            return make_response({"error": "Bunny not found"}, 404)

        db.session.delete(bunny)
        db.session.commit()
        return make_response("", 204)


api.add_resource (Bunnies, '/bunnies')
api.add_resource(BunnyByID, '/bunnies/<int:id>')

class Users(Resource):
    def get(self):
        return make_response ([u.to_dict() for u in User.query.all()])

    def post(self):
        data = request.get_json()

        # Check if username already exists
        existing_user = User.query.filter_by(username=data['username']).first()
        if existing_user:
            return make_response({"error": "Username already exists. Please choose another."}, 400)

        try:
            # Add password
            new_user = User(name=data['name'], username=data['username'], email=data['email'], password_hash=data['password'])
        except Exception as e:
            return make_response({"error": "Error while creating user: " + str(e)}, 400)

        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id

        return make_response(new_user.to_dict(), 201)

class UserById(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response({"message" : "we have an error"}, 404)
        
        return make_response(user.to_dict())
    
    def patch(self, id):
        data = request.get_json()
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response({"message" : "we have an error"}, 404)

        for key in data:
            setattr(user, key, data[key])

        db.session.commit()
        return make_response(user.to_dict())

api.add_resource(UserById, '/users/<int:id>')
api.add_resource(Users, '/users')

class Logs(Resource):
    def get(self):
        logs_with_names = []
        logs = Log.query.all()

        for log in logs:
            user = User.query.get(log.user_id)
            bunny = Bunny.query.get(log.bunny_id)
            log_data = {
                "log": log.log,
                "user_name": user.username,
                "bunny_name": bunny.name
            }
            logs_with_names.append(log_data)

        return make_response(jsonify(logs_with_names), 200)

    def post(self):
        data = request.get_json()
        try:
            log = Log(
                log=data['log'],
                bunny_id=data['bunny_id'],
                user_id=data['user_id']
            )
        except ValueError as value_error:
            return make_response({"errors": [str(value_error)]}, 422)

        db.session.add(log)
        db.session.commit()

        return make_response(log.to_dict(), 201)

api.add_resource(Logs, '/logs')

class Reviews(Resource):
    def get(self):
        reviews = Review.query.all()
        reviews_dict_list = [review.to_dict() for review in reviews]
        return make_response (reviews_dict_list)
    
api.add_resource (Reviews, '/reviews')

# Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    # Check if user exists
    user = User.query.filter_by(username=username).first()
    if not user:
        return make_response({'error': 'User not found'}, 404)
    
    # Authenticate the user
    if user.authenticate(password):
        session['user_id'] = user.id
        return make_response(user.to_dict(), 200)
    else:
        return make_response({'error': 'Incorrect password'}, 401)

# Logout
@app.route('/logout', methods=['DELETE'])
def logout():
    session['user_id'] = None
    return make_response({'message': 'Logged out successfully'}, 204)

# check if browser has session 
@app.route('/check_session')
def check_session ():
    user = User.query.filter(User.id == session.get('user_id')).first()
    if user:
        return make_response (user.to_dict())
    else:
        return {'message': '401: Not Authorized'}, 401  

# Adding bunny to breeding schedule


if __name__ == '__main__':
    app.run(port=5557, debug=True)