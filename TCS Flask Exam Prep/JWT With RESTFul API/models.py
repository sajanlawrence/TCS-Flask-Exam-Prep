from app import db 
from datetime import datetime
from flask_bcrypt import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    email = db.Column(db.String(80))
    password = db.Column(db.String(60))
    #created = db.Column(db.DateTime, default = datetime.utcnow(),nullable=True)

    def __init__(self,**kwargs):
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf-8')

    def check_password(self,password):
        return check_password_hash(self.password,password)
    
