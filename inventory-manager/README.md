# inventory-manager

A CLI-based Python project for managing an e-commerce inventory. Items are persisted to a CSV file and can be added, viewed, filtered by price, and deleted through an interactive menu.

## Project Structure

```
inventory-manager/
├── main.py                # Entry point: interactive menu loop
├── inventory_manager.py   # InventoryManager class (CRUD + CSV persistence)
├── inventory_item.py      # InventoryItem data class (auto-generates SKU via uuid)
└── inventory.csv          # Persisted inventory data
```

## Data Format

`inventory.csv` stores items with the following columns:

| Column     | Description                        |
|------------|------------------------------------|
| `ItemID`   | Auto-incremented integer ID        |
| `Name`     | Product name                       |
| `Quantity` | Number of units in stock           |
| `Price`    | Unit price (float)                 |
| `SKU`      | Auto-generated UUID for the item   |

## Requirements

- Python 3.9+
- No third-party dependencies

## Usage

```bash
python main.py
```

You will be presented with a menu:

```
===== E-Commerce System =====
1. Add an Item
2. Display Inventory
3. Filter items by price
4. Delete an item by ID
5. Save Inventory
6. Exit
```

## Classes

**`InventoryItem`** (`inventory_item.py`)
- Stores `item_id`, `name`, `quantity`, `price`, and an auto-generated `sku`.
- `display_info()` — prints a formatted summary of the item.

**`InventoryManager`** (`inventory_manager.py`)
- `load_inventory()` — reads items from the CSV file into memory.
- `save_inventory()` — writes the current inventory back to the CSV file.
- `add_item(name, quantity, price)` — creates a new item and saves.
- `display_inventory()` — prints all items.
- `delete_item_by_id(item_id)` — removes an item by ID and saves.
- `filter_items(price)` — returns items with price at or below the given value.
