from flask import request, jsonify

from flask.ext.restful import Resource

from oauth.models import User,Dname

from oauth.common.util import abort_if_userid_doesnt_exist, dbadd, json_message, login_required,get_obj,dbdel

class DomainName(Resource):
    method_decorators = [login_required]
    def get(self):
        '''
            Get user's Domain name
        '''
        userid = request.args.get('userid')
        userobj = abort_if_userid_doesnt_exist(userid=userid)
        dname = userobj.dname.all()

        dnamelist = [{'dnameid': i.id, 'username': i.dname} for i in dname]

        return jsonify({'status': 200, 'dnamelist': dnamelist})


    def post(self):
        '''
            Add Domain name
        '''
        userid = request.json.get('userid')
        dname = request.json.get('dname')

        u = abort_if_userid_doesnt_exist(userid)
        d = Dname(dname=dname, user=u)

        if dbadd(d):
            return json_message(200, 'message', 'Domain name insert success')
        else:
            return json_message(200, 'error', 'Domain name insert failed')


    def put(self):
        '''
            update Domain name message
        '''
        pass

    def delete(self):
        '''
            Delete User's Domain name
        '''
        dname_id = request.args.get('dnameid')
        if dbdel(Dname,id=dname_id):
            return json_message('200', 'message', 'Delete Success')
        else:
            return json_message('200', 'error', 'Delete Failed')