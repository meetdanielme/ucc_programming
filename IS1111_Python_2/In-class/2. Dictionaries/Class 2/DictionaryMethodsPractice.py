# EXERCISE A: DICTIONARY METHODS PRACTICE
# Fill in the blanks to complete each section.

# ── Section 1: Counting with get() ──────────────────────────────

# Count how many times each product category appears in the sales log
sales_log = ["Electronics", "Books", "Electronics", "Clothing",
             "Books", "Books", "Electronics", "Clothing", "Food"]

category_counts = {}

for category in sales_log:
    category_counts[category] = category_counts.get(category, 0) + 1

print("Category counts:", category_counts)


# ── Section 2: Finding the most popular ──────────────────────────

top_cat = None
top_num = 0

for category, count in category_counts.items():
    if count > top_num:
        top_num = count
        top_cat = category

print(f"Top category: {top_cat} ({top_num} sales)")


# ── Section 3: Aggregations ─────────────────────────────────────

# How many total items were sold?
total_sold = sum(category_counts.values())
print(f"Total items sold: {total_sold}")


# ── Section 4: Using pop() ──────────────────────────────────────

# Remove "Food" from the counts and store the removed value
removed = category_counts.pop('Food', 0)
print(f"Removed Food (count was {removed})")
print("After pop:", category_counts)


# ── Section 5: Merging with a loop ──────────────────────────────

# Online sales came in separately. ADD them to existing counts.
online_sales = {"Electronics": 5, "Books": 2, "Toys": 8}

for cat, count in online_sales.items():
    category_counts[cat] = category_counts.get(cat, 0) + count

print("After merging online:", category_counts)


# ── Section 6: Snapshot with copy() ─────────────────────────────

# Save a backup before clearing
backup = category_counts.copy()
category_counts.items()

print("Original after clear:", category_counts)
print("Backup preserved:", backup)