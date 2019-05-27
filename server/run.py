from routes.departments import *
from routes.EmployeeRegistration import *
from routes.Cadre import *
from routes.LeaveTypes import *
from routes.LeaveApplications import *
from routes.general import *
from routes.LeaveApproval import *
#from  auths.appAuth import *
from routes.testDate import *
from  routes.Login import *
from  routes.Holidays import *
from  routes.AccumulatedAnnualLeavedays import *

from initializer import  app

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0')