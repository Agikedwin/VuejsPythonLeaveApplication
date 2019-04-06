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



@app.route('/api/getHolidays', methods=['GET','POST'])
def getHolidays():
    print("TEST SESS AT getHolidays")

    fetch = db.session.query(Holidays)\
        .filter(Holidays.is_deleted==0).all()
    holidays =holidayArray(fetch)


    return jsonify({
        'status': 'success',
        'result': holidays
    })


def holidayArray(data):
    result =[]

    for holiday in data:
        deptData ={}
        deptData['holiday_id'] =holiday.holiday_id
        deptData['holiday_name']= holiday.holiday_name
        deptData['holiday_date'] = holiday.holiday_date.strftime("%Y-%m-%d")
        deptData['date_created'] = holiday.date_created

        result.append(deptData)
    return result


@app.route('/api/addHoliday', methods=['POST'])
def addHoliday():
    post_data = request.get_json()
    response_object = {'status': 'success'}


    holiday =Holidays(holiday_name = post_data.get('holiday_name'),
                             holiday_date = post_data.get('holiday_date'))
    db.session.add(holiday)
    db.session.commit()

    return jsonify(response_object)


@app.route('/api/hodiday/<holiday_id>',methods = ['PUT','DELETE'])

def upadte_delete_hodiday(holiday_id):
    response_object = {'status': 'success'}
    print(request.get_json())

    if request.method == 'PUT':
        post_data = request.get_json()
        print(post_data)

        query = Holidays.query.filter(Holidays.holiday_id==holiday_id).first()
        query.holiday_name = post_data.get('holiday_name')
        query.holiday_date = post_data.get('holiday_date')


        db.session.commit()

    response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_dept(holiday_id)
        print('delete books' + holiday_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)

def remove_dept(holiday_id):

    query = Holidays.query.filter(Holidays.holiday_id == holiday_id).first()
    query.is_deleted =True
    db.session.commit()





