from flask import request
from app import db, app
from models import User
import jwt
from datetime import datetime, timedelta

def createUser(request,input_data):
    check_username_exists = User.query.filter_by(
        username = input_data.get('username')
    ).first()
    check_email_exists = User.query.filter_by(
        email = input_data.get('email')
    ).first()

    if check_username_exists:
        return {
            'message' : 'Username already exists',
            'status_bool' : False,
            'status' : 400
        }
    if check_email_exists:
        return {
            'message' : 'Email already exists',
            'status_bool' : False,
            'status' : 400
        }
    new_user = User(**input_data)
    new_user.hash_password()
    db.session.add(new_user)
    db.session.commit()
    del input_data["password"]
    return {
            'data' : input_data,
            'message' : 'User created!!!',
            'status_bool' : True,
            'status' : 201
        }


def loginUser(request,input_data):
    user = User.query.filter_by(
        username = input_data.get('username')
    ).first()
    if user is None:
        return {
            'message' : 'User not found',
            'status_bool' : False,
            'status' : 400
        }
    if user.check_password(input_data.get('password')):
        token = jwt.encode(
            {'username' : input_data.get('username'),
             'exp' : datetime.utcnow() + timedelta(minutes=30)
             }, app.config['SECRET_KEY'],algorithm='HS256'
        )
        input_data['token'] = token
        return {
            'data' : input_data,
            'message' : 'Login Success',
            'status_bool' : True,
            'status' : 201
        }
    else:
        return {
            'message' : 'Wrong password!!!',
            'status_bool' : False,
            'status' : 400
        }
