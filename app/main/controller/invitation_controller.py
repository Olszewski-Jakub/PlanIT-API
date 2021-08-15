from flask import request
from flask_restplus import Resource

from ..util.dto import InvitationDto
from ..service.invitation_service import save_new_invitation,\
     get_all_invitations, get_invitation_by_id, get_all_invitation_for_user

api = InvitationDto.api
_invitation = InvitationDto.invitation_dto
    
@api.route('/')
class InvitationList(Resource):
    @api.doc('list_of_send_invitations')
    @api.marshal_list_with(_invitation,envelope='data')
    def get(self):
        return get_all_invitations


@api.route('/send/<invitation_id>')
@api.param('invitation_id', 'The invitation identifier')
@api.response(404, 'Invitation not found.')
class Invitation(Resource):
    @api.doc('get invitaion')
    @api.marshal_with(_invitation)
    def get(self,invitation_id):
        """get a invitation by a given id """
        invitation = get_invitation_by_id(str(invitation_id))
        if not invitation:
            api.abort(404)
        else:
            return invitation
    
    def post(self,invitation_id):
        return save_new_invitation(invitation_id)


@api.route("/invited/<public_id>")
@api.param('public_id','The user identifier')
@api.response(404, "User not found")
class InvitedUserInvitation(Resource):
    @api.doc('get all invitation for the specified user')
    @api.marshal_with(_invitation, envelope='data')
    def get(self,public_id):
        """get all invitation for invited user public_id"""
        return get_all_invitation_for_user(public_id,"to_id")


@api.route("/invitee/<public_id>")
@api.param('public_id','The user identifier')
@api.response(404, "User not found")
class SendUserInvitation(Resource):
    @api.doc('get all invitation for the specified user')
    #@api.marshal_with(_invitation)
    def get(self,public_id):
        """get all invitation for send user public_id"""
        return get_all_invitation_for_user(public_id,"from_id")

@api.route('/accept/<invitation_id>')
@api.param('invitation_id', 'The invitation identifier')
@api.response(404,'Invitation not found')
class AcceptInvitation(Resource):
    @api.doc('accept an invitation')
    @api.marshal_with(_invitation)
    def get(self,invitation_id):
        return invitation_id