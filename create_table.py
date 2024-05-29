#Part 3: Creating database tables

from models import Base, User, Comment
from connect import engine


print("CREATING TABLES >>>> ")
Base.metadata.create_all(bind=engine) #Creates the database and all the tables associated with it.
#define a meta data object and then you attach all the database tables you created onto the object and then you bind it to an engine for it to be able to create 
# a database table on ur database
