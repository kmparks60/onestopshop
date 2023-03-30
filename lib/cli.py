from db.models import Store, Owner, Inventory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class CLI:
    def __init__(self, user_input):
        self.stores = [ store for store in session.query( Store ) ]
        self.owners = [ owner for owner in session.query( Owner ) ]
        self.supplies = [ inventory for inventory in session.query( Inventory ) ]
        self.name = user_input
        self.begin()

    def begin( self ):
        print(' ')
        print(f'***** Welcome to the Shop-O-Rama-Palooza *****')
        print(' ')



if __name__ == '__main__':
    engine = create_engine('sqlite:///onestopshop.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Testing, please enter anything to get started: ")
    CLI(user_input)