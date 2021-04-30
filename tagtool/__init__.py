# -*- coding: utf-8 -*-

""" 
@author: Jin.Fish
@file: __init__.py.py
@version: 1.0
@time: 2021/04/27 02:30:18
@contact: jinxy@pku.edu.cn

init
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from tagtool import routes
