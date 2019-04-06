
from flask import url_for, request, redirect, session, flash, g, render_template, jsonify, make_response, current_app
from flask_cors import cross_origin
import uuid
from functools import update_wrapper, wraps
from datetime import timedelta
import datetime
import json
from app import  app
import jwt


def cors(f):
    print('HERE ####################### 2222')
    def wrapper(*args, **kwargs):
        print('HERE ####################### ***********')
        origin = request.headers.get('Access-Control-Allow-Origin')
        print(origin)
        if origin == '2y$17$epybOfmF':
            return f(*args, **kwargs)
    return update_wrapper(wrapper, f)

def auth(f):
    def wrapper(*args, **kwargs):
        print('HERE #######################')
        auth = request.headers.get('Authorization')
        print('Auth ',auth)

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
                user = True
                if user:
                    return f(*args, **kwargs)
                return jsonify({'message': 'User not found'})
            except jwt.ExpiredSignatureError:
                return jsonify(expired_msg), 401  # 401 is Unauthorized HTTP status code
            except (jwt.InvalidTokenError, Exception) as e:
                print(e)
                return jsonify(invalid_msg), 401
    return update_wrapper(wrapper, f)

@app.route('/api/auth', methods=['POST'])

def loginofficer():
    print('HERE ####################### &&&&&&&&&&&&&&&&&7')

    return 'SUCCESS'
"""
from  server.app import  app
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    basestring = str
    print('cross domain &&&&&&&&& 2')
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        print('cross domain &&&&&&&&& 3')
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            print('cross domain &&&&&&&&& 3')
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

"""
@app.route('/my_service', methods=['GET', 'OPTIONS'])
@auth
def my_service():
    print('SUCCESS')
    return 'cross domain ftw'