from inventory_item import InventoryItem
from inventory_manager import InventoryManager


def main(): 
    store = InventoryManager("inventory.csv")
    store.load_inventory() 

    while True: 
        print("\n===== E-Commerce System =====")
        print("1. Add an Item")
        print("2. Display Inventory")
        print("3. Filter items by price")
        print("4. Delete an item by ID")
        print("5. Save Inventory")
        print("6. Exit")
    
        option = input("Enter your choice (1-6): ")
        if option == "1": 
            name = input("Enter name: ")
            quantity = int(input("Enter quanity: ")) # convert since input is string
            price = float(input("Enter price: ")) # convert since input is string

            store.add_item(name, quantity, price)
             
        elif option == "2": 
            store.display_inventory() 

        elif option == "3": 
            price = float(input("Enter max price: "))
            filtered_items = store.filter_items(price) 

            print(f"Items les than {price}:")
            for item in filtered_items: 
                item.display_info()

        elif option == "4": 
            id = int(input("Enter item id to delete: "))
            store.delete_item_by_id(id)

            print("Successfully deleted item")
        elif option == "5": 
            store.save_inventory()
            print("Saved to CSV")
        elif option == "6":
            print("Exiting...")
            break
        else: 
            print("Invalid option... ")

if __name__ == "__main__": 
    main() 