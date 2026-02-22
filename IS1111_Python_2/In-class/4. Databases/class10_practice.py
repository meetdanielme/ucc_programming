# ══════════════════════════════════════════════════════════════════
# EXERCISE B: PERSISTENT INVENTORY DATABASE
# Client: "TidyDesk Stationery"
#
# Background:
# TidyDesk is a small stationery shop near UCC campus that
# supplies students with notebooks, pens, and tech accessories.
# The owner, Fiona, needs a system that REMEMBERS inventory
# between sessions (JSON document database) and can EXPORT a
# price list for the UCC Students' Union (CSV flat-file).
#
# Build the three database functions below. Each one uses
# patterns you already know from the live demo and Class 9.
# ══════════════════════════════════════════════════════════════════

import json
import csv

# Sample inventory (same nested dict structure as A3)
inventory = {
    "S001": {"name": "A4 Notebook",     "category": "Paper",  "price": 3.50, "stock": 45},
    "S002": {"name": "Ballpoint Pens",  "category": "Pens",   "price": 1.20, "stock": 120},
    "S003": {"name": "Highlighter Set", "category": "Pens",   "price": 4.99, "stock": 30},
    "S004": {"name": "USB-C Cable",     "category": "Tech",   "price": 8.99, "stock": 15},
}


# TASK 1: load_inventory(filename)
# ----------------------------------
# READ operation: Load inventory from a JSON document database.
#
# Handle TWO errors:
#   - FileNotFoundError → print a note, return empty dict
#   - json.JSONDecodeError → print an error message, return empty dict
# On success, print how many products were loaded.
# Return the loaded dictionary.
#
# This is exactly what A3's load_inventory() does at startup.
#
# Expected:
#   load_inventory("stationery.json")  → loads dict, prints count
#   load_inventory("missing.json")     → prints note, returns {}

def load_inventory(filename):
    pass


# TASK 2: update_price(inventory, product_id, new_price, filename)
# -----------------------------------------------------------------
# UPDATE operation: change a product's price and persist to disk.
#
# Steps:
#   1. Check if product_id exists in inventory
#   2. If not found, print error message and return False
#   3. If found, update the price in the dict
#   4. Save the entire inventory to the JSON file
#   5. Print confirmation with old and new price
#   6. Return True
#
# Expected:
#   update_price(inv, "S002", 1.50, "stationery.json")
#   → prints "Updated S002: €1.20 → €1.50", returns True
#
#   update_price(inv, "S999", 5.00, "stationery.json")
#   → prints "Error: S999 not found", returns False

def update_price(inventory, product_id, new_price, filename):
    pass


# TASK 3: export_price_list(inventory, filename)
# ------------------------------------------------
# EXPORT to CSV flat-file for the Students' Union.
#
# Include header row: ID, Name, Category, Price, Stock
# Write one row per product.
# Remember: use newline="" when opening for CSV.
# Print confirmation with count of products exported.
#
# Expected CSV:
#   ID,Name,Category,Price,Stock
#   S001,A4 Notebook,Paper,3.50,45
#   S002,Ballpoint Pens,Pens,1.50,120
#   ...

def export_price_list(inventory, filename):
    pass


# ── Test your functions ──────────────────────────────────────────
print("=" * 55)
print("  TIDYDESK STATIONERY — DATABASE SYSTEM TEST")
print("=" * 55)

# Save initial data to create our JSON "database"
with open("stationery.json", "w") as f:
    json.dump(inventory, f, indent=2)
print("Initial data saved to stationery.json")

# Task 1: Load (valid file + missing file)
print("\n--- Task 1: Load ---")
loaded = load_inventory("stationery.json")
print(f"Notebooks in stock: {loaded['S001']['stock']}")

empty = load_inventory("nonexistent.json")
print(f"Missing file result: {empty}")

# Task 2: Update (valid ID + invalid ID)
print("\n--- Task 2: Update ---")
update_price(loaded, "S002", 1.50, "stationery.json")
update_price(loaded, "S999", 5.00, "stationery.json")

# Task 3: Export to CSV
print("\n--- Task 3: Export ---")
export_price_list(loaded, "price_list.csv")

# Verify CSV output
print("\nCSV contents:")
with open("price_list.csv", "r") as f:
    for line in f:
        print(f"  {line.rstrip()}")