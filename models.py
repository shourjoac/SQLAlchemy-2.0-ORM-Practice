#Part 2: Create database models


from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column,relationship #creates out base class from which all the database model classes are going to inherit
#the mapped class allows us to define the attributes of each of the columns which we define in our specific classes
from sqlalchemy import ForeignKey, Text
from typing import List

class Base(DeclarativeBase):
    pass

class User(Base):
    
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(nullable=False)
    email_address:Mapped[str] 
    comments:Mapped [List["Comment"]] = relationship(back_populates='user')

    def __repr__(self) -> str:
        return f"<User username={self.username}>"

    

class Comment(Base):

    __tablename__ = 'comments'
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'),nullable=False)
    text:Mapped[str] = mapped_column(Text,nullable=False)
    user:Mapped["User"] =relationship(back_populates='comments')

    def __repr__(self):
        return f"<Comment text={self.text} by {self.user.username}>"

#we use these database models to create objects which will then be going through a object oriented approach to be saved onto our database