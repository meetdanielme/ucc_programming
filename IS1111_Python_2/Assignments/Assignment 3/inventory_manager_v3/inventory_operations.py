# inventory_operations.py
# Name: Daniel Marcinkowski
# Student ID: 125701129
# Date: 25/02/2026
# Description: Inventory and transaction processing functions for Assignment 3.

from datetime import datetime


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


def generate_product_id(inventory):
    """
    Generate the next unique product ID (P001, P002, P003, etc.).

    Parameters:
        inventory (dict): The inventory dictionary with product IDs as keys

    Returns:
        str: Next product ID in format P001, P002, etc.
    """
    if not inventory:
        return "P001"

    max_num = 0
    for product_id in inventory.keys():
        num = int(product_id[1:])
        if num > max_num:
            max_num = num

    next_num = max_num + 1
    return f"P{next_num:03d}"


def find_product_by_name(inventory, search_term):
    """
    Search for products whose name contains the search term (case-insensitive).

    Parameters:
        inventory (dict): The inventory dictionary
        search_term (str): The term to search for

    Returns:
        list: List of (product_id, product_dict) tuples matching the search
    """
    matches = []
    search_lower = search_term.lower()

    for product_id, product in inventory.items():
        if search_lower in product["name"].lower():
            matches.append((product_id, product))

    return matches


def find_product_by_category(inventory, category):
    """
    Find all products in a specific category (case-insensitive exact match).

    Parameters:
        inventory (dict): The inventory dictionary
        category (str): The category to search for

    Returns:
        list: List of (product_id, product_dict) tuples in the category
    """
    matches = []
    category_lower = category.lower()

    for product_id, product in inventory.items():
        if product["category"].lower() == category_lower:
            matches.append((product_id, product))

    return matches


def log_transaction(transactions, trans_type, product_id, product_name, quantity):
    """
    Log a transaction (sale, delivery, or product addition).

    Parameters:
        transactions (list): The list of transaction dictionaries
        trans_type (str): Type of transaction ("sale", "delivery", or "added")
        product_id (str): The product ID involved
        product_name (str): The product name
        quantity (int): The quantity (negative for sales, positive for deliveries/additions)
    """
    transaction = {
        "type": trans_type,
        "product_id": product_id,
        "product_name": product_name,
        "quantity": quantity,
        "timestamp": datetime.now().isoformat()
    }
    transactions.append(transaction)


def view_transaction_log(transactions, num_recent=10):
    """
    Display recent transactions from the log.

    Parameters:
        transactions (list): The list of transaction dictionaries
        num_recent (int): Number of recent transactions to display (default: 10)
    """
    print(f"\n--- Transaction Log (Last {num_recent}) ---")

    if not transactions:
        print("No transactions recorded yet.")
        return

    print(f"{'Timestamp':<20} {'Type':<10} {'Product':<20} {'Quantity':<10}")
    print("=" * 60)

    recent = transactions[-num_recent:] if len(transactions) > num_recent else transactions

    for trans in reversed(recent):
        timestamp = datetime.fromisoformat(trans["timestamp"])
        time_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        qty_str = f"{trans['quantity']:+d}" if trans['type'] != 'added' else str(trans['quantity'])

        print(f"{time_str:<20} {trans['type'].capitalize():<10} "
              f"{trans['product_name']:<20} {qty_str:<10}")

    print("=" * 60)


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

    print(f"{'ID':<6} {'Product':<20} {'Category':<15} {'Price':<10} {'Stock':<10} {'Min Stock':<10}")
    print("=" * 71)

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

    name = input("Enter product name: ").strip()

    for product in inventory.values():
        if product["name"].lower() == name.lower():
            print(f"Error: Product '{name}' already exists in inventory.")
            return None

    category = input("Enter category: ").strip()
    price = get_valid_float("Enter price (€): ", min_value=0.01)
    qty = get_valid_int("Enter current stock quantity: ", min_value=0)
    min_stock = get_valid_int("Enter minimum stock level: ", min_value=0)

    product_id = generate_product_id(inventory)

    new_product = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": qty,
        "min_stock": min_stock
    }

    inventory[product_id] = new_product
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

    name = input("Enter product name: ").strip()

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

    transaction_type = input("Is this a (S)ale or (D)elivery? ").strip().lower()

    while transaction_type not in ['s', 'd', 'sale', 'delivery']:
        print("Error: Please enter 'S' for sale or 'D' for delivery")
        transaction_type = input("Is this a (S)ale or (D)elivery? ").strip().lower()

    quantity = get_valid_int("Enter quantity: ", min_value=1)

    if transaction_type in ['s', 'sale']:
        if product["quantity"] < quantity:
            print(f"Error: Insufficient stock. Only {product['quantity']} units available.")
            return False
        product["quantity"] -= quantity
        log_transaction(transactions, "sale", product_id, product["name"], -quantity)
        print(f"\nStock updated! {product['name']} now has {product['quantity']} units.")
    else:
        product["quantity"] += quantity
        log_transaction(transactions, "delivery", product_id, product["name"], quantity)
        print(f"\nStock updated! {product['name']} now has {product['quantity']} units.")

    return True


def update_product_details(inventory):
    """
    Update product details (name, category, price, min_stock) for an existing product.

    Note: Quantity is updated through update_stock() to maintain transaction log.

    Parameters:
        inventory (dict): The inventory dictionary

    Returns:
        bool: True if updated successfully, False if product not found
    """
    print("\n--- Update Product Details ---")

    name = input("Enter product name: ").strip()

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

    print(f"\nCurrent details for '{product['name']}' ({product_id}):")
    print(f"Name: {product['name']}")
    print(f"Category: {product['category']}")
    print(f"Price: €{product['price']:.2f}")
    print(f"Minimum stock: {product['min_stock']}")

    print("\nEnter new values (press Enter to keep current):")

    new_name = input("Enter new name (or press Enter to keep current): ").strip()
    if new_name:
        for other_pid, other_prod in inventory.items():
            if other_pid != product_id and other_prod["name"].lower() == new_name.lower():
                print(f"Error: Product name '{new_name}' already exists.")
                return False
        product["name"] = new_name

    new_category = input("Enter new category (or press Enter to keep current): ").strip()
    if new_category:
        product["category"] = new_category

    print("Enter new price (or -1 to keep current): ", end='')
    new_price = get_valid_float("", min_value=-1.0)
    if new_price > 0:
        product["price"] = new_price

    print("Enter new minimum stock (or -1 to keep current): ", end='')
    new_min = get_valid_int("", min_value=-1)
    if new_min >= 0:
        product["min_stock"] = new_min

    print("\nProduct details updated successfully!")
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

    name = input("Enter product name: ").strip()

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

    confirm = input(f"Are you sure you want to remove '{product['name']}'? (Y/N): ").strip().lower()

    if confirm == 'y' or confirm == 'yes':
        del inventory[product_id]
        print(f"\nProduct '{name}' removed successfully!")
        return True
    else:
        print("Removal cancelled.")
        return False


def search_products(inventory):
    """
    Search for products by name or category and display results.

    Parameters:
        inventory (dict): The inventory dictionary
    """
    print("\n--- Search Products ---")

    search_type = input("Search by (N)ame or (C)ategory? ").strip().lower()

    while search_type not in ['n', 'c', 'name', 'category']:
        print("Error: Please enter 'N' for name or 'C' for category")
        search_type = input("Search by (N)ame or (C)ategory? ").strip().lower()

    if search_type in ['n', 'name']:
        search_term = input("Enter search term: ").strip()
        matches = find_product_by_name(inventory, search_term)
    else:
        category = input("Enter category: ").strip()
        matches = find_product_by_category(inventory, category)

    print("\n--- Search Results ---")

    if not matches:
        print("No products found matching your search.")
        return

    print(f"{'ID':<6} {'Product':<20} {'Category':<15} {'Price':<10} {'Stock':<10}")
    print("=" * 61)

    for product_id, product in matches:
        print(f"{product_id:<6} {product['name']:<20} {product['category']:<15} "
              f"€{product['price']:<9.2f} {product['quantity']:<10}")

    print("=" * 61)
    print(f"Found {len(matches)} product(s)")


def view_low_stock(inventory):
    """
    Display products that are at or below their minimum stock level.

    Parameters:
        inventory (dict): The inventory dictionary
    """
    print("\n--- Low Stock Alerts ---")

    low_stock_products = []
    for product_id, product in inventory.items():
        if product["quantity"] <= product["min_stock"]:
            low_stock_products.append((product_id, product))

    if not low_stock_products:
        print("No products currently below minimum stock level.")
        return

    print(f"{'ID':<6} {'Product':<20} {'Category':<15} {'Current':<10} {'Minimum':<10} {'Order':<10}")
    print("=" * 71)

    for product_id, product in low_stock_products:
        order_qty = product["min_stock"] - product["quantity"] + product["min_stock"]
        print(f"{product_id:<6} {product['name']:<20} {product['category']:<15} "
              f"{product['quantity']:<10} {product['min_stock']:<10} {order_qty:<10}")

    print("=" * 71)
    print(f"Total products needing reorder: {len(low_stock_products)}")


def generate_category_report(inventory):
    """
    Generate a report showing product count and total value per category.

    Parameters:
        inventory (dict): The inventory dictionary

    Returns:
        dict: Dictionary mapping category to {"count": n, "value": v}
    """
    print("\n--- Category Report ---")

    if not inventory:
        print("No products in inventory.")
        return {}

    category_data = {}

    for product in inventory.values():
        category = product["category"]
        product_value = product["price"] * product["quantity"]

        if category not in category_data:
            category_data[category] = {"count": 0, "value": 0.0}

        category_data[category]["count"] += 1
        category_data[category]["value"] += product_value

    print(f"{'Category':<20} {'Products':<12} {'Total Value':<15}")
    print("=" * 47)

    total_products = 0
    total_value = 0.0

    for category, data in sorted(category_data.items()):
        print(f"{category:<20} {data['count']:<12} €{data['value']:<14.2f}")
        total_products += data["count"]
        total_value += data["value"]

    print("=" * 47)
    print(f"{'Total:':<20} {total_products:<12} €{total_value:<14.2f}")

    return category_data


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
