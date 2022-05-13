from sqlalchemy_utils import URLType
from game_app.extensions import db, app
from flask_login import UserMixin

class Collection(db.Model):
    '''Collection Model'''
    __tablename__ = 'collections'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(400), nullable=False)
    games = db.relationship('VideoGame', back_populates='collection')
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')


class VideoGame(db.Model):
    '''Video Game Model'''
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Float(precision=1), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'), nullable=False)
    collection = db.relationship('Collection', back_populates='games')
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')

class User(UserMixin, db.Model):
    '''User Model'''
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    bio = db.Column(db.String(300), nullable=False)