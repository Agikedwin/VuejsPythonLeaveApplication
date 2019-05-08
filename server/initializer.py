"""
from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:admin@localhost:5432/pythonvuedb'
db.init_app(app)

# enable CORS
CORS(app)


"""
from app import app
import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from routes.routes import *

from flask_mail import Mail, Message
from datetime import date, timedelta


#Sending Email settings
app.config['SECRET_KEY'] = '23456agik'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@localhost/flask_app_db'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'agikedwin@gmail.com'  # enter your email here
app.config['MAIL_DEFAULT_SENDER'] = 'agikedwin73@gmail.com' # enter your email here
app.config['MAIL_PASSWORD'] = 'edvinag73' # enter your password here
import os

mail = Mail(app)


from werkzeug.debug import DebuggedApplication

app.config['DEBUG'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:agik@localhost:3306/leave_system'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:test12@41.89.200.55:3306/leave_system'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)
CORS(app)
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

db.init_app(app)
flask_bcrypt = Bcrypt(app)
app.permanent_session_lifetime = timedelta(minutes=1)

#api = Blueprint('api', __name__)

#app.register_blueprint('api', url_prefix="/api")

app.wsgi_app = DebuggedApplication(app.wsgi_app, True)



cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


db.init_app(app)







