from flask_restful import Resource
from flask import request, make_response
from service import createUser, loginUser


class SignUpApi(Resource):
    def post(self):
        input_data = request.get_json()
        response = createUser(request,input_data)
        return make_response(response,response['status'])

class LoginApi(Resource):
    def post(self):
        input_data = request.get_json()
        response = loginUser(request,input_data)
        return make_response(response,response['status'])

