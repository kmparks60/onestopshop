#!/usr/bin/env python3

from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker

from db.models import ( Base, Store, Owner, Inventory )

if __name__ == '__main__':
    engine = create_engine('sqlite:///lib/onestopshop.db')
    # Base.metadata.create_all( engine )
    Session = sessionmaker( bind=engine )
    session = Session()

    # <<< STORES >>>
    # seven11 = Store( name='7/11', location='Raymonds House, Florida' )
    # session.add( seven11 )
    # session.commit()
    # stores = session.query( Store )
    # print( [ store for store in stores ] )


    # <<< OWNERS >>> 
    # mason_parks = Owner( name='Mason Parks' )
    # session.add( mason_parks )
    # session.commit()
    # owners = session.query( Owner )
    # print( [ owner for owner in owners ] )

    # <<< SUPPLIES >>>
    # raw_papers = Inventory(item='Raw Papers', price=5, stores_id=2, owners_id=2 )
    # session.add( raw_papers )
    # session.commit()
    # supplies = session.query( Inventory )
    # print( [ inventory for inventory in supplies ] )
    


    import ipdb; ipdb.set_trace()