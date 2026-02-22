# ══════════════════════════════════════════════════════════════════
# EXERCISE B: PERSISTENT INVENTORY DATABASE — SOLUTIONS
# Client: "TidyDesk Stationery"
# ══════════════════════════════════════════════════════════════════

import json
import csv

inventory = {
    "S001": {"name": "A4 Notebook",     "category": "Paper",  "price": 3.50, "stock": 45},
    "S002": {"name": "Ballpoint Pens",  "category": "Pens",   "price": 1.20, "stock": 120},
    "S003": {"name": "Highlighter Set", "category": "Pens",   "price": 4.99, "stock": 30},
    "S004": {"name": "USB-C Cable",     "category": "Tech",   "price": 8.99, "stock": 15},
}


def load_inventory(filename):
    """Load inventory from a JSON file (READ operation).

    Parameters:
        filename (str): Path to the JSON file

    Returns:
        dict: Inventory dictionary, or empty dict on failure
    """
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        print(f"Loaded {len(data)} products from {filename}")
        return data
    except FileNotFoundError:
        print(f"Note: {filename} not found. Starting empty.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: {filename} corrupted. Starting empty.")
        return {}


def update_price(inventory, product_id, new_price, filename):
    """Update a product's price and save to JSON (UPDATE operation).

    Parameters:
        inventory (dict): The inventory dictionary
        product_id (str): ID of the product to update
        new_price (float): New price value
        filename (str): JSON file to save to

    Returns:
        bool: True if updated, False if product not found
    """
    if product_id not in inventory:
        print(f"Error: {product_id} not found in inventory.")
        return False

    old_price = inventory[product_id]["price"]
    inventory[product_id]["price"] = new_price

    with open(filename, "w") as f:
        json.dump(inventory, f, indent=2)

    print(f"Updated {product_id}: €{old_price:.2f} → €{new_price:.2f}")
    return True


def export_price_list(inventory, filename):
    """Export inventory to CSV flat-file (EXPORT operation).

    Parameters:
        inventory (dict): The inventory dictionary
        filename (str): CSV file to export to
    """
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Category", "Price", "Stock"])
        for pid, product in inventory.items():
            writer.writerow([
                pid,
                product["name"],
                product["category"],
                f"{product['price']:.2f}",
                product["stock"]
            ])
    print(f"Exported {len(inventory)} products to {filename}")


# ── Test ─────────────────────────────────────────────────────────
print("=" * 55)
print("  TIDYDESK STATIONERY — DATABASE SYSTEM TEST")
print("=" * 55)

with open("stationery.json", "w") as f:
    json.dump(inventory, f, indent=2)
print("Initial data saved to stationery.json")

print("\n--- Task 1: Load ---")
loaded = load_inventory("stationery.json")
print(f"Notebooks in stock: {loaded['S001']['stock']}")

empty = load_inventory("nonexistent.json")
print(f"Missing file result: {empty}")

print("\n--- Task 2: Update ---")
update_price(loaded, "S002", 1.50, "stationery.json")
update_price(loaded, "S999", 5.00, "stationery.json")

print("\n--- Task 3: Export ---")
export_price_list(loaded, "price_list.csv")

print("\nCSV contents:")
with open("price_list.csv", "r") as f:
    for line in f:
        print(f"  {line.rstrip()}")


# ══════════════════════════════════════════════════════════════════
# MASTERY CHECK — You can now:
#   ✓ Load data from JSON with error handling  
#   ✓ Modify data and persist changes to disk  
#   ✓ Export data to CSV for non-programmers   
#   ✓ Name the CRUD operations in your own code
#   ✓ Explain when JSON vs CSV is the right choice
#   → These are the exact patterns A3's data_handler.py uses!
# ══════════════════════════════════════════════════════════════════