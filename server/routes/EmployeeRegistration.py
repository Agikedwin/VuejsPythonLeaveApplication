from  flask import flash, jsonify, request
from  app import  app
from  models.models import *
from initializer import flask_bcrypt
from datetime import datetime

from initializer import Message, mail

now = ''


@app.route('/api/getAllEmployees', methods=['GET'])
def getAllEmp():

    result = []


    for emp, cadre in db.session.query(EmployeesRegistration,Cadre)\
        .filter(EmployeesRegistration.designation == Cadre.designation_id).all():
        data = {}
        data['employee_id'] = emp.employee_id
        data['payroll_no'] = emp.payroll_no
        data['surname'] = emp.surname
        data['other_names'] = emp.other_names
        data['designation_id'] = emp.designation
        data['designation'] = cadre.designation_name
        data['entry_salary'] = emp.entry_salary
        data['program'] = emp.program
        data['department_id'] = emp.department_id
        data['terms_of_service'] = emp.terms_of_service
        data['dob'] = emp.dob.strftime("%Y-%m-%d")
        data['birth_place'] = emp.birth_place
        data['nationalty'] = emp.nationalty
        data['passport_idno'] = emp.passport_idno
        data['marital_status'] = emp.marital_status
        data["email"] = emp.email
        data["phone_no"] = emp.phone_no
        data['spause_name'] = emp.spause_name
        data["spause_idno"] =emp.spause_idno
        data['kra_no'] = emp.kra_no
        data['nssf_no'] = emp.nssf_no
        data['nhif_no'] = emp.nhif_no
        data['bank_name'] = emp.bank_name
        data['account_no'] = emp.account_no
        data['branch'] = emp.branch
        data['appointment_date'] = emp.appointment_date.strftime("%Y-%m-%d")

        result.append(data)



    return jsonify({
        'status': 'success',
        'result': result
    })


@app.route('/api/getEmployee/<payroll_no>', methods=['GET'])
def getEmployee(payroll_no):

    result = []


    for emp, cadre in db.session.query(EmployeesRegistration,Cadre)\
        .filter(EmployeesRegistration.designation == Cadre.designation_id)\
            .filter(EmployeesRegistration.payroll_no==payroll_no).all():
        data = {}
        data['employee_id'] = emp.employee_id
        data['payroll_no'] = emp.payroll_no
        data['surname'] = emp.surname
        data['other_names'] = emp.other_names
        data['designation_id'] = emp.designation
        data['designation'] = cadre.designation_name
        data['entry_salary'] = emp.entry_salary
        data['program'] = emp.program
        data['department_id'] = emp.department_id
        data['terms_of_service'] = emp.terms_of_service
        data['dob'] = emp.dob.strftime("%Y-%m-%d")
        data['birth_place'] = emp.birth_place
        data['nationalty'] = emp.nationalty
        data['passport_idno'] = emp.passport_idno
        data['marital_status'] = emp.marital_status
        data['spause_name'] = emp.spause_name
        data['kra_no'] = emp.kra_no
        data['nssf_no'] = emp.nssf_no
        data['nhif_no'] = emp.nhif_no
        data['bank_name'] = emp.bank_name
        data['account_no'] = emp.account_no
        data['branch'] = emp.branch
        data['appointment_date'] = emp.appointment_date.strftime("%Y-%m-%d")

        result.append(data)



    return jsonify({
        'status': 'success',
        'result': result
    })




def EmpArray(object):
    result =[]
    for registration in object:
        data ={}
        data['employee_id'] =registration.employee_id
        data['payroll_no']= registration.payroll_no
        data['surname'] = registration.surname
        data['other_names'] = registration.other_names
        data['designation'] = registration.designation
        data['entry_salary'] = registration.entry_salary
        data['program'] = registration.program
        data['department_id'] = registration.department_id
        data['terms_of_service'] = registration.terms_of_service
        data['dob'] = registration.dob
        data['birth_place'] = registration.birth_place
        data['nationalty'] = registration.nationalty
        data['passport_idno'] = registration.passport_idno
        data['marital_status'] = registration.marital_status
        data['spause_name'] = registration.spause_name
        data['kra_no'] = registration.kra_no
        data['nssf_no'] = registration.nssf_no
        data['nhif_no'] = registration.nhif_no
        data['bank_name'] = registration.bank_name
        data['account_no'] = registration.account_no
        data['branch'] = registration.branch
        data['appointment_date'] = registration.appointment_date.strftime("%Y-%m-%d")

        result.append(data)
    return result


@app.route('/api/addEmployee', methods=['POST'])
def addEmp():
    post_data = request.get_json()
    payroll_no = post_data.get('payroll_no')
    rawusername ="Leave@"+payroll_no
    print("ROW USERNAME ", rawusername)
    pw_hash = flask_bcrypt.generate_password_hash(rawusername)
    userEmail = post_data.get('email')
    print(pw_hash)
    response_object = {'status': 'success'}

    deptId = post_data.get('department')
    employees =EmployeesRegistration(employee_id =post_data.get('employee_id'),
                             payroll_no = post_data.get('payroll_no'),
                             surname = post_data.get('surname'),
                             other_names=post_data.get('other_names'),
                             appointment_date=post_data.get('appointment_date'),
                             designation=post_data.get('designation_id'),
                             entry_salary = post_data.get('entry_salary'),
                             program=post_data.get('program'),
                             department_id = deptId,
                             terms_of_service = post_data.get('terms_of_service'),
                             dob=post_data.get('dob'),
                             birth_place=post_data.get('birth_place'),
                             nationalty=post_data.get('nationalty'),
                             passport_idno=post_data.get('passport_idno'),
                             marital_status=post_data.get('marital_status'),
                             email =post_data.get('email'),
                             phone_no = post_data.get('phone_no'),
                             spause_name=post_data.get('spause_name'),
                             spause_idno=post_data.get('spause_idno'),
                             kra_no=post_data.get('kra_no'),
                             nssf_no=post_data.get('nssf_no'),
                             nhif_no=post_data.get('nhif_no'),
                             bank_name=post_data.get('bank_name'),
                             account_no = post_data.get('account_no'),
                             branch = post_data.get('branch'),
                             username = rawusername,
                             password= pw_hash
    )
    db.session.add(employees)
    db.session.commit()

    sendCredentials(userEmail,rawusername)

    return jsonify(response_object)


@app.route('/api/editemployee/<payroll_no>',methods = ['PUT','DELETE'])
def update_deleteEmp(payroll_no):
    response_object = {'status': 'success'}

    if request.method == 'PUT':
        post_data = request.get_json()
        print("at the update ", post_data)

        query = EmployeesRegistration.query.filter(EmployeesRegistration.payroll_no==payroll_no).first()
        if query is not None:
            print("at the query ", query)

            query.surname = post_data.get('surname'),
            query.other_names = post_data.get('other_names'),
            query.appointment_date = post_data.get('appointment_date'),
            query.designation = post_data.get('designation_id'),
            query.entry_salary = post_data.get('entry_salary'),
            query.program = post_data.get('program'),
            query.department = post_data.get('department'),
            query.terms_of_service = post_data.get('terms_of_service'),
            query.dob = post_data.get('dob'),
            query.birth_place = post_data.get('birth_place'),
            query.nationalty = post_data.get('nationalty'),
            query.Passport_idno = post_data.get('Passport_idno'),
            query.marital_status = post_data.get('marital_status'),
            query.spause_name = post_data.get('spause_name'),
            query.spause_idno = post_data.get('spause_idno'),
            query.kra_no = post_data.get('kra_no'),
            query.nssf_no = post_data.get('nssf_no'),
            query.nhif_no = post_data.get('nhif_no'),
            query.bank_name = post_data.get('bank_name'),
            query.account_no = post_data.get('account_no'),
            query.branch = post_data.get('branch'),


            db.session.commit()
            return  jsonify(response_object)
        else:
            print("at the query out ")
            return  jsonify(response_object)




    if request.method == 'DELETE':
        remove_emp(payroll_no)
        print('delete books' + payroll_no)
        response_object['message'] = 'Cadre removed!'
    return jsonify(response_object)


def remove_emp(empid):
    fetch = EmployeesRegistration.query.filter(EmployeesRegistration.employee_id == empid).first()
    fetch.is_deleted = True
    db.session.commit()


@app.route("/api/assignSupervisor", methods=['POST'])
def assignSup():
    post_data = request.get_json()
    print(post_data)
    print("****************")

    for data in post_data:
        emp_payroll_no = data['emp_payroll_no']
        supervisor_id = data['supervisor_id']

        #if employee already assigned supervisor , override do not insert

        alreadyAssigned = StaffSupervisors.query.filter(StaffSupervisors.payroll_no == emp_payroll_no)\
            .filter(StaffSupervisors.is_deleted==0).first()

        if alreadyAssigned is not None:
            print("THE SUP IS NOT NONE")
            return 'do not save already exists '

        else:
            print(supervisor_id)
            print("************")
            saveTescord(supervisor_id, emp_payroll_no)
            update_employee_table(emp_payroll_no)


            return 'well saved '

def saveTescord(supid,empid):
    print(supid)
    saveRecord = StaffSupervisors(supervisor_payroll_no=supid
                                  , payroll_no=empid)

    db.session.add(saveRecord)
    db.session.commit()
    pass

#call this function to update the employee table by setting assign sup to 1
def update_employee_table(emp_payroll_no):

    print("UPADATING EMP TABLE    ",emp_payroll_no)

    getEmp = EmployeesRegistration.query.filter(EmployeesRegistration.payroll_no==emp_payroll_no).first()

    if getEmp is not None:
        getEmp.supervisor_status=True
        db.session.commit()
    pass




@app.route('/api/getAllSupervisors', methods=['GET'])
def getAllSupervisors():

    result = []

    for emp, cadre in db.session.query(EmployeesRegistration,Cadre)\
        .filter(EmployeesRegistration.designation == Cadre.designation_id).all():
        data = {}
        data['employee_id'] = emp.employee_id
        data['payroll_no'] = emp.payroll_no
        data['surname'] = emp.surname
        data['other_names'] = emp.other_names
        data['designation_id'] = emp.designation
        data['designation'] = cadre.designation_name
        data['entry_salary'] = emp.entry_salary
        data['program'] = emp.program
        data['department_id'] = emp.department_id
        data['terms_of_service'] = emp.terms_of_service
        data['dob'] = emp.dob.strftime("%Y-%m-%d")
        data['birth_place'] = emp.birth_place
        data['nationalty'] = emp.nationalty
        data['passport_idno'] = emp.passport_idno
        data['marital_status'] = emp.marital_status
        data['spause_name'] = emp.spause_name
        data['kra_no'] = emp.kra_no
        data['nssf_no'] = emp.nssf_no
        data['nhif_no'] = emp.nhif_no
        data['bank_name'] = emp.bank_name
        data['account_no'] = emp.account_no
        data['branch'] = emp.branch
        data['appointment_date'] = emp.appointment_date.strftime("%Y-%m-%d")
        data['supervisor_status'] = emp.supervisor_status

        result.append(data)



    return jsonify({
        'status': 'success',
        'result': result
    })


@app.route('/api/allSupervisors', methods=['GET'])
def allSupervisors():

    result = []

    for emp, cadre in db.session.query(EmployeesRegistration,Cadre)\
        .filter(EmployeesRegistration.designation == Cadre.designation_id)\
        .filter(EmployeesRegistration.designation<=6).all():
        data = {}
        data['employee_id'] = emp.employee_id
        data['payroll_no'] = emp.payroll_no
        data['surname'] = emp.surname
        data['other_names'] = emp.other_names
        data['designation_id'] = emp.designation
        data['designation'] = cadre.designation_name
        data['entry_salary'] = emp.entry_salary
        data['program'] = emp.program
        data['department_id'] = emp.department_id
        data['terms_of_service'] = emp.terms_of_service
        data['dob'] = emp.dob.strftime("%Y-%m-%d")
        data['birth_place'] = emp.birth_place
        data['nationalty'] = emp.nationalty
        data['passport_idno'] = emp.passport_idno
        data['marital_status'] = emp.marital_status
        data['spause_name'] = emp.spause_name
        data['kra_no'] = emp.kra_no
        data['nssf_no'] = emp.nssf_no
        data['nhif_no'] = emp.nhif_no
        data['bank_name'] = emp.bank_name
        data['account_no'] = emp.account_no
        data['branch'] = emp.branch
        result.append(data)



    return jsonify({
        'status': 'success',
        'result': result
    })

@app.route('/api/getSupervisorEmp/<supid>', methods=['GET'])
def getSupervisorEmp(supid):
    print(" THE SUPLICATION :::: ",supid)

    result = []
    data = {}

   #Note is_deleted is the status of value 0 when the supervisor is assigned and 1 when not assined
    for empSup,emp, cadre in db.session.query(StaffSupervisors, EmployeesRegistration,Cadre)\
        .filter(StaffSupervisors.payroll_no == EmployeesRegistration.payroll_no)\
        .filter(EmployeesRegistration.designation == Cadre.designation_id)\
        .filter(StaffSupervisors.supervisor_payroll_no==supid)\
        .filter(StaffSupervisors.is_deleted==0).all():

        data['id'] = empSup.id
        print("THE SECONE  ",supid)
        data['employee_id'] = emp.employee_id
        data['payroll_no'] = emp.payroll_no
        data['surname'] = emp.surname
        data['other_names'] = emp.other_names
        data['designation_id'] = emp.designation
        data['designation'] = cadre.designation_name
        data['entry_salary'] = emp.entry_salary
        data['program'] = emp.program

        print("the results  ::::",result)


        result.append(data)



    return jsonify({
        'status': 'success',
        'result': result
    })



@app.route("/api/removeSupervisorEmp", methods=['POST'])
def removeSupervisorEmp():
    post_data = request.get_json()

    for data in post_data:
        emp_payroll_no = data['emp_payroll_no']
        supervisor_id = data['supervisor_id']

        print(supervisor_id)
        removeEmpFromEmpTable(emp_payroll_no)
        removeEmpSup(supervisor_id,emp_payroll_no)

    return 'well saved '
def removeEmpSup(supid,empid):

    remove = StaffSupervisors.query.filter_by(supervisor_payroll_no=supid).filter_by(payroll_no=empid)\
        .filter_by(is_deleted=0).first()
    print("TEST REMOVE" ,remove)
    if remove is not  None:
        print("TEST REMOVE")
        remove.is_deleted =1
        db.session.commit()

        removeEmpFromEmpTable(empid)
    pass

#remove employee the supervisor status from the employee table

def removeEmpFromEmpTable(empid):
    print("*************** supervisor_id 1", empid)

    emp = EmployeesRegistration.query.filter(EmployeesRegistration.payroll_no == empid)\
        .filter(EmployeesRegistration.supervisor_status == 1).first()

    if emp is not None:
        emp.supervisor_status = False

        db.session.commit()

    pass



@app.route('/api/getAllStaff', methods=['GET'])
def getAllStaff():

    result = []


    for emp, cadre  in db.session.query(EmployeesRegistration,Cadre)\
        .filter(EmployeesRegistration.designation == Cadre.designation_id)\
            .all():
        data = {}
        data['employee_id'] = emp.employee_id
        data['payroll_no'] = emp.payroll_no
        data['surname'] = emp.surname
        data['other_names'] = emp.other_names
        data['designation_id'] = emp.designation
        data['designation'] = cadre.designation_name
        data['entry_salary'] = emp.entry_salary
        data['program'] = emp.program
        data['department_id'] = emp.department_id
        data['terms_of_service'] = emp.terms_of_service
        data['dob'] = emp.dob.strftime("%Y-%m-%d")
        data['birth_place'] = emp.birth_place
        data['nationalty'] = emp.nationalty
        data['passport_idno'] = emp.passport_idno
        data['marital_status'] = emp.marital_status
        data['spause_name'] = emp.spause_name
        data['kra_no'] = emp.kra_no
        data['nssf_no'] = emp.nssf_no
        data['nhif_no'] = emp.nhif_no
        data['bank_name'] = emp.bank_name
        data['account_no'] = emp.account_no
        data['branch'] = emp.branch
        data['appointment_date'] = emp.appointment_date.strftime("%Y-%m-%d")


        result.append(data)



    return jsonify({
        'status': 'success',
        'result': result
    })

@app.route('/api/getAllStaffAssignedSupervisors/<supid>', methods=['GET'])
def getAllStaffAssignedSupervisors(supid):
    print(supid)

    result = []


    for emp,supvsr,cadre  in db.session.query(EmployeesRegistration,StaffSupervisors,Cadre) \
        .filter(EmployeesRegistration.payroll_no == StaffSupervisors.supervisor_payroll_no ) \
        .filter(StaffSupervisors.supervisor_payroll_no == supid)\
        .filter(Cadre.designation_id ==EmployeesRegistration.designation).all():
        data = {}
        data['employee_id'] = emp.employee_id
        data['payroll_no'] = supvsr.payroll_no
        data['surname'] = emp.surname
        data['other_names'] = emp.other_names
        data['designation_id'] = emp.designation
        data['entry_salary'] = emp.entry_salary
        data['program'] = emp.program
        data['department_id'] = emp.department_id
        data['terms_of_service'] = emp.terms_of_service
        data['designation'] = cadre.designation_name
        data['dob'] = emp.dob.strftime("%Y-%m-%d")
        data['birth_place'] = emp.birth_place
        data['nationalty'] = emp.nationalty
        data['passport_idno'] = emp.passport_idno
        data['marital_status'] = emp.marital_status
        data['spause_name'] = emp.spause_name
        data['kra_no'] = emp.kra_no
        data['nssf_no'] = emp.nssf_no
        data['nhif_no'] = emp.nhif_no
        data['bank_name'] = emp.bank_name
        data['account_no'] = emp.account_no
        data['branch'] = emp.branch
        data['appointment_date'] = emp.appointment_date.strftime("%Y-%m-%d")
        data['supervisor'] = supvsr.supervisor_payroll_no

        result.append(data)
    print(result)



    return jsonify({
        'status': 'success',
        'result': result
    })


@app.route('/api/getAllSupervisorsList', methods=['GET'])
def getAllSupervisorsList():

    result = []


    for emp, cadre in db.session.query(EmployeesRegistration,Cadre)\
        .filter(EmployeesRegistration.designation == Cadre.designation_id)\
        .filter(EmployeesRegistration.designation <=3).all():
        data = {}
        data['employee_id'] = emp.employee_id
        data['payroll_no'] = emp.payroll_no
        data['surname'] = emp.surname
        data['other_names'] = emp.other_names
        data['designation_id'] = emp.designation
        data['designation'] = cadre.designation_name
        data['entry_salary'] = emp.entry_salary
        data['program'] = emp.program
        data['department_id'] = emp.department_id
        data['terms_of_service'] = emp.terms_of_service
        data['dob'] = emp.dob.strftime("%Y-%m-%d")
        data['birth_place'] = emp.birth_place
        data['nationalty'] = emp.nationalty
        data['passport_idno'] = emp.passport_idno
        data['marital_status'] = emp.marital_status
        data['spause_name'] = emp.spause_name
        data['kra_no'] = emp.kra_no
        data['nssf_no'] = emp.nssf_no
        data['nhif_no'] = emp.nhif_no
        data['bank_name'] = emp.bank_name
        data['account_no'] = emp.account_no
        data['branch'] = emp.branch
        data['appointment_date'] = emp.appointment_date.strftime("%Y-%m-%d")

        result.append(data)
        print(result)



    return jsonify({
        'status': 'success',
        'result': result
    })

@app.route('/api/addLeaveBalance', methods = ['POST'])
def leaveBalance():
    post_data = request.get_json()
    print(post_data)
    response_object={'success':'Added successfully'}

    payroll_no= post_data.get('payroll_no')

    print("the prl  ",payroll_no)



    query = InitialLeaveBalane.query.filter(InitialLeaveBalane.payroll_no==payroll_no).first()
    #print('zero', query)

    if query is  None:
        print('one',query)

        addBal=InitialLeaveBalane(payroll_no=post_data.get('payroll_no'),
                       initial_balance=post_data.get('leave_balance'))

        db.session.add(addBal)
        db.session.commit()

    else:
        print('two', query)
        query.initial_balance=post_data.get('leave_balance')


        db.session.commit()

    return jsonify(response_object)

@app.route('/api/getAllBalance', methods=['GET'])
def getAllBalance():

    result = []


    for emp, cadre in db.session.query(EmployeesRegistration,Cadre)\
        .filter(EmployeesRegistration.designation == Cadre.designation_id).all():
        data = {}

        balance = InitialLeaveBalane.query.filter(InitialLeaveBalane.payroll_no==emp.payroll_no).first()

        if balance is None:
            data['leave_balance'] ="Not Assined Balance"
        else:
            data['leave_balance'] = balance.initial_balance

        data['employee_id'] = emp.employee_id
        data['payroll_no'] = emp.payroll_no
        data['surname'] = emp.surname
        data['other_names'] = emp.other_names
        data['designation_id'] = emp.designation
        data['designation'] = cadre.designation_name
        data['entry_salary'] = emp.entry_salary
        data['program'] = emp.program
        data['department_id'] = emp.department_id
        data['terms_of_service'] = emp.terms_of_service
        data['dob'] = emp.dob.strftime("%Y-%m-%d")
        data['birth_place'] = emp.birth_place
        data['nationalty'] = emp.nationalty
        data['passport_idno'] = emp.passport_idno
        data['marital_status'] = emp.marital_status
        data['spause_name'] = emp.spause_name
        data['kra_no'] = emp.kra_no
        data['nssf_no'] = emp.nssf_no
        data['nhif_no'] = emp.nhif_no
        data['bank_name'] = emp.bank_name
        data['account_no'] = emp.account_no
        data['branch'] = emp.branch
        data['appointment_date'] = emp.appointment_date.strftime("%Y-%m-%d")

        result.append(data)

    return jsonify({
        'status': 'success',
        'result': result
    })


def sendCredentials(email,username):
    print(email)


    print('SENDING EMAIL HERE')
    msg = Message(subject="Faces Leave application system credentials",
                    sender="agikedwin@gmail.com",
                    recipients=[email],  # replace with your email for testing
                    body="Use the following credentials to login to FACES LEAVE MANGEMENT SYSTEM. "+"Username:  "+username+  ", Password:  "+username)
    mail.send(msg)
    return "Sent"
