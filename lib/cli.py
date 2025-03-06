# lib/cli.py

from helpers import (
    exit_program,
    interact_with_brand_data,
    interact_with_car_model_data
)


def main():
    while True:
        # print("1.Car Brand & Model Catalog")
        # print("2.Add a New Car Brand")
        # print("View All Car Brands")
        # print("Add a Model to a Brand")
        # print("View Models for a Brand")
        # print("Delete a Brand")
        # print("Exit")

        # choice = input("Enter your choice: ")

        # if choice == "1":
        #     name = input("Enter brand name: ").strip()
        #     country = input("Enter country of origin: ").strip()
        #     Brand.add_brand(name, country)

        # elif choice == "2":
        #     Brand.get_all_brands()

        # elif choice == "3":
        #     Brand.get_all_brands()
        #     brand_id = input("Enter Brand ID to add a model: ").strip()
        #     model_name = input("Enter model name: ").strip()
        #     year = input("Enter model year: ").strip()

        #     if brand_id.isdigit() and year.isdigit():
        #         CarModel.add_model(int(brand_id), model_name, int(year))
        #     else:
        #         print("Invalid input! Brand ID and Year must be numbers.")

        # elif choice == "4":
        #     Brand.get_all_brands()
        #     brand_id = input("Enter Brand ID to view models: ").strip()

        #     if brand_id.isdigit():
        #         CarModel.get_models_by_brand(int(brand_id))
        #     else:
        #         print("Invalid input! Brand ID must be a number.")

        # elif choice == "5":
        #     Brand.get_all_brands()
        #     brand_id = input("Enter Brand ID to delete: ").strip()

        #     if brand_id.isdigit():
        #         Brand.delete_brand(int(brand_id))
        #     else:
        #         print("Invalid input! Brand ID must be a number.")

        # elif choice == "0":
        #     print("Exiting the catalog. Goodbye!")
        #     conn.close()
        #     break

        # else:
        #     print("Invalid choice! Please enter a number from the menu.")
