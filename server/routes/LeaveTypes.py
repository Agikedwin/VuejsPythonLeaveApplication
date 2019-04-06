from  flask import flash, jsonify, request
from  app import  app
from  models.models import *
from datetime import datetime

now = datetime.now()


@app.route('/api/getAllLeaveTypes', methods=['GET'])
def getAllLeaveTypes():

    fetch = db.session.query(LeaveTypes)\
        .filter(LeaveTypes.is_deleted==0).all()
    leaveTypes =typesArray(fetch)


    return jsonify({
        'status': 'success',
        'result': leaveTypes
    })



def typesArray(object):
    result =[]

    for leaveTypes in object:
        data ={}
        data['leave_id'] =leaveTypes.leave_id
        data['leave_name']= leaveTypes.leave_name
        data['no_days'] = leaveTypes.no_days
        data['countinous'] = leaveTypes.countinous
        data['date_created'] = now

        result.append(data)
    return result


@app.route('/api/addLeaveTypes', methods=['POST'])
def addLeaveTypes():
    response_object = {'status': 'success'}

    post_data = request.get_json()
    leave_days= post_data.get('no_days')
    print(post_data)

    leaveTypes =LeaveTypes(leave_id =post_data.get('leave_id'),
                             leave_name = post_data.get('name'),
                             countinous = post_data.get('countinous'),
                             no_days = leave_days)
    db.session.add(leaveTypes)
    db.session.commit()

    return jsonify(response_object)


@app.route('/api/leaveTypes/<typeid>',methods = ['PUT','DELETE'])
def upadte_deleteLeaveTypes(typeid):
    response_object = {'status': 'success'}
    print("REACHED HERE***",request.get_json())

    if request.method == 'PUT':
        post_data = request.get_json()
        leave_days = post_data.get('no_days')

        query = LeaveTypes.query.filter(LeaveTypes.leave_id==typeid).first()
        query.leave_id =post_data.get('leave_id')
        query.leave_name = post_data.get('name')
        query.countinous = 0
        query.no_days = leave_days
        query.date_updated = now
        db.session.commit()

    response_object['message'] = 'Leave Types updated!'
    if request.method == 'DELETE':
        remove_leaveType(typeid)
        print('delete books' + typeid)
        response_object['message'] = 'LeaveApproval removed!'
    return jsonify(response_object)


def remove_leaveType(typeid):
    fetch = LeaveTypes.query.filter(LeaveTypes.leave_id == typeid).first()
    fetch.is_deleted = True
    db.session.commit()





