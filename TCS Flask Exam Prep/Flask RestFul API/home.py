from flask import Flask, jsonify
from flask_restful import Api, Resource
#https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask
#request.form.get('question')   request.args.get('start')
app = Flask(__name__)
api = Api(app)

family = {1:'member1',2:'member2',3:'member3',4:'member4',5:'member5'}

class GetDetails(Resource):
    def get(self,number=None):
        if number == None:
            return jsonify({'error' : 'use the correct format'})
        if number not in family:
            return jsonify({'status' : 'Failure','error' : 'member not found'})
        return jsonify({'status' : 'Success', 'details' : family[number]})


    def post(self):
        pass

api.add_resource(GetDetails,'/member/<int:number>','/')

if __name__ == "__main__":
    app.run(debug=True)