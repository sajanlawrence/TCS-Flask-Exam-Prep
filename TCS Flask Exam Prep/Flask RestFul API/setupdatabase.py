from basic import db, Puppy

#converts all the models into tables
db.create_all()

#Create
sam = Puppy("Sammy",6)
frank = Puppy("Frankie",3)
db.session.add_all([sam,frank])
#db.session.add(sam)
#db.session.add(frank)
db.session.commit()
print(sam.id)
print(frank.id)

#Read

all_puppies = Puppy.query.all() #List of puppies object from Puppy table.
print(all_puppies)
#SELECT by ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name)
#FILTERS
puppy_frankie = Puppy.query.filter_by(name="Frankie")
print(puppy_frankie.all()) #list of repr strings
#####UPDATE#####
first_puppy = Puppy.query.get(1)
first_puppy.name = "Jacky"
db.session.add(first_puppy)
db.session.commit()
print(first_puppy.name)
#########DELETE#########
all_puppy_before = Puppy.query.all()
print(len(all_puppy_before))
second_puppy = Puppy.query.get(3)
db.session.delete(second_puppy)
db.session.commit()
all_puppy = Puppy.query.all()
print(len(all_puppy))