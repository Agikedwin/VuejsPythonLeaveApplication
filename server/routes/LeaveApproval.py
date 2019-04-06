from  flask import flash, jsonify, request
from  app import  app
from  models.models import *
from datetime import datetime
from initializer import mail,Message

now = datetime.now()


@app.route('/api/getAllAprovals', methods=['GET'])
def getAllApprovals():

    fetch = db.session.query(LeaveApproval).all()
    aprovals =fetch(fetch)


    return jsonify({
        'status': 'success',
        'result': aprovals
    })



def aprovalsArray(object):
    result =[]

    for aprovals in object:
        data ={}
        data['approval_id'] =aprovals.approval_id
        data['application_id']= aprovals.application_id
        data['payroll_no'] = aprovals.payroll_no
        data['aproval_status'] = aprovals.aproval_status
        data['note'] = aprovals.note
        data['date_created'] = now

        result.append(data)
    return result


@app.route('/api/addApprovals', methods=['POST'])
def addApprovals():
    post_data = request.get_json()
    response_object = {'status': 'success'}


    payroll_no = post_data.get('payroll_no')
    approval_status = post_data.get('leave_status')
    application_id = post_data.get('application_id')
    next_person = post_data.get('nextPersonToApprove')
    print("APPROVE STATUS********::: ",post_data )
    if next_person == 0:
        #insert and approve leave(update status to 1)
        print("AT UPDATE APP STATUS  0")
        leaveApproval =LeaveApproval(application_id = post_data.get('application_id'),
                                 payroll_no = payroll_no,
                                 next_person_to_approve=post_data.get('nextPersonToApprove'),
                                 aproval_status=approval_status,
                                 note=post_data.get('note'))
        db.session.add(leaveApproval)
        db.session.commit()
        #update leave application to finalize the approval
        updateApplicationStatus(application_id,approval_status)
        return jsonify(response_object)

    else:
        #insert but do not approve, wait for the next supervisor to approve(do not update staus to 1)
        print("AT UPDATE APP STATUS 1")
        leaveApproval = LeaveApproval(application_id=post_data.get('application_id'),
                                      payroll_no=payroll_no,
                                      next_person_to_approve= post_data.get('nextPersonToApprove'),
                                      aproval_status=approval_status,
                                      note=post_data.get('note'))
        db.session.add(leaveApproval)
        db.session.commit()
        #update the leave application to decline val 2

        updateApplicationStatus(application_id,approval_status)
        sendEmailNotification()
        response_object = {'status': 'success'}
        return jsonify(response_object)

def updateApplicationStatus(id,approval_status):
    print("AT UPDATE APP STATUS **************b" , approval_status)

    updateApplication = LeaveApplications.query.filter(LeaveApplications.application_id == id).first()

    if updateApplication:
        response_object = {'status': 'success'}

        #leave declined
        updateApplication.approved = approval_status
        db.session.commit()

        pass
    else:
        print("AT UPDATE APP STATUS outside")

        response_object = {'status': 'Failed'}
        print('failed**********')
        pass


@app.route('/api/approvals/<appid>',methods = ['PUT','DELETE'])
def upadte_delete_approvals(appid):
    response_object = {'status': 'success'}
    post_data = request.get_json()
    print("ID ",appid)
    print("DATA ",post_data)

    if post_data is not  None and request.method == 'PUT':

        #leave_state = post_data.get('leave_status')

        query = LeaveApplications.query.filter(LeaveApplications.application_id==appid).first()
        query.approve = 2
        db.session.commit()

        approveQuery = LeaveApproval(application_id=post_data.get('application_id'),
                                      payroll_no=post_data('payroll_no'),
                                      next_person_to_approve= post_data.get('nextPersonToApprove'),
                                      aproval_status=2,
                                      note=post_data.get('note'))
        db.session.add(approveQuery)
        db.session.commit()



    response_object['message'] = 'LeaveApproval updated!'
    if request.method == 'DELETE':
        remove_aproval(appid)
        print('delete books' + appid)
        response_object['message'] = 'LeaveApproval removed!'
    return jsonify(response_object)


def remove_aproval(appid):
    fetch = LeaveApproval.query.filter(LeaveApproval.approval_id == appid).first()
    fetch.is_deleted = True
    db.session.commit()


def sendEmailNotification():
   print('SENDING EMAIL HERE')
   msg = Message(subject="Hello",
                 sender="agikedwin@gmail.com",
                 recipients=["rickysilas7@gmail.com"],  # replace with your email for testing
                 body="Dear Mel, Your leave application has bee approved , you can proceed!")
   mail.send(msg)
   return "Sent"



