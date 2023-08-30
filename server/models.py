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


class Bunny(db.Model, SerializerMixin):
    __tablename__ = 'bunnies'

    # Add serialization rules
    # serialize_rules = ( '-reviews', '-user.reviews', )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

    # Add relationship
    
    logs = db.relationship( 'Log', back_populates = 'bunny', cascade = 'all, delete-orphan' )
    users = association_proxy( 'logs', 'user' )

    def __repr__(self):
        return f'<Bunny id={self.id} name={self.name}>'
    

class User(db.Model, SerializerMixin, UserMixin):
    __tablename__ = 'users'
    # Add serialization rules
    

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)
    

    # Add relationship
    logs = db.relationship( 'Log', back_populates = 'user', cascade = 'all,delete-orphan' )
    bunnies = association_proxy( 'logs', 'bunny' )

    serialize_rules = ('-log.user', '-_password_hash',)
    
    # add password properties
    @property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, new_password_string):
        plain_byte_obj = new_password_string.encode('utf-8')
        encrypted_hash_object = bcrypt.generate_password_hash(plain_byte_obj)
        hash_object_as_string = encrypted_hash_object.decode('utf-8')
        self._password_hash = hash_object_as_string

    def authenticate(self, some_string):
        return bcrypt.check_password_hash(self.password_hash, some_string.encode('utf-8'))

    # Add validation
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
    # date = db.Column(db.String, nullable = False )
    log = db.Column(db.Integer)

    # Add relationships 

    user_id = db.Column( db.Integer, db.ForeignKey( 'users.id' ) )
    bunny_id = db.Column( db.Integer, db.ForeignKey( 'bunnies.id' ) )

    bunny = db.relationship( 'Bunny', back_populates = 'logs' )
    user = db.relationship( 'User', back_populates = 'logs' )

    # Add serialization rules
    serialize_rules =('-user.logs')
    
    # Add validation
    @validates ('log')
    def validates_log(self,key,new_log):
        if 1 <= new_log <= 1825:
            return new_log
        raise ValueError ('Rabbit must be between 1 day and 1825 dys old')


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