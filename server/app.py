#!/usr/bin/env python3

# Standard library imports

# Remote library imports

# Local imports
from config import app, db, api, bcrypt
# Add your model imports
from models import Bunny, User, Log, Review
from flask_restful import Resource
from flask import make_response, jsonify, request, session

# Views go here!

@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'

class Bunnies(Resource):
    def get(self):
        bunnies = Bunny.query.all()
        bunnies_dict_list = [bunny.to_dict( rules= ('-logs',)) for bunny in bunnies]
        return make_response (bunnies_dict_list)
    
    def post(self):
        data = request.get_json()
        new_bunny = Bunny(name = data['name'], log = ['log'])
        db.session.commit()
        db.session.commit()
        return make_response(new_bunny.to_dict(), 201)

api.add_resource (Bunnies, '/bunnies')

class BunnyByID(Resource):
    def get(self,id):
        bunny = Bunny.query.filter_by(id=id).first()
        if not bunny:
            return make_response({"error": "Bunny not found"}, 404)
        return make_response(bunny.to_dict())
    
    def delete (self, id):
        bunny = Bunny.query.filter_by_id(id=id).first()
        if not bunny:
            return make_response ({"error": "Bunny not found"},404)
        
        db.session.delete(bunny)
        db.session.commit()
        return make_response ("", 204)
    
api.add_resource(BunnyByID, '/bunnies/<int:id>')

class Users (Resource):
    def get (self):
        users = User.query.all()
        users_dict_list = [user._to_dict_(rules = ('logs',)) for user in users]
        if len(users) == 0:
            return make_response({'error': 'no Users'}, 404)
        return make_response(users_dict_list,200)
    
    def post (self):
        data = request.get_json()
        newUser = User(
            email = data['email'],
            username= data["username"],
            password = data["password"],
            )
        try:
            db.session.add(newUser)
            db.session.commit()
            return make_response (newUser.to_dict(), 200)
        except Exception as e:
            db.session.rollback()
            return make_response({'error': f'{repr(e)}'}, 422)
    
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



class Login(Resource):
    def post(self):
        request_json = request.get_json()

        username = request_json.get("username")
        password = request_json.get("password")

        user = User.query.filter_by(username = username).first()
        

        if user:
            if user.authenticate(password):
                print(user.id)
                session['user_id'] = user.id
                return user.to_dict(), 200
        else:
            return {'error': 'Invalid Credentials'}, 401
        
api.add_resource(Login, '/login')

class Logout(Resource):
    def delete(self):
        
        if session.get('user_id'):
            
            session['user_id'] = None
            
            return {}, 204
        
        return {'error': '401 Unauthorized'}, 401
    
api.add_resource(Logout, '/logout')








if __name__ == '__main__':
    app.run(port=5557, debug=True)

