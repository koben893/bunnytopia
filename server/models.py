from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from flask_restful import Api
from sqlalchemy.ext.hybrid import hybrid_property
from config import db, bcrypt

# Models go here!


class Bunny(db.Model, SerializerMixin):
    __tablename__ = 'bunnies'

    # Add serialization rules
    # serialize_rules = ( '-reviews', '-user.reviews', )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # Add relationship
    
    logs = db.relationship( 'Log', back_populates = 'bunny', cascade = 'all, delete-orphan' )
    users = association_proxy( 'logs', 'user' )

    def __repr__(self):
        return f'<Bunny id={self.id} name={self.name}>'
    



class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    # Add serialization rules
    #serialize_rules = ( '-reviews.user', '-reviews.bunny.reviews' )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String)
    

    # Add relationship
    logs = db.relationship( 'Log', back_populates = 'user' )
    bunnies = association_proxy( 'logs', 'bunny' )
    
    # Add validation
    @validates( 'name' )
    def validate_name( self, key, new_name ):
        if not new_name:
            raise ValueError('must have a name!')
        return new_name

    @validates( 'age' )
    def validate_age( self, key, new_age ):
        if 21 <= new_age:
            return new_age
        raise ValueError('Must be older than 21')
    
    
    def __repr__(self):
        return f'<user id={self.id} name={self.name}>'
    

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))


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
        if 1 <= new_log <=5:
            return new_log
        raise ValueError ('Log must be between 1 and 5')


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