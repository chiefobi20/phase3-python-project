# lib/cli.py

from helpers import (
    exit_program,
    interact_with_brand_data,
    interact_with_car_model_data,
    create_animals_table
)


def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter brand name: ")
            country = input("Enter country of origin: ")
            Brand.add_brand(name, country)

        elif choice == "2":
            Brand.get_all()

        elif choice == "3":
            Brand.get_all()
            brand_id = input("Enter Brand ID to add a model: ")
            model_name = input("Enter model name: ")
            year = input("Enter model year: ")

            if brand_id.isdigit() and year.isdigit():
                CarModel.create(int(brand_id), model_name, int(year))
            else:
                print("Invalid input! Brand ID and Year must be numbers.")

        elif choice == "4":
            Brand.get_all()
            brand_id = input("Enter Brand ID to view models: ").strip()

            if brand_id.isdigit():
                CarModel.get_models_by_id(int(brand_id))
            else:
                print("Invalid input! Brand ID must be a number.")

        elif choice == "5":
            Brand.get_all()
            brand_id = input("Enter Brand ID to delete: ")

            if brand_id.isdigit():
                Brand.delete_brand(int(brand_id))
            else:
                print("Invalid input! Brand ID must be a number.")

        elif choice == "8":
            create_animals_table()

        elif choice == "0":
            print("Exiting the catalog. Goodbye!")
            conn.close()
            break

        else:
            print("Invalid choice! Please enter a number from the menu.")


def menu():
        print("1.Car Brand & Model Catalog")
        print("2.Add a New Car Brand")
        print("3.View All Car Brands")
        print("4.Add a Model to a Brand")
        print("5.View Models for a Brand")
        print("6.Delete a Brand")
        print("7.Exit")
        print("8.Create animals table")


