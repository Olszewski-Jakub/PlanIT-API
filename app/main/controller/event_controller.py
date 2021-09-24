from flask import request
from flask_restplus import Resource
from flask_restplus.marshalling import marshal_with_field
from ..service.event_service import *

from ..util.dto import EventDto

api = EventDto.api
_event = EventDto.event


#TODO #18 Create controller for "create event function"
@api.route('/')
class EventCreate(Resource):
    @api.doc('Create an event')
    @api.expect(_event, validate=True)
    def post(self):
        data = request.json
        return create_event(data=data)
#TODO #19 Create controller for "del    ete envent function"
@api.route('/<event_id>')
class EventCreate(Resource):
    @api.doc('Delete event')
    def delete(self,event_id):
        return delete_event(event_id)

#TODO #20 Create controller for "Modify event function"
    @api.doc('Modify event')
    @api.expect(_event)
    def patch(self, event_id, data):
        return modify_event(event_id, data)




#TODO #21 Create controller for "invite to an event function"
#TODO #22 Create controller for "Acccept event invitation"
#TODO #23 Create controller for "Denie event invitation"
