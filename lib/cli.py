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
            option = input(f'To Get Started Type "start"\nEnter Text Here ==> ')
            print('')
            if option.lower() == "start":
                show_stores( self )
            # elif option.lower() == "sign me":
            #     sign_contract( self )
            
def show_stores( self ):
    option = input('To View Selection of Stores type "S" or "s"\nTo View Selection of Owners type "O" or "o"\nEnter Text Here ==> ')
    print("")
    if option == "S" or option == "s":
        stores_list(self.stores)
    elif option == "O" or option == "o":
        owners_list(self.owners)
    # elif option == "I" or option == "i":
    #     supplies_list(self.stores)

def stores_list(stores):
    print('')
    print('Stores')
    print('')

    for index, store in enumerate(stores):
        print(f"{index +1}. {store.name}")
    
    print('')
    option = input('To View Inventory Enter the id of the Store\nEnter Text Here ==> ')
    print("")
    if option == "1":
        oss_inventory()
    elif option == "2":
        bb_inventory()
    elif option == "3":
        jj_inventory()


def oss_inventory(supplies):
    print('')
    oss_list = [s.item for s in supplies ]
    print(oss_list)
    print('')

def bb_inventory():
    print('')
    print('Inventory for Bud and Booze')
    print('')

def jj_inventory():
    print("")
    print("Inventory for Joystick Junction")
    print("")

def owners_list(owners):
    print('')
    print('Owners')
    print('')

    for index, owner in enumerate(owners):
        print(f"{index +1}. {owner.name}")
    
    print('')

    option = input('To View Which Stores That Each Owner Owns Enter Number\nEnter Text Here ==> ')
    print("")
    if option == "1":
        print("1. One Stop Shop")
        print("")
    elif option == "2":
        print("2. Budz and Booze")
        print("")
    elif option == "3":
        print("3. Joystick Junction")
        print("")

# def show_supplies(inventory):
#     print('')
#     print(f'Item: {inventory.item}')
#     print(f'Price: {inventory.price}')

# def supplies_list(supplies):
    # print('')
    # print('Inventory')
    # print('')

#     for index, inventory in enumerate(supplies):
#         print(f"{index +1}. {Inventory.name}")

#     print('')   


def sign_contract( self ):
    print("contract be here")








if __name__ == '__main__':
    engine = create_engine('sqlite:///onestopshop.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Testing, please enter anything to get started: ")
    CLI(user_input)