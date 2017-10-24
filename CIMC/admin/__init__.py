from flask import Blueprint

admin_blueprint = Blueprint(
    'admin_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from .views import *
