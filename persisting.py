# Part 4: Creating and persisting objects

from models import User,Comment
from main import session


#creating a session object and persisting them(the following model objects) into the database 

user1 = User(
    username = 'jona',
    email_address = "jonathan@sql.irg",
    comments = [
        Comment(text="Hello World"),
        Comment(text="Please subscribe")
    ]
)

paul = User(
    username = 'paul',
    email_address = "paul@sql.irg",
    comments = [
        Comment(text="What's up?"),
        Comment(text="Please subscribe")
    ]
)

cathy = User(
    username = 'cathy',
    email_address = "cathy@sql.irg",
)


session.add_all([user1,paul,cathy]) #adding a variety of model objects

session.commit()