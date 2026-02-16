# class8_dictionaries_live.py
# Class 8: datetime, Transaction Logging, Integration & Comprehension Preview
# (Dict class 4 of 4 — final dictionary class)

print("\nCLASS 8: DATETIME, TRANSACTIONS & INTEGRATION\n")

# ══════════════════════════════════════════════════════════════
# SECTION 1: THE DATETIME MODULE
# ══════════════════════════════════════════════════════════════
# A2 requires timestamps on every transaction.
# Python's datetime module gives us the current date/time
# and tools to convert and format it.


# Import — goes at the TOP of your file
# "from datetime import datetime" gives us the datetime CLASS
# from the datetime MODULE (yes, same name — confusing but standard).

# import datetime
# ts = datetime.datetime.now().isoformat()

from datetime import datetime

# ── Getting the current date and time ─────────────────────────
now = datetime.now()
print("datetime.now():", now)
print("Type:", type(now))
# A datetime object — not a string, not a number.

# It has attributes (don't need to know):
print(f"  Year: {now.year}, Month: {now.month}, Day: {now.day}")
print(f"  Hour: {now.hour}, Minute: {now.minute}, Second: {now.second}")
print()

# ── isoformat(): datetime → string for STORAGE ───────────────
# Datetime objects can't be saved to files or JSON directly.
# .isoformat() converts to a standard string: "2026-02-12T14:30:00.123456"
# ISO 8601 is an international standard — works everywhere.
iso_str = now.isoformat()
print("isoformat():", iso_str)
print("Type:", type(iso_str))       # str — can be stored in a dict, file, JSON
print()

# ── fromisoformat(): string → datetime for PARSING ───────────
# When you LOAD data, timestamps come back as strings.
# fromisoformat() converts back to a datetime object.
restored = datetime.fromisoformat(iso_str)
print("fromisoformat():", restored)
print("Type:", type(restored))      # datetime again
print()

# ── strftime(): datetime → string for DISPLAY ────────────────
# strftime = "string format time"
# Use format codes to control exactly how the date looks:
#   %Y = 4-digit year    %m = 2-digit month    %d = 2-digit day
#   %H = 24-hour hour    %M = minute            %S = second
print("strftime examples:")
print(f"  '%Y-%m-%d %H:%M:%S' → {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"  '%d/%m/%Y'          → {now.strftime('%d/%m/%Y')}")
print(f"  '%H:%M'             → {now.strftime('%H:%M')}")
print()

# ── Why two methods that both produce strings? ────────────────
# isoformat() → for STORAGE  (precise, sortable, machine-readable) 
# "2026-02-15T14:30:00.123456" always means the same thing (unlike "15/02/26 2:30").

# strftime()  → for DISPLAY  (human-friendly, customisable format)
#
# isoformat() always gives the same format. No choices.
# strftime() lets you pick the format. Great for reports.

# Don't need to know but ISO lets us sort where as str formatting doesnt:
# sorted_trans = sorted(transactions, key=lambda t: t["timestamp"])
# All we need for CA (last 10):
# recent = transactions[-10:]

# ── The full round-trip (CA) ───────
#   1. SAVE:    datetime.now().isoformat()     → string → store in dict
#   2. LOAD:    datetime.fromisoformat(s)      → datetime → work with it
#   3. DISPLAY: dt.strftime(fmt)               → string → show to user
stored = datetime.now().isoformat()                          # Step 1
print("Stored:", stored)
parsed = datetime.fromisoformat(stored)                      # Step 2
display = parsed.strftime("%Y-%m-%d %H:%M:%S")               # Step 3
print("Display:", display)
print()

# Why do we need Step 2? Because: the timestamp is stored in each transaction dict as a string (because you saved it with .isoformat()).
# We must: convert string → datetime object, then format it for display
# For our purposes Step 2 is not needed:
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# later: just print timestamp

# ══════════════════════════════════════════════════════════════
# SECTION 2: TRANSACTION LOGGING PATTERN
# ══════════════════════════════════════════════════════════════
# Business systems need an audit trail: WHAT happened, WHEN,
# and to WHAT. We store each event as a dict in a list.
# transactions = [ {transaction1}, {transaction2}, {transaction3}, ... ]
# You could use a dict of dicts, but you’d have to answer: what is the key for each transaction?


# ── What a single transaction looks like ──────────────────────
example = {
    "type": "sale",
    "product_id": "P001",
    "product_name": "Milk",
    "quantity": -5,                         # negative = stock decreased
    "timestamp": datetime.now().isoformat()
}

print("Single transaction:")
for key, val in example.items():
    print(f"  {key}: {val}")
print()

# Convention for quantity:
#   sale     → negative  (stock goes DOWN)
#   delivery → positive  (stock goes UP)
#   added    → positive  (new product created)

# ── The log_transaction function ──────────────────────────────
# Builds the dict and appends it. Simple but important.
# This is called by OTHER functions (add_product, update_stock).

def log_transaction(transactions, trans_type, product_id, product_name, quantity):
    """Record a stock change in the transaction log."""
    transaction = {
        "type": trans_type,
        "product_id": product_id,
        "product_name": product_name,
        "quantity": quantity,
        "timestamp": datetime.now().isoformat()
    }
    transactions.append(transaction)

# Simulate some activity
transactions = []
log_transaction(transactions, "added",    "P001", "Milk",  20)
log_transaction(transactions, "added",    "P002", "Bread", 15)
log_transaction(transactions, "sale",     "P001", "Milk",  -5)
log_transaction(transactions, "delivery", "P002", "Bread", 10)
log_transaction(transactions, "sale",     "P001", "Milk",  -3)

print(f"Logged: {len(transactions)} transactions")
print("First:", transactions[0])
print("Last: ", transactions[-1])
print()

# Last 3


# ══════════════════════════════════════════════════════════════
# SECTION 3: VIEWING THE TRANSACTION LOG
# ══════════════════════════════════════════════════════════════
# Users want a formatted table showing recent events, newest first.


# ── Signed quantity formatting: :+d (CA) ───────────────────────────
# :+d always shows the sign: positive gets +, negative gets -
print("Signed formatting (:+d):")
for val in [20, -5, 10, -3]:
    print(f"  {val:>4} → {val:+d}")
print()

# ── List slicing for recent items ─────────────────────────────
# [-3:] gets the last 3 elements of any list
print("Last 3 transactions:")
for t in transactions[-3:]:
    print(f"  {t['type']}: {t['product_name']}")
print()

# ── reversed(): iterate newest-first ─────────────────────────
# reversed() gives items in reverse WITHOUT modifying the list
# Different from .reverse() which modifies in place and returns None  | Why not use sorted?
print("Last 3, newest first:")

for t in reversed(transactions[-3:]):
    print(f"  {t['type']}: {t['product_name']}")
print()

#  Also possible but more complex!
# transactions = ["t0", "t1", "t2", "t3", "t4"]
# print(transactions[0:3])          # ["t2", "t3", "t4"]  (last 3)
# print(transactions[:-4:-1])# "t4", "t3", "t2"    (newest first)

# Dont confuse with:
# sorted(...) - sort items (alphabetical / numeric / custom key) outof place
# sort a list - inplace

# ── The view_transaction_log function ─────────────────────────
def view_transaction_log(transactions, num_recent=10):
    """Display recent transactions, newest first."""
    print(f"\n--- Transaction Log (Last {num_recent}) ---")

    if not transactions:
        print("No transactions recorded yet.")
        return

    recent = transactions[-num_recent:]

    print(f"{'Timestamp':<22} {'Type':<12} {'Product':<15} {'Qty':>6}")
    print("=" * 57)

    for trans in reversed(recent):
        ts = datetime.fromisoformat(trans["timestamp"])
        time_str = ts.strftime("%Y-%m-%d %H:%M:%S")
        qty_str = f"{trans['quantity']:+d}"
        print(f"{time_str:<22} {trans['type'].capitalize():<12} "
              f"{trans['product_name']:<15} {qty_str:>6}")

    print("=" * 57)
    print(f"Showing {len(recent)} of {len(transactions)} transaction(s)")

view_transaction_log(transactions)
print()
view_transaction_log(transactions, 2)
print()
view_transaction_log([])
print()


# ══════════════════════════════════════════════════════════════
# SECTION 4: INTEGRATION — HOW IT ALL CONNECTS
# ══════════════════════════════════════════════════════════════
# log_transaction doesn't have to be called on its own — it can be called
# INSIDE add_product() and update_stock(). Here's that pattern.

grades = {}
grade_log = []

def generate_student_id(grades_dict):
    """Generate next ID (S001, S002, etc.)."""
    if not grades_dict:
        return "S001"
    max_num = 0
    for sid in grades_dict:
        num = int(sid[1:])
        if num > max_num:
            max_num = num
    return f"S{max_num + 1:03d}"

def log_grade_event(log, event_type, student_id, name, detail):
    """Record a grade event with timestamp."""
    log.append({
        "type": event_type, "student_id": student_id,
        "student_name": name, "detail": detail,
        "timestamp": datetime.now().isoformat()
    })

# KEY PATTERN: add_student calls generate_id AND log_grade_event
# add_product() calls generate_product_id() AND log_transaction()
def add_student(grades_dict, log, name, programme, grade):
    """Add a student AND log the addition."""
    sid = generate_student_id(grades_dict)
    grades_dict[sid] = {"name": name, "programme": programme, "grade": grade}
    log_grade_event(log, "added", sid, name, f"Grade: {grade}")
    print(f"  Added {sid}: {name} ({programme}) — {grade}")
    return sid

# KEY PATTERN: update_grade calls log_grade_event
# update_stock() calls log_transaction()
def update_grade(grades_dict, log, student_id, new_grade):
    """Update a grade AND log the change."""
    if student_id not in grades_dict:
        print(f"  Student {student_id} not found.")
        return False
    student = grades_dict[student_id]
    old = student["grade"]
    student["grade"] = new_grade
    change = new_grade - old
    log_grade_event(log, "updated", student_id, student["name"],
                    f"{old} → {new_grade} ({change:+d})")
    print(f"  Updated {student['name']}: {old} → {new_grade} ({change:+d})")
    return True

# Simulate — both add and update automatically log events
print("Adding students:")
add_student(grades, grade_log, "Siobhan", "BIS", 72)
add_student(grades, grade_log, "Cian", "CS", 65)
add_student(grades, grade_log, "Aoife", "BIS", 88)
print()

print("Updating grades:")
update_grade(grades, grade_log, "S001", 78)
update_grade(grades, grade_log, "S002", 70)
print()

# View the log — ALL events captured automatically
print(f"{'Timestamp':<22} {'Type':<10} {'Name':<10} {'Detail'}")
print("=" * 58)
for entry in reversed(grade_log):
    ts = datetime.fromisoformat(entry["timestamp"])
    print(f"{ts.strftime('%Y-%m-%d %H:%M:%S'):<22} "
          f"{entry['type'].capitalize():<10} "
          f"{entry['student_name']:<10} {entry['detail']}")
print()

# A2 connection: the same pattern exactly.
#   add_product()  → calls generate_product_id() + log_transaction()
#   update_stock() → calls log_transaction()
#   Your log_transaction() just builds the dict and appends.
#   Your view_transaction_log() reads the list and displays it.


# ══════════════════════════════════════════════════════════════
# SECTION 5: DICT COMPREHENSION (overview)
# ══════════════════════════════════════════════════════════════
# Possible in a few places in CA but certainly not required 
#
prices = {"Milk": 1.50, "Bread": 0.85, "Tea": 3.20}

# Loop way (what you know):
increased = {}
for item, price in prices.items():
    increased[item] = round(price * 1.10, 2)
print("Loop (10% increase):", increased)

# Comprehension (same thing, one line):
# Pattern: {new_key: new_value for key, value in dict.items()}
increased = {item: round(price * 1.10, 2) for item, price in prices.items()}
print("Comprehension:      ", increased)

# With a filter:
expensive = {item: price for item, price in prices.items() if price > 1.00}
print("Filtered (>€1.00): ", expensive)

# Extract names from nested dicts:
name_lookup = {sid: stu["name"] for sid, stu in grades.items()}
print("Name lookup:        ", name_lookup)
print()

# When to use:
#   ✓ Independent calculation per item (price × 1.10)
#   ✓ Filtering (keep items matching a condition)
#   ✓ Extracting fields from nested dicts
#   ✗ Counting/accumulating (need get() loop)
#   ✗ Grouping (need if-not-in + accumulate pattern)



#  Another example wiht nested Dict

inventory = {
    "P001": {"name": "Milk",  "price": 1.50, "quantity": 20},
    "P002": {"name": "Bread", "price": 0.85, "quantity": 15},
    "P003": {"name": "Tea",   "price": 3.20, "quantity": 30},
}

# Loop version (what you already know):
product_values_loop = {}
for pid, prod in inventory.items():
    product_values_loop[pid] = prod["price"] * prod["quantity"]

print("Loop product values:", product_values_loop)

# Comprehension version (one-liner):
# Pattern: {new_key: new_value for key, value in dict.items()}
product_values = {pid: prod["price"] * prod["quantity"] for pid, prod in inventory.items()}

print("Comprehension product values:", product_values)

# Filter version (only include products worth over €30):
# Pattern: {k: v for k, v in dict.items() if condition}
high_value = {pid: (prod["price"] * prod["quantity"])
              for pid, prod in inventory.items()
              if (prod["price"] * prod["quantity"]) > 30}

print("High-value products (>€30):", high_value)

# TODAY'S SUMMARY

# DATETIME
#   datetime.now().isoformat()        → string (store in dict/file)
#   datetime.fromisoformat(s)         → datetime (parse it back)
#   dt.strftime("%Y-%m-%d %H:%M:%S") → string (display to user)
#
# TRANSACTION LOGGING
#   Build a dict (type, id, name, quantity, timestamp)
#   Append to a list — negative qty = sale, positive = delivery
#   Functions that change data call the log function automatically
#   (combines nested dicts, ID generation, and get() from earlier)
#
# VIEWING LOGS
#   list[-n:]      last N items
#   reversed()     newest first
#   f"{val:+d}"    show +/- sign
#
# DICT COMPREHENSION (preview)
#   {k: v for k, v in dict.items()}
#   Good for transforms/filters — not for counting or grouping
# ══════════════════════════════════════════════════════════════