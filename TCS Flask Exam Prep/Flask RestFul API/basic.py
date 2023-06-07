import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) #database
##########For migration#############
Migrate(app,db)
'''
First in terminal,
set FLASK_APP=basic.py          #filename
then following 3 lines
flask db init
flask db migrate -m "message"
flask db upgrade
'''
###################################
class Puppy(db.Model): #model
    __tablename__ = 'Puppies'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return("Puppy {} is {} year old".format(self.name,self.age))