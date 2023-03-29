from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///onestopshop.db')

Base = declarative_base()


class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    location = Column(String())

    def __repr__(self):
        return f'Store(id={self.id}, ' \
        + f'name={self.name}, ' \
        + f'location={self.location} ' \
        
    
class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f'Owner(id={self.id}, ' \
        + f'name={self.name}) ' \

class Inventory(Base):
    __tablename__ = 'supplies'

    id = Column(Integer(), primary_key=True)
    item = Column(String())
    price = Column(Integer())
    quantity = Column(Integer())
    stores_id = Column(Integer(), ForeignKey( Store.id ) )
    owners_id = Column(Integer(), ForeignKey( Owner.id ) )

    stores = relationship( 'Store', foreign_keys='Inventory.stores_id' )
    owners = relationship( 'Owner', foreign_keys='Inventory.owners_id' )

    def __repr__(self):
        return f'Inventory(id={self.id}, ' \
            + f'item={self.item}, ' \
            + f'price={self.price}, ' \
            + f'quantity={self.quantity}, ' \
            + f'stores_id={self.stores_id}),' \
            + f'owners_id={self.owners_id})'