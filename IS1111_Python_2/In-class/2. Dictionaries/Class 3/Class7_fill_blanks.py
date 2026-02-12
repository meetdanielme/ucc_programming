# ══════════════════════════════════════════════════════════════
# EXERCISE A: NESTED DICTS, SEARCH & ID GENERATION
# Fill in the blanks to complete each section.
# ══════════════════════════════════════════════════════════════

inventory = {
    "P001": {"name": "Milk",    "category": "Dairy",     "price": 1.50, "quantity": 20},
    "P002": {"name": "Bread",   "category": "Bakery",    "price": 0.85, "quantity": 15},
    "P003": {"name": "Butter",  "category": "Dairy",     "price": 2.50, "quantity": 12},
    "P004": {"name": "Tea",     "category": "Beverages", "price": 3.20, "quantity": 30},
    "P005": {"name": "Muffins", "category": "Bakery",    "price": 1.75, "quantity": 8},
}


# ──────────────────────────────────────────────────────────────
# SECTION 1: NESTED DICTIONARY ACCESS
# ──────────────────────────────────────────────────────────────

# 1) Print the name of product P002 (should print "Bread")
print(inventory["P002"]["name"])

# 2) Print the price of product P004 (should print 3.2)
print(inventory["P004"]["price"])

# 3) Update P003's quantity from 12 to 22 (delivery arrived).
inventory["P003"]["quantity"] = 22

# 4) Safely get the name of product P009 (doesn't exist).
#    Use chained get() so it returns None instead of crashing.
result = inventory.get("P009", {}).get("name")
print("P009 name:", result)

# 5) Check if P001 has a "discount" field before accessing it.
pid = "P001"
field = "discount"
if field in inventory[pid]:
    print(f"Discount: {inventory[pid][field]}")
else:
    print(f"{pid} has no '{field}' on file.")


# ──────────────────────────────────────────────────────────────
# SECTION 2: SEARCH PATTERNS
# ──────────────────────────────────────────────────────────────

# 6) PARTIAL name search (case-insensitive).
#    Find all products whose name contains "mi".
search_term = "mi"
name_matches = []

for pid, product in inventory.items():
    if search_term.lower() in product["name"].lower():
        name_matches.append((pid, product))

print(f"\nName search for '{search_term}':")
for pid, product in name_matches:
    print(f"  {pid}: {product['name']}")
print(f"Found {len(name_matches)} product(s)")

# 7) EXACT category search (case-insensitive).
#    Find all products in the "dairy" category.
search_cat = "dairy"
cat_matches = []

for pid, product in inventory.items():
    if product["category"].lower() == search_cat.lower():
        cat_matches.append((pid, product))

print(f"\nCategory search for '{search_cat}':")
for pid, product in cat_matches:
    print(f"  {pid}: {product['name']} ({product['category']})")
print(f"Found {len(cat_matches)} product(s)")


# ──────────────────────────────────────────────────────────────
# SECTION 3: KEY EXTRACTION & ID GENERATION
# ──────────────────────────────────────────────────────────────

# 8) Extract the number from the key "P003".
sample_key = "P003"
number = int(sample_key[1:])
print(f"\n'{sample_key}' → number: {number}")

# 9) Format the number 7 as a zero-padded product ID → "P007"
n = 7
formatted_id = f"P{n:03d}"
print(f"n={n} → ID: '{formatted_id}'")

# 10) Generate the next product ID.
if not inventory:
    next_id = "P001"
else:
    max_num = 0
    for pid in inventory:
        num = int(pid[1:])
        if num > max_num:
            max_num = num
    next_id = f"P{max_num + 1:03d}"

print(f"Next product ID: '{next_id}'")


# ──────────────────────────────────────────────────────────────
# SECTION 4: GROUPING & AGGREGATION
# ──────────────────────────────────────────────────────────────

# 11) Build a category summary: count of products and total
#     value (price × quantity) per category.

category_data = {}

for product in inventory.items():
    cat = product[1]["category"]
    value = product[1]["price"] * product[1]["quantity"]

    if cat not in category_data:
        category_data[cat] = {"count": 0, "value": 0.0}

    category_data[cat]["count"] += 1
    category_data[cat]["value"] += value

print(f"\n{'Category':<15} {'Products':<10} {'Total Value':<12}")
print("=" * 37)
grand_count = 0
grand_value = 0.0
for cat, data in sorted(category_data.items()):
    print(f"{cat:<15} {data['count']:<10} €{data['value']:<11.2f}")
    grand_count += data["count"]
    grand_value += data["value"]
print("=" * 37)
print(f"{'Total':<15} {grand_count:<10} €{grand_value:<11.2f}")


# ──────────────────────────────────────────────────────────────
# SECTION 5: BUILDING A NESTED DICT FROM A LIST
# ──────────────────────────────────────────────────────────────
# This is how A2's main() loads sample data — understand this
# pattern so the provided code makes sense.

new_products = [
    {"name": "Cheese",  "category": "Dairy",  "price": 3.00, "quantity": 18},
    {"name": "Rolls",   "category": "Bakery", "price": 1.20, "quantity": 24},
    {"name": "Coffee",  "category": "Beverages", "price": 4.50, "quantity": 15},
]

new_inventory = {}

for item in new_products:
    if not new_inventory:
        product_id = "P001"
    else:
        max_num = 0
        for pid in new_inventory:
            num = int(pid[1:])
            if num > max_num:
                max_num = num
        product_id = f"P{max_num + 1:03d}"

    new_inventory[product_id] = item

# 12) Print the resulting inventory to verify
print("\nBuilt from list:")
for pid, prod in new_inventory.items():
    print(f"  {pid}: {prod['name']} ({prod['category']}) — €{prod['price']:.2f} × {prod['quantity']}")

# 13) Add one more product: "Jam", "Preserves", €2.80, qty 10.
#     Generate the ID, then add it. (Same pattern — try with fewer hints.)
if not new_inventory:
    new_id = "P001"
else:
    max_num = 0
    for pid in new_inventory:
        num = int(pid[1:])
        if num > max_num:
            max_num = num
    new_id = f"P{max_num + 1:03d}"

new_inventory[new_id] = {"name": "Jam", "category": "Preserves", "price": 2.80, "quantity": 10}