import os

import flask_admin as admin
from .. import app

# Declare administration object.
# admin = Admin(app)
#dir_path =  os.path.dirname(os.path.realpath(__file__))
admin = admin.Admin(app,base_template='admin/base.html', template_mode='custom')


# Monkey patch the admin app so that it looks for template files
# in a modular fashion. All files should be contained within a
# singular directory, not in the pip install location
# or the general templates folder
this_directory = os.path.dirname(os.path.realpath(__file__))
monkey_access = app.blueprints['admin']
monkey_access.root_path = this_directory
monkey_access.static_folder = this_directory + '\\static'
monkey_access.static_url_path = '/static'
monkey_access.jinja_loader.searchpath[0] = this_directory + '\\templates'
#monkey_access.template_folder = 'templates'
app.blueprints['admin'] = monkey_access
pass

