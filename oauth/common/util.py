from functools import wraps
from flask import abort, session, jsonify

from app import db
from oauth.models import User

from token_manager import Token_Manager

def dbadd(object):
    '''
        Insert data into Database
    '''
    db.session.add(object)
    db.session.commit()
    return True

def dbdel(model, **kwargs):
    '''
        Detele data from Database
    '''
    for value in kwargs.values():
        if not value:
            return None

    dbobj = db.session.query(model).filter_by(**kwargs).first()
    if dbobj is not None:
        db.session.delete(dbobj)
        db.session.commit()
        return True
    else:
        return False

def json_message(status=200, msgkey='message',msg = None):
    '''
        Formatting jsonify
    '''
    message = {}
    if msgkey == 'message':
        message = {'status': status, 'message': msg}
    elif msgkey == 'error':
        message = {'status': status, 'error': msg}
    return jsonify(message)

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = session.get('token', None)
        if token is None:
            abort(401)
        token = Token_Manager().verify_auth_token(token=token)
        if token == 401:
            abort(401)
        if token == 408:
            abort(408)
        return func(*args, **kwargs)
    return decorated_function

def abort_if_userid_doesnt_exist(userid):
    userobj = User.query.filter_by(id = userid).first()
    if userobj is None:
        abort(410)
    else:
        return userobj

def abort_if_id_doesnt_exist(object,**kwargs):
    obj = object.query.filter_by(**kwargs).first()
    if obj is None:
        abort(410)
    else:
        return obj

def get_obj(object,**kwargs):
    obj = object.query.get(*kwargs)
    if obj is None:
        abort(410)
    else:
        return obj