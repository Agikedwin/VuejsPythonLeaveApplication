from  flask import flash, jsonify, request
from  models.models import *
from datetime import datetime,date,timedelta
import datetime, calendar
#from routes.Login import getUserId
from datetime import datetime as dt

@app.route('/api/accumulatedLeaveDays', methods=['GET'])

def getAccumulatedLeavedays(getUserId):
    #loggedUser = getUserId()

    todayDateIs = datetime.datetime.now().strftime("%Y-%m-%d")
    tartOfFinancialYear = '2018-09-15'

    AvailableLeaveDays = None

    print("tartOfFinancialYear :: ",tartOfFinancialYear)

    #returns the date of first appointment
    appointmentDate = getDateOfFirstAppointment(getUserId)

    # if the employee joins in the middle of the financial year delay leave elligibilty by 3months
    if  appointmentDate > tartOfFinancialYear:
        newEmpStartsLeaveOn = datetime.datetime.strptime(appointmentDate, "%Y-%m-%d")  +  datetime.timedelta(days=91)
        print("Greater ", newEmpStartsLeaveOn)
        newEmpStartsLeaveOnTrim = newEmpStartsLeaveOn.strftime("%Y-%m-%d")
        print("Greater2 ", newEmpStartsLeaveOnTrim)
        AvailableLeaveDays=accumulatedLeaveDaysNew(todayDateIs, newEmpStartsLeaveOnTrim)

    else:
        #else use noarmal leave calculation algorithm
        AvailableLeaveDays=accumulatedLeaveDaysNew(todayDateIs, tartOfFinancialYear)

        print("Not Greater")
    print("The current date is ", datetime.datetime.now().strftime('%B'))
    #jsonify({'AvailableLeaveDays':AvailableLeaveDays})
    return AvailableLeaveDays

#Leave days accumulated as the year progresses from the start of the financial year
def accumulatedLeaveDaysOld(todayDateIs,startOfFinancial):

    dateObject = []
    startOfFinancialYear = datetime.datetime.strptime(startOfFinancial, "%Y-%m-%d")
    currentDate = datetime.datetime.strptime(todayDateIs, "%Y-%m-%d")
    date_array = \
        (startOfFinancialYear + datetime.timedelta(days=x) for x in range(0, (currentDate - startOfFinancialYear).days))

    for date_object in date_array:

        dateObtained = date_object.strftime("%Y-%m-%d")
        dateObtained2 = datetime.datetime.strptime(dateObtained, "%Y-%m-%d").month
        if dateObtained2 not in dateObject:
            dateObject.append(dateObtained2)
            # while dateObtained2 == ob
            # print(dateObtained)
    print(dateObject)
    print(len(dateObject))
    # Each month is 2.5 days
    acruedLeaveDays = (len(dateObject)) * 2.5
    print("Leave days :: ", acruedLeaveDays)

    return acruedLeaveDays


def accumulatedLeaveDaysNew(todayDateIs,startOfFinancial):

    dateObject = []
    startOfFinancialYear = datetime.datetime.strptime(startOfFinancial, "%Y-%m-%d")
    currentDate = datetime.datetime.strptime(todayDateIs, "%Y-%m-%d")
    date_array = \
        (startOfFinancialYear + datetime.timedelta(days=x) for x in range(0, (currentDate - startOfFinancialYear).days))

    for date_object in date_array:

        dateObtained = date_object.strftime("%Y-%m-%d")
        dateObtained2=datetime.datetime.strptime(dateObtained, "%Y-%m-%d").month
        if dateObtained2 not in dateObject:
            dateObject.append(dateObtained2)
            #while dateObtained2 == ob
            #print(dateObtained)
    print(dateObject)
    print(len(dateObject))
    #Each month is 2.5 days
    acruedLeaveDays = (len(dateObject)) * 2.5
    print("Leave days :: ", acruedLeaveDays)


    return acruedLeaveDays

#The first appointment date
def getDateOfFirstAppointment(getUserId):



    appointmentdate = db.session.query(EmployeesRegistration).filter(EmployeesRegistration.payroll_no==getUserId).first()
    firstAppointmentDate = appointmentdate.appointment_date.strftime("%Y-%m-%d")
    print(firstAppointmentDate)
    print("reached here..........")
    return  firstAppointmentDate




