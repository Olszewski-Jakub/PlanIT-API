# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.invitation_controller import api as invitation_ns
from .main.controller.friends_list_controller import api as friends_list_ns
blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Plan IT REST API',
          version='0.1',
          description='rest api for mobile planning app'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(invitation_ns, path="/invitation")
api.add_namespace(friends_list_ns,path='/friends')