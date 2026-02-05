# EXERCISE B: RESTAURANT ORDERING SYSTEM
# Client: "BiteByte Café"
#
# In Class 1, you stored menus as lists of strings like "Cheeseburger - 5.99"
# Finding a price meant looping and splitting strings.
#
# With a dictionary, the item name IS the key and the price IS the value.
# Lookups are instant: menu["Caesar Salad"] gives you the price directly.

menu = {
    "Cheeseburger": 5.99,
    "Grilled Chicken Sandwich": 7.49,
    "Caesar Salad": 4.99,
    "Veggie Wrap": 6.29,
    "Iced Coffee": 2.99,
    "Lemonade": 1.99,
    "Orange Juice": 3.49
}


# TASK 1: get_price()
# Takes menu and item_name. Returns price if found, -1 if not.
# Use get()!
# Examples:
#   get_price(menu, "Lemonade") → 1.99
#   get_price(menu, "Pizza") → -1

def get_price(menu, item_name):
    pass


# TASK 2: add_item()
# Adds a new item. If item already exists, print warning (don't overwrite).
# Examples:
#   add_item(menu, "Espresso", 2.49) → adds it
#   add_item(menu, "Lemonade", 2.49) → warning, already exists

def add_item(menu, item_name, price):
    pass


# TASK 3: update_price()
# Updates price of existing item. If item doesn't exist, print error.
# Examples:
#   update_price(menu, "Lemonade", 2.29) → updates
#   update_price(menu, "Pizza", 9.99) → error, not on menu

def update_price(menu, item_name, new_price):
    pass


# TASK 4: calculate_order_total()
# Takes menu and a list of item names. Returns total cost.
# Skip items not on the menu (optionally print a note).
# Example:
#   order = ["Cheeseburger", "Lemonade", "Iced Coffee"]
#   calculate_order_total(menu, order) → 10.97

def calculate_order_total(menu, order):
    pass


# TASK 5: display_menu()
# Prints all items and prices. Loop through dictionary keys.
# Hint: for item in menu:
#           price = menu[item]

def display_menu(menu):
    pass


# TEST YOUR FUNCTIONS

print("=" * 40)
print("BITEBYTE CAFÉ - ORDERING SYSTEM")
print("=" * 40)

# Test get_price
print("\n--- Price Lookups ---")
print(f"Cheeseburger: €{get_price(menu, 'Cheeseburger')}")
print(f"Pizza: €{get_price(menu, 'Pizza')}")

# Test add_item
print("\n--- Adding Items ---")
add_item(menu, "Espresso", 2.49)
add_item(menu, "Lemonade", 2.49)

# Test update_price
print("\n--- Updating Prices ---")
update_price(menu, "Lemonade", 2.29)
update_price(menu, "Pizza", 12.99)

# Test calculate_order_total
print("\n--- Order Calculation ---")
customer_order = ["Cheeseburger", "Caesar Salad", "Iced Coffee", "Espresso"]
total = calculate_order_total(menu, customer_order)
print(f"Order: {customer_order}")
print(f"Total: €{total:.2f}")

# Test display_menu
print("\n--- Full Menu ---")
display_menu(menu)


# REFLECTION:
# 1. How would you find "Caesar Salad" price using the Class 1 list format?
# 2. With a dictionary, how many steps does it take?
# 3. How does get() help when a customer orders something not on the menu?