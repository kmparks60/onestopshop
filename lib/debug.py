#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import ( Base, Store, Owner, Inventory )

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/onestopshop.db')
    Base.metadata.create_all( engine )
    Session = sessionmaker( bind=engine )
    session = Session()


    # seven11 = Store( name='7/11', location='Raymonds House, Florida' )
    # session.add( seven11 )
    # session.commit()
    # stores = session.query( Store )
    # print( [ store for store in stores ] )
    
    # mason_parks = Owner( name='Mason Parks' )
    # session.add( mason_parks )
    # session.commit()
    # owners = session.query( Owner )
    # print( [ owner for owner in owners ] )


    import ipdb; ipdb.set_trace()