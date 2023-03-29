from sqlalchemy import (Column, String, Integer, ForeignKey )
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///onestopshop.db')

Base = declarative_base()


class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    location = Column(String())
    supplies = relationship('Inventory', backref=('stores'))

    def __repr__(self):
        return f'Store(id={self.id}, ' \
        + f'name={self.name}, ' \
        + f'location={self.location} ' \
        
    
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    supplies = relationship('Inventory', backref=('customers'))

    def __repr__(self):
        return f'Customer(id={self.id}, ' \
        + f'name={self.name}) ' \

class Inventory(Base):
    __tablename__ = 'supplies'

    id = Column(Integer(), primary_key=True)
    item = Column(String())
    price = Column(Integer())
    quantity = Column(Integer())
    stores_id = Column(Integer(), ForeignKey( Store.id ) )
    customers_id = Column(Integer(), ForeignKey( Customer.id ) )

    stores = relationship( 'Store', foreign_keys='Inventory.stores_id' )
    customers = relationship( 'Customer', foreign_keys='Inventory.customers_id' )

    def __repr__(self):
        return f'Inventory(id={self.id}, ' \
            + f'item={self.item}, ' \
            + f'price={self.price}, ' \
            + f'quantity={self.quantity}, ' \
            + f'stores_id={self.stores_id}),' \
            + f'customers_id={self.customers_id})'