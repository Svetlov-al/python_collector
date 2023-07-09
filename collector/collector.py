from datetime import datetime as dt
import json

PATH = "collections.json"

item_types = ["Computer", "Camera", "Phone", "Video Player"]  # Define item types as a global variable


# Function to load data from a file
def get_collections(filepath=PATH):
    try:
        with open(filepath, 'r') as file:
            collection = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    return collection


# Function to save data to a file
def write_collections(collection, filepath=PATH):
    with open(filepath, "w") as file:  # Изменили имя файла на "collections.json"
        json.dump(collection, file)


def add_item_to_collection():
    collection = get_collections()
    print("Adding an Item\n--------------")
    title = input("Title> ")
    types = " ".join(f"{i + 1}. {item}" for i, item in enumerate(item_types))
    print(types)

    # Request and validate type
    while True:
        try:
            choose_type = int(input("\nType> "))
            if 1 <= choose_type <= len(item_types):
                break
            else:
                print("\nInvalid number. Please enter a number within the range.")
        except ValueError:
            print("\nThat's not a valid number. Please enter a number.")

    # Request and validate date added
    while True:
        date_added = input("\nDate Added (DD/MM/YYYY) [Press Enter for today's date]> ")
        if not date_added:  # Default to today's date if empty
            date_added = dt.today().strftime("%d/%m/%Y")
            break
        try:
            dt.strptime(date_added, "%d/%m/%Y")
            break
        except ValueError:
            print("\nInvalid date format. Please enter the date in DD/MM/YYYY format.")

    # Request and validate date of manufacture
    while True:
        date_manufacture = input("\nDate of Manufacture (DD/MM/YYYY)> ")
        try:
            dt.strptime(date_manufacture, "%d/%m/%Y")
            break
        except ValueError:
            print("\nInvalid date format. Please enter the date in DD/MM/YYYY format.")

    # Request description
    description = input("\nDescription> ")

    # Append to collection
    collection_item = [title, item_types[choose_type - 1], date_added, date_manufacture, description]
    collection.append(collection_item)
    write_collections(collection)

    print("\nItem Added!")


# Function to show items in the collection
def show_items(collection, item_types):
    print("\nItem Types:")
    for index, item in enumerate(item_types):
        print(f"{index + 1}. {item}")

    # Request and validate type
    while True:
        try:
            item_type = int(input("\nType> "))
            if 1 <= item_type <= len(item_types):
                break
            else:
                print("\nInvalid number. Please enter a number within the range.")
        except ValueError:
            print("\nThat's not a valid number. Please enter a number.")

    # Debug print
    print("\nCollection:", collection)

    filtered_items = [item for item in collection if item[1] == item_types[item_type - 1]]

    if not filtered_items:
        print("\nNo items of that type found.")
    else:
        print("\nItem Type Date Added Date of Manufacture Description")
        for item in filtered_items:
            print(f"{item[0]} {item[1]} {item[2]} {item[3]} {item[4]}")


def delete_items(collection, item_types):
    print("Item Types:")
    for index, item in enumerate(item_types):
        print(f"{index + 1}. {item}")

    # Request and validate type
    while True:
        try:
            item_type = int(input("\nType> "))
            if 1 <= item_type <= len(item_types):
                break
            else:
                print("\nInvalid number. Please enter a number within the range.")
        except ValueError:
            print("\nThat's not a valid number. Please enter a number.")

    deleted = False
    for item in collection[:]:
        if item[1] == item_types[item_type - 1]:
            collection.remove(item)
            deleted = True

    write_collections(collection)

    if deleted:
        print("Items deleted!")
    else:
        print("No items of that type found.")


def main():
    while True:
        print("\nPython Collector")
        print("----------------")
        print("1. Add Item to Collection.")
        print("2. Show Items in Collection.")
        print("3. Delete Items from Collection.")
        print("4. Exit")

        try:
            user_action = int(input("Choose action: "))
        except ValueError:
            print("Invalid input. Please enter a number from the menu.")
            continue

        if user_action == 1:
            add_item_to_collection()

        elif user_action == 2:
            collection = get_collections()
            show_items(collection, item_types)

        elif user_action == 3:
            collection = get_collections()
            delete_items(collection, item_types)

        elif user_action == 4:
            print("Have a nice day!")
            break

if __name__ == "__main__":
    main()
