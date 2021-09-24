from app.main import db
from app.main.model.invitation import Invitation
from app.main.model.event_invitation import EventInvitation
from flask import jsonify, request
from sqlalchemy import and_
from sqlalchemy.orm import query

#TODO #29 save_new_invitation
def save_new_event_invitation(to_id, event_id):
    eventInvitation = EventInvitation.query.filter(and_(EventInvitation.event_invitation_id == event_id, EventInvitation.to_id==to_id)).all()
    if eventInvitation[len(eventInvitation)-1].status != "Accepted" and  eventInvitation[len(eventInvitation)-1].status != "Pending":
        eventInvitation =  EventInvitation(
            to_id = to_id,
            event_id=event_id
        )

        
#TODO #30 get_all_invitation_for_user
#TODO #31 accept_invitation
#TODO #33 #32 decline_invitation