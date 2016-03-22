from flask import request, jsonify

from flask.ext.restful import Resource

from oauth.models import User, Dname, Record

from oauth.common.util import abort_if_userid_doesnt_exist, dbadd, \
    json_message, login_required,get_obj,dbdel, abort_if_id_doesnt_exist


class RecordManager(Resource):
    method_decorators = [login_required]
    def get(self):
        '''
            Get record
        '''
        dname_id = request.args.get('dname_id')
        obj = abort_if_id_doesnt_exist(Dname, id=dname_id)

        record = obj.record.all()

        RecordMessage = [
            {'record_id':       i.id,
             'record':          i.record,
             'type':            i.type,
             'line':            i.line_type,
             'value':           i.value,
             'weight':          i.weight,
             'mx':              i.mx,
             'ttl':             i.ttl,
             }
            for i in record
        ]

        return jsonify({'status': 200, 'RecordMessage': RecordMessage})

    def put(self):
        '''
            Update domain's record
        '''
        pass

    def post(self):
        '''
            Insert domain's record
        '''
        dname_id = request.json.get('dnameid')
        record = request.json.get('record')
        type = request.json.get('type')
        value = request.json.get('value')
        ttl = request.json.get('ttl')

        dnameobj = abort_if_id_doesnt_exist(Dname,id=dname_id)
        recordobj = Record(record=record,type=type,value=value,ttl=ttl,dname=dnameobj)

        if dbadd(recordobj):
            return json_message(200, 'message', 'Record Insert Success')
        else:
            return json_message(200, 'error', 'Record Insert Failed')

    def delete(self):
        '''
            Delete Record
        '''
        record_id = request.args.get('record_id')
        obj = abort_if_id_doesnt_exist(Record,id=record_id)
        if obj:
            if dbdel(Record,id=record_id):
                return json_message('200', 'message', 'Delete Success')
            else:
                return json_message('200', 'error', 'Delete Failed')
        else:
            return json_message('200', 'error', 'Delete Failed')