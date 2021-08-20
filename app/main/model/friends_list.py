from .. import db
from flask import request
from app.main.controller.auth_controller import Auth

class FriendsList(db.Model):
    """Friend list model for storing firend lists of specified user"""
    __tablename__ = "friends"

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    friends_list = db.Column(db.String(100))
    friends_count = db.Column(db.Integer)

    def __init__(self, public_id, friends_list, friends_count):
        self.public_id = public_id
        self.friends_list = friends_list
        self.friends_count = friends_count

    def __repr__(self):
        return "<Firends count '{}'>".format(self.friends_count)