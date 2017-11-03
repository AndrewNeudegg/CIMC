# Defines the authentication models.
from ..database import db


"""
User model
Version: v0.0.1
"""
class users_administration(db.Model):
    __tablename__ = "users_administration"
    id = db.Column('user_id', db.Integer , primary_key=True)
    username = db.Column('username', db.String(50), unique=True , index=True)
    password = db.Column('password' , db.String(255))
    registered_on = db.Column('registered_on' , db.DateTime)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return str(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.username)
