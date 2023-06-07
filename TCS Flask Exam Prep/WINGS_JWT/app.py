from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_restful import Api


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
#Very IMP : sqlite:/// need to add 3 slashes otherwise you get an error like 
# ValueError: invalid literal for int() with base 10: Flask 
# during migration.


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "UH6N2KJ4N689TJ4JN643657M"
db = SQLAlchemy(app)
Migrate(app,db)
api = Api(app)

'''
First in terminal,
set FLASK_APP=basic.py          #filename
then following 3 lines
flask db init
flask db migrate -m "message"
flask db upgrade
'''

if __name__ == "__main__":
    from routes import create_routes
    create_routes(api)
    app.run(debug=True)
