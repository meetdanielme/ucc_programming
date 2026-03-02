# topic5_lecture1_exercise2.py
# Lecture 1 | Exercise 2: Classify & sketch imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Time: ~15 minutes
#
# This file contains a single-file café programme with 9 functions.
# A developer has written everything in one place, which is hard
# to maintain as the programme grows.
#
# Your tasks:
#
#   TASK A (10 min)
#   Read each function and write which of the three modules it
#   belongs to in the "# MODULE:" comment directly below its def line.
#   Choose from:
#       main.py              - user interface (menus, prompts, print statements)
#       cafe_operations.py   - business logic (calculations, data processing)
#       data_handler.py      - file operations (reading/writing files)
#
#   TASK B (5 min)
#   Scroll to the bottom and sketch the import statements that
#   main.py, cafe_operations.py, and data_handler.py would each need.
#
#   Note: there is no need to type or run any code - work on paper or
#   as comments in this file.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import json
import csv

menu = {
    "P001": {"name": "Cappuccino", "price": 3.50, "category": "Hot Drinks"},
    "P002": {"name": "Croissant",  "price": 2.80, "category": "Food"},
    "P003": {"name": "Americano",  "price": 2.90, "category": "Hot Drinks"},
    "P004": {"name": "Muffin",     "price": 2.50, "category": "Food"},
}

orders = []


# -----------------------------------------------------------------------
# FUNCTION 1
def display_main_menu():
    """Prints the main menu options to the screen."""
    # MODULE: main.py
    print("\n=== Mocha's Café ===")
    print("1. Place order")
    print("2. View daily report")
    print("3. Export orders to CSV")
    print("4. Save & exit")


# -----------------------------------------------------------------------
# FUNCTION 2
def get_menu_item(item_id):
    """Returns the menu item dict for a given item ID, or None if not found."""
    # MODULE: cafe_operations.py 
    return menu.get(item_id)


# -----------------------------------------------------------------------
# FUNCTION 3
def calculate_order_total(item_ids):
    """Calculates and returns the total price for a list of item IDs."""
    # MODULE: cafe_operations.py
    total = 0.0
    for item_id in item_ids:
        item = menu.get(item_id)
        if item:
            total += item["price"]
    return total


# -----------------------------------------------------------------------
# FUNCTION 4
def add_order(item_ids):
    """Records a new order (list of item IDs) in the orders list."""
    # MODULE: cafe_operations.py
    order = {
        "items": item_ids,
        "total": calculate_order_total(item_ids)
    }
    orders.append(order)
    print(f"Order added. Total: €{order['total']:.2f}")


# -----------------------------------------------------------------------
# FUNCTION 5
def get_user_choice(prompt, valid_choices):
    """Prompts user for input and keeps asking until a valid choice is entered."""
    # MODULE: main.py
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please enter one of: {valid_choices}")


# -----------------------------------------------------------------------
# FUNCTION 6
def calculate_daily_total():
    """Returns the sum of all order totals recorded today."""
    # MODULE: cafe_operations.py
    return sum(order["total"] for order in orders)


# -----------------------------------------------------------------------
# FUNCTION 7
def save_orders_to_json(filename):
    """Saves the orders list to a JSON file."""
    # MODULE: data_handler.py
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(orders, f, indent=2)
        print(f"Orders saved to {filename}.")
    except IOError as e:
        print(f"Error saving file: {e}")


# -----------------------------------------------------------------------
# FUNCTION 8
def export_orders_to_csv(filename):
    """Exports orders to a CSV file with columns: order_number, total."""
    # MODULE: data_handler.py
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Order Number", "Total (€)"])
            for i, order in enumerate(orders, 1):
                writer.writerow([i, f"{order['total']:.2f}"])
        print(f"Orders exported to {filename}.")
    except IOError as e:
        print(f"Error exporting to CSV: {e}")


# -----------------------------------------------------------------------
# FUNCTION 9
def main():
    """Main programme loop."""
    # MODULE: main.py
    while True:
        display_main_menu()
        choice = get_user_choice("Enter choice: ", ["1", "2", "3", "4"])
        if choice == "1":
            add_order(["P001", "P002"])   # simplified for demo
        elif choice == "2":
            print(f"Daily total: €{calculate_daily_total():.2f}")
        elif choice == "3":
            export_orders_to_csv("orders.csv")
        elif choice == "4":
            save_orders_to_json("orders.json")
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()


# =======================================================================
# TASK B: Sketch the import statements
# =======================================================================
# Once you have classified all functions, think about which imports
# each file will need. Remember: only main.py should import from the
# other two modules - avoid circular imports.
#
# main.py imports:
# TODO: from cafe_operations import calculate_order_total, add_order
# TODO: from data_handler import save_orders_to_json, export_orders_to_csv
#
# cafe_operations.py imports:
# TODO: (think carefully - does it need to import from other modules?)
#
# data_handler.py imports:
# TODO: (think carefully - does it need to import from other modules?)
#       (hint: it will at least need some standard library imports)
