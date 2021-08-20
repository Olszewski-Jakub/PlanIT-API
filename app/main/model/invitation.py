from .. import db
import datetime
import uuid
from flask import request
from app.main.controller.auth_controller import Auth

class Invitation(db.Model):
    """ invitation Model for storing user related details """
    __tablename__ = "invitation"

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    invitation_id = db.Column(db.String(100))
    invited_on = db.Column(db.DateTime)
    from_id = db.Column(db.String(100))
    to_id = db.Column(db.String(100))
    is_reviewed = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(10), default="Pending")
        
    def __init__(self,to_id):
        user, status = Auth.get_logged_in_user(request)
        self.invited_on = datetime.datetime.now()
        self.invitation_id = str(uuid.uuid4())
        self.from_id = str(user['data']['public_id'])
        self.to_id = to_id

    def __repr__(self):
        return "<invitation '{}'>".format(self.to_id)