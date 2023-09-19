from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from flask_restful import Api
from sqlalchemy.ext.hybrid import hybrid_property
from config import db, bcrypt
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class Bunny(db.Model, SerializerMixin):
    __tablename__ = 'bunnies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

    # Add relationship
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='bunnies')
    logs = db.relationship('Log', back_populates='bunny', cascade='all, delete-orphan')
    breeding = db.relationship('Breeding', back_populates='bunny', cascade='all, delete-orphan')

    # Define serialization rules to exclude circular references
    serialize_rules = ('-user.bunnies', '-user.logs', '-logs.bunny')

    def __repr__(self):
        return f'<Bunny id={self.id} name={self.name}>'

class User(db.Model, SerializerMixin, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String)

    # Add relationship
    bunnies = db.relationship('Bunny', back_populates='user')
    logs = db.relationship('Log', back_populates='user')
    breeding = db.relationship('Breeding', back_populates='user')

    # Define serialization rules to exclude circular references
    serialize_rules = ('-bunnies.user', '-logs.user')

    @property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, new_password_string):
        plain_byte_obj = new_password_string.encode('utf-8')
        encrypted_hash_object = bcrypt.generate_password_hash(plain_byte_obj)
        hash_object_as_string = encrypted_hash_object.decode('utf-8')
        self._password_hash = hash_object_as_string

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

    @validates('username')
    def validate_username(self, key, new_username):
        if not isinstance(new_username, str) or len(new_username) < 5 or len(new_username) > 25:
            raise ValueError('Username must String between 5 and 25 characters')
        return new_username
    
    @validates('password_hash')
    def validate_password_hash(self, key, new_password):
        if not isinstance(new_password, str) or len(new_password) < 6 or len(new_password) > 25:
            raise ValueError('Password must between 6 and 25 characters')
        return new_password

    def __repr__(self):
        return f'<user id={self.id} name={self.name}>'

class Log(db.Model, SerializerMixin):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    log = db.Column(db.Integer)

    # Add relationships
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='logs')

    bunny_id = db.Column(db.Integer, db.ForeignKey('bunnies.id'))
    bunny = db.relationship('Bunny', back_populates='logs')

    # Add serialization rules
    serialize_rules = ('-user.bunnies', '-bunny.logs')
    
    # Add validation
    @validates ('log')
    def validates_log(self,key,new_log):
        if 1 <= new_log <=1825:
            return new_log
        raise ValueError ('Rabbit must be between 1 and 1825 days old')


    def __repr__(self):
        return f'<Log {self.id}>'

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    

    # Add relationship


    # Add serialization rules
    
    def __repr__(self):
        return f'<Review id={self.id} name={self.name}>'
    
class Breeding(db.Model, SerializerMixin):
    __tablename__ = 'breeding'

    id = db.Column(db.Integer, primary_key=True)
    bunny_id = db.Column(db.Integer, db.ForeignKey('bunnies.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    bunny = db.relationship('Bunny', back_populates='breeding')
    user = db.relationship('User', back_populates='breeding')

    def __repr__(self):
        return f'<Breeding id={self.id} name={self.name}>'