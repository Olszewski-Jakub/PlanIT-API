import datetime
import uuid
import datetime

from app.main.controller.auth_controller import Auth
from flask import request
from .. import db

import datetime
import uuid

class EventInvitation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.String(50))
    to_id = db.Column(db.String(50))
    invitation_id = db.Column(db.String(100))
    invited_on = db.Column(db.DateTime)
    is_reviewed = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(10), default="Pending")


    def __init__(self, event_id, to_id):
        self.event_id = event_id
        self.invitation_id = str(uuid.uuid4())
        self.invited_on = str(datetime.datetime.now())
        self.to_id = to_id

    def __repr__(self):
        return "<invitation '{}'>".format(self.to_id)
        