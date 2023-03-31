from db.models import Store, Owner, Inventory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class CLI:
    def __init__(self, user_input):
        self.stores = [ store for store in session.query( Store ) ]
        self.owners = [ owner for owner in session.query( Owner ) ]
        self.supplies = [ inventory for inventory in session.query( Inventory ) ]
        self.name = user_input
        if any(owner.name == user_input for owner in self.owners):
            print(' ')
            print(f'<<<<< Welcome Back {user_input} >>>>>')
            print('           ||||||||||||||             ')
            print('      <<<<< OWNER PORTAL >>>>>    ')
            print('           vvvvvvvvvvvvvv            ')
            print(' ')

            exit = False
            while exit == False:
                option = input(f'If you would like to add an item to your inventory enter "add"\nIf you would like to view other owners or stores enter "view"\nTo Exit at any time Type "exit"\nEnter Text Here ==> ')
                print('')
                if option.lower() == "add":
                    add_inventory( self )
                elif option.lower() == "view":
                    show_stores( self )
                elif option.lower() == "exit":
                    return        
        else:
            self.begin()

    def begin( self ):
        print(' ')
        print('***** Welcome to the Shop-O-Rama-Palooza *****')
        print('         <<<<< GUEST PORTAL >>>>>          ')
        print(' ')

        exit = False
        while exit == False:
            option = input(f'To Get Started Type "start"\nTo Exit at any time Type "exit"\nEnter Text Here ==> ')
            print('')
            if option.lower() == "start":
                show_stores( self )
            elif option.lower() == "exit":
                return
            # elif option.lower() == "sign me":
            #     sign_contract( self )
            
def show_stores( self ):
    option = input('To View Selection of Stores type "S" or "s"\nTo View Selection of Owners type "O" or "o"\nEnter Text Here ==> ')
    print("")
    if option == "S" or option == "s":
        stores_list(self.stores)
    elif option == "O" or option == "o":
        owners_list(self.owners)

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


def oss_inventory():
    print('')
    stores_id=1
    supplies=session.query(Inventory).filter_by(stores_id=stores_id).all()
    for i, item in enumerate(supplies, start=1):
        print(f'{i}.{item.item} ${item.price}')
    print('')

def bb_inventory():
    print('')
    stores_id=2
    supplies=session.query(Inventory).filter_by(stores_id=stores_id).all()
    for i, item in enumerate(supplies, start=1):
        print(f'{i}.{item.item} ${item.price}')
    print('')

def jj_inventory():
    print("")
    stores_id=3
    supplies=session.query(Inventory).filter_by(stores_id=stores_id).all()
    for i, item in enumerate(supplies, start=1):
        print(f'{i}.{item.item} ${item.price}')
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



def add_inventory( self ):
    add_item = input("Enter the item you would like to add: ")
    add_price = input("Enter the price of this item: ")
    same_store_id = input("Enter the id of your store: ")
    same_owner_id = input("Enter your owner id for confirmation: ")

    added_inventory = Inventory(
        item = add_item,
        price = add_price,
        stores_id = same_store_id,
        owners_id = same_owner_id
    )

    session.add( added_inventory )
    session.commit()

    self.supplies.append( added_inventory )
    print('')
    print(f'Thank you {user_input}, your item has been added!')
    print('')



# def sign_contract( self ):
#     print("contract be here")








if __name__ == '__main__':
    engine = create_engine('sqlite:///onestopshop.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("\nWelcome!\nIf you are an owner type your full name to access the OWNER PORTAL\nPress Enter if you would like to enter the GUEST PORTAL\n==> ")
    CLI(user_input)