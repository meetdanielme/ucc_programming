# inventory_v1.py
# Name: Daniel Marcinkowski
# Student ID: 125701129
# Date: 02/02/2026
# Description: Product Inventory Management System using a 2D List
#              for Murphy's General Store (Assignment 1)

# =============================================================================
# ASSIGNMENT 1: List-Based Inventory (Version 1.0)
# =============================================================================
#
# For complete instructions, step-by-step guidance, sample outputs,
# and implementation checklists, see A1_INSTRUCTIONS.txt
#
# Quick Reference:
# ----------------
# - Use ONE main list called 'inventory' containing sub-lists.
# - Each sub-list: [name, category, price, quantity, min_stock]
# - Use the CONSTANTS provided below to access data safely.
#
# =============================================================================

# --- CONSTANTS ---
# Use these variables to access data in your sub-lists.
# This makes your code readable. "product[IDX_PRICE]" is clearer than "product[2]"

# Assign the corresponding index values to the variables below
IDX_NAME = 0
IDX_CATEGORY = 1
IDX_PRICE = 2
IDX_QTY = 3
IDX_MIN = 4

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_valid_float(prompt, min_value=0.0):
    """
    Repeatedly asks user for input until a valid float is entered.
    Returns the valid float.
    """
    while True:
        try:
            value = float(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"Please enter a number greater than or equal to {min_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_int(prompt, min_value=0):
    """
    Repeatedly asks user for input until a valid integer is entered.
    Returns the valid integer.
    """
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"Please enter an integer greater than or equal to {min_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# You may add other helper functions as needed 

# =============================================================================
# CORE FUNCTIONS
# =============================================================================
# Write your functions below.
# Refer to the sample outputs in the instructions for formatting guidance.

# Main menu function
def display_menu():
    
    """
    Function to display the main menu and get user choice
    - Print formatted menu
    - Use validation function to ensure choice is between 1 and 7
    - Keep asking until valid range
    """

    print("\n=== Murphy's General Store - Inventory System ===\n")
    print("1. View All Products")
    print("2. Add New Product")
    print("3. Update Stock")
    print("4. Remove Product")
    print("5. View Low Stock Alerts")
    print("6. View Total Inventory Value")
    print("7. Exit\n")

    choice = get_valid_int("Enter your choice (1-7): ", 1)
    while choice > 7:
        print("Invalid choice. Please select a number between 1 and 7.")
        choice = get_valid_int("Enter your choice (1-7): ", 1)
    return choice

# --- Viewing All Products ---
def view_all_products(inventory):

    """
    Function to view all products in the inventory in a formatted table
    - Check if inventory is empty
    - Print table header
    - Print each product using index constants
    """

    if not inventory:
        print("\nInventory is empty.\n")
        return
    else:
        print("\n--- All Products ---\n")
        print(f"{'Product':<20} {'Category':<10} {'Price':<10} {'Stock':<10} {'Min Stock':<10}")
        print("=" * 65)
        for product in inventory:
            print(f"{product[IDX_NAME]:<20} {product[IDX_CATEGORY]:<10} €{product[IDX_PRICE]:<10,.2f} {product[IDX_QTY]:<10} {product[IDX_MIN]:<10}")

# --- Adding a New Product ---
def add_product(inventory):

    """
    Function to add a new product to the inventory
    - Get product name and check for duplicates (case-insensitive)
    - Loop through inventory to check if product already exists
    - Get remaining product details with validation
    - Create new product sub-list and append to inventory
    """

    print("\n--- Add a New Product ---\n")
    name = input("Enter product name: ").strip()
    # Check for duplicates
    for product in inventory:
        if product[IDX_NAME].lower() == name.lower():
            print(f"Error: Product '{name}' already exists in inventory.\n")
            return
    category = input("Enter category: ").strip().title()
    price = get_valid_float("Enter price (€): ", 0.01)
    quantity = get_valid_int("Enter current stock quantity: ", 0)
    min_stock = get_valid_int("Enter minimum stock level: ", 0)
    new_product = [name, category, price, quantity, min_stock]
    inventory.append(new_product)
    
    print(f"\nProduct '{name}' added successfully!\n")

# --- Updating Stock (Sale) ---
def update_stock(inventory):
    """
    Function to update stock quantity of a product
    - Get product name to update
    - Find the product in inventory
    - Check if product exists
    - Ask whether it's a sale or delivery
    - Validate transaction type (loop until valid option entered by user)
    - Get quantity
    - Process sale (update stock)
    - Process delivery (update stock)
    """

    print("\n--- Update Stock ---\n")
    name = input("Enter product name to update: ").strip()
    for product in inventory:
        if product[IDX_NAME].lower() == name.lower():
            sale_or_delivery = input("Is this a (S)ale or (D)elivery? ").strip().upper()
            while sale_or_delivery not in ['S', 'D']:
                print("Invalid option. Please enter 'S' for Sale or 'D' for Delivery.")
                sale_or_delivery = input("Is this a (S)ale or (D)elivery? ").strip().upper()
            if sale_or_delivery == 'S': # Sale
                qty = get_valid_int("Enter quantity: ", 1)
                if qty > product[IDX_QTY]:
                    print(f"Error: Cannot sell {qty} units. Only {product[IDX_QTY]} in stock.\n")
                else: # Sale
                    product[IDX_QTY] -= qty
                    print(f"\nStock updated! '{product[IDX_NAME]}' now has {product[IDX_QTY]} units.\n")
            else:  # Delivery 
                qty = get_valid_int("Enter quantity: ", 1)
                product[IDX_QTY] += qty
                print(f"\nStock updated! '{product[IDX_NAME]}' now has {product[IDX_QTY]} units.\n")
            return
    print(f"Error: Product '{name}' not found in inventory.\n")


# --- Removing a Product ---
def remove_product(inventory):
    """
    Function to remove a product from the inventory
    - Get product name to remove
    - Find the product's index in inventory
    - Check if product exists
    - Confirm removal
    - Remove product from inventory
    """
    print("\n--- Remove Product ---\n")
    name = input("Enter product name: ").strip()
    for i, product in enumerate(inventory):
        if product[IDX_NAME].lower() == name.lower():
            confirm = input(f"Are you sure you want to remove '{product[IDX_NAME]}'? (yes/no): ").strip().lower()
            if confirm == 'yes':
                inventory.pop(i)
                print(f"\nProduct '{product[IDX_NAME]}' removed successfully!\n")
            else:
                print("\nRemoval cancelled.\n")
            return
    print(f"Error: Product '{name}' not found in inventory.\n")


# --- Viewing Low Stock Alerts ---
def view_low_stock(inventory):
    """
    Function to view low stock products in formatted table
    - Find products with low stock
    - If no product needs restocking, print message
    - Print table header
    - Display each low stock product with amount to order
    """

    low_stock_products = [product for product in inventory if product[IDX_QTY] <= product[IDX_MIN]]
    if not low_stock_products:
        print("\nNo products need restocking.\n")
        return
    else:
        print("\n--- Low Stock Alerts ---\n")
        print(f"{'Product':<20} {'Current':<10} {'Minimum':<10} {'Order':<10}")
        print("=" * 50)
        for product in low_stock_products:
            to_order = product[IDX_MIN] - product[IDX_QTY]
            print(f"{product[IDX_NAME]:<20} {product[IDX_QTY]:<10} {product[IDX_MIN]:<10} {to_order:<10}")
        print("=" * 50)

# --- Viewing Total Inventory Value ---
def total_inventory_value(inventory):
    """
    Function to calculate total inventory value
    - Sum up (price * quantity) for each product
    """

    total_value = sum(product[IDX_PRICE] * product[IDX_QTY] for product in inventory)
    print(f"\nTotal Inventory Value: €{total_value:,.2f}\n")


# =============================================================================
# MAIN PROGRAMME
# =============================================================================

if __name__ == "__main__":
    
    inventory = [
      ["Milk",   "Dairy",   1.50,  20,  10],
      ["Bread",  "Bakery",  0.85,  15,   5],
      ["Tea",    "Bevs",    3.20,  30,   8]
  ]


    # 2. Display a welcome message
    print("\nWelcome to Murphy's General Store Inventory Management System!\n")

    # 3. Your main menu loop goes here
    # - Display menu
    # - Get user choice
    # - Call appropriate function based on choice
    # - Repeat until user exits
    # - Display results or error messages

    while True:
        choice = display_menu()
        if choice == 1:
            view_all_products(inventory)
        elif choice == 2:
            add_product(inventory)
        elif choice == 3:
            update_stock(inventory)
        elif choice == 4:
            remove_product(inventory)
        elif choice == 5:
            view_low_stock(inventory)
        elif choice == 6:
            total_inventory_value(inventory)
        elif choice == 7:
            print("\nThank you for using the Inventory Management System. Goodbye!\n")
            break




# =============================================================================
# REFERENCES & AI STATEMENT
# =============================================================================
# References to any external sources used (following Canvas guidelines):
#
#
# AI Tool Usage:
# I acknowledge the use of Claude Sonnet 4.5 via GitHub Copilot (integrated into Visual Studio Code IDE) 
# to generate inline code suggestions during development. 
# 
# The AI assistant provided suggestions for function implementations, code structure, and formatting 
# which I reviewed, adapted, and integrated into my solution.
#
# =============================================================================

# =============================================================================
# SELF-REFLECTION (2-3 sentences)
# =============================================================================
# Write about the most challenging aspect of this assignment 
# and what you learned from it:
#
# I found creating the update_stock function most challenging due to the nesting if statements.
# It required careful handling of user input and stock validation. 
# This assignment enhanced my skills in list manipulation and user input validation in Python.
#
# =============================================================================