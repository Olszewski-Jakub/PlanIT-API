import json
import uuid

from werkzeug.wrappers import Response
from app.main import db
from app.main.controller.auth_controller import Auth
from app.main.model.event import Event
from flask import jsonify, request
from sqlalchemy import and_
from sqlalchemy.orm import query

#TODO #12 Create "create event function"
def create_event(data):
    event = Event.query.filter_by(name = data['name']).first()
    if not event:
        new_event = Event(
            name = data['name'],
            description = data['description'],
            lat_long = data['lat_long'],
            date_of_event = data['date_of_event'],
            invitations = data['invitations'],
            participants = data['participants'],
            product_list = data['product_list']
        )
            #TODO #27 Add auto invitation send for user invited during creating events 
        save_changes(new_event)
    else:
        response_object = {
            'status' : 'fail',
            'message' : "Event with this name already exists"
        }
        return response_object, 409
        

#TODO #13 Create "delete envent function"
def delete_event(event_id):
    event = Event.query.filter_by(event_id=event_id).first()
    if event:
        db.session.delete(event)
        db.session.commit()
        response_object = {
                    'status': 'Success',
                    'message': 'Event successfully deleted',
                }
        return response_object
    else:
        response_object = {
                    'status': 'Fail',
                    'message': 'Event does not exists',
                }
        return response_object


#TODO #14 Create "Modify event function"
def modify_event(event_id, data):
    event = Event.query.filter_by(event_id=event_id).first()
    if event:
        event.name = data['name'],
        event.description = data['description'],
        event.lat_long = data['lat_long'],
        event.date_of_event = data['date_of_event'],
        event.invitations = data['invitations'],
        event.participants = data['participants'],
        event.product_list = data['product_list']
        db.session.commit()
        response_object = {
            'status' : "Succes",
            "message": 'Event modified successfully'
        }
        return response_object
    else:
        response_object = {
            "status" : "Failed",
            "message" : "Event does not exists"
        }
        return response_object


#TODO #15 Create "invite to an event function"
#TODO #28 Create event invitation logic 
def send_event_invitatione(event_ud, public_id):
    print()

#TODO #16 Create "Acccept event invitation"




#TODO #17 Create "Denie event invitation"


def save_changes(data):
    db.session.add(data)
    db.session.commit()