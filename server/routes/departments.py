from  flask import flash, jsonify, request, session,g
from  app import  app
from  initializer import db
from  models.models import *
from datetime import datetime
from auths.appAuth import *
from flask_login import login_required, current_user
from routes.Login import getUserId
from flask import session

from functools import update_wrapper, wraps

now = ''



@app.route('/api/getDepts', methods=['GET','POST'])
def getAll():
    print("TEST SESS AT DEP")
    #testSession()
    mysession = getUserId()
    print('AT DEP%%%%%%%%%%%%% ',mysession)



    fetchDepatments = db.session.query(Departments).all()
    department =deptArray(fetchDepatments)


    return jsonify({
        'status': 'success',
        'result': department
    })


def deptArray(data):
    result =[]

    for department in data:
        deptData ={}
        deptData['department_id'] =department.department_id
        deptData['department_name']= department.department_name
        deptData['description'] = department.description
        deptData['date_created'] = department.date_created

        result.append(deptData)
    return result


@app.route('/api/addDeptment', methods=['POST'])
def addDepartment():
    post_data = request.get_json()
    response_object = {}
    print('Reached add deps')


    departments =Departments(department_name = post_data.get('name'),
                             description = post_data.get('description'))
    db.session.add(departments)
    db.session.commit()
    response_object = {'status': 'success', 'msg': 'Record successfully updated'}

    return jsonify(response_object)


@app.route('/api/department/<dept_id>',methods = ['PUT','DELETE'])

def upadte_delete(dept_id):
    response_object = {}
    print(request.get_json())

    if request.method == 'PUT':
        post_data = request.get_json()
        print(post_data)

        queryDept = Departments.query.filter(Departments.department_id==dept_id).first()
        queryDept.department_name = post_data.get('name')
        queryDept.description = post_data.get('description')
        db.session.commit()

        response_object = {'status': 'success', 'msg': 'Record successfully updated'}
    if request.method == 'DELETE':
        remove_dept(dept_id)
        db.session.commit()
        response_object = {'status': 'success', 'msg': 'Record successfully deleted'}

    return jsonify(response_object)

def remove_dept(dept_id):
    print("dekte ", dept_id)

    fetchdept = Departments.query.filter(Departments.department_id== dept_id).first()
    fetchdept.is_deleted =True
    db.session.commit()





