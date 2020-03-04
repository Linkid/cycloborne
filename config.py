#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))
#load_dotenv(os.path.join(basedir, '.env'))


#LANGUAGES = {
#    'en': 'English',
#    'fr': 'Français'
#}
LANGUAGES = ['en', 'fr']
SECRET_KEY = 'dev'
BOOTSTRAP_SERVE_LOCAL = True
BABEL_DEFAULT_LOCALE = 'fr'

# database
DATABASE = os.path.join(basedir, 'instance', 'flaskr.sqlite')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE
SQLALCHEMY_TRACK_MODIFICATIONS = False
