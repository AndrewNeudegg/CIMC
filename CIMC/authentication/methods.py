# Implements the registration and validation methods.
from .models import users_administration
from ..database import db


def register(username, password):
# Adds a user based on validation rules.
# Todo: Increase security.
    user = users_administration(username, password)
    db.session.add(user)
    db.session.commit()


def validate (username, password):
# Validates a user.
# Returns true or false.
# TODO: Make secure.
    try:
        # Procedure: get from username, test password. If it doesn't exist will error.
        user = users_administration.query.filter_by(username=username).first()
        if password == user.password:
            return True
        # All validation failed.    
        return False        
    except Exception as e:
        #raise e
        # We should fail this login.
        # TODO: Log in a meaningful way.
        return False
    # End