from  flask import flash, jsonify, request
from  app import  app
from  models.models import *
from datetime import datetime
now = datetime.now()
from routes.Login import getUserId
from routes.testDate import getHolidays
#user_id=testToken()

from sqlalchemy import func
from routes.testDate import GetLeaveDayApplied
@app.route('/api/',methods=['GET'])
def connCheck():
    return jsonify({'con':'ok'})
@app.route('/api/getNoDays/<id>',methods=['GET'])

def get_no_days(id):

    initial_balance =0;

    #Get the leave type allwable days
    query = db.session.query(LeaveTypes).filter(LeaveTypes.leave_id == id ).first()
    leave_days = query.no_days

    loggedInUser = getUserId()

    # get initial balance only for annual leave type

    print("THE INITIAL ::",query.leave_id)

    if (query.leave_id == 1):
        initial_balance = initialLeaveBalance(loggedInUser)

    else:
        initial_balance = 0

    #Get start and end date



    queryApproved = db.session.query(LeaveApplications)\
        .filter(LeaveApplications.leave_id==query.leave_id)\
        .filter(LeaveApplications.payroll_no == loggedInUser).all()
    if queryApproved:
        data=getApplication(queryApproved,leave_days)



        return jsonify({'status':'success','remaining':data, 'initial_balance':initial_balance})
    else:
        return jsonify({'status':'success','remaining':leave_days-initial_balance,'initial_balance':initial_balance})


def getApplication(queryApproved,leave_days):
    remaining_days =0
    #response_object = {'status': 'success'}
    actual_days_remaining=0


    for approves in queryApproved:



        date_from = approves.date_from
        date_to = approves.date_to
        days_applied = abs(date_to - date_from).days

        print("DAYS APPLIED ", days_applied)

        #print(days_applied)

        # subtract to get diff

        sum_remaining = days_applied

        print("DAYS SUM REMAINING ", sum_remaining)

    remaining_days = leave_days - sum_remaining
    print("DAYS REMAIMING HERE ",remaining_days)


    #loop through the dates leave applied to get the holidays
    total_holiday_days=0

    for leave in queryApproved:

        holiday=getHolidays(approves.date_from.strftime("%Y-%m-%d"),date_to.strftime("%Y-%m-%d"))

        total_holiday_days = holiday

    print("THE HOLIDAYS RETURNED ", total_holiday_days)

    #add leave holidays to the remaining leavedays

    actual_days_remaining = remaining_days + total_holiday_days



    return actual_days_remaining


@app.route('/api/approveLeaveApplications', methods=['GET'])
def leaveApplications():


    #queryApprovals = db.session.query(Cadre,Departments)\
    #   .join(Departments, Departments.department_id==Cadre.department_id)
    result = []

    #get get leave applications escaleted to you though you are not the immediate supervisor

    for approval,leave,emp, ap in db.session.query(LeaveApproval,LeaveTypes,EmployeesRegistration,LeaveApplications)\
            .filter(LeaveApplications.leave_id==LeaveTypes.leave_id)\
            .filter(EmployeesRegistration.payroll_no==LeaveApplications.payroll_no)\
            .filter(LeaveApproval.application_id == LeaveApplications.application_id) \
            .filter(LeaveApproval.next_person_to_approve == getUserId()) \
            .filter(LeaveApplications.approved == 0)\
            .filter(LeaveApproval.aproval_status == 0).all():
        data = {}
        data['application_id'] = ap.application_id
        data['payroll_no'] = ap.payroll_no
        data['leave_type'] = leave.leave_name
        data['date_from'] = ap.date_from.strftime("%Y-%m-%d")
        data['date_to'] = ap.date_to.strftime("%Y-%m-%d")
        data['approved'] = ap.approved
        data['leave_note'] = ap.application_note
        data['surname'] = emp.surname
        data['other_names'] = emp.other_names

        result.append(data)

    # Normal leave application criteria
    for ap,leave,emp,auth in db.session.query(LeaveApplications,LeaveTypes,EmployeesRegistration,LeaveAuthorization)\
            .filter(LeaveApplications.leave_id==LeaveTypes.leave_id)\
            .filter(EmployeesRegistration.payroll_no==LeaveApplications.payroll_no)\
            .filter(LeaveAuthorization.leave_application_id == LeaveApplications.application_id)\
            .filter(LeaveAuthorization.supervisor_payroll_no == getUserId())\
            .filter(LeaveApplications.approved == 0).all():

        data = {}
        data['application_id'] = ap.application_id
        data['payroll_no'] = ap.payroll_no
        data['leave_type'] = leave.leave_name
        data['date_from'] = ap.date_from.strftime("%Y-%m-%d")
        data['date_to'] = ap.date_to.strftime("%Y-%m-%d")
        data['approved'] = ap.approved
        data['leave_note'] = ap.application_note
        data['surname'] = emp.surname
        data['other_names'] = emp.other_names

        result.append(data)


    leave= result


    return  jsonify({'result':result})


def initialLeaveBalance(payroll_no):
    initial_balance = 0

    balance = InitialLeaveBalane.query.filter(InitialLeaveBalane.payroll_no == payroll_no).first()

    if balance is None:
        initial_balance = 0;
    else:
        initial_balance = balance.initial_balance

    return  initial_balance

@app.route('/api/getLeaveApplicationsHistory', methods=['GET'])
def leaveApplicationsHistory():

    result = []

    for ap, emp ,leave in db.session.query(LeaveApplications, EmployeesRegistration,LeaveTypes)\
            .filter(LeaveApplications.payroll_no == EmployeesRegistration.payroll_no)\
            .filter(LeaveApplications.leave_id==LeaveTypes.leave_id)\
            .filter(LeaveApplications.payroll_no == getUserId()).all():
        data = {}
        data['application_id'] = ap.application_id
        data['payroll_no'] = ap.payroll_no
        data['leave_type'] = leave.leave_name
        data['date_from'] = ap.date_from.strftime("%Y-%m-%d")
        data['date_to'] = ap.date_to.strftime("%Y-%m-%d")
        data['approved'] = ap.approved
        data['leave_status'] = ap.leave_status
        data['leave_note'] = ap.application_note
        data['surname'] = emp.surname
        data['other_names'] = emp.other_names

        result.append(data)


    leave= result

    return  jsonify({'result':result})

@app.route('/api/test',methods=['GET'])
def test():
    query = db.session.query(func.max(LeaveApplications.application_id)).first()
    print(query)

    return query





@app.route('/api/getAllLeaveApplications', methods=['GET'])
def getAllLeaveApplications():

    #get being supervised by this user
    result = []

    for myEmployees in db.session.query(StaffSupervisors)\
        .filter(StaffSupervisors.supervisor_payroll_no == getUserId()).all():
        if myEmployees is not None:


            for ap, emp ,leave in db.session.query(LeaveApplications, EmployeesRegistration,LeaveTypes)\
                    .filter(LeaveApplications.payroll_no == EmployeesRegistration.payroll_no)\
                    .filter(LeaveTypes.leave_id==LeaveApplications.leave_id)\
                    .filter(EmployeesRegistration.payroll_no == myEmployees.payroll_no).all():
                data = {}
                data['application_id'] = ap.application_id
                data['payroll_no'] = ap.payroll_no
                data['leave_type'] = leave.leave_name
                data['date_from'] = ap.date_from.strftime("%Y-%m-%d")
                data['date_to'] = ap.date_to.strftime("%Y-%m-%d")
                data['approved'] = ap.approved
                data['leave_status'] = ap.leave_status
                data['leave_note'] = ap.application_note
                data['surname'] = emp.surname
                data['other_names'] = emp.other_names
                data['application_note'] = ap.application_note

                result.append(data)
                print(result)


    leave= result

    return  jsonify({'result':result})



"""
@app.route('/api/getEmpLeaveApplications', methods=['GET'])
def getEmpLeaveApplications():


    result = []

    for ap, emp ,leave in db.session.query(LeaveApplications, EmployeesRegistration,LeaveTypes)\
            .filter(LeaveApplications.payroll_no == EmployeesRegistration.payroll_no)\
            .filter(LeaveTypes.leave_id==LeaveApplications.leave_id)\
            .filter(LeaveApplications.payroll_no == getUserId()).all():
        data = {}
        data['application_id'] = ap.application_id
        data['payroll_no'] = ap.payroll_no
        data['leave_type'] = leave.leave_name
        data['date_from'] = ap.date_from.strftime("%Y-%m-%d")
        data['date_to'] = ap.date_to.strftime("%Y-%m-%d")
        data['approved'] = ap.approved
        data['leave_status'] = ap.leave_status
        data['leave_note'] = ap.application_note
        data['surname'] = emp.surname
        data['other_names'] = emp.other_names

        result.append(data)


    leave= result

    return  jsonify({'result':result})

"""



@app.route('/api/leaveHistory',methods=['GET'])
def applicationHistoryStatus():

    result = []
    #.filter(LeaveTypes.leave_id == 1)
    for leave in LeaveTypes.query.all():
        data = {}

        data['leave_type'] = leave.leave_name
        data['leave_days'] = leave.no_days
        mydays = leave.no_days
        remaining = loopApplications(leave.leave_id)
        print("DAYS RETURNED " ,remaining)
        percentage = round(remaining/mydays * 100)
        data['per_remaining'] = percentage
        print("% REm ", percentage)
        diff = mydays -remaining
        data['leave_balance'] = diff
        data['days'] = ""

        result.append(data)


    leave= result

    return  jsonify({'result':result})

def loopApplications(leaveid):
    result = []
    remaining_days=0
    #print("Loop up11 ", getUserId())
    queryApp = LeaveApplications.query\
        .filter(LeaveApplications.payroll_no == getUserId())\
        .filter(LeaveApplications.leave_id == leaveid).all()
        #.filter(LeaveApplications.approved==1).all()

    if queryApp is not None:
        data = {}
        for days in queryApp:
            date_from = days.date_from
            date_to = days.date_to
            days_applied = abs(date_to - date_from).days
            result.append(days_applied)


        return sum(result)
    else:
        return 0



@app.route('/api/leaveTypesHistory/<payroll_no>',methods=['GET'])
def leaveTypesHistory(payroll_no):
    print("THE PAY ",payroll_no)

    result = []
    #.filter(LeaveTypes.leave_id == 1)
    for leave in LeaveTypes.query.all():
        data = {}

        data['leave_type'] = leave.leave_name
        data['leave_days'] = leave.no_days
        mydays = leave.no_days
        remaining = loopLeaveTypesHistory(leave.leave_id,payroll_no)
        print("DAYS RETURNED " ,remaining)
        percentage = remaining/mydays * 100
        data['per_remaining'] = percentage
        print("% REm ", percentage)
        diff = mydays -remaining
        data['leave_balance'] = diff
        data['days'] = ""

        result.append(data)


    leave= result

    return  jsonify({'result':result})

def loopLeaveTypesHistory(leaveid,payroll_no):
    result = []
    remaining_days=0
    #print("Loop up11 ", getUserId())
    queryApp = LeaveApplications.query\
        .filter(LeaveApplications.payroll_no == payroll_no)\
        .filter(LeaveApplications.leave_id == leaveid).all()
        #.filter(LeaveApplications.approved==1).all()

    if queryApp is not None:
        data = {}
        for days in queryApp:
            date_from = days.date_from
            date_to = days.date_to
            days_applied = abs(date_to - date_from).days
            result.append(days_applied)


        return sum(result)
    else:
        return 0







