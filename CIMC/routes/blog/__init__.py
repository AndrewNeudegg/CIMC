from flask import Blueprint

blog_blueprint = Blueprint(
    'blog_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from .views import *
