from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

'''
First in terminal,
set FLASK_APP=basic.py          #filename
then following 3 lines
flask db init
flask db migrate -m "message"
flask db upgrade
'''



#One-to-One relationship
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    #One User --- Many Post
    #so we get a list of posts. To handle that we specify lazy.
    posts = db.relationship('Post',backref='user',lazy='dynamic')
    #Note : if one-to-one relatioship, instead of lazy we specify uselist=False

#One more important thing to note : if primary key of table 'A' is used as ForeignKey in table 'B',
#then db.relationship(.............) this line needs to write inside Table 'A'.
# and  db.Column(db.Integer, db.ForeignKey(.........) this should write inside Table 'B'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))








if __name__ == "__main__":
    app.run(debug=True)