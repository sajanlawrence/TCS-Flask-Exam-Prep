#https://flask-restful.readthedocs.io/en/latest/reqparse.html refer this
'''
import datetime as dt

today = dt.date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)
'''
from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)
#By default, RequestParser aborts when it encounters the first error.
#However, it is possible to combine all errors together and send them at once to client.
#It can be achieved by setting bundle_errors parameter of RequestParser class to True, while creating it's object, as shown below.
parser = reqparse.RequestParser(bundle_errors=True)

# required=True is optional
# don't forget to add location='form'
parser.add_argument('principal_amount',location='form', type=float, help='Principal amount must be a number')
parser.add_argument('period',location='form', type=int, help="No. of Years must be an integer")
parser.add_argument('rate',location='form', type=float, help='Rate must be a number')

class SimpleInterest(Resource):
    def post(self):
        args = parser.parse_args()
        p = args['principal_amount']
        n = args['period']
        r = args['rate']
        si = (p*n*r)/100.0
        return {'simple_interest':si}

api.add_resource(SimpleInterest,"/simpleInterest/")

if __name__ == "__main__":
    app.run()

'''
Limiting an Argument Values
If an argument needs to take any one value from a list of defined choices, it can be done using choices parameter of add_argument method.

An example of associating four choices to argument year is shown below.

from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument(
    'year',
    choices=('2017', '2018', '2019', '2020'),
    help='Bad choice'
)
'''