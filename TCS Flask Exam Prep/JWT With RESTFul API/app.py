from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "V24B8535B548GHRGJEGTR95475U"
api = Api(app)
db = SQLAlchemy(app)
Migrate(app,db)





if __name__ == "__main__":
    from routes import create_authentication_routes
    create_authentication_routes(api)
    app.run(debug=True)