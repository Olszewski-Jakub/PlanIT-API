from .. import db
import datetime
import uuid

class EventInvitation(db.Model):
    __tablename__="EventInvitation"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_invitation_id = db.Column(db.String(100))
    invited_on = db.Column(db.DateTime)
    event_id = db.Column(db.String(100))
    to_id =db.Column(db.String(100))
    is_reviewed = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(10), default="Pending")


    def __init__(self,event_id,to_id):
        self.event_invitation_id = event_id
        self.invited_on = datetime.datetime.now()
        self.event_id = str(uuid.uuid4())
        self.to_id = to_id

    def __repr__(self):
        return "<event invitation id: {}".format(self.event_invitation_id)
