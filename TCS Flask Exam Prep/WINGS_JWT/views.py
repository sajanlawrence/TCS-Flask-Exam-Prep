from flask_restful import Resource
from functools import wraps
from flask import request, make_response, jsonify
from models import User
import jwt
from datetime import datetime, timedelta
from app import app, db

#jsonify may cause error. so better use return make_response() or return {'message' : 'token required'}, 400
def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = request.args.get('token')
        if not token:
            return make_response({'message' : 'token required'}, 400)
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'],algorithms=['HS256'])
        except:
            return make_response({'message' : 'Invalid Token'}, 400)
        return f(*args,**kwargs) #important
    return decorated

def jwt_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None
        print("request is : {}".format(request))
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            token = auth_header.split(" ")[1]
        print("token is", token, app.config['SECRET_KEY'])
        if not token:
            return {'message' : 'token required'}, 400
        try:
            payload = jwt.decode(token,app.config['SECRET_KEY'],algorithms=['HS256'])
        except:
            return {'message' : 'Invalid Token'}, 400
        return f(*args, **kwargs)
    return decorated



class Login(Resource):
    def post(self):
        print("login called")
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        print(username,password)
        if not username or not password:
            return {'message' : 'username and password required'}, 400
        
        user = User.query.filter_by(username=username).first()
        
        if not user:
            print("User not found in table")
            return {'message' : 'User not found in table'}, 401
        if user.check_password(password):
            token = jwt.encode(
                {
                    'username' : username,
                    'exp' : datetime.utcnow() + timedelta(minutes=3)
                 }, app.config['SECRET_KEY'], algorithm="HS256"
            )
            return {'token' : token}, 200
        else:
            return {'message' : 'Wrong password'}, 400
        
class SignUp(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        admin = data.get('isAdmin')

        user = User.query.filter_by(username = username).first()
        if user:
            return {'message' : 'Username already exists'}, 400
        isAdmin = False
        if admin == "YES":
            isAdmin = True

        newUser = User(id=45,username=username,password=password,isAdmin=isAdmin)
        newUser.hash_password()
        db.session.add(newUser)
        db.session.commit()
        return {'message' : 'User created successfully'}

class Protected(Resource):
    @jwt_required
    def get(self):
        return {'message' : 'This is a protected content'}

class Protected2(Resource):
    @jwt_required
    def get(self):
        return {'message' : 'This is a protected content 2'}

class Public(Resource):
    def get(self):
        return {'message' : 'This is a public content'}


        