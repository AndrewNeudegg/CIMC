from flask import render_template, abort
from jinja2 import TemplateNotFound
from ...cache import cache
from ... import app
from . import admin_blueprint

@admin_blueprint.route('/', defaults={'page': 'index'})
@admin_blueprint.route('/<page>')
@cache.cached(timeout=app.config.get('CACHE_TIMEOUT'))
def show(page):
    try:
        return render_template('admin/%s.html' % page)
    except TemplateNotFound:
        abort(404)



# NB: To prevent cache collisions uniquely name error functions.
# NB2: Turns out there was no cache collision, instead when the url ends in a slash the route
#      no longer is treated as this blueprint, therefore flask falls back to the general 404 handler.
@admin_blueprint.errorhandler(404)
@cache.cached(timeout=app.config.get('CACHE_TIMEOUT'), key_prefix='admin_blueprint.errorhandler')
def admin_page_not_found(e):
    return render_template('admin/404.html'), 404
