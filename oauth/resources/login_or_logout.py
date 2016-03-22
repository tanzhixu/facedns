from flask import session
from flask.ext.restful import Resource

from oauth.models import User
from oauth.common.util import json_message, login_required
from oauth.common.requestparser import login_parser
from oauth.common.token_manager import Token_Manager
from config import UserOrPassIsNone

class Login(Resource):
    '''
        Login
    '''
    def post(self):
        args = login_parser.parse_args()
        username = args['username']
        password = args['password']

        if not username or not password:
            raise UserOrPassIsNone()

        userobj = User.query.filter_by(username = username).first()

        if not userobj:
            return json_message(200, 'error', 'User is not exist')

        if not userobj.verify_password(password):
            return json_message(200, 'error', 'Password Error')

        userid = userobj.id

        data = dict(username=username,userid=userid)

        token = Token_Manager()
        token = token.generate_auth_token(data= data)


        session['token'] = token

        return json_message(200, 'message', 'Login Success')

class Logout(Resource):
    '''
        Logout
    '''
    method_decorators = [login_required]
    def get(self):
        session.clear()

        return json_message(200, 'message', 'Logout Sucess')

