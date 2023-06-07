from app import db, User, Post

# Get the table object
table = User.query.all()

# Delete all rows from the table
for row in table:
    db.session.delete(row)

# Commit the changes to the database
db.session.commit()

# Get the table object
table = Post.query.all()

# Delete all rows from the table
for row in table:
    db.session.delete(row)

# Commit the changes to the database
db.session.commit()

user1 = User(name="Sajan")
post11 = Post(post="I'm a Software Developer",user=user1)
################## Note : for the ForeignKey, we just need to pass the User object.
post12 = Post(post="I'm a Python Developer",user=user1)

user2 = User(name="Ashwin")
post21 = Post(post="I'm a React Developer",user=user2)
post22 = Post(post="I'm a Java Developer",user=user2)


db.session.add(user1)
db.session.add(user2)
db.session.add(post11)
db.session.add(post12)
db.session.add(post21)
db.session.add(post22)
db.session.commit()


users = User.query.all()
for user in users:
    print("User name : {}".format(user.name))

sajan = User.query.filter_by(name='Sajan').first()
posts = sajan.posts.all()
########## Note : to get all the posts of a user, we just need to write sajan.posts.all()
# here posts is the relationship field.

for post in posts:
    print("Post is : {}".format(post.post))