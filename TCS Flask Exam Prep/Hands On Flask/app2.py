import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'database.sqlite')
app.config['SQLALCHEMY_TRACKING_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)


class User(db.Model):
   # __tablename__ = "user"
   user_id = db.Column(db.Integer,primary_key=True)
   user_name = db.Column(db.String(80))
   password = db.Column(db.String(80))
   user_role = db.Column(db.Integer,db.ForeignKey('role.role_id'))

   cart = db.relationship('Cart',backref='user',uselist=False)
   product = db.relationship('Product',backref='user',lazy='dynamic')

   def __init__(self,user_name,password,user_role):
       self.user_name = user_name
       self.password = password
       self.user_role = user_role



