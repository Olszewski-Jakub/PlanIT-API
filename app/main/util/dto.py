from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'name': fields.String(required=True, description="user name"),
        'surname': fields.String(required=True, description="user surname"),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class InvitationDto:
    api = Namespace('invitation', description='invitation related operations')
    invitation = api.model('invitation',{
        'invitation_id': fields.String(description='invitation Identifier'),
        "from_id": fields.String(description='Inviter Identifier'),
        "to_id": fields.String(description='Invitee Identifier')
    })

class FriendsListDto:
    api = Namespace('friends', description='friends list related operations')
    friends = api.model('friends', {
        'public_id': fields.String(description='user Identifier'),
        'friends_list': fields.String(description='Friends list of specified user'),
        'friends_count': fields.String(description="Number of friends of specified user")
    })