from app import db
from flask_bcrypt import generate_password_hash, check_password_hash




class User(db.Model):
    username = db.Column(db.String(80),primary_key=True)
    password = db.Column(db.String(80))
    isAdmin = db.Column(db.Boolean,default=False)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf-8')
    def check_password(self,password):
        return check_password_hash(self.password,password)
    
db.create_all()