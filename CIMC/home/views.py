from flask import render_template, abort
from jinja2 import TemplateNotFound
from ..cache import cache
from .. import app
from . import home_blueprint


@home_blueprint.route('/', defaults={'page': 'index.html'})
@home_blueprint.route('/<page>')
@cache.cached(timeout=app.config.get('CACHE_TIMEOUT'))
def show(page):
    try:
        return render_template('home/%s' % page)
    except TemplateNotFound:
        abort(404)


@home_blueprint.errorhandler(404)
@cache.cached(timeout=app.config.get('CACHE_TIMEOUT'))
def page_not_found(e):
    return render_template('home/404.html')