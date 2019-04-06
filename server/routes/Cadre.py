from  flask import flash, jsonify, request
from  app import  app
from  models.models import *
from datetime import datetime
from routes.Login import *




@app.route('/api/getAllDesignations', methods=['GET'])
#@auth
def getAllDesig():
    result = []

    for desig, dep in db.session.query(Cadre, Departments)\
            .filter(Cadre.department_id == Departments.department_id)\
            .filter(Cadre.is_deleted==0).all():

        data = {}
        data['designation_id'] = desig.designation_id
        data['designation_name'] = desig.designation_name
        data['description'] = desig.description
        data['department_id'] = dep.department_name
        data['level'] = desig.level

        result.append(data)



    return jsonify({
        'status': 'success',
        'result': result
    })



def DesnArray(object):
    result =[]

    for designations in object:
        data ={}
        data['designation_id'] =designations.designation_id
        data['designation_name']= designations.designation_name
        data['description'] = designations.description
        data['department_id'] = designations.department_id
        data['level'] = designations.level


        result.append(data)
    return result


@app.route('/api/addDesignation', methods=['POST'])
def addDesig():
    response_object = {}

    post_data = request.get_json()
    designation =Cadre(designation_name = post_data.get('name'),
                       description = 'description',
                       department_id=post_data.get('department_id'),
                       level=2
                       )
    db.session.add(designation)
    db.session.commit()
    response_object = {'status': 'success', 'msg': 'Record successfully saved'}

    return jsonify(response_object)


@app.route('/api/designation/<desgn_id>',methods = ['PUT','DELETE'])
def upadte_deleteDesig(desgn_id):
    response_object = {'status': 'success'}

    if request.method == 'PUT':
        post_data = request.get_json()
        print(post_data)

        query = Cadre.query.filter(Cadre.designation_id == desgn_id).first()
        query.designation_name = post_data.get('name'),
        query.department_id = post_data.get('department_id')
        query.date_updated = now
        db.session.commit()

    response_object['message'] = 'Cadre updated!'
    if request.method == 'DELETE':
        remove_desn(desgn_id)
        print('delete desn' + desgn_id)
        response_object['message'] = 'Cadre removed!'
    return jsonify(response_object)


def remove_desn(desgn_id):
    fetchdesign = Cadre.query.filter(Cadre.designation_id == desgn_id).first()
    fetchdesign.is_deleted = True
    db.session.commit()


@app.route("/api/getSingleCadre/<cadreid>", methods=['GET'])
def getSingleCadre(cadreid):
    print("ID CADRE ",cadreid)

    query = Cadre.query.filter(Cadre.designation_id == cadreid).first()
    print(" RETURN ", query.designation_name)

    return jsonify({'cadre':query.designation_name})







