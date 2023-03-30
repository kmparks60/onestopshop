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
            option = input(f'To Get Started Type "start"')
            print('')
            if option.lower() == "start":
                show_stores( self )
            # elif option.lower() == "sign me":
            #     sign_contract( self )
            
def show_stores( self ):
    option = input('To View Selection of Stores type "S" or "s"\nTo View Selection of Owners type "O" or "o"\nTo View Inventory type "I" or "i"\nEnter Text Here ==>')
    print("")
    if option == "S" or option == "s":
        stores_list(self.stores)
    elif option == "O" or option == "o":
        owners_list(self.owners)
    elif option == "I" or option == "i":
        supplies_list(self.supplies)

def stores_list(stores):
    print('')
    print('Stores')
    print('')

    for index, store in enumerate(stores):
        print(f"{index +1}. {store.name}")

    print('')

def owners_list(owners):
    print('')
    print('Owners')
    print('')

    for index, owner in enumerate(owners):
        print(f"{index +1}. {owner.name}")
    
    print('')

def supplies_list(supplies):
    print('')
    print('Inventory')
    print('')

    for index, inventory in enumerate(supplies):
        print(f"{index +1}. {inventory.name}")

    print('')   


def sign_contract( self ):
    print("contract be here")








if __name__ == '__main__':
    engine = create_engine('sqlite:///onestopshop.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Testing, please enter anything to get started: ")
    CLI(user_input)