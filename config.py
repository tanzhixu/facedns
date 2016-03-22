from werkzeug.exceptions import HTTPException
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://facedns:123456@192.168.33.10/facedns'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SECRET_KEY = '\xa8H\xe4;R@pi:Mo\x92\xe4M\xa7*E\x80\n\x8d\xfav3\xd8'
TIMEOUT = 3600

class UserOrPassIsNone(HTTPException):
    code = 402
    description = 'User or Password is None'

ERRORS = {
    'Unauthorized': {
        'message': "Not Authorized.",
        'status': 401,
    },
    'FORBIDDEN': {
        'message': "No Permission.",
        'status': 403,
    },
    'NotFound': {
        'message': "The requested URL was not found on the server.",
        'status': 404,
    },
    'RequestTimeout': {
        'message': "Request Token Timeout.",
        'status': 408,
    },
    'Conflict': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
    'Gone': {
        'message': "Id is not exist.",
        'status': 410,
    },
}