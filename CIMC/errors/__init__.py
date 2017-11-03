# This file handles app level errors.
# Is neccacery because flask will prevent 404 and 405 errors
# being handled by blueprints properly.
from flask import render_template, request, url_for
from .. import app


# Import the blueprints.
from ..routes.admin import admin_page_not_found
from ..routes.blog import blog_page_not_found
#from ..routes.home import home_page_not_found

@app.errorhandler(404)
def page_not_found(e):
# V.0.0.1
# We want to select the appropriate 404 rejection method for each route.
# However, we also want to handle this inside the blueprint.
# This is a bit messy. 
# Possibly it should be refactored into a dict, registerable upon
# introducing the errors component to the app.
# Maybe an error_handler.register('/admin/',admin_page_not_found)
# ???
# TODO: Refactor.
    if request.path.startswith('/admin/'):
        return admin_page_not_found(e)
    elif request.path.startswith('/blog/'):
        return blog_page_not_found(e)
    else:
        return render_template('errors/404.html'), 404
