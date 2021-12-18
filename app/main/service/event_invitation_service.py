import json
import uuid

from werkzeug.wrappers import Response
from app.main import db
from app.main.controller.auth_controller import Auth
from app.main.model.event import Event
from flask import jsonify, request
from sqlalchemy import and_
from sqlalchemy.orm import query

from app.main.model.user import User
from app.main.model.event_invitation import EventInvitation


def createInviatation(event_id, to_id):
    eventInvitatoin = EventInvitation.query.filter(and_(EventInvitation.event_id==event_id, EventInvitation.to_id=to_id))
    if not eventInvitatoin:
        eventInvitation = EventInvitation(event_id=event_id, to_id=to_id)
        db.session.add(eventInvitation)
        db.session.commit()
        response_object = {
            'status' : "Succes",
            "message": 'Event modified successfully'
        }
        return response_object
    else:
        response_object = {
            "status" : "Failed",
            "message" : "Inviatation already exists"
        }
        return response_object