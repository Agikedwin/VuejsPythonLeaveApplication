from  flask import flash, jsonify, request
from  app import  app
from  models.models import *
from datetime import datetime
from initializer import Message, mail
from routes.Login import getUserId
from sqlalchemy import func
from sqlalchemy import desc
from sqlalchemy import desc

from routes.testDate import GetLeaveDayApplied

leavedaysApplied = GetLeaveDayApplied()



#from flask_mail import Mail, Message


now = datetime.now()


@app.route('/api/getAllLeaveApp', methods=['GET'])
def getAllApplications():


    fetch = db.session.query(LeaveApplications).all()
    leaveApp =fetch(fetch)


    return jsonify({
        'status': 'success',
        'result': leaveApp
    })




def LeaveAppArray(object):
    result =[]

    for leave in object:
        data ={}
        data['application_id'] =leave.application_id
        data['leave_id']= leave.leave_id
        data['payroll_no'] = leave.payroll_no
        data['date_from'] = leave.date_from
        data['date_to'] = leave.date_to
        data['date_applied'] = leave.date_applied
        data['date_created'] = now

        result.append(data)
    return result


@app.route('/api/addApplication', methods=['POST'])
def addLeaveApplication():
    response_object = {}
    #try:

    #the person requeting to be relieved

    userPayroll = getUserId()



    post_data = request.get_json()
    payroll_no =post_data.get('payroll_no')
    leave_id=post_data.get('leave_id')

    print("LEAVE APPLICATIONS AT POST DATA ",post_data)


    employees =LeaveApplications(leave_id = post_data.get('leave_id'),
                             payroll_no = payroll_no,
                             date_from=post_data.get('date_from'),
                             application_note =post_data.get('note'),
                             date_to=post_data.get('date_to'))



    db.session.add(employees)
    db.session.commit()

    # get leave id to be inserted into auth table
    applicationId = getLeaveApplicationId()

    #add the person to relieve you while away
    addReliever(post_data,userPayroll)

    #Notify the reliever

    # get supervisor payroll number
    supervisorid = getSupervisor(payroll_no)




    #leave_application_id =db.session.flush()
   # db.session.commit()




    #insert record into authorization table

    authTable = LeaveAuthorization(supervisor_payroll_no =supervisorid,
                                   emp_payroll_no=payroll_no,
                                   leave_id =leave_id,
                                   leave_application_id=applicationId,
                                   auth_stage=0,
                                   note="AUTH NOTE")

    db.session.add(authTable)
    db.session.commit()



    response_object = {'status': 'success','msg':'Leave successfully applied and Email sent to your supervisor '}


    #except Exception as e:


    sendEmailNotification(supervisorid)
    #response_object = {'status': 'failed','msg':'Failed some unknown error occured'}
    #print(e)

    #finally:

    return jsonify(response_object)


def getSupervisor(emp_payroll):

    query = db.session.query(StaffSupervisors)\
        .filter(StaffSupervisors.payroll_no==emp_payroll).first()


    if query:

        supervisorId = query.supervisor_payroll_no
        print(supervisorId)
        return supervisorId

    else:

        return False

def getLeaveApplicationId():
    query = db.session.query(LeaveApplications).order_by(LeaveApplications.application_id.desc()).first()
    print(query.application_id)
    return query.application_id



def addReliever(post_data,userPayroll):
    print("THE RELIEVER ", post_data)
    print("THE RELIEVER userPayroll", userPayroll)
    reliever = LeaveReliever(payroll_no=userPayroll,
                                  leave_id = post_data.get('leave_id'),
                                  reliever_payroll_no=post_data.get('reliever_payroll_no'),
                                  date_from=post_data.get('date_from'),
                                  application_note=post_data.get('note'),
                                  date_to=post_data.get('date_to'))

    db.session.add(reliever)
    db.session.commit()



@app.route('/api/employee/<appid>',methods = ['PUT','DELETE'])
def upadte_delete_applications(appid):
    response_object = {'status': 'success'}

    if request.method == 'PUT':
        post_data = request.get_json()
        payroll_no =post_data.get('payroll_no')

        query = LeaveApplications.query.filter(LeaveApplications.application_id==appid).first()
        query.application_id = post_data.get('application_id'),
        query.leave_id = post_data.get('leave_id'),
        query.payroll_no = payroll_no,
        query.date_from = post_data.get('date_from'),
        query.date_to = post_data.get('date_to'),
        query.date_applied = post_data.get('date_applied'),
        query.query.date_updated = now
        db.session.commit()

    response_object['message'] = 'LeaveApplications updated!'
    if request.method == 'DELETE':
        remove_emp(appid)
        print('delete books' + appid)
        response_object['message'] = 'LeaveApplications removed!'
    return jsonify(response_object)


def remove_emp(appid):
    fetch = LeaveApplications.query.filter(LeaveApplications.application_id == appid).first()
    fetch.is_deleted = True
    db.session.commit()







def sendEmailNotification(supid):
    print(supid)
    print("Leave App *****")

    supEmail = db.session.query(EmployeesRegistration.email)\
        .filter(EmployeesRegistration.payroll_no == supid).first()
    supervisorEmail = supEmail.email
    print(supervisorEmail)

    print('SENDING EMAIL HERE')
    msg = Message(subject="Hello",
                    sender="agikedwin@gmail.com",
                    recipients=[supervisorEmail],  # replace with your email for testing
                    body="Dear ... agik  applied for leave kindly login to approve!")
    mail.send(msg)
    return "Sent"





