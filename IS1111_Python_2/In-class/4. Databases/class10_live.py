# class10_databases_live.py
# Class 10: Databases — Flat-File (CSV) vs Document (JSON)

import json
import csv

print("\nCLASS 10: DATABASES\n")


# ══════════════════════════════════════════════════════════════
# SECTION 1: WHAT IS A DATABASE?
# ══════════════════════════════════════════════════════════════
# Last class: HOW to read/write files (open, with, json, csv)
# This class: WHY we structure data — and what a database is.
#
# A DATABASE is an organised collection of structured data.
# A file is just bytes on disk — it becomes a database when
# we impose structure and perform organised operations on it.
#
# Three types you need to know:
#   FLAT-FILE  → CSV: single table, rows & columns, plain text
#   DOCUMENT   → JSON: nested structures, flexible, key-based
#   RELATIONAL → SQL: multiple related tables, primary keys
#                     (conceptual only — not coding SQL here)
#
# ALL databases support four basic operations — CRUD:
#   Create → add new records
#   Read   → retrieve / search records
#   Update → modify existing records
#   Delete → remove records

print("=" * 55)
print("SECTION 1: DATABASE CONCEPTS & CRUD")
print("=" * 55)

# CRUD is just a name for what you've already been doing:
#   Create → add_product()     
#   Read   → view_all_products() 
#   Update → update_stock()     
#   Delete → remove_product()   
print("CRUD = Create, Read, Update, Delete")
print()

# A flat table (like a spreadsheet or CSV):
#   ID     Name      Category   Price
#   M001   Latte     Coffee     3.80
#   M002   Scone     Pastry     2.50
#
# Each ROW = one record (all info about one item)
# Each COLUMN = one field (same type of info across all items)

# Relational databases have MULTIPLE tables linked by keys:
#   Products:              Orders:
#   ID    Name    Price    OrderID  ProductID  Qty
#   P001  Milk    1.50     O001     P001       5
#   P002  Bread   0.85     O002     P002       3
#
# ProductID in Orders REFERENCES the Products table — that's
# the "relational" part. We won't write SQL — just know the idea.
print()


# ══════════════════════════════════════════════════════════════
# SECTION 2: CSV AS A FLAT-FILE DATABASE
# ══════════════════════════════════════════════════════════════
# CSV = one table. Rows = records. Columns = fields.
# Simple, opens in Excel, but painful for updates.

print("=" * 55)
print("SECTION 2: CSV — FLAT-FILE DATABASE")
print("=" * 55)

# ── CREATE: write initial records ─────────────────────────────
menu_data = [
    ["M001", "Latte",     "Coffee", "3.80"],
    ["M002", "Scone",     "Pastry", "2.50"],
    ["M003", "Americano", "Coffee", "3.00"],
]

with open("cafe_menu.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name", "Category", "Price"])  # header
    writer.writerows(menu_data)
print("CREATE: Wrote 3 records to cafe_menu.csv")

# ── READ: load all records ────────────────────────────────────
print("\nREAD: All records:")
with open("cafe_menu.csv", "r") as f:
    reader = csv.reader()
    header = next(reader)     # next() reads one row — skips header
    print(f"  Columns: {header}")
    for row in reader:
        print(f"  {row}")

# Remember: everything from csv.reader comes back as STRINGS
print()

# ── UPDATE: change Scone price to 2.80 ───────────────────────
# This is where flat-files get PAINFUL:
#   1. Read ALL rows into memory
#   2. Find and modify the target row
#   3. Rewrite the ENTIRE file
# There's no way to edit "just row 2" in a CSV.

print("UPDATE: Change Scone price:")
rows = []
with open("cafe_menu.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 1 and row[1] == "Scone":
            row[3] = "2.80"
            print(f"  Found and updated: {row}")
        rows.append(row)

# Must rewrite the ENTIRE file just to change one value
with open("cafe_menu.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
print("  Rewrote entire file for ONE change")

# DELETE follows the same pattern: read all, skip the unwanted
# row, rewrite everything. Same cost. That's the key limitation
# of flat-file databases — every change touches the whole file.
# ── DELETE: remove Americano ──────────────────────────────────
print("DELETE: Remove Americano:")
kept_rows = []

with open("cafe_menu.csv", "r", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        # Keep header row (row[1] doesn't exist for header? it does, but it's "Name")
        if len(row) > 1 and row[1] == "Americano":
            print(f"  Skipping (deleted): {row}")
            continue
        kept_rows.append(row)

with open("cafe_menu.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(kept_rows)

print("  Rewrote entire file to delete ONE record")

# Verify final file contents
print("\nCSV after DELETE:")
with open("cafe_menu.csv", "r", newline="") as f:
    for line in f:
        print(" ", line.rstrip())
print()


# ══════════════════════════════════════════════════════════════
# SECTION 3: JSON AS A DOCUMENT DATABASE
# ══════════════════════════════════════════════════════════════
# JSON stores data as nested dicts. CRUD = normal dict operations
# plus a save at the end. MUCH more natural for updates/deletes.

print("=" * 55)
print("SECTION 3: JSON — DOCUMENT DATABASE")
print("=" * 55)

# ── CREATE: build dict and save ───────────────────────────────
menu = {
    "M001": {"name": "Latte",     "category": "Coffee", "price": 3.80},
    "M002": {"name": "Scone",     "category": "Pastry", "price": 2.50},
    "M003": {"name": "Americano", "category": "Coffee", "price": 3.00},
}

with open("cafe_menu.json", "w") as f:
    json.dump(menu, f, indent=2)
print("CREATE: Saved 3 records to cafe_menu.json")

# ── READ: load and access ────────────────────────────────────
with open("cafe_menu.json", "r") as f:
    loaded = json.load(f)

print("\nREAD: All records:")
for mid, item in loaded.items():
    print(f"  {mid}: {item['name']} ({item['category']}) — €{item['price']:.2f}")

# Direct lookup by key — no loop needed!
print(f"\n  Direct lookup M002: {loaded['M002']['name']}")
print()

# ── UPDATE: change Scone price ────────────────────────────────
# With JSON: modify the dict, then save. Two steps.
print("UPDATE: Change Scone price:")
loaded["M002"]["price"] = 2.80
with open("cafe_menu.json", "w") as f:
    json.dump(loaded, f, indent=2)
print(f"  Updated and saved: {loaded['M002']}")
# Compare: CSV update needed ~10 lines. JSON needed 2.
print()

# ── DELETE: remove Americano ─────────────────────────────────
print("DELETE: Remove Americano:")
del loaded["M003"]
with open("cafe_menu.json", "w") as f:
    json.dump(loaded, f, indent=2)
print(f"  Deleted and saved. Remaining: {len(loaded)} records")
print()

# ── CREATE (add new): add Espresso ────────────────────────────
print("CREATE (add): Add Espresso:")
loaded["M004"] = {"name": "Espresso", "category": "Coffee", "price": 2.50}
with open("cafe_menu.json", "w") as f:
    json.dump(loaded, f, indent=2)
print(f"  Added and saved: {loaded['M004']}")
print()


# ══════════════════════════════════════════════════════════════
# SECTION 4: CSV vs JSON — WHEN TO USE WHICH
# ══════════════════════════════════════════════════════════════

print("=" * 55)
print("SECTION 5: CSV vs JSON — SUMMARY")
print("=" * 55)

# CSV (flat-file):                JSON (document):
#   + Opens in Excel                + Preserves  types
#   + Simple, universal             + Supports nested data
#   + Good for exports/sharing      + Direct key lookup
#   - Update/Delete = rewrite all   + CRUD = dict operations
#   - All values are strings        - Not easy in Excel
#   - No nesting                    - Whole file in memory

print("You'll use BOTH — and that's the real-world pattern:")
print("  JSON → primary storage (load at startup, save on exit)")
print("  CSV  → exports for management (open in Excel)")
print("  Store in JSON, export to CSV. Best of both worlds.")
print()

# CA mapping:
#   inventory.json  → load_inventory(), save_inventory()
#   transactions.json → load_transactions(), save_transactions()
#   inventory.csv   → export_inventory_to_csv()
#   low_stock.csv   → export_low_stock_to_csv()

# ══════════════════════════════════════════════════════════════
# FILES & DATABASES SUMMARY
# ══════════════════════════════════════════════════════════════
#
# ── FILE BASICS (Class 9) ─────────────────────────────────────
#
# OPENING FILES:
#   with open(filename, mode) as f:    Auto-closes file (preferred)
#   f = open(filename, mode)           Manual — must call f.close()
#
# MODES:
#   "r"   Read (default) — file must exist
#   "w"   Write — creates file, OVERWRITES if exists ⚠️
#   "a"   Append — adds to end, keeps existing content
#
# READING TEXT FILES:
#   for line in f:           Line by line (most common)
#   f.read()                 Entire file as one string
#   f.readlines()            List of all lines
#   f.readline()             One line at a time
#   line.rstrip()            Remove trailing \n
#
# WRITING TEXT FILES:
#   f.write(string)          Write one string — no auto \n
#   f.writelines(list)       Write list of strings — no auto \n
#
# ERROR HANDLING:
#   try:
#       with open(filename) as f:
#           data = f.read()
#   except FileNotFoundError:
#       data = ""            # Start empty if file missing
#
# ── DATABASE CONCEPTS (Class 10) ──────────────────────────────
#
# DATABASE TYPES:
#   Flat-file (CSV)    Single table, rows & columns, plain text
#   Document (JSON)    Nested structures, flexible, key-based
#   Relational (SQL)   Multiple related tables, primary keys
#
# CRUD OPERATIONS:
#   Create   Add new records         (add_product)
#   Read     Retrieve / query        (view_all_products)
#   Update   Modify existing         (update_stock)
#   Delete   Remove records          (remove_product)
#
# ── CSV METHODS ───────────────────────────────────────────────
#
# WRITING:
#   writer = csv.writer(f)           Create writer object
#   writer.writerow([...])           Write one row (e.g. header)
#   writer.writerows([[...], ...])   Write multiple rows
#
# READING:
#   reader = csv.reader(f)           Create reader object
#   next(reader)                     Skip one row (e.g. header)
#   for row in reader:               Loop through rows
#
# CSV LIMITATIONS:
#   ⚠️ All values come back as strings — must convert manually
#   ⚠️ Update/Delete = read ALL → modify → rewrite ENTIRE file
#
# ── JSON METHODS ──────────────────────────────────────────────
#
# FILE OPERATIONS:
#   json.dump(data, f, indent=2)     Dict/list → JSON file
#   json.load(f)                     JSON file → dict/list
#
# ERROR HANDLING:
#   except FileNotFoundError         File doesn't exist
#   except json.JSONDecodeError      File is corrupted
#
# JSON ADVANTAGES:
#   ✓ Preserves types (3.80 stays float, True stays bool)
#   ✓ Supports nesting (dicts inside dicts)
#   ✓ Update/Delete = modify dict → json.dump() once
#
# ── CSV vs JSON ───────────────────────────────────────────────
#
#   CSV                          JSON
#   + Opens in Excel             + Preserves data types
#   + Simple, universal          + Supports nesting
#   + Good for exports           + Direct key lookup
#   - All values are strings     - Not easy in Excel
#   - Update = rewrite all       + CRUD = dict operations
#
# ── PATTERN ────────────────────────────────────────────────
#
#   JSON → primary storage (load at startup, save on exit)
#   CSV  → exports for management (open in Excel)
#
#   Store in JSON, export to CSV. Best of both worlds.
#
# ══════════════════════════════════════════════════════════════