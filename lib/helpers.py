# lib/helpers.py

from models.brand import Brand
from models.car_model import CarModel

def interact_with_brand_data():
    print("Performing useful function#1.")


def interact_with_car_model_data():
    CarModel.get_all()

    print("Here is the data for all car models:\n")

    for car_model in CarModel.all:
        print(car_model)



def exit_program():
    print("Goodbye!")
    exit()

def brand_menu():
    pass


def car_model_menu():
    pass