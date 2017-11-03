from .. import app
from flask_sqlalchemy import SQLAlchemy

# Introduce the database.
db = SQLAlchemy(app)
