# data_handler.py
# Name: Daniel Marcinkowski
# Student ID: 125701129
# Date: 25/02/2026
# Description: File operation functions for loading, saving, and exporting inventory data.

import csv
import json
from datetime import datetime


def load_inventory(filename="inventory.json"):
    """
    Load inventory data from a JSON file.

    Parameters:
        filename (str): Name of the inventory JSON file

    Returns:
        dict: Inventory dictionary, or empty dict if file not found/invalid
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, dict):
                return data
            print(f"Error: {filename} has invalid format. Starting with empty inventory.")
            return {}
    except FileNotFoundError:
        print(f"Note: {filename} not found. Starting with empty inventory.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: {filename} is corrupted. Starting with empty inventory.")
        return {}
    except IOError as error:
        print(f"Error reading {filename}: {error}")
        return {}


def save_inventory(inventory, filename="inventory.json"):
    """
    Save inventory data to a JSON file.

    Parameters:
        inventory (dict): The inventory dictionary
        filename (str): Name of the inventory JSON file
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(inventory, file, indent=2)
        print(f"Inventory saved to {filename}")
    except IOError as error:
        print(f"Error saving inventory to {filename}: {error}")


def load_transactions(filename="transactions.json"):
    """
    Load transaction history from a JSON file.

    Parameters:
        filename (str): Name of the transactions JSON file

    Returns:
        list: Transaction list, or empty list if file not found/invalid
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            print(f"Error: {filename} has invalid format. Starting with empty transaction log.")
            return []
    except FileNotFoundError:
        print(f"Note: {filename} not found. Starting with empty transaction log.")
        return []
    except json.JSONDecodeError:
        print(f"Error: {filename} is corrupted. Starting with empty transaction log.")
        return []
    except IOError as error:
        print(f"Error reading {filename}: {error}")
        return []


def save_transactions(transactions, filename="transactions.json"):
    """
    Save transaction history to a JSON file.

    Parameters:
        transactions (list): The transaction list
        filename (str): Name of the transactions JSON file
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(transactions, file, indent=2)
        print(f"Transactions saved to {filename}")
    except IOError as error:
        print(f"Error saving transactions to {filename}: {error}")


def export_inventory_to_csv(inventory, filename="inventory_export.csv"):
    """
    Export all inventory items to a CSV file.

    Parameters:
        inventory (dict): The inventory dictionary
        filename (str): Name of the CSV output file
    """
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Product ID", "Name", "Category", "Price", "Quantity", "Min Stock"])

            for product_id, product in inventory.items():
                writer.writerow([
                    product_id,
                    product["name"],
                    product["category"],
                    f"{product['price']:.2f}",
                    product["quantity"],
                    product["min_stock"]
                ])
    except IOError as error:
        print(f"Error exporting inventory to {filename}: {error}")


def export_low_stock_to_csv(inventory, filename="low_stock_report.csv"):
    """
    Export low-stock products to a CSV file.

    Parameters:
        inventory (dict): The inventory dictionary
        filename (str): Name of the CSV output file
    """
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Product ID", "Name", "Category", "Current Stock", "Min Stock", "Reorder Qty"])

            for product_id, product in inventory.items():
                if product["quantity"] <= product["min_stock"]:
                    reorder_qty = product["min_stock"] - product["quantity"] + product["min_stock"]
                    writer.writerow([
                        product_id,
                        product["name"],
                        product["category"],
                        product["quantity"],
                        product["min_stock"],
                        reorder_qty
                    ])
    except IOError as error:
        print(f"Error exporting low stock report to {filename}: {error}")


def generate_text_report(inventory, filename="inventory_report.txt"):
    """
    Generate a formatted text report summarising inventory information.

    Parameters:
        inventory (dict): The inventory dictionary
        filename (str): Name of the text report output file
    """
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    total_value = 0.0
    low_stock_count = 0

    for product in inventory.values():
        total_value += product["price"] * product["quantity"]
        if product["quantity"] <= product["min_stock"]:
            low_stock_count += 1

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("============================================================\n")
            file.write("      MURPHY'S GENERAL STORE - INVENTORY REPORT\n")
            file.write(f"      Generated: {now_str}\n")
            file.write("============================================================\n\n")

            file.write(f"{'ID':<6} {'Product':<15} {'Category':<12} {'Price':<8} {'Stock':<8} {'Min':<6}\n")
            file.write("============================================================\n")

            for product_id, product in inventory.items():
                file.write(
                    f"{product_id:<6} {product['name']:<15} {product['category']:<12} "
                    f"€{product['price']:<7.2f} {product['quantity']:<8} {product['min_stock']:<6}\n"
                )

            file.write("============================================================\n")
            file.write(f"Total Products: {len(inventory)}\n")
            file.write(f"Total Value: €{total_value:.2f}\n")
            file.write(f"Low Stock Items: {low_stock_count}\n")
            file.write("============================================================\n")
    except IOError as error:
        print(f"Error generating text report {filename}: {error}")
