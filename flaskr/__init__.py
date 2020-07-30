# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 17:10:28 2020

@author: Jeff-Tesi
"""

import os

from flask import Flask


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:

        app.config.from_pyfile('config.py', silent=True)
    else:

        app.config.from_mapping(test_config)


    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def fuck():
        return "..."
    return app

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
    