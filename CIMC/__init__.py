from flask import Flask


# ========= Flask Init ========= #
# Introduce flask.
app = Flask(__name__, instance_relative_config=True)
# Inherit variables from the global config.
app.config.from_object('config')
# Inherit variables from the private config.
app.config.from_pyfile('config.py')
# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
# app.config.from_envvar('APP_CONFIG_FILE')


# ========= Database ========= #

# Register the database.
from .database import db


# ========= Cache ========= #
# Register the cache.
from .cache import cache
cache.init_app(app, config={'CACHE_TYPE': app.config.get('CACHE_TYPE')})


# ========= Authentication ========= #
# Load the authentication.
from .authentication import login_manager
login_manager.init_app(app)


# ========= Master Error Handling ========= #
# Init error handling for routes (404..etc)
# This could be wildcarded, but that doesn't suit development.
from .errors import page_not_found


# ========= Blueprints ========= #
# Import home blueprint
from .routes.home import home_blueprint
app.register_blueprint(home_blueprint, url_prefix='')

# Import Admin blueprint.
# from .routes.admin import admin_blueprint
# app.register_blueprint(admin_blueprint, url_prefix='/admin')

# Import Blog blueprint.
from .routes.blog import blog_blueprint
app.register_blueprint(blog_blueprint, url_prefix='/blog')


# ========= Before First Request ========= #
db.create_all()


# ========= Execute ========= #
# Run the app.
