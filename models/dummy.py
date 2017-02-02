import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///tutorial.db', echo=True)


# create a session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin", "password")
session.add(user)

user = User("python", "python")
session.add(user)

user = User("Jumpiness", "Python")
session.add(user)

# commit records to the database
session.commit()
