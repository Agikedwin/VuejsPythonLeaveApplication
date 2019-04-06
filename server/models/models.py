import datetime
from app import app
from  initializer import db
from datetime import datetime

from flask import g
from flask_login import UserMixin, LoginManager

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'index'
login_manager.session_protection = "strong"

now = datetime.now()

current_date = now.strftime("%Y-%m-%d")
from initializer import flask_bcrypt

def defaultUser():

    payroll_no = 10101
    rawusername = "LeaveAdmin@" + "10101"
    print("ROW USERNAME ", rawusername)
    pw_hash = flask_bcrypt.generate_password_hash(rawusername)

    print(pw_hash)
    response_object = {'status': 'success'}

    query = db.session.query(EmployeesRegistration).filter(EmployeesRegistration.payroll_no == payroll_no).first()

    if query is  None:
        print("Inserting default user...")

        employees = EmployeesRegistration(payroll_no=10101,
                                          surname="Admin",
                                          other_names="Leave System",
                                          appointment_date="2004-12-01 00:00:00",
                                          designation=1,
                                          entry_salary=500000,
                                          program="Faces",
                                          department_id=1,
                                          terms_of_service="Permanent",
                                          dob="2004-12-01 00:00:00",
                                          birth_place="Mbita",
                                          nationalty="Kenyan",
                                          passport_idno="27358109",
                                          marital_status="Single",
                                          email="eagik@kemri-ucsf.org",
                                          phone_no="0780698944",
                                          spause_name="JK",
                                          spause_idno="9090909",
                                          kra_no="",
                                          nssf_no="",
                                          nhif_no="",
                                          bank_name="",
                                          account_no="",
                                          branch="",
                                          username=rawusername,
                                          password=pw_hash
                                          )
        db.session.add(employees)
        db.session.commit()

    pass


class Departments(db.Model):
    """Model for the stations table"""
    __tablename__ = 'departments'

    department_id = db.Column(db.Integer, primary_key = True)
    department_name = db.Column(db.String(300),  nullable=False)
    description= db.Column(db.String(100),  nullable=True)
    is_deleted = db.Column(db.Boolean(), default=False)

    userid = db.Column(db.Integer, nullable=False,default='001')
    editor = db.Column(db.String(20), nullable=True,default='001')
    date_created = db.Column(db.DateTime, nullable=True, default=now)
    date_updated = db.Column(db.DateTime, nullable=True, default=now)


    def __repr__(self):
        return self.department_id

class EmployeesRegistration(UserMixin,db.Model):



    __tablename__ ='employee_registration'



    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    payroll_no = db.Column(db.Integer,primary_key=True, unique=True)
    surname = db.Column(db.String(50), nullable=False)
    other_names = db.Column(db.String(100), nullable=True)
    appointment_date = db.Column(db.DateTime, default=now, nullable=True)
    designation = db.Column(db.String(100), nullable=True)
    dob = db.Column(db.DateTime, nullable=True)
    entry_salary = db.Column(db.String(100), nullable=True)
    department_id = db.Column(db.Integer,  nullable=True)
    program = db.Column(db.String(100), nullable=True)
    terms_of_service = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    phone_no = db.Column(db.String(100), nullable=True)
    birth_place = db.Column(db.String(100), nullable=True)
    nationalty = db.Column(db.String(100), nullable=True)
    passport_idno = db.Column(db.String(100), nullable=True)
    marital_status = db.Column(db.String(100), nullable=True)
    spause_name = db.Column(db.String(100), nullable=True)
    spause_idno = db.Column(db.String(100), nullable=True)
    kra_no = db.Column(db.String(100), nullable=True)
    nssf_no = db.Column(db.String(100), nullable=True)
    nhif_no = db.Column(db.String(100), nullable=True)
    bank_name = db.Column(db.String(100), nullable=True)
    branch = db.Column(db.String(100), nullable =True)
    account_no = db.Column(db.String(100), nullable=True)
    supervisor_status = db.Column(db.Boolean(),default=False, nullable=True)
    date_created = db.Column(db.DateTime, nullable=True, default=now)
    is_deleted = db.Column(db.Boolean(), default=False)
    userid = db.Column(db.Integer, nullable=False, default='001')
    editor = db.Column(db.String(20), nullable=True, default='001')
    date_created = db.Column(db.DateTime, nullable=True, default=now)
    date_updated = db.Column(db.DateTime, nullable=True, default=now)
    username = db.Column(db.String(150), nullable=False)
    password = db.Column(db.Text, nullable = False)
    resev1 = db.Column(db.String(100), nullable=True)
    presev12 = db.Column(db.String(100), nullable=True)
    resev13 = db.Column(db.String(100), nullable=True)
    presev14 = db.Column(db.String(100), nullable=True)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.username

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def __repr__(self):
        return self.username

    def __repr__(self):
        return self.username

    @login_manager.user_loader
    def load_user(username):
        '''
        :param email:
        :return: user object
        '''
        return EmployeesRegistration.query.filter_by(username=username).first()

class Cadre(db.Model):
    __tablename__ = 'designation'

    designation_id = db.Column(db.Integer, primary_key =True,autoincrement=True)
    designation_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=True)
    code = db.Column(db.String(50), nullable=True)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.department_id'), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    is_deleted = db.Column(db.Boolean(), default=False)

    userid = db.Column(db.Integer, nullable=False,default='001')
    editor = db.Column(db.String(20), nullable=True,default='001')
    date_created = db.Column(db.DateTime, nullable=True, default=now)
    date_updated = db.Column(db.DateTime, nullable=True, default=now)

    def __repr__(self):
        return self.designation_id


class LeaveTypes(db.Model):
    __tablename__ = 'leave_types'

    leave_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    leave_name = db.Column(db.String(50), nullable=False)
    no_days = db.Column(db.Integer, nullable=False)
    countinous = db.Column(db.Boolean(), default=False)
    is_deleted = db.Column(db.Boolean(), default=False)
    userid = db.Column(db.Integer, nullable=False,default='001')
    editor = db.Column(db.String(20), nullable=True,default='001')
    date_created = db.Column(db.DateTime, nullable=True, default=now)
    date_updated = db.Column(db.DateTime, nullable=True, default=now)

    #def __repr__(self):
        #return self.leave_id


class LeaveApplications(db.Model):
    __tablename__ = 'leave_applications'

    application_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    leave_id = db.Column(db.Integer, db.ForeignKey('leave_types.leave_id'), nullable=False)
    payroll_no = db.Column(db.Integer, db.ForeignKey('employee_registration.payroll_no'), nullable=False)
    date_from = db.Column(db.Date, nullable=True, default=current_date)
    date_to = db.Column(db.Date, nullable=True, default=current_date)
    approved = db.Column(db.Integer, default = False)
    leave_status = db.Column(db.Integer, default=0, nullable=False)
    application_note = db.Column(db.String(300),nullable =True)
    date_applied = current_date,
    is_deleted = db.Column(db.Boolean(), default=False)

    userid = db.Column(db.Integer, nullable=False,default='001')
    editor = db.Column(db.String(20), nullable=True,default='001')
    date_created = db.Column(db.DateTime, nullable=True, default=now)
    date_updated = db.Column(db.DateTime, nullable=True, default=now)

    def __repr__(self):
        return self.application_id

class LeaveReliever(db.Model):
    __tablename__ = 'leave_reliever'

    reliever_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    leave_id = db.Column(db.Integer, db.ForeignKey('leave_types.leave_id'), nullable=False)
    payroll_no = db.Column(db.Integer, db.ForeignKey('employee_registration.payroll_no'), nullable=False)
    reliever_payroll_no = db.Column(db.Integer, db.ForeignKey('employee_registration.payroll_no'), nullable=False)
    date_from = db.Column(db.Date, nullable=True, default=current_date)
    date_to = db.Column(db.Date, nullable=True, default=current_date)
    relieve_status = db.Column(db.Integer, default=0, nullable=False)
    application_note = db.Column(db.String(300), nullable=True)
    date_applied = current_date,
    is_deleted = db.Column(db.Boolean(), default=False)

    userid = db.Column(db.Integer, nullable=False, default='001')
    editor = db.Column(db.String(20), nullable=True, default='001')
    date_created = db.Column(db.DateTime, nullable=True, default=now)
    date_updated = db.Column(db.DateTime, nullable=True, default=now)

    def __repr__(self):
        return self.reliever_id


# Create Login_Activity
class login_activity(db.Model):
    __tablename__ = 'login_activity'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    payroll_no = db.Column(db.String(80), nullable=False)
    # employee = db.relationship('Employee')
    token=db.Column(db.Text,nullable=True)
    account_status = db.Column(db.String(80), nullable=False)
    login_timestamp = db.Column(db.DateTime)
    logout_timestamp = db.Column(db.DateTime)
    ip_address = db.Column(db.String(80), nullable=False)
    user_agent = db.Column(db.String(300), nullable=False)
    uuid = db.Column(db.String(80), nullable=True)
    is_deleted = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        return self.payroll_no,




class LeaveApproval(db.Model):
    __tablename__ = 'leave_approval'

    approval_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    application_id = db.Column(db.Integer, db.ForeignKey('leave_applications.application_id'),  nullable=False)
    payroll_no = db.Column(db.Integer,  db.ForeignKey('employee_registration.payroll_no'), nullable=False)
    next_person_to_approve = db.Column(db.Integer,   nullable=False)
    aproval_status = db.Column(db.Integer , nullable=False)
    note = db.Column(db.String(350),  nullable=False)
    is_deleted = db.Column(db.Boolean(), default=False)

    userid = db.Column(db.Integer, nullable=False,default='001')
    editor = db.Column(db.String(20), nullable=True,default='001')
    date_created = db.Column(db.DateTime, nullable=True, default=now)
    date_updated = db.Column(db.DateTime, nullable=True, default=now)

    def __repr__(self):
        return self.approval_id

class StaffSupervisors(db.Model):
    __tablename__ = 'staff_supervisors'

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    supervisor_payroll_no =db.Column(db.Integer , nullable=False)
    payroll_no = db.Column(db.Integer, db.ForeignKey('employee_registration.payroll_no'), primary_key=True, nullable=False)

    note = db.Column(db.String(350), nullable=True)
    is_deleted = db.Column(db.Boolean(), default=False)

    userid = db.Column(db.Integer, nullable=False, default='001')
    editor = db.Column(db.String(20), nullable=True, default='001')
    date_created = db.Column(db.DateTime, nullable=True, default=now)
    date_updated = db.Column(db.DateTime, nullable=True, default=now)

class LeaveAuthorization(db.Model):
    __tablename__ ='leave_authorization'

    auth_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    supervisor_payroll_no = db.Column(db.Integer, db.ForeignKey('employee_registration.payroll_no'), nullable=False)
    emp_payroll_no = db.Column(db.Integer, nullable=False)
    leave_application_id = db.Column(db.Integer, nullable=False)
    leave_id = db.Column(db.Integer, nullable=False)
    auth_stage = db.Column(db.Integer, nullable=False)

    note = db.Column(db.String(350), nullable=True)
    is_deleted = db.Column(db.Boolean(), default=False)

    userid = db.Column(db.Integer, nullable=False, default='001')
    editor = db.Column(db.String(20), nullable=True, default='001')
    date_created = db.Column(db.DateTime, nullable=True, default=now)
    date_updated = db.Column(db.DateTime, nullable=True, default=now)



class Holidays(db.Model):
    """Model for the stations table"""
    __tablename__ = 'public_holidays'

    holiday_id = db.Column(db.Integer, primary_key = True)
    holiday_name = db.Column(db.String(100),  nullable=False)
    holiday_date = db.Column(db.Date, nullable=True, default=current_date)
    is_deleted = db.Column(db.Boolean(), default=False)

    userid = db.Column(db.Integer, nullable=False,default='001')
    editor = db.Column(db.String(20), nullable=True,default='001')
    date_created = db.Column(db.DateTime, nullable=True, default=now)
    date_updated = db.Column(db.DateTime, nullable=True, default=now)


    def __repr__(self):
        return self.holiday_id


class InitialLeaveBalane(db.Model):
    """Model for the stations table"""
    __tablename__ = 'initial_leave_balance'

    balance_id = db.Column(db.Integer, primary_key = True)
    payroll_no=db.Column(db.Integer, db.ForeignKey('employee_registration.payroll_no'), nullable=False)

    initial_balance = db.Column(db.Integer,  nullable=False)
    is_deleted = db.Column(db.Boolean(), default=False)

    userid = db.Column(db.Integer, nullable=False,default='001')
    editor = db.Column(db.String(20), nullable=True,default='001')
    date_created = db.Column(db.DateTime, nullable=True, default=now)
    date_updated = db.Column(db.DateTime, nullable=True, default=now)






#db.drop_all()
db.create_all()
defaultUser()

"""
class Books(db.Model):
    __tablename__ = 'books'

    id =db.Column(db.Integer, primary_key=True, autoincrement=True)
    uuid = db.Column(db.String(200),nullable=True)
    title = db.Column(db.String(200),nullable=True)
    author = db.Column(db.String(200),nullable=True)
    read = db.Column(db.String(200),nullable=True)
    is_deleted = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        return self.title
class SkuCategory(db.Model):
    __tablename__ ='sku_categories_registration'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    skucategoryid = db.Column(db.String(100), primary_key=True, nullable=False)
    skucategoryname = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(100), nullable=True)
    is_deleted = db.Column(db.Boolean(), default=False)
    userid = db.Column(db.Integer, nullable=False),
    editor = db.Column(db.String(20),nullable=True)
    date_created = db.Column(db.DateTime, nullable=True, default=now)
    date_updated = db.Column(db.DateTime, nullable=True, default=now)



class SkuRegistration(db.Model):
    __tablename__ ='sku_registration'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    skuid = db.Column(db.String(100), primary_key=True, nullable=True)
    skucategoryid = db.Column(db.String(100), db.ForeignKey('sku_categories_registration.skucategoryid'), nullable=False)
    skuname = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    retailprice = db.Column(db.Integer, nullable=False)
    wholesaleprice = db.Column(db.Integer, nullable=False)
    reorderlevel = db.Column(db.Integer)
    is_deleted = db.Column(db.Boolean(), default=False)
    userid = db.Column(db.Integer, nullable=True)
    editor = db.Column(db.String(20), nullable=True)
    date_created = db.Column(db.DateTime, nullable=True, default=now)
    date_updated = db.Column(db.DateTime, nullable=True, default=now)

class Stocking(db.Model):
    __tablename__ ='sku_stocking'

    id = db.Column(db.Integer, autoincrement=True)
    stockid = db.Column(db.String(25), primary_key=True, nullable=False)
    skuid = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    priceperunit = db.Column(db.Float, nullable=True)
    orderdate = db.Column(db.DateTime(), nullable = False)
    is_deleted = db.Column(db.Boolean(), default=False)
    userid = db.Column(db.String(20))
    date_created = db.Column(db.DateTime, nullable=False)
    date_updated = db.Column(db.DateTime, nullable=False)




class SkuSales(db.Model):
    __tablename__ ='sku_sales'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    orderid = db.Column(db.String(25), nullable=True)
    skuid = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    priceperunit = db.Column(db.Float, nullable=True)
    buyingprice = db.Column(db.Float, nullable=False)
    vat = db.Column(db.Float, nullable=False)
    mode = db.Column(db.String(25))
    customerid = db.Column(db.String(25))
    is_deleted = db.Column(db.Boolean(), default=False)
    userid = db.Column(db.String(20))
    date_created = db.Column(db.DateTime, nullable=False)
    date_updated = db.Column(db.DateTime, nullable=False)
"""

