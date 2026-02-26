# topic5_lecture1_exercise1.py
# Lecture 1 | Exercise 1: Your first multi-file programme
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Time: ~15 minutes
#
# You are given cafe_reports.py, which contains three functions.
# Your job is to complete this file (the "main" file) so that it
# imports those functions and uses them to display a daily summary.
#
# Files in your project folder:
#   cafe_reports.py          <-- provided, do not modify
#   topic5_lecture1_exercise1.py  <-- this file, complete the TODOs
#
# Expected output when you run this file:
#   === Mocha's Café - Daily Summary ===
#   Total sales: €35.70
#   Most popular item: Latte
#   Orders by category - Hot Drinks: 5, Food: 3
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 1: Import calculate_total_sales from cafe_reports
from cafe_reports import calculate_total_sales
# 2: Import get_most_popular_item from cafe_reports
from cafe_reports import get_most_popular_item
# 3: Import count_orders_by_category from cafe_reports
from cafe_reports import count_orders_by_category


# --- Sample data (do not change) ---
SAMPLE_ORDERS = [4.50, 3.20, 5.00, 2.80, 4.50, 6.00, 3.20, 6.50]

SAMPLE_ITEM_COUNTS = {
    "Cappuccino": 45,
    "Americano": 32,
    "Latte": 51,
    "Espresso": 28,
}

SAMPLE_ORDERS_WITH_CATEGORY = [
    {"category": "Hot Drinks", "amount": 4.50},
    {"category": "Hot Drinks", "amount": 3.20},
    {"category": "Food",       "amount": 2.80},
    {"category": "Hot Drinks", "amount": 5.00},
    {"category": "Food",       "amount": 3.20},
    {"category": "Hot Drinks", "amount": 4.50},
    {"category": "Hot Drinks", "amount": 6.00},
    {"category": "Food",       "amount": 6.50},
]
# ------------------------------------


def display_daily_summary():
    """Prints the daily sales summary for Mocha's Café."""

    # TODO 4: Call calculate_total_sales() with SAMPLE_ORDERS and store the result
    total = calculate_total_sales(SAMPLE_ORDERS)

    # TODO 5: Call get_most_popular_item() with SAMPLE_ITEM_COUNTS and store the result
    popular = get_most_popular_item(SAMPLE_ITEM_COUNTS)

    # TODO 6: Call count_orders_by_category() with SAMPLE_ORDERS_WITH_CATEGORY
    category_counts = count_orders_by_category(SAMPLE_ORDERS_WITH_CATEGORY)

    print("=== Mocha's Café - Daily Summary ===")

    # TODO 7: Print total sales formatted to 2 decimal places with a € sign
    # Expected: Total sales: €35.70
    print(f"Total sales: €{total:.2f}")        # fix this line

    # TODO 8: Print the most popular item
    # Expected: Most popular item: Latte
    print(f"Most popular item: {popular}")   # fix this line

    # TODO 9: Print orders by category on one line separated by commas
    # Expected: Orders by category - Hot Drinks: 5, Food: 3
    # Hint: build the string in a loop or use join()
    category_str = ", ".join([f"{category}: {count}" for category, count in category_counts.items()])
    print(f"Orders by category - {category_str}")

# TODO 10: Add the if __name__ == "__main__" guard here
#          and call display_daily_summary() inside it.
#          Why is this guard needed? Discuss with a neighbour.

if __name__ == "__main__":
    display_daily_summary()