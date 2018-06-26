#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from app.models import tables
from app.controllers import routes