from flask.ext.restful import fields
from datetime import datetime

user_fields = {
    'status': fields.Integer(default='200'),
    'username': fields.String,
    'userid': fields.String(attribute='id'),
    'datetime': fields.DateTime(dt_format='rfc822', default=str(datetime.now()))
}