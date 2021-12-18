from flask.json import jsonify
from app.main import db
from app.main.controller.auth_controller import Auth
from app.main.model.friends_list import FriendsList
from app.main.model.user import User
import json
from flask import request


def delete_friend(public_id):
    user, service = Auth.get_logged_in_user(request)
    to_user = FriendsList.query.filter_by(public_id=public_id).first()
    from_user = FriendsList.query.filter_by(public_id=user['data']['public_id']).first()
    users = [to_user,from_user]
    for user in users:
        json_str = str(user.friends_list).replace("'", '"')
        friends_dict ={}
        friends_dict = json.loads(json_str)
        arr = friends_dict['list']
        if user == to_user:
            for x in range(len(arr)):
                if arr[x] == from_user.public_id:
                    arr.pop(x)
        if user == from_user:
            for x in range(len(arr)):
                if arr[x] == to_user.public_id:
                    arr.pop(x)
        friends_dict["list"] = arr
        user.friends_list = str(friends_dict)
    db.session.commit()
    response_object = {
            'status': 'Succes',
            'message': 'Deleted user from firends list',
        }
    return response_object  

def get_all_friends(public_id):
    return FriendsList.query.filter_by(public_id=public_id).first()

def get_all_friends_details(public_id):
    friendsList = FriendsList.query.filter_by(public_id=public_id).first()
    json_str = str(friendsList.friends_list).replace("'", '"')
    friends_dict ={}
    friends_dict = json.loads(json_str)
    arr= friends_dict['list']
    return User.query.filter(User.public_id.in_(arr)).all()

    