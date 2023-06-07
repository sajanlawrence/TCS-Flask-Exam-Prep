from app import db 
from flask_bcrypt import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(150))
    isAdmin = db.Column(db.Boolean)


    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf-8') #IMP to decode

    def check_password(self,password):
        return check_password_hash(self.password,password)
    
db.create_all() #IMPORTANT : after creating the models only this command should write. Otherwise 
#you get an error like table doesn't exists.