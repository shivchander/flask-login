# models.py

from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))
    file_name = db.Column(db.String(300))
    file_data = db.Column(db.LargeBinary)
    file_word_count = db.Column(db.String(100))
