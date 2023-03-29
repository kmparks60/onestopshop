#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import ( Store, Customer, Inventory )

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/onestopshop.db')
    Base.metadata.create_all( engine )
    Session = sessionmaker( bind=engine )
    session = Session()

    