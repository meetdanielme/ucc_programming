# Name: Daniel Marcinkowski
# Student ID: 125701129
# Date: 02/02/2026
# Description: Inventory management system v1

# Indices for inventory items: product[IDX_NAME] instead of product[0]
IDX_NAME = 0
IDX_CATEGORY = 1
IDX_PRICE = 2
IDX_QTY = 3
IDX_MIN = 4

# Sample inventory data
inventory = [
      ["Milk",   "Dairy",   1.50,  20,  10],
      ["Bread",  "Bakery",  0.85,  15,   5],
      ["Tea",    "Bevs",    3.20,  30,   8]
  ]

def main_menu():
    '''
    Displays the main menu and returns the user's choice as an integer
    '''
    print("\n=== Murphy's General Store - Inventory System ===\n")
    print("1. View All Products")
    print("2. Add New Product")
    print("3. Update Stock")
    print("4. Remove Product")
    print("5. View Low Stock Alerts")
    print("6. View Total Inventory Value")
    print("7. Exit\n")
    try:
        choice = int(input("Enter your choice: (1-7)" ))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")
        return None
    return choice


