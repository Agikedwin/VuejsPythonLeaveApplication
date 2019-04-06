import datetime
from app import app
from  flask import flash, jsonify, request,session
from  flask_login import current_user
now = datetime.datetime(2019, 2, 26)
from datetime import date
d = date.fromordinal(730920) # 730920th day after 1. 1. 0001
from  models.models import *
import datetime
import calendar
from datetime import timedelta, date
@app.route('/api/calculateLeaveDays',methods=['POST'])

def weekday_count():
    response_object = {'status': 'success'}

    post_data = request.get_json()
    start = post_data.get('date_from')
    end = post_data.get('date_to')
    #function to mage holidays


    #Add one day to start date to start counting from the start date day
    start_date  = datetime.datetime.strptime(start, '%Y-%m-%d') - datetime.timedelta(days=1)
    # Add one day to end date to end counting on end day
    end_date    = datetime.datetime.strptime(end, '%Y-%m-%d') + datetime.timedelta(days=1)
    week        = {}
    no_days=0
    for i in range((end_date - start_date).days-1):
        day = calendar.day_name[(start_date + datetime.timedelta(days=i+1)).weekday()]
        week[day] = week[day] + 1 if day in week else 1
        print('here@@@@@@@@@@@@@@'+day)
        #remove Weekends from the day
        if day == "Sunday" or day == "Saturday":
            print("WEEKEND FOUND : " +day)
        else:
            print("WEEK DAY : "+day)
            no_days += 1
            print(no_days)
    #returns the number of holidays found
    holidays_count=getHolidays(start, end)

    #gets the number of days after removing weekends and holidays
    actual_leave_days_taken = no_days - holidays_count
    print("THE COUNT HOLIDAYS :::: ", holidays_count)
    print("THE Leave DAYS APPLIED :::: ", no_days)
    print("THE ACTUAL DAYS TAKEN :::: ", no_days)
    return jsonify({'no_days':actual_leave_days_taken})

#print(weekday_count("01/03/2019", "04/03/2019"))

def getHolidays(start,end):
    result  = []
    #get all holiday dates
    query= Holidays.query.filter(Holidays.holiday_id>=1)
    print("HOLIDAY TEST ",query)
    for  holiday in query:
        data = {}
        data['holiday_date'] = holiday.holiday_date.strftime("%Y-%m-%d")
        data['holiday_name'] = holiday.holiday_name

        result.append(data['holiday_date'])
    print("THE SSSSS ",result)

    print("START ",start)
    print("END ", end)
    #gets number of holidays date that fall in between the leave application range
    holiday_dates_counts=0
    for index in range(len(result)):
        holiday_date =result[index]
        print("HOLIDAY DATES ", holiday_date)
        if start <= holiday_date <=  end:
            holiday_dates_counts =holiday_dates_counts + 1
            print("HOLIDAY DATES FOUND ", holiday_dates_counts)
        else:
            print("HOLIDAY DATES NOT FOUND", holiday_dates_counts)

    print("In the loop")
    print('Current result FUNCTION RETURN :',holiday_dates_counts)



    return holiday_dates_counts


class GetLeaveDayApplied(object):
    def weekday_count(self,start,end):
        #start = "01/03/2019"
        #end = "04/03/2019"
        # Add one day to start date to start counting from the start date day
        start_date = datetime.datetime.strptime(start, '%d/%m/%Y') - datetime.timedelta(days=1)
        # Add one day to end date to end counting on end day
        end_date = datetime.datetime.strptime(end, '%d/%m/%Y') + datetime.timedelta(days=1)
        week = {}
        no_days = 0
        for i in range((end_date - start_date).days - 1):
            day = calendar.day_name[(start_date + datetime.timedelta(days=i + 1)).weekday()]
            week[day] = week[day] + 1 if day in week else 1
            print('here@@@@@@@@@@@@@@' + day)
            # remove Weekends from the day
            if day == "Sunday" or day == "Saturday":
                print("WEEKEND FOUND : " + day)
            else:
                print("WEEK DAY : " + day)
                no_days += 1
                print(no_days)
        return ({'days': day, 'no_days': no_days})




def testSession():
    my_session = session.get('username')
    print(current_user.employee_id)
    return my_session


