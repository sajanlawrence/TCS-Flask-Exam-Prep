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
    #__tablename__ = 'User'
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

class Role(db.Model):
    #__tablename__ = 'Role'
    role_id = db.Column(db.Integer,primary_key=True)
    role_name = db.Column(db.String(80))

    user = db.relationship('User',backref='role',uselist=False)

    def __init__(self,role_name):
        self.role_name = role_name

class Category(db.Model):
    category_id = db.Column(db.Integer,primary_key=True)
    category_name = db.Column(db.String(120))

    product = db.relationship('Product',backref='category',lazy='dynamic')

    def __init__(self,category_name):
        self.category_name = category_name

class Product(db.Model):
    product_id = db.Column(db.Integer,primary_key=True)
    product_name = db.Column(db.String(120))
    price = db.Column(db.Float)
    seller_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    category_id = db.Column(db.Integer,db.ForeignKey('category.category_id'))

    cartProduct = db.relationship('CartProduct',backref='product',lazy='dynamic')

    def __init__(self,price,product_name,seller_id,category_id):
        self.product_name = product_name
        self.price = price
        self.seller_id = seller_id
        self.category_id = category_id

class Cart(db.Model):
    cart_id = db.Column(db.Integer,primary_key=True)
    total_amount = db.Column(db.Float)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))

    cartProduct = db.relationship('CartProduct',backref='cart',lazy='dynamic')
    
    def __init__(self,total_amount,user_id):
        self.total_amount = total_amount
        self.user_id = user_id

class CartProduct(db.Model):
    cp_id = db.Column(db.Integer,primary_key=True)
    cart_id = db.Column(db.String(80),db.ForeignKey('cart.cart_id'))
    product_id = db.Column(db.Integer,db.ForeignKey('product.product_id'))
    quantity = db.Column(db.Integer)

    def __init__(self,cart_id,product_id,quantity):
        self.cart_id = cart_id
        self.product_id = product_id 
        self.quantity = quantity
        