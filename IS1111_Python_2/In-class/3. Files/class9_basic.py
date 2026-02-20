# ══════════════════════════════════════════════════════════════
# EXERCISE A: FILE OPERATIONS PRACTICE
# Client: "FreshBite Meal Prep"
#
# FreshBite is a Cork-based meal prep delivery service.
# They prepare weekly menus and track customer orders but
# currently write everything on paper. They need a simple
# system to save menus and orders to files so data isn't
# lost at the end of each day. Fill in the blanks to build
# their file operations.
# ══════════════════════════════════════════════════════════════

import json
import csv


# ── Section 1: Writing a text file ───────────────────────────

# Save three menu items to a text file (one per line)
with open("menu.txt", "w") as f:
    f.write("Grilled Chicken Bowl\n")
    f.write("Veggie Wrap\n")
    f.write("Salmon Salad\n")

print("Menu saved to file")


# ── Section 2: Reading a file line by line ───────────────────

# Read and print each menu item, removing the trailing newline
print("\nToday's Menu:")
with open("menu.txt", "r") as f:
    for line in f:
        print(" ", line.rstrip())


# ── Section 3: Appending to a file ───────────────────────────

# Add a new item WITHOUT erasing the existing menu
with open("menu.txt", "a") as f:
    f.write("Protein Pancakes\n")

print("New item appended")


# ── Section 4: Reading entire file as a list ─────────────────

with open("menu.txt", "r") as f:
    all_items = f.readlines()

print(f"\nTotal items: {len(all_items)}")
print("Last item:", all_items[-1].rstrip())


# ── Section 5: Error handling ────────────────────────────────

# Try to load a file that might not exist
filename = "orders.txt"
try:
    with open(filename, "r") as f:
        data = f.read()
    print("Orders loaded successfully")
except FileNotFoundError:
    print(f"Note: {filename} not found. Starting fresh.")
    data = ""


# ── Section 6: Saving a dictionary as JSON ───────────────────

weekly_orders = {
    "Monday": ["Grilled Chicken Bowl", "Veggie Wrap"],
    "Tuesday": ["Salmon Salad", "Protein Pancakes"],
}

with open("orders.json", "w") as f:
    json.dump(weekly_orders, f, indent=2)

print("\nOrders saved to JSON")


# ── Section 7: Loading JSON back ─────────────────────────────

with open("orders.json", "r") as f:
    loaded_orders = json.load(f)

print("Monday's orders:", loaded_orders["Monday"])
print("Type:", type(loaded_orders))


# ── Section 8: Exporting to CSV ──────────────────────────────

with open("menu_summary.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Day", "Item Count"])
    for day, items in weekly_orders.items():
        writer.writerow([day, len(items)])

print("Exported to CSV")