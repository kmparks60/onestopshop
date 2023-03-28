from sqlalchemy import ( PrimaryKeyConstraint, Column, String, Integer )
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, backref

# engine = create_engine('sqlite:///onestopshop.db')

Base = declarative_base()


class Store(Base):
    __tablename__ = 'stores'
    __table_args__ = ( PrimaryKeyConstraint( 'id' ),)

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    location = Column(String())

    # bottles = relationship('Bottle', backref=backref('winery'))

    def __repr__(self):
        return f'Store(id={self.id}, ' \
        + f'name={self.name}), ' \
        + f'location={self.location}'
    
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    #:Possibly add foreign id key

    # bottles = relationship('Bottle', backref=backref('grape'))

    def __repr__(self):
        return f'Customer(id={self.id}, ' + \
            f'name={self.name}) ' \

class Inventory(Base):
    __tablename__ = 'supplies'

    id = Column(Integer(), primary_key=True)
    item = Column(String())
    price = Column(Integer())
    quantity = Column(Integer())
    # stores_id = Column(Integer(), ForeignKey('stores.id'))
    # customers_id = Column(Integer(), ForeignKey('customers.id'))

    # grape = relationship('Grape', backref_populates='bottles')
    # winery = relationship('Winery', backref_populates='bottles')

    def __repr__(self):
        return f'Inventory(id={self.id}, ' \
            + f'item={self.item}, ' \
            + f'price={self.price}, ' \
            + f'quantity={self.quantity}, ' \
            + f'stores_id={self.stores_id}),' \
            + f'customers_id={self.customers_id})'