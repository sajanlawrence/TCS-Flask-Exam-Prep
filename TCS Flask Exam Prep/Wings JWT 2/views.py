from flask_restful import Resource
from flask import request, make_response
from models import User
import jwt
from datetime import datetime, timedelta
from app import app

class Login(Resource):
    def post(self):
        input_data = request.get_json()
        username = input_data['username']
        password = input_data['password']
        if username is None or password is None:
            return make_response({'message' : 'Username or Password is missing'}, 400)
        user = User.query.filter_by(username=username).first()
        if not user:
            return make_response({'message' : 'User not exists'}, 400)
        if user.check_password(password):
            token = jwt.encode(
                {
                'username' : username,
                'exp' : datetime.utcnow() + timedelta(minutes=3)
                }, app.config['SECRET_KEY'], algorithm='HS256'
            )
            return make_response({'token' : token}, 200)
        else:
            return make_response({'message' : 'Incorrect Password'}, 400)
        
class SignUp(Resource):
    def post(self):
        input_data = request.get_json()
        username = input_data['username']
        password = input_data['password']
        if username is None or password is None:
            return make_response({'message' : 'Username or Password is missing'}, 400)