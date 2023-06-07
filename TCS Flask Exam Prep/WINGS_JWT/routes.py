from flask_restful import Api
from views import Login, SignUp, Protected, Public


def create_routes(api:Api):
    api.add_resource(Login,'/login')
    api.add_resource(SignUp,'/signup')
    api.add_resource(Protected,'/protected')
    api.add_resource(Public,'/public')