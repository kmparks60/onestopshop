from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Store, Customer, Inventory

if __name__ == '__main__':
    engine = create_engine('sqlite:///onestopshop.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # session.query(Customer).delete()
    
    faker = Faker()
    print( faker.name() )

    item = ["Soda", "Chips", "Chargers", "Sunglasses", "Water", "Candy", "Coffee", "Taquitos", "Hammer"]

    price = [1, 2, 7, 10, 1.5, 1, 1, 2, 45]

    quantity = [10, 10, 5, 7, 20, 15, 30, 50, 1]

    customers = []

    # for _ in range(7):
        
    #     customer = Customer(
    #         name=f"{faker.first_name()} {faker.last_name()}"
    #     )

    #     session.add(customer)
    #     session.commit()

    #     customers.append(customer)

    

    
