# ══════════════════════════════════════════════════════════════════
# EXERCISE B: INVENTORY ACTIVITY TRACKER
# Client: "GreenLeaf Garden Centre"
#
# Background:
# GreenLeaf is a garden centre in Ballincollig that sells plants,
# seeds, tools, and accessories. The manager, Tomás, wants to
# replace their clipboard-based tracking with a digital log.
#
# Your system must:
#   - Log every stock change with a timestamp
#   - Process sales (validate, update stock, and log automatically)
#   - Display recent activity in a formatted table
#
# This mirrors A2's structure directly:
#   log_activity     → A2's log_transaction
#   process_sale     → A2's update_stock (calls log internally)
#   view_recent      → A2's view_transaction_log
# ══════════════════════════════════════════════════════════════════

from datetime import datetime

# Starting inventory
inventory = {
    "P001": {"name": "Tomato Seeds",    "category": "Seeds", "price": 2.50, "quantity": 45},
    "P002": {"name": "Potting Compost", "category": "Soil",  "price": 8.99, "quantity": 30},
    "P003": {"name": "Pruning Shears",  "category": "Tools", "price": 14.50, "quantity": 12},
    "P004": {"name": "Herb Seeds",      "category": "Seeds", "price": 1.99, "quantity": 60},
    "P005": {"name": "Watering Can",    "category": "Tools", "price": 11.00, "quantity": 8},
}

# Transaction log (starts empty)
transactions = []


# TASK 1: log_activity(transactions, activity_type, product_id,
#                      product_name, quantity)
# ──────────────────────────────────────────────────────────────────
# Record a stock change in the activity log.
#
# Requirements:
#   - Build a dict with keys: "type", "product_id", "product_name",
#     "quantity", "timestamp"
#   - timestamp: use datetime.now().isoformat()
#   - Append the dict to the transactions list
#
# This is the SAME pattern as A2's log_transaction().
# ──────────────────────────────────────────────────────────────────

def log_activity(transactions, activity_type, product_id, product_name, quantity):
    activity = {
        "type": activity_type,
        "product_id": product_id,
        "product_name": product_name,
        "quantity": quantity,
        "timestamp": datetime.now().isoformat()
    }
    transactions.append(activity)


# TASK 2: process_sale(inventory, transactions, product_name, qty)
# ──────────────────────────────────────────────────────────────────
# Process a sale: find the product, validate stock, update
# quantity, and log the transaction AUTOMATICALLY.
#
# Requirements:
#   - Search for the product by name (case-insensitive, exact match)
#   - If not found, print error and return False
#   - If insufficient stock, print error and return False
#   - Decrease quantity
#   - Call log_activity with type "sale" and NEGATIVE quantity
#   - Print confirmation with new stock level
#   - Return True on success
#
# This mirrors A2's update_stock() calling log_transaction().
# The KEY pattern: one function does its work AND calls another
# to record what happened.
# ──────────────────────────────────────────────────────────────────

def process_sale(inventory, transactions, product_name, qty):
    product_id = None
    for pid, details in inventory.items():
        if details["name"].lower() == product_name.lower():
            product_id = pid
            break

    if not product_id:
        print(f"Error: Product '{product_name}' not found.")
        return False

    if inventory[product_id]["quantity"] < qty:
        print(f"Error: Insufficient stock for '{product_name}'. Available: {inventory[product_id]['quantity']}")
        return False

    inventory[product_id]["quantity"] -= qty
    log_activity(transactions, "sale", product_id, product_name, -qty)
    print(f"Sale processed: {qty} × {product_name}. New stock: {inventory[product_id]['quantity']}")

    return True


# TASK 3: view_recent_activity(transactions, num_recent=5)
# ──────────────────────────────────────────────────────────────────
# Display the most recent transactions, newest first.
#
# Requirements:
#   - If empty, print "No activity recorded." and return
#   - Use list slicing [-num_recent:] for recent entries
#   - Loop in REVERSE order (newest first)
#   - Parse timestamp: datetime.fromisoformat(trans["timestamp"])
#   - Format for display: ts.strftime("%Y-%m-%d %H:%M:%S")
#   - Format quantity with sign: f"{qty:+d}"
#   - Print header, rows, and "Showing X of Y" footer
#
# This is the SAME pattern as A2's view_transaction_log().
# ──────────────────────────────────────────────────────────────────

def view_recent_activity(transactions, num_recent=5):
    if not transactions:
        print("No activity recorded.")
        return
    recent = transactions[-num_recent:]
    print(f"\n{'Time':<22} {'Type':<10} {'Product':<20} {'Qty':>5}")
    print("=" * 60)
    for trans in reversed(recent):
        ts = datetime.fromisoformat(trans["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
        print(f"{ts:<22} {trans['type']:<10} {trans['product_name']:<20} {trans['quantity']:>5d}")
    print(f"\nShowing {len(recent)} of {len(transactions)} total transactions.")


# ── Run the system ───────────────────────────────────────────────
print("=" * 55)
print("  GREENLEAF GARDEN CENTRE — ACTIVITY TRACKER")
print("=" * 55)

# Process some sales (integration: updates stock + logs automatically)
print("\n--- Processing Sales ---")
process_sale(inventory, transactions, "Tomato Seeds", 10)
process_sale(inventory, transactions, "Pruning Shears", 3)
process_sale(inventory, transactions, "Herb Seeds", 15)
process_sale(inventory, transactions, "Watering Can", 20)    # Should fail: only 8
process_sale(inventory, transactions, "Rose Bush", 5)         # Should fail: not found

# Process a delivery (log_activity called directly)
print("\n--- Processing Delivery ---")
inventory["P002"]["quantity"] += 20
log_activity(transactions, "delivery", "P002", "Potting Compost", 20)
print("Delivered 20 × Potting Compost (stock now: 50)")

# View all activity
print("\n--- Recent Activity ---")
view_recent_activity(transactions)

# View with limit
print("\n--- Last 2 Only ---")
view_recent_activity(transactions, 2)

# Test empty log
print("\n--- Empty Log ---")
view_recent_activity([])


# REFLECTION:
# 1. How does process_sale() calling log_activity() mirror
#    A2's update_stock() calling log_transaction()?
# 2. Why store timestamps as ISO strings rather than formatted
#    strings like "10/02/2026 2:30 PM"?
# 3. A2 also needs generate_category_report() — that uses the
#    grouping pattern from Class 3. Which exercise practised it?