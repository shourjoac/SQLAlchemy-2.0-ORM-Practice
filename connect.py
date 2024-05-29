# SQLAlchemy
# It is a python library used to work with databases.
# ORM → Object Relational Mapping(allows you to interact with the database with python objects)


#Part 1: Connecting to the database


from sqlalchemy import create_engine,text

db_url = "sqlite:///database.db"
engine = create_engine(db_url, echo= True) #Create a database engine(responsible for connecting to the database and executing sql commands).

with engine.connect() as connection:
    result = connection.execute(text('select "Hello"'))
    print(result.all())  


