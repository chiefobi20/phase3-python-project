# lib/cli.py

from helpers import (
    exit_program,
    create_brand,
    display_all_brands,
    find_brand_by_id,
    view_models_for_brand,
    delete_brand
)


def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            create_brand()


        elif choice == "2":
            display_all_brands()

        elif choice == "3":
            find_brand_by_id()
        # elif choice == "3":
        #     Brand.get_all()
        #     brand_id = input("Enter Brand ID to add a model: ")
        #     model_name = input("Enter model name: ")
        #     year = input("Enter model year: ")

        #     if brand_id.isdigit() and year.isdigit():
        #         interact_with_car_model_data.create(int(brand_id), model_name, int(year))
        #     else:
        #         print("Invalid input! Brand ID and Year must be numbers.")

        elif choice == "4":
            view_models_for_brand()

        elif choice == "5":
           delete_brand()


        elif choice == "0":
            print("Exiting the catalog. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number from the menu.")


def menu():
        print("Car Brand & Model Catalog")
        print("1.Add a New Car Brand")
        print("2.View All Car Brands")
        print("3.Find Car Brand by ID")
        print("4.View Models for a Brand")
        print("5.Delete a Brand")
        print("6.Exit")


if __name__ == "__main__":
    main()