from app import app
from flask import request, jsonify,session,current_app,g
from models.models import *
from initializer import *
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import uuid
from flask_cors import cross_origin
from initializer import *
import uuid
from functools import update_wrapper, wraps
import jwt
import datetime
from routes.testDate import testSession




@app.route("/api/userLogin",methods=['POST','GET'])
def getUser():


    response_msg =""
    #response_object = {'status': 'success'}
    post_data = request.get_json()
    print(post_data)
    username= ""
    hash_pwd= ""
    raw_password =post_data.get('password')
    raw_username = post_data.get('username')
    print('Username')
    print(raw_username)


    #usernames must be unique
    userExists = EmployeesRegistration.query.\
        filter(EmployeesRegistration.username == raw_username).first()
        #.filter(EmployeesRegistration.password == pw_hash).first()
    print("here")


    if userExists :
        username = userExists.username
        hash_pwd = userExists.password
        print('Username 2')
        print(userExists.password)
        valid_pwd=comparePasswords(userExists.password,raw_password,userExists)
        if valid_pwd:

            print(valid_pwd)
            supervisorState = checkSupExist(userExists.payroll_no)
            print('Username HERE 000000 ')
            print(supervisorState)
            if supervisorState is True:
                genToken = gettoken(userExists.password)
                session['username'] = userExists.username
                session.permanent = True
                response_msg = {'login_state':"Login successful", 'token':genToken,'user_id':userExists.payroll_no,
                                'user_details':{'designation':userExists.designation,'payroll_no':userExists.payroll_no,
                                'other_names':userExists.other_names,'surname':userExists.surname,
                                'username':userExists.username,'appointment_date':userExists.appointment_date.strftime("%Y-%m-%d"),
                                'department_id':userExists.department_id}}
                insertUserActivities(genToken)
                #return jsonify(response_msg)
            else:
                print("print false 777")
                #no supervisor
                response_msg={'login_state':'False'}

                #return jsonify(response_msg)


        else:
            response_msg = {'login_state':"Login Failed"}
            #return jsonify(response_msg)
    else:
        print('Wrong username::::::::::')
        response_msg = {'login_state':"Username or passward is wrong "}
        print("TEST **** ", response_msg)
    return jsonify(response_msg)

def comparePasswords(password,username,obj):
    authenticate=False
    compare_pwd = flask_bcrypt.check_password_hash(password,username)
    print(compare_pwd)
    if compare_pwd:
        login_user(obj)
        print("-0------------------------Jamaa ameshalogiwa in")

        if current_user.is_authenticated:
            print(current_user)
            print('ako authenticated')
        else:
            print('hayuko authenticated')


        authenticate=True


    else:
        authenticate=False


    return authenticate

def insertUserActivities(token):
    session['uuid'] = uuid.uuid4()
    session['gid'] = current_user.employee_id
    session.permanent = True
    session.expire_on_commit = False
    #print("TOKEN AT USER ACTIVITY  ::", token)
    data = jwt.decode(token, verify=False)
    login_timestamp = login_activity(payroll_no=current_user.payroll_no,
                                     account_status='active',
                                     token=data['sub'],
                                     ip_address=request.remote_addr,
                                     user_agent=request.user_agent.string
                                     )
    db.session.add(login_timestamp)
    db.session.commit()



def cors(f):
    def wrapper(*args, **kwargs):
        origin = request.headers.get('Access-Control-Allow-Origin')
        if origin == '23456agik':
            return f(*args, **kwargs)
    return update_wrapper(wrapper, f)

def auth(f):
    def wrapper(*args, **kwargs):
        #print("AT AUTHENTICATION HERE################")
        auth = request.headers.get('Authorization')

        auth_headers = auth.split('.')

        if auth == 'loginrequired':
            return jsonify({'message': 'Please log in to continue'})
        else:
            invalid_msg = {
                'message': 'Invalid token. Registeration and / or authentication required',
                'authenticated': False
            }
            expired_msg = {
                'message': 'Expired token. Reauthentication required.',
                'authenticated': False
            }

            if len(auth_headers) != 3:
                return jsonify(invalid_msg), 401
            try:
                data = jwt.decode(auth, current_app.config['SECRET_KEY'])
                user = EmployeesRegistration.query.filter_by(username=data['surname']).first()
                if user:
                    return f(*args, **kwargs)
                return jsonify({'message': 'User not found'})
            except jwt.ExpiredSignatureError:
                return jsonify(expired_msg), 401  # 401 is Unauthorized HTTP status code
            except (jwt.InvalidTokenError, Exception) as e:
                print(e)
                return jsonify(invalid_msg), 401
    return update_wrapper(wrapper, f)

def gettoken(payroll_no):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=20000),
            'iat': datetime.datetime.utcnow(),
            'sub': payroll_no
        }
        token = jwt.encode(
            payload,
            'test1234',
            algorithm='HS256'
        )

        return token.decode('UTF-8')
    except Exception as e:
        return e

def getUserId():
    #print("reached here AT GET LOGED")
    token = request.headers['Authorization']
    #print("THE TOKEN AT LOGIN ", token)

   # print(token)
    data = jwt.decode(token, verify=False)
   #S print('token  :',data)
    user = login_activity.query.filter_by(token=data['sub']).first()


    return  user.payroll_no

@app.route("/api/checkPwdvalid", methods=['GET','POST'])
def checkPwdvalid():
    print("REACHED CHANGE PWD")
    post_data = request.get_json()
    print(post_data)
    current_password = post_data.get('current_password')
    print("HERE ",post_data.get('current_password'))

    loginUser = getUserId()

    #get password stored in db
    getPassword = EmployeesRegistration.query.filter(EmployeesRegistration.payroll_no == loginUser).first()
    print("THE TEST PWD ", getPassword.password)

    #compare passwords

    compare_pwd = flask_bcrypt.check_password_hash(getPassword.password, current_password)

    print("THE TEST PWD ::::::::::  ", compare_pwd)


    print("USER  ############", loginUser)
    if compare_pwd:
        return jsonify({'state':'valid'})
    else:
        return jsonify({'state':'invalid'})


@app.route("/api/changepwd",methods=['GET','POST'])
def changepwd():
    post_data = request.get_json()
    print(post_data)
    loginUser = getUserId()
    new_password = post_data.get('new_password')
    new_username = post_data.get('new_username')
    print("HERE ", post_data.get('current_password'))

    pw_hash = flask_bcrypt.generate_password_hash(new_password)

    queryUser = EmployeesRegistration.query.filter(EmployeesRegistration.payroll_no == loginUser).first()
    print("USER ",queryUser)

    if queryUser is not None:
        #check if username already taken
        if queryUser.username == new_username:
            return jsonify({'state':'exists'})
        else:
            print("USERNAME ",queryUser.username)
            queryUser.username= new_username
            queryUser.password = pw_hash
            print("PWD changed ")
            db.session.commit()
            return  jsonify({'state': 'successfull'})

    else:
        print("PWD failed ")
        return  jsonify({'state':'Failed'})



#check if supervisor exists

def checkSupExist(emp_payroll_no):

   print("AT check sup exists emp_payroll_no" ,emp_payroll_no)

   #if the user is a default user , do not check if the is assigned

   if emp_payroll_no == 10101:

       return True

   else:

       getSup = StaffSupervisors.query.filter(StaffSupervisors.payroll_no == emp_payroll_no)\
           .filter(StaffSupervisors.is_deleted==0).first()

       if getSup is not None:
           print("AT check sup exists 33" ,getSup)
           return  True

       else:
           print("AT check sup exists 11", getSup)
           return False
