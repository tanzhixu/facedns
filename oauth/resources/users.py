from flask import jsonify, request, abort
from flask.ext.restful import Resource, marshal_with
from passlib.apps import custom_app_context as pwd_context

from oauth.common.util import json_message, dbadd, dbdel, login_required, abort_if_userid_doesnt_exist
from oauth.common.resource_field import user_fields
from login_or_logout import login_parser
from oauth.models import User
from app import db
from config import UserOrPassIsNone


class UserManager(Resource):
    method_decorators = [login_required]
    @marshal_with(user_fields)
    def get(self,userid):
        '''
            Get users list
        '''
        userobj = abort_if_userid_doesnt_exist(userid)

        return userobj

    def put(self,userid):
        '''
            Update user's password
        '''
        abort_if_userid_doesnt_exist(userid)

        password = request.json.get('password', None)

        if not password:
            return json_message(200, 'error', 'Password is None')

        query = db.session.query(User)
        newpasswd = pwd_context.encrypt(password)

        try:
            query.filter(User.id == userid).update({User.password_hash: newpasswd})
        except Exception:
            return json_message(200, 'error', 'Password Change Failed')

        return json_message(200, 'message', 'Password Change Success')

    def delete(self,userid):
        '''
            Delete User
        '''
        abort_if_userid_doesnt_exist(userid)

        dbdel(User, id=userid)

        return json_message(200, 'message', 'User Delete Success')

class UserList(Resource):
    method_decorators = [login_required]
    def get(self):
        '''
            Get users list
        '''
        userslist = User.query.all()
        userslist = [{'id': i.id, 'username': i.username} for i in userslist]

        return jsonify({'status': 200, 'userslist': userslist})


class Register(Resource):
    def post(self):
        '''
            User Register
        '''
        args = login_parser.parse_args()
        username = args['username']
        password = args['password']

        if not username or not password:
            raise UserOrPassIsNone()

        if User.query.filter_by(username=username).first() is not None:
            return abort(409)

        userobj = User(username=username)
        userobj.hash_password(password)
        dbadd(userobj)

        return json_message(200, 'message', 'User Register Success')
