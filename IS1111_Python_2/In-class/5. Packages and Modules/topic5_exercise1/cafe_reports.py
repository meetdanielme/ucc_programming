# cafe_reports.py
# PROVIDED FILE - do not modify
# Mocha's Café - Reporting functions

def calculate_total_sales(orders):
    """Returns the total sales amount from a list of order amounts (floats)."""
    total = 0.0
    for amount in orders:
        total += amount
    return total


def get_most_popular_item(item_counts):
    """
    Returns the name of the item with the highest order count.

    Parameters:
        item_counts (dict): item name -> number of orders (int)

    Returns:
        str: name of the most popular item
    """
    best_item = None
    best_count = 0
    for item, count in item_counts.items():
        if count > best_count:
            best_count = count
            best_item = item
    return best_item


def count_orders_by_category(orders_with_category):
    """
    Counts how many orders belong to each category.

    Parameters:
        orders_with_category (list of dict): each dict has keys "category" and "amount"

    Returns:
        dict: category name -> number of orders
    """
    counts = {}
    for order in orders_with_category:
        category = order["category"]
        counts[category] = counts.get(category, 0) + 1
    return counts
