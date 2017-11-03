from flask import render_template
from .. import app

# This file handles app level errors.

# Monkey patch for Jina
app.template_folder='templates'
app.static_folder='static'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

