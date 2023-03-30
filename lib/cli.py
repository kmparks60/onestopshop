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

        exit = False
        while exit == False:
            option = input(f'Enter "view stores" to see a list of our funded stores created by our signed owners, or enter "sign me" to become an owner today: ')
            print('')
            if option.lower() == "view stores":
                show_stores( self )
            elif option.lower() == "sign me":
                sign_contract( self )
            
def show_stores( self ):
    print("stores showing here")
    print("")

def sign_contract( self ):
    print("contract be here")








if __name__ == '__main__':
    engine = create_engine('sqlite:///onestopshop.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Testing, please enter anything to get started: ")
    CLI(user_input)