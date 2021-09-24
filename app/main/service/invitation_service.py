import json
import uuid

from app.main import db
from app.main.controller.auth_controller import Auth
from app.main.model.friends_list import FriendsList
from app.main.model.invitation import Invitation
from flask import jsonify, request
from sqlalchemy import and_
from sqlalchemy.orm import query


def save_new_invitation(to_id):
    user,serivice = Auth.get_logged_in_user(request)
    invitation = Invitation.query.filter(and_(Invitation.from_id==user['data']['public_id'], Invitation.to_id==to_id)).all()
        
    if  invitation[len(invitation)-1].status != "Accepted" and  invitation[len(invitation)-1].status != "Pending":
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

def get_all_invitations():
    return Invitation.query.filter(Invitation.status=="Pending").all()

def get_invitation_by_id(invitation_id):
    return Invitation.query.filter(and_(Invitation.status=="Pending", Invitation.invitation_id==invitation_id)).all()


def get_all_invitation_for_user(public_id,type):
    if type == "to_id":        
        return Invitation.query.filter(and_(Invitation.status=="Pending", Invitation.to_id==public_id)).all()

    elif type == "from_id":
        return Invitation.query.filter(and_(Invitation.status=="Pending", Invitation.from_id==public_id)).all()
    else:
        response_object = {
            'status': 'fail',
            'message': 'User does not have any invitations',
        }
    
    return response_object

def accept_invitation(invitation_id):
    invitation = Invitation.query.filter_by(invitation_id=invitation_id).first()
    user,service = Auth.get_logged_in_user(request)
    if user['data']['public_id'] == invitation.to_id:
        if invitation:
            from_user_list = FriendsList.query.filter_by(public_id=invitation.from_id).first()
            to_user_list = FriendsList.query.filter_by(public_id=invitation.to_id).first()
            for friends_list in [from_user_list,to_user_list]:
                json_str = str(friends_list.friends_list).replace("'", '"')
                friends_dict = json.loads(json_str)
                arr = friends_dict["list"]
                if friends_list == from_user_list:
                    arr.append(invitation.to_id)
                else:
                    arr.append(invitation.from_id)
                friends_dict["list"] = arr
                friends_list.friends_list = str(friends_dict)
                friends_list.friends_count += 1
            invitation.is_reviewed = True
            invitation.status = "Accepted"
            db.session.commit()
        response_object = {
                'status': 'Succes',
                'message': 'Added user to firends list',
            }
        return response_object
    else:
        response_object = {
                    'status': 'Fail',
                    'message': 'User is not authorised',
                }
        return response_object

def decline_invitation(invitation_id):
    invitation = Invitation.query.filter_by(invitation_id=invitation_id).first()
    if invitation:
        invitation.is_reviewed = True
        invitation.status = "Declined"
        db.session.commit() 
    response_object = {
            'status': 'Succes',
            'message': 'Declined invitation',
        }
    return response_object
