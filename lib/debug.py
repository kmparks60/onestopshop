from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer) 
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()



class Store(Base):
    __tablename__ = 'stores'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column( Integer() )
    name = Column( String() )
    location = Column( String() )

    # def __repr__(self):
    #     return f"ID: { self.id }, " \
    #     + f"Name: { self.name } " \
    #     + f"Species: { self.location } "