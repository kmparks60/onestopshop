#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import ( Base, Store, Customer, Inventory )

if __name__ == '__main__':
    engine = create_engine('sqlite:///onestopshop.db')
    Base.metadata.create_all( engine )
    Session = sessionmaker( bind=engine )
    session = Session()


    # seven11 = Store( name='7/11', location='Raymonds House, Florida' )
    # session.add( seven11 )
    # session.commit()
    # stores = session.query( Store )
    # print( [ store for store in stores ] )
    


    import ipdb; ipdb.set_trace()