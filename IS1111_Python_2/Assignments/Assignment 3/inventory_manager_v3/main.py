# main.py
# Name: Daniel Marcinkowski
# Student ID: 125701129
# Date: 25/02/2026
# Description: Main menu and programme flow for the inventory management system.

# =============================================================================
# IMPORTS
# =============================================================================
from datetime import datetime

from data_handler import (
    export_inventory_to_csv,
    export_low_stock_to_csv,
    generate_text_report,
    load_inventory,
    load_transactions,
    save_inventory,
    save_transactions,
)
import inventory_operations as inv_ops

# =============================================================================
# ASSIGNMENT 3: Persistent Storage & Modules
# =============================================================================
#
# For complete instructions, project structure, step-by-step guidance, sample
# outputs, JSON/CSV examples, and implementation checklists, see A3_INSTRUCTIONS.txt
#
# Quick Reference:
# ----------------
# Rename this file as main.py
#
# Additional files to create:
#   - data_handler.py (file operations)
#   - inventory_operations.py (business logic)
#
# Provided file:
#   - functions_for_reuse.py (ALL 19 functions to move to the appropriate modules)
#
# Your work:
#   - Copy all 19 functions to the appropriate modules (NO changes needed)
#   - Write 7 new file operation functions in the appropriate module
#
# =============================================================================

# =============================================================================
# YOUR CODE STARTS HERE
# =============================================================================

def display_menu():
    """
    Display the main menu and return the user's validated choice.

    Returns:
        int: The user's menu choice (1-11)
    """
    print("\n=== Murphy's General Store - Inventory System ===")
    print("1. View All Products")
    print("2. Add New Product")
    print("3. Update Stock (Sale/Delivery)")
    print("4. Update Product Details")
    print("5. Remove Product")
    print("6. Search Products")
    print("7. View Low Stock Alerts")
    print("8. View Category Report")
    print("9. View Transaction Log")
    print("10. Export Reports")
    print("11. Save & Exit")

    choice = inv_ops.get_valid_int("\nEnter your choice (1-11): ", min_value=1)

    while choice > 11:
        print("Error: Please enter a number between 1 and 11")
        choice = inv_ops.get_valid_int("Enter your choice (1-11): ", min_value=1)

    return choice


def handle_export_menu(inventory):
    """
    Display export submenu and handle export operations.

    Parameters:
        inventory (dict): The inventory dictionary to export
    """
    print("\n--- Export Reports ---")
    print("1. Export inventory to CSV")
    print("2. Export low stock report to CSV")
    print("3. Generate formatted text report")
    print("4. Export all reports")
    print("5. Cancel")

    choice = inv_ops.get_valid_int("\nEnter your choice (1-5): ", min_value=1)

    while choice < 1 or choice > 5:
        print("Error: Please enter a number between 1 and 5")
        choice = inv_ops.get_valid_int("Enter your choice (1-5): ", min_value=1)

    if choice == 1:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"inventory_{timestamp}.csv"
        export_inventory_to_csv(inventory, filename)
        print(f"\nInventory exported to {filename}")

    elif choice == 2:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"low_stock_{timestamp}.csv"
        export_low_stock_to_csv(inventory, filename)
        print(f"\nLow stock report exported to {filename}")

    elif choice == 3:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"inventory_report_{timestamp}.txt"
        generate_text_report(inventory, filename)
        print(f"\nReport saved to {filename}")

    elif choice == 4:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        export_inventory_to_csv(inventory, f"inventory_{timestamp}.csv")
        export_low_stock_to_csv(inventory, f"low_stock_{timestamp}.csv")
        generate_text_report(inventory, f"inventory_report_{timestamp}.txt")
        print(f"\nInventory exported to inventory_{timestamp}.csv")
        print(f"Low stock report exported to low_stock_{timestamp}.csv")
        print(f"Report saved to inventory_report_{timestamp}.txt")
        print("\nAll reports exported successfully!")

    elif choice == 5:
        print("\nExport cancelled.")


def main():
    """
    Main programme loop with persistent storage.
    """
    print("\nWelcome to Murphy's General Store Inventory System!")

    inventory = load_inventory()
    transactions = load_transactions()

    print(f"Loaded {len(inventory)} products from inventory.json")
    print(f"Loaded {len(transactions)} transactions from transactions.json")

    while True:
        choice = display_menu()

        if choice == 1:
            inv_ops.view_all_products(inventory)

        elif choice == 2:
            inv_ops.add_product(inventory, transactions)

        elif choice == 3:
            inv_ops.update_stock(inventory, transactions)

        elif choice == 4:
            inv_ops.update_product_details(inventory)

        elif choice == 5:
            inv_ops.remove_product(inventory)

        elif choice == 6:
            inv_ops.search_products(inventory)

        elif choice == 7:
            inv_ops.view_low_stock(inventory)

        elif choice == 8:
            inv_ops.generate_category_report(inventory)

        elif choice == 9:
            inv_ops.view_transaction_log(transactions)

        elif choice == 10:
            handle_export_menu(inventory)

        elif choice == 11:
            print("\nSaving data...")
            save_inventory(inventory)
            save_transactions(transactions)
            print("\nThank you for using Murphy's General Store Inventory System!")
            print("Goodbye!")
            break


# Main programme
if __name__ == "__main__":
    main()


# =============================================================================
# REFERENCES & AI STATEMENT
# =============================================================================
# References to any external sources used (following Canvas guidelines):
#
#
# AI Tool Usage:
# I acknowledge the use of GPT-5.3-Codex via GitHub Copilot
# (integrated into Visual Studio Code IDE) to generate inline
# code suggestions during development and to assist with code
# structure, formatting, and function implementations.
# 
# The AI assistant provided suggestions for function
# implementations, code structure, and formatting, which I
# reviewed, adapted, and integrated into my solution.
#
# The AI assistant provided autocomplete suggestions for:
# - Function structure and formatting
# - Dictionary syntax and operations
# - String formatting in f-strings
#
# The AI assistant also helped me review my final code against
# the provided instructions, rubric, and checklists to ensure
# all requirements were met.
# 
#
# =============================================================================

# =============================================================================
# SELF-REFLECTION (2-3 sentences)
# =============================================================================
# Write about the most challenging aspect of this assignment 
# and what you learned from it:
#
# At this stage of the project, the amount of code and number
# of functions to manage can feel overwhelming.
# Dividing the codebase into separate modules has made it
# easier to manage and understand the different components of
# the system.
# I learned how to structure a larger Python project using
# modules and how to handle file operations for persistent
# storage effectively.
#
# =============================================================================
