import csv
from inventory_item import InventoryItem

class InventoryManager: 
    def __init__(self, file): 
        self.file = file
        self.inventory: list[InventoryItem] = []
        self.next_item_id = 0

    # loads existing items from CSV file 
    def load_inventory(self):
        try:
            # open CSV file 
            with open(self.file, "r") as file:
                # read each row - returns a dictionary map 
                reader = csv.DictReader(file)
                
                self.inventory = []
                # for each row create an InventoryItem 
                for row in reader:
                    item_id = int(row["ItemID"])
                    name = row["Name"]
                    quantity = int(row["Quantity"])
                    price = float(row["Price"])
                    
                    item = InventoryItem(item_id, name, quantity, price)
                    # add item to inventory list 
                    self.inventory.append(item)
                    self.next_item_id = len(self.inventory) + 1 # create new id for next item
                    
        except FileNotFoundError:
            print("No file found at path:", self.file)

    def save_inventory(self):
        # open file 
        with open(self.file, "w", newline="") as file:
            fieldnames = ["ItemID", "Name", "Quantity", "Price", "SKU"]
            # use csv writer 
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            # for each item in invetory write row to csv file 
            for item in self.inventory:
                row = {
                    "ItemID": item.item_id,
                    "Name": item.name,
                    "Quantity": item.quantity,
                    "Price": item.price,
                    "SKU": item.sku
                }
                writer.writerow(row)

    # adding new item to inventory list and save to CSV file 
    def add_item(self, name, quantity, price): 
        item = InventoryItem(self.next_item_id, name, quantity, price)  
        self.inventory.append(item)
        self.next_item_id += 1

        # save
        self.save_inventory()

    # display everything from csv file 
    def display_inventory(self): 
        if not self.inventory: 
            print("Empty...")
        else: 
            for item in self.inventory: 
                item.display_info()

    def delete_item_by_id(self, item_id):
        for item in self.inventory:
            if item.item_id == item_id:
                self.inventory.remove(item)
                self.save_inventory()
                break

    # filter by price 
    def filter_items(self, price): 
        filtered_items = [] 
        for item in self.inventory: 
            if item.price <= price: 
                filtered_items.append(item)

        return filtered_items 

