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

class EventDto:
    api = Namespace('event', description='Event related operations')
    event = api.model('event', {
        'event_id': fields.String(description='event identifier'),
        'creator' : fields.String(description='event creator'),
        'name' : fields.String(description='name of an event'),
        'description' : fields.String(description='description of an event'),
        'lat_long' : fields.String(description='lat_long of an event'),
        'date_of_event' : fields.String(description='date when event takes place'),
        'invitations' : fields.String(description='invitation send for users'),
        'participants' : fields.String(description='user takieng part in an event'),
        'product_list' : fields.String(description='product list identifier'),
    })


class EventInvitationDto:
    api = Namespace('event', description="Event Invitation realted operations")
    event_invitation = api.model('event invitation', {
        'event_invitation_id': fields.String(description='event invitation Identifier'),
        "event_id": fields.String(description='Event Identifier'),
        "to_id": fields.String(description='Invitee Identifier')
    })