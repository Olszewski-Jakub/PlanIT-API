import datetime
import uuid

from app.main.controller.auth_controller import Auth
from flask import request

from .. import db

import datetime
import uuid


#TODO #10 Create event model
class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)
    creator = db.Column(db.String(100))
    name = db.Column(db.String)
    description = db.Column(db.String(300))
    lat_long = db.Column(db.String)
    date_of_event = db.Column(db.DateTime)
    invitations = db.Column(db.String)
    participants = db.Column(db.String)
    product_list = db.Column(db.String)

#TODO #11 Craete event setter (__init__)
    def __init__(self,name,description,lat_long,date_of_event,invitations,participants,product_list):
        user,service = Auth.get_logged_in_user(request)
        self.name = name
        self.description = description,
        self.lat_long = lat_long
        self.date_of_event = date_of_event
        self.invitations = invitations,
        self.participants = participants,
        self.product_list = product_list
        self.creator = user['data']['public_id']
        self.created_at = datetime.datetime.now()
        self.event_id = str(uuid.uuid4())

    def __repr__(self):
        return "<Event '{}'>".format(self.name)
