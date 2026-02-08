# ══════════════════════════════════════════════════════════════════
# EXERCISE B: DAILY SALES DASHBOARD
# Client: "ShelfSmart Retail"
#
# Background:
# ShelfSmart Retail is a small electronics store near campus.
# Staff log every product sold into a flat list throughout the day.
# The store also maintains a price dictionary for their range.
#
# Management wants a dashboard tool that can answer:
#   - How many of each product sold today?
#   - Which product was the best seller?
#   - What is the revenue breakdown per product?
#   - Process end-of-day tasks (customer returns, merging online)
#   - Print a clean daily summary
#
# Build the functions below to power the dashboard.
# ══════════════════════════════════════════════════════════════════

# Today's in-store transactions (each entry = one unit sold)
transactions = [
    "USB Cable", "Wireless Mouse", "USB Cable", "Keyboard",
    "Monitor Stand", "Wireless Mouse", "USB Cable", "Keyboard",
    "Wireless Mouse", "USB Cable", "Headphones", "Keyboard",
    "Wireless Mouse", "Headphones", "USB Cable"
]

# Product price list
prices = {
    "USB Cable": 8.99,
    "Wireless Mouse": 24.99,
    "Keyboard": 49.99,
    "Monitor Stand": 89.99,
    "Headphones": 34.99,
    "Webcam": 59.99
}

# Online sales tracked separately (already counted)
online_sales = {
    "Wireless Mouse": 6,
    "Webcam": 3,
    "USB Cable": 2,
    "Desk Lamp": 4
}


# TASK 1: count_sales(transaction_list)
# Takes a list of product names (one per sale).
# Returns a dictionary: product name → number sold.
# Use get() for counting.
#
# Expected: {"USB Cable": 5, "Wireless Mouse": 4, "Keyboard": 3,
#            "Monitor Stand": 1, "Headphones": 2}

def count_sales(transaction_list):
    in_store_sales = {}
    for sale in transaction_list:
        in_store_sales[sale] = in_store_sales.get(sale, 0) + 1
    return in_store_sales

# TASK 2: best_seller(sales_counts)
# Takes a sales count dictionary (like Task 1's output).
# Returns a tuple: (product_name, count) for the top seller.
# Loop through .items() and track the highest.
#
# Expected: ("USB Cable", 5)

def best_seller(sales_counts):
    top_seller = None
    top_count = 0
    for item, count in sales_counts.items():
        if count > top_count:
            top_seller = item
            top_count = count
    return top_seller, top_count
        

# TASK 3: calculate_revenue(sales_counts, price_dict)
# Takes sales counts and the price dictionary.
# Returns a NEW dictionary: product → total revenue (count × price).
# If a product has no price listed, use 0.00.
#
# Expected: {"USB Cable": 44.95, "Wireless Mouse": 99.96, ...}

def calculate_revenue(sales_counts, price_dict):
    total_revenue = {}
    for item, count in sales_counts.items():
        total_revenue[sale] = total_revenue(item, )


# TASK 4: process_return(sales_counts, product_name)
# A customer returned one unit of a product.
# Decrease its count by 1.
# If the count hits 0, remove it from the dictionary using pop().
# If the product isn't in the dict at all, print a message.

def process_return(sales_counts, product_name):
    pass


# TASK 5: merge_online(in_store_counts, online_counts)
# Merge online sales INTO the in-store counts by ADDING values
# together (not overwriting).
# Use first so you don't modify the original in-store dict.
# Return the combined dictionary.

def merge_online(in_store_counts, online_counts):
    pass


# TASK 6: print_dashboard(sales_counts, price_dict)
# Prints a formatted daily report showing:
#   - Each product, quantity sold, and revenue
#   - Totals at the bottom (units + revenue)
#   - The best-selling product
# Use f-strings for alignment.

def print_dashboard(sales_counts, price_dict):
    pass


# ── Run the dashboard ────────────────────────────────────────────
print("=" * 50)
print("  SHELFSMART RETAIL — DAILY SALES DASHBOARD")
print("=" * 50)

# Step 1: Count in-store sales
in_store = count_sales(transactions)
print("\nIn-store sales:", in_store)

# Step 2: Best seller
top = best_seller(in_store)
print(f"Best seller: {top[0]} ({top[1]} units)")

# Step 3: Revenue breakdown
rev = calculate_revenue(in_store, prices)
print("Revenue:", rev)

# Step 4: Process returns
print("\n--- Processing Returns ---")
process_return(in_store, "Monitor Stand")   # count → 0 → removed
process_return(in_store, "Webcam")          # not in sales
print("After returns:", in_store)

# Step 5: Merge online
print("\n--- Merging Online Sales ---")
combined = merge_online(in_store, online_sales)
print("Combined sales:", combined)

# Step 6: Full dashboard
print("\n--- Daily Dashboard (Combined) ---")
print_dashboard(combined, prices)


# REFLECTION:
# 1. "Desk Lamp" appears in online_sales but NOT in the prices dict.
#    What happens to its revenue? How does get() handle this?
# 2. Why did we use .copy() in merge_online instead of just
#    modifying in_store_counts directly?
# 3. In process_return, why use pop() instead of del?