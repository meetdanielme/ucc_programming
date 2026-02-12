# ══════════════════════════════════════════════════════════════════
# EXERCISE B: DAILY SALES DASHBOARD — SOLUTIONS
# Client: "ShelfSmart Retail"
# ══════════════════════════════════════════════════════════════════

transactions = [
    "USB Cable", "Wireless Mouse", "USB Cable", "Keyboard",
    "Monitor Stand", "Wireless Mouse", "USB Cable", "Keyboard",
    "Wireless Mouse", "USB Cable", "Headphones", "Keyboard",
    "Wireless Mouse", "Headphones", "USB Cable"
]

prices = {
    "USB Cable": 8.99,
    "Wireless Mouse": 24.99,
    "Keyboard": 49.99,
    "Monitor Stand": 89.99,
    "Headphones": 34.99,
    "Webcam": 59.99
}

online_sales = {
    "Wireless Mouse": 6,
    "Webcam": 3,
    "USB Cable": 2,
    "Desk Lamp": 4
}


def count_sales(transaction_list):
    """Counts how many of each product were sold."""
    counts = {}
    for product in transaction_list:
        counts[product] = counts.get(product, 0) + 1
    return counts


def best_seller(sales_counts):
    """Returns (product, count) for the top-selling product."""
    top_product = None
    top_count = 0
    for product, count in sales_counts.items():
        if count > top_count:
            top_count = count
            top_product = product
    return (top_product, top_count)


def calculate_revenue(sales_counts, price_dict):
    """Returns a dict of product → revenue (count × unit price)."""
    revenue = {}
    for product, count in sales_counts.items():
        unit_price = price_dict.get(product, 0.00)
        revenue[product] = count * unit_price
    return revenue
    # return {product: count * price_dict.get(product, 0.00) for product, count in sales_counts.items()}


def process_return(sales_counts, product_name):
    """Decrements count by 1. Removes product if count hits 0."""
    if product_name not in sales_counts:
        print(f"  '{product_name}' not in today's sales — nothing to return.")
        return

    sales_counts[product_name] = sales_counts[product_name] - 1

    if sales_counts[product_name] <= 0:
        sales_counts.pop(product_name)
        print(f"  '{product_name}' returned and removed (count reached 0).")
    else:
        print(f"  '{product_name}' returned. Remaining: {sales_counts[product_name]}")


def merge_online(in_store_counts, online_counts):
    """Merges online counts into in-store by adding (not overwriting)."""
    combined = in_store_counts.copy()
    for product, count in online_counts.items():
        combined[product] = combined.get(product, 0) + count
    return combined


def print_dashboard(sales_counts, price_dict):
    """Prints a formatted daily sales summary."""
    revenue = calculate_revenue(sales_counts, price_dict)
    top = best_seller(sales_counts)

    print(f"\n{'Product':<20} {'Qty':>6} {'Revenue':>12}")
    print("-" * 40)

    for product, count in sales_counts.items():
        rev = revenue[product]
        print(f"{product:<20} {count:>6} {'€' + f'{rev:.2f}':>12}")

    print("-" * 40)
    total_units = sum(sales_counts.values())
    total_rev = sum(revenue.values())
    print(f"{'TOTAL':<20} {total_units:>6} {'€' + f'{total_rev:.2f}':>12}")
    print(f"\nBest seller: {top[0]} ({top[1]} units)")


# ── Run the dashboard ────────────────────────────────────────────
print("=" * 50)
print("  SHELFSMART RETAIL — DAILY SALES DASHBOARD")
print("=" * 50)

in_store = count_sales(transactions)
print("\nIn-store sales:", in_store)

top = best_seller(in_store)
print(f"Best seller: {top[0]} ({top[1]} units)")

rev = calculate_revenue(in_store, prices)
print("Revenue:", rev)

print("\n--- Processing Returns ---")
process_return(in_store, "Monitor Stand")
process_return(in_store, "Webcam")
print("After returns:", in_store)

print("\n--- Merging Online Sales ---")
combined = merge_online(in_store, online_sales)
print("Combined sales:", combined)

print("\n--- Daily Dashboard (Combined) ---")
print_dashboard(combined, prices)