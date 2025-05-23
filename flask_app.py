# This file marks the directory as a Python package.

from flask import Flask
from app.db import *
#import the blueprint from the views.py file

from .views import views_bp


def create_app():
    app=Flask(__name__)
    # app.teardown_appcontext(close_db)
    app.register_blueprint(views_bp, url_prefix='/')
    # get_db()
    return app