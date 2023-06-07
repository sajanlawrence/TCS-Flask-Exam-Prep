import os
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from validators import validate

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Migrate(app,db)


class AddressBook(db.Model):
    __tablename__ = "addressBook"
    name = db.Column(db.String(100))


@app.route('/address/',methods=['GET','POST'])
def address():
    if(request.method == 'POST'):
        if(validate(request)[0] == "False"):
            return "Failure",400
        else:
            obj = AddressBook()
            db.session.add(obj)
            db.session.commit()
    else:
        data = AddressBook.query.all()
        if(len(data)>0):
            return "",200

