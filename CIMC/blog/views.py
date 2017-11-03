from flask import render_template, abort
from jinja2 import TemplateNotFound
from ..cache import cache
from .. import app
from . import blog_blueprint


@blog_blueprint.route('/', defaults={'page': 'index.html'})
@blog_blueprint.route('/<page>')
@cache.cached(timeout=app.config.get('CACHE_TIMEOUT'))
def show(page):
    try:
        return render_template('blog/%s' % page)
    except TemplateNotFound:
        abort(404)


@blog_blueprint.errorhandler(404)
@cache.cached(timeout=app.config.get('CACHE_TIMEOUT'))
def page_not_found(e):
    return render_template('blog/404.html'), 404