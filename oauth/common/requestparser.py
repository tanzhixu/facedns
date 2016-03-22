from flask.ext.restful import reqparse

login_parser = reqparse.RequestParser()
login_parser.add_argument('username', type = str, required = True)
login_parser.add_argument('password', type = str, required = True)
