# Introduce models.
from .models import users_administration
from .methods import register, validate

# Introduce login component.
from flask_login import LoginManager
login_manager = LoginManager()