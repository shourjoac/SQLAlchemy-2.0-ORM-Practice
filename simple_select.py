# select statements
from main import session
from models import User,Comment
from sqlalchemy import select


# First method on querying
# statement = select(User).where(User.username.in_(['cathy','paul']))

# result = session.scalars(statement)  # executes out sql statement and return it as an iterable of scalars

# for user in result:
#     print(user)

#Second method of querying
#using sessions to select
users = session.query(User).all()


for user in users:
    print(user)  
