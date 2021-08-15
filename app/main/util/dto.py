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
    invitation_dto = api.model('invitation',{
        'invitation_id': fields.String(description='invitation Identifier',required=True),
        "from_id": fields.String(description='Inviter Identifier',required=True),
        "to_id": fields.String(description='Invitee Identifier',required=True)
    })