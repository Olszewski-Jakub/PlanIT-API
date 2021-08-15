from sqlalchemy.orm import query
from app.main.model.invitation import Invitation
import uuid
from app.main import db
from flask import request
from app.main.controller.auth_controller import Auth

def save_new_invitation(to_id):
    invitation = Invitation.query.filter_by(to_id=to_id).first()
    if not invitation:
        new_invitation = Invitation(
            to_id = to_id
        )
        db.session.add(new_invitation)
        db.session.commit()
        response_object = {
            'status' : "succes",
            'message' : "Inviation created succesfuly",
            "invitation_id" : str(new_invitation.invitation_id)
        }
        return response_object, 201
    else: 
        response_object = {
            'status': 'fail',
            'message': 'Invitation already exists.',
        }
        return response_object, 409

# FIXME Fix get_all_invitations. Returns null value. 
def get_all_invitations():
    return Invitation.query.all()

def get_invitation_by_id(invitation_id):
    return Invitation.query.filter_by(invitation_id=invitation_id).first()

# FIXME Fix get_all_invitation_for_user. Returns null value. 
def get_all_invitation_for_user(public_id,type):
    response_object = ""
    if type == "to_id":
        arr =[]
        for invitation in Invitation.query.filter(Invitation.to_id==public_id):
            arr.append(invitation)
        response_object = {
            "status":"succes",
            "data":str(arr)
        }

    elif type == "from_id":
        arr = Invitation.query.filter_by(from_id=public_id).first()
        if len(arr) > 0:
            response_object = {
                "status":"succes",
                "data":str(arr)
            }  
    else:
        response_object = {
            'status': 'fail',
            'message': 'User does not have any invitations',
        }
    
    return response_object

#TODO Accept friend invitation function

#TODO Decline friend invitation function

