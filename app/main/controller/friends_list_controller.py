from flask import request
from flask_restplus import Resource

from ..util.dto import FriendsListDto, UserDto
from ..service.friends_list_service import delete_friend, get_all_friends, get_all_friends_details 

api = FriendsListDto.api
_FriendsList = FriendsListDto.friends
_User = UserDto.user

@api.route('/<public_id>')
class DeleteFriends(Resource):
    @api.doc('Delete friends')
    def delete(self,public_id):
        return delete_friend(public_id)

@api.route('/list/<public_id>')
class FriendsList(Resource):
    @api.doc('Friends list')
    @api.marshal_list_with(_FriendsList, envelope='data')
    def get(self,public_id):
        return get_all_friends(public_id)   

@api.route('/details/<public_id>')
class FriendDetails(Resource):
    @api.doc('Friends details')
    @api.marshal_with(_User, envelope='data')
    def get(self,public_id):
        return get_all_friends_details(public_id)