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

def create_brand():
    name = input("Enter brand name: ")
    country = input("Enter country of origin: ")
    try:
        brand = Brand.create(name, country)
        print("New brand successfully created!")
        print(brand)
    except Exception as e:
        print(e)

def display_all_brands():
    brands = Brand.get_all()
    if len(brands) == 0:
        print("There are no brands.")
    else:
        print("Here is the data for all the brands!")
        for brand in brands:
            print(brand)

def find_brand_by_id():
    id = input("Enter an value for the ID!")
    brand = Brand.find_by_id(id)
    if brand:
        print(brand)
    else:
        print("Brand not found")

def view_models_for_brand():
    brand_id = input("Enter Brand ID to view models")
    brand = Brand.find_by_id(brand_id)
    if brand:
        for car_model in brand.car_models():
            print(car_model)
    else:
        print("Brand not found!")

def delete_brand():
    brand_id = input("Enter Brand ID to view models")
    brand = Brand.find_by_id(brand_id)
    if brand:
        brand.delete()
        print("Brand successfully deleted!")
    else:
        print("Brand not found!")



def exit_program():
    print("Goodbye!")
    exit()

def brand_menu():
    pass


def car_model_menu():
    pass