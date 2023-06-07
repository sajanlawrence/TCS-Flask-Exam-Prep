from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class helloWorld(Resource):
    def get(self):
        return{"message":"Hi Sajan. Welcome to your first REST app"},209,{'response_header1':'just a header'}
api.add_resource(helloWorld,'/','/home','/index')

if __name__ == '__main__':
    app.run()

'''
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloFresco(Resource):
  def get(self):
    return {'message': 'Welcome to Fresco Play Sajan'}

api.add_resource(HelloFresco, '/')

if __name__ == '__main__':
    app.run()
    '''