# inventory_v2.py
# Name: Daniel Marcinkowski
# Student ID: 125701129
# Date: 12/02/2026
# Description: Product Inventory Management System using dictionaries
#              for Murphy's General Store (Assignment 2)

# =============================================================================
# IMPORTS
# =============================================================================
# YOUR CODE: Import datetime here
from datetime import datetime

# =============================================================================
# ASSIGNMENT 2: Dictionaries & Transaction Logging
# =============================================================================
#
# NEW APPROACH: Full dictionary-based code for basic operations is provided.
# Your task: Add NEW features that demonstrate dictionary mastery.
#
# For complete instructions, step-by-step guidance, sample outputs, and 
# implementation checklists, see A2_INSTRUCTIONS.txt
#
# What's PROVIDED (full code below):
# - Helper functions (get_valid_float, get_valid_int)
# - display_menu() - shows 11 options
# - view_all_products() - displays inventory using dictionaries
# - add_product() - adds products to dictionary (calls YOUR generate_product_id)
# - update_stock() - modifies stock (calls YOUR log_transaction)
# - remove_product() - removes from dictionary
# - view_low_stock() - finds products needing reorder
# - calculate_inventory_value() - sums total value
#
# What YOU WRITE (5 new functions):
# 1. generate_product_id(inventory) - creates P001, P002, etc.
# 2. search_products(inventory) - searches by name or category
# 3. log_transaction(...) - records stock changes with timestamp
# 4. view_transaction_log(transactions) - displays recent transactions
# 5. generate_category_report(inventory) - groups by category
#
# =============================================================================

# =============================================================================
# PROVIDED: HELPER FUNCTIONS
# =============================================================================
# These work exactly as they did in A1 - no changes needed

def get_valid_float(prompt, min_value=0.0):
    """
    Prompt the user for a float value and validate it.
    
    Parameters:
        prompt (str): The message to display to the user
        min_value (float): The minimum acceptable value (default: 0.0)
    
    Returns:
        float: A valid float value >= min_value
    """
    while True:
        try:
            value = float(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"Error: Value must be at least {min_value}")
        except ValueError:
            print("Error: Please enter a valid number")


def get_valid_int(prompt, min_value=0):
    """
    Prompt the user for an integer value and validate it.
    
    Parameters:
        prompt (str): The message to display to the user
        min_value (int): The minimum acceptable value (default: 0)
    
    Returns:
        int: A valid integer value >= min_value
    """
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"Error: Value must be at least {min_value}")
        except ValueError:
            print("Error: Please enter a valid whole number")


# =============================================================================
# YOUR CODE: ID GENERATION (NEW FUNCTION #1)
# =============================================================================

def generate_product_id(inventory):
    """
    Create unique product IDs (P001, P002, P003, etc.)
    
    Parameters:
        inventory (dict): The inventory dictionary to check existing IDs

    Returns:
        str: A new unique product ID
    """

    # If inventory is empty, start with P001

    if not inventory:
        return "P001"
    
    # Extract existing IDs and find the highest number
    
    max_num = 0
    for product_id in inventory.keys():
        try:
            num_part = int(product_id[1:])  # Extract number after 'P'
            if num_part > max_num:
                max_num = num_part
        except ValueError:
            continue  # Skip any IDs that don't follow the format
  
    next_num = max_num + 1
    return f"P{next_num:03d}"


# =============================================================================
# PROVIDED: MENU FUNCTION
# =============================================================================

def display_menu():
    """
    Display the main menu and return the user's validated choice.
    
    Returns:
        int: The user's menu choice (1-10)
    """
    print("\n=== Murphy's General Store - Inventory System ===")
    print("1. View All Products")
    print("2. Add New Product")
    print("3. Update Stock")
    print("4. Remove Product")
    print("5. Search Products")
    print("6. View Low Stock Alerts")
    print("7. View Category Report")
    print("8. View Transaction Log")
    print("9. View Total Inventory Value")
    print("10. Exit")
    
    choice = get_valid_int("\nEnter your choice (1-10): ", min_value=1)
    
    while choice > 10:
        print("Error: Please enter a number between 1 and 10")
        choice = get_valid_int("Enter your choice (1-10): ", min_value=1)
    
    return choice


# =============================================================================
# PROVIDED: BASIC INVENTORY OPERATIONS
# =============================================================================

def view_all_products(inventory):
    """
    Display all products in the inventory in a formatted table.
    
    Parameters:
        inventory (dict): The inventory dictionary with product IDs as keys
    """
    print("\n--- All Products ---")
    
    if not inventory:
        print("No products in inventory.")
        return
    
    # Print table header
    print(f"{'ID':<6} {'Product':<20} {'Category':<15} {'Price':<10} {'Stock':<10} {'Min Stock':<10}")
    print("=" * 71)
    
    # Loop through dictionary using .items()
    for product_id, product in inventory.items():
        print(f"{product_id:<6} {product['name']:<20} {product['category']:<15} "
              f"€{product['price']:<9.2f} {product['quantity']:<10} {product['min_stock']:<10}")
    
    print("=" * 71)
    print(f"Total products: {len(inventory)}")


def add_product(inventory, transactions):
    """
    Add a new product to the inventory after checking for duplicates.
    
    Parameters:
        inventory (dict): The inventory dictionary
        transactions (list): The transactions list for logging
    
    Returns:
        str or None: Product ID if successful, None if duplicate found
    """
    print("\n--- Add New Product ---")
    
    # Get product name and check for duplicates
    name = input("Enter product name: ").strip()
    
    # Check if name already exists by looping through values
    for product in inventory.values():
        if product["name"].lower() == name.lower():
            print(f"Error: Product '{name}' already exists in inventory.")
            return None
    
    # Get remaining product details
    category = input("Enter category: ").strip()
    price = get_valid_float("Enter price (€): ", min_value=0.01)
    qty = get_valid_int("Enter current stock quantity: ", min_value=0)
    min_stock = get_valid_int("Enter minimum stock level: ", min_value=0)
    
    # Generate unique product ID
    product_id = generate_product_id(inventory)
    
    # Create new product dictionary
    new_product = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": qty,
        "min_stock": min_stock
    }
    
    # Add to inventory using product_id as key
    inventory[product_id] = new_product
    
    # Log the transaction
    log_transaction(transactions, "added", product_id, name, qty)
    
    print(f"\nProduct '{name}' added successfully with ID: {product_id}")
    return product_id


def update_stock(inventory, transactions):
    """
    Update the stock quantity for a product (sale or delivery).
    
    Parameters:
        inventory (dict): The inventory dictionary
        transactions (list): The transactions list for logging
    
    Returns:
        bool: True if stock was updated successfully, False otherwise
    """
    print("\n--- Update Stock ---")
    
    # Get product name
    name = input("Enter product name: ").strip()
    
    # Find the product
    product_id = None
    product = None
    for pid, prod in inventory.items():
        if prod["name"].lower() == name.lower():
            product_id = pid
            product = prod
            break
    
    if product is None:
        print(f"Error: Product '{name}' not found in inventory.")
        return False
    
    # Ask transaction type
    transaction_type = input("Is this a (S)ale or (D)elivery? ").strip().lower()
    
    while transaction_type not in ['s', 'd', 'sale', 'delivery']:
        print("Error: Please enter 'S' for sale or 'D' for delivery")
        transaction_type = input("Is this a (S)ale or (D)elivery? ").strip().lower()
    
    # Get quantity
    quantity = get_valid_int("Enter quantity: ", min_value=1)
    
    # Process sale
    if transaction_type in ['s', 'sale']:
        if product["quantity"] < quantity:
            print(f"Error: Insufficient stock. Only {product['quantity']} units available.")
            return False
        product["quantity"] -= quantity
        log_transaction(transactions, "sale", product_id, product["name"], -quantity)
        print(f"\nStock updated! {product['name']} now has {product['quantity']} units.")
    
    # Process delivery
    else:
        product["quantity"] += quantity
        log_transaction(transactions, "delivery", product_id, product["name"], quantity)
        print(f"\nStock updated! {product['name']} now has {product['quantity']} units.")
    
    return True


def remove_product(inventory):
    """
    Remove a product from the inventory after confirmation.
    
    Parameters:
        inventory (dict): The inventory dictionary
    
    Returns:
        bool: True if product was removed successfully, False otherwise
    """
    print("\n--- Remove Product ---")
    
    # Get product name
    name = input("Enter product name: ").strip()
    
    # Find the product
    product_id = None
    product = None
    for pid, prod in inventory.items():
        if prod["name"].lower() == name.lower():
            product_id = pid
            product = prod
            break
    
    if product is None:
        print(f"Error: Product '{name}' not found in inventory.")
        return False
    
    # Confirm deletion
    confirm = input(f"Are you sure you want to remove '{product['name']}'? (Y/N): ").strip().lower()
    
    if confirm == 'y' or confirm == 'yes':
        del inventory[product_id]
        print(f"\nProduct '{name}' removed successfully!")
        return True
    else:
        print("Removal cancelled.")
        return False


def view_low_stock(inventory):
    """
    Display products that are at or below their minimum stock level.
    
    Parameters:
        inventory (dict): The inventory dictionary
    """
    print("\n--- Low Stock Alerts ---")
    
    # Find products with low stock
    low_stock_products = []
    for product_id, product in inventory.items():
        if product["quantity"] <= product["min_stock"]:
            low_stock_products.append((product_id, product))
    
    if not low_stock_products:
        print("No products currently below minimum stock level.")
        return
    
    # Display low stock products
    print(f"{'ID':<6} {'Product':<20} {'Category':<15} {'Current':<10} {'Minimum':<10} {'Order':<10}")
    print("=" * 71)
    
    for product_id, product in low_stock_products:
        order_qty = product["min_stock"] - product["quantity"] + product["min_stock"]
        print(f"{product_id:<6} {product['name']:<20} {product['category']:<15} "
              f"{product['quantity']:<10} {product['min_stock']:<10} {order_qty:<10}")
    
    print("=" * 71)
    print(f"Total products needing reorder: {len(low_stock_products)}")


def calculate_inventory_value(inventory):
    """
    Calculate the total value of all inventory (price × quantity).
    
    Parameters:
        inventory (dict): The inventory dictionary
    
    Returns:
        float: Total inventory value
    """
    print("\n--- Total Inventory Value ---")
    
    if not inventory:
        print("No products in inventory.")
        return 0.0
    
    total = 0.0
    for product in inventory.values():
        product_value = product["price"] * product["quantity"]
        total += product_value
    
    print(f"Total inventory value: €{total:.2f}")
    return total


# =============================================================================
# YOUR CODE: SEARCH FUNCTION (NEW FUNCTION #2)
# =============================================================================

def search_products(inventory):
    """
    Search for products by name or category
    
    Parameters:
        inventory (dict): The inventory dictionary

    Returns:
        None: Displays results in formatted table
    """

    # Ask user for search type
    search_type = input("Search by (N)ame or (C)ategory? ").strip().lower()

    while search_type not in ['n', 'c', 'name', 'category']:
        print("Error: Please enter 'N' for name or 'C' for category")
        search_type = input("Search by (N)ame or (C)ategory? ").strip().lower()
    
    # Get search term
    search_term = input("Enter search term: ").strip().lower()

    # Find matches
    matches = []
    for product_id, product in inventory.items():
        if search_type in ['n', 'name']: # Name search
            if search_term in product["name"].lower():
                matches.append((product_id, product))
        else:  # Category search
            if search_term == product["category"].lower():
                matches.append((product_id, product))

    # Display results
    print("\n--- Search Results ---")
    if not matches:
        print("No products found matching the search criteria.")
        return

    # Display table header
    print(f"{'ID':<6} {'Product':<15} {'Category':<12} {'Price':<8} {'Stock':<6}")
    print("=" * 50)

    # Display matching products
    for product_id, product in matches:
        print(f"{product_id:<6} {product['name']:<15} {product['category']:<12} €{product['price']:<7.2f} {product['quantity']:<6}")

    print("=" * 50)
    if len(matches) == 1:
        print("Found 1 product")
    else:
        print(f"Found {len(matches)} products")

# =============================================================================
# YOUR CODE: TRANSACTION LOGGING (NEW FUNCTIONS #3 and #4)
# =============================================================================

def log_transaction(transactions, trans_type, product_id, product_name, quantity):
    """
    Record stock changes in a transaction log

    Parameters:
        transactions (list): The list to store transaction records
        trans_type (str): The type of transaction ("sale", "delivery", "added")
        product_id (str): The ID of the product involved in the transaction
        product_name (str): The name of the product involved in the transaction
        quantity (int): The quantity changed (positive for delivery/added, negative for sale)

    Returns:
        None: This function modifies the transactions list in place
    """

    transaction_types = ["sale", "delivery", "added"]
    if trans_type not in transaction_types:
        print(f"Error: Invalid transaction type '{trans_type}'. Must be one of {transaction_types}.")
        return  # Stop execution if invalid type
    
    # Create transaction dictionary
    
    transaction = {
        "type": trans_type,
        "product_id": product_id,
        "product_name": product_name,
        "quantity": quantity,
        "timestamp": datetime.now().isoformat()
    }

    # Append to transactions list
    transactions.append(transaction)

def view_transaction_log(transactions, num_recent=10):
    """
    Display recent transactions from the log

    Parameters:
        transactions (list): The list of transaction records
        num_recent (int): The number of recent transactions to display (default: 10)

    Returns:
        None: This function prints the transaction log to the console
    """
    
    if not transactions:
        print("No transactions recorded yet.")
        return
    
    print(f"\n--- Transaction Log (Last {num_recent}) ---")

    # Get the most recent transactions
    recent_transactions = transactions[-num_recent:]
    
    # Print table header
    print(f"{'Timestamp':<20} {'Type':<10} {'Product':<15} {'Quantity':<10}")
    print("=" * 60)
    
    # Display transactions in reverse order (newest first)
    for trans in reversed(recent_transactions):
        timestamp = datetime.fromisoformat(trans["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
        trans_type = trans["type"].capitalize()
        product_name = trans["product_name"]
        quantity = f"{'+' if trans['quantity'] > 0 else ''}{trans['quantity']}"
        print(f"{timestamp:<20} {trans_type:<10} {product_name:<15} {quantity:<10}")

    print("=" * 60)


# =============================================================================
# YOUR CODE: CATEGORY REPORT (NEW FUNCTION #5)
# =============================================================================

def generate_category_report(inventory):
    """
    Show product count and total value per category

    Parameters:
        inventory (dict): The inventory dictionary

    Returns:
        dict: A dictionary with category summaries (count and total value)
    """

    print("\n--- Category Report ---")
    
    if not inventory:
        print("No products in inventory.")
        return {}
    
    category_data = {}
    grand_total_value = 0
    grand_total_count = 0
    
    # Loop through products to build category data
    for product in inventory.values():
        category = product["category"]
        value = product["price"] * product["quantity"]
        
        if category not in category_data:
            category_data[category] = {"count": 0, "value": 0.0}
        
        category_data[category]["count"] += 1
        category_data[category]["value"] += value
        grand_total_value += value
        grand_total_count += 1
    
    # Display report
    print(f"{'Category':<20} {'Products':<10} {'Total Value':<12}")
    print("=" * 45)
    
    for category, data in category_data.items():
        print(f"{category:<20} {data['count']:<10} €{data['value']:<11.2f}")
    
    print("=" * 45)
    print(f"{'Total:':<20} {grand_total_count:<10} €{grand_total_value:<11.2f}")
    
    return category_data


# =============================================================================
# PROVIDED: MAIN PROGRAMME
# =============================================================================

def main():
    """Main programme loop."""
    
    # Initialise data structures
    inventory = {}
    transactions = []
    
    # Add sample data for testing
    sample_data = [
        {"name": "Milk", "category": "Dairy", "price": 1.50, "quantity": 20, "min_stock": 10},
        {"name": "Bread", "category": "Bakery", "price": 0.85, "quantity": 15, "min_stock": 5},
        {"name": "Tea", "category": "Beverages", "price": 3.20, "quantity": 30, "min_stock": 8},
    ]
    
    for item in sample_data:
        product_id = generate_product_id(inventory)
        inventory[product_id] = item
        log_transaction(transactions, "added", product_id, item["name"], item["quantity"])
    
    # Main menu loop
    while True:
        choice = display_menu()
        
        if choice == 1:
            view_all_products(inventory)
        
        elif choice == 2:
            add_product(inventory, transactions)
        
        elif choice == 3:
            update_stock(inventory, transactions)
        
        elif choice == 4:
            remove_product(inventory)
        
        elif choice == 5:
            search_products(inventory)
        
        elif choice == 6:
            view_low_stock(inventory)
        
        elif choice == 7:
            generate_category_report(inventory)
        
        elif choice == 8:
            view_transaction_log(transactions)
        
        elif choice == 9:
            calculate_inventory_value(inventory)
        
        elif choice == 10:
            print("\nThank you for using Murphy's General Store Inventory System!")
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()


# =============================================================================
# REFERENCES & AI STATEMENT
# =============================================================================
#
# AI Tool Usage:
# I acknowledge the use of Claude Opus 4.6 via GitHub Copilot (integrated into Visual Studio Code IDE) 
# only to generate inline code suggestions during development.
# 
# The AI assistant provided suggestions for function implementations, code structure, and formatting 
# which I reviewed, adapted, and integrated into my solution.
#
# The AI assistant provided autocomplete suggestions for:
# - Function structure and formatting
# - Dictionary syntax and operations
# - String formatting in f-strings
#
# =============================================================================

# =============================================================================
# SELF-REFLECTION (2-3 sentences)
# =============================================================================
# Write about the most challenging aspect of this assignment 
# and what you learned from it:
#
# I found dictionaries to be far more powerful and logical than lists for this kind of application.
# Introduction on dictionaries into the project was somewhat challenging at first, but it made the code much cleaner and more efficient.
# I struggle the most with formatting table outputs etc. but I think I have improved a lot in that regard.
#
# =============================================================================
