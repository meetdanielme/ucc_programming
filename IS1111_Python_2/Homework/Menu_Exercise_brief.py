# Programming Exercise: Food and Drink Menu Display

# Objective:
# This exercise is designed to review basic concepts such as functions, iterations, string slicing, output formatting, and lists.

# Task:
# Write a Python program that allows a restaurant to display their food and drink menus 
# using the same function. The menus should include items with their respective prices, and the program 
# should allow the user to view the menu with neatly formatted output.
# Steps:
# 1. Define a function with two parameters: a list of items and a title (string).
# 2. Each item in `menu_list` is a string formatted as 'item_name - price'.
# 3. The function should iterate over the list and display each item with proper formatting.
# 4. Implement string slicing to display only the first 20 characters of the item name, 
#    followed by its price in a formatted manner.
# 5. Test the function by displaying a food menu and a drink menu using two different lists.
# 6. Ensure proper spacing and alignment in the output for readability.

# Example Output:
# ----------- Food Menu -----------
# 1. Cheeseburger          €5.99
# 2. Grilled Chicken       €7.49
# 3. Caesar Salad          €4.99
# ----------- Drink Menu -----------
# 1. Iced Coffee           €2.99
# 2. Lemonade              €1.99
# 3. Orange Juice          €3.49

# TYPE YOUR CODE BELOW THIS LINE


def display_menu(menu_list, title="Menu"):
    print(f"----------- {title} -----------")
    for index, item in enumerate(menu_list, start=1):
        name, price = item.split(" - ")
        name = name[:20]  # Limit item name to first 20 characters
        print(f"{index}. {name:<20} €{price}")
    print()  # Add a blank line after the menu for better readability

# Main program
# Define the food menu and drink menu
food_menu = [
    "Cheeseburger - 5.99",
    "Grilled Chicken Sandwich - 7.49",
    "Caesar Salad - 4.99",
    "Veggie Wrap - 6.29"
]

drink_menu = [
    "Iced Coffee - 2.99",
    "Lemonade - 1.99",
    "Orange Juice - 3.49",
    "Herbal Tea - 2.79"
]

# Display the menus
# Call the function twice
display_menu(food_menu, "Food Menu")
display_menu(drink_menu, "Drink Menu")