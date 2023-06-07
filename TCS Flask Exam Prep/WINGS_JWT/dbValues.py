from models import User
from app import db

sajan = User(username="Sajan2", password="efrn",isAdmin=True)
sajan.hash_password()
db.session.add(sajan)
db.session.commit()

user = User.query.filter_by(username="Sajan2").first()
print("username fetched is {}".format(user.username))