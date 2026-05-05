import uuid

class InventoryItem: 
    def __init__(self, item_id, name, quantity, price): 
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.sku = str(uuid.uuid4())

    def display_info(self): 
        print(f"Item ID: {self.item_id}, Name: {self.name}, Qantity: {self.quantity}, Price: ${self.price:.2f}, Sku: {self.sku}") 