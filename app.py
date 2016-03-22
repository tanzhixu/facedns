from flask import Flask
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from oauth.resources.users import UserList, Register, UserManager
from oauth.resources.dname import DomainName
from oauth.resources.record import RecordManager
from oauth.resources.login_or_logout import Login, Logout


api = restful.Api(app, errors= app.config['ERRORS'])

api.add_resource(UserList, '/userlist')
api.add_resource(UserManager, '/user/<userid>')
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')

api.add_resource(DomainName, '/dname')

api.add_resource(RecordManager, '/record')
