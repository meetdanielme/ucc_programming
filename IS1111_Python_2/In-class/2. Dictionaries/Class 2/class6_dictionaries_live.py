# class6_dictionaries_live.py
# Dictionaries — Counting, Methods & Aggregations


# ── Muddiest point from the quiz ──────────────────────────────

# Q3 used print(fruit, end=" ") — a few of you weren't sure about that.
# By default, print() adds a newline. The end= parameter changes that.

print("Hello", end=" ")
print("World")
# Output: Hello World

# Useful for building a line piece by piece in a loop
flavours = ["Vanilla", "Chocolate", "Strawberry"]
for f in flavours:
    print(f, end=" | ")
print()  # blank print to move to the next line after the loop
print()


# ── Quick del refresher (quiz sticking point) ─────────────────

# del removes the key-value pair and changes the length. No return value.
demo = {"a": 1, "b": 2, "c": 3}
print("Before del:", demo, "| len:", len(demo))
del demo["b"]
print("After del:", demo, "| len:", len(demo))
print()

# .items() gives tuples — that's why type() showed <class 'tuple'> in Q2
for key, value in demo.items():
    print(f"  key={key}, value={value}")
    print(type())

print()
print(type(demo.items()))

# ── Counting pattern: if/else way first ───────────────────────

# Scenario: coffee shop logs every drink sold. How many of each?
orders = ["Latte", "Espresso", "Latte", "Cappuccino", "Espresso",
          "Latte", "Americano", "Cappuccino", "Latte", "Espresso"]

# Check if the drink is already a key. If yes, add 1. If no, set to 1.
drink_counts = {}
for drink in orders:
    if drink in drink_counts:
        drink_counts[drink] += 1
    else:
        drink_counts[drink] = 1

print("Counting (if/else):", drink_counts)
# Works but verbose — 4 lines inside the loop. get() does it in 1...


# ── Counting pattern: get() shortcut ──────────────────────────

drink_counts = {}
for drink in orders:
    drink_counts[drink] = drink_counts.get(drink, 0) + 1

print("Counting (get()):", drink_counts)

# Trace through what happens:
# "Latte" first time  → get returns 0 (not found) → 0 + 1 = 1
# "Latte" second time → get returns 1 (found)     → 1 + 1 = 2
# "Latte" third time  → get returns 2 (found)     → 2 + 1 = 3
#
# That one line replaces the entire if/else block.
# This pattern works on anything — words, sales, survey responses.
# Tip: use .lower() if comparing strings to avoid "The" ≠ "the".
print()


# ── Finding the most common item ──────────────────────────────

# Pattern: track "best so far" as you loop through .items()
print("Drink counts:", drink_counts)

best_drink = None
best_count = 0
for drink, count in drink_counts.items():
    if count > best_count:
        best_count = count
        best_drink = drink

print(f"Most popular: {best_drink} ({best_count} orders)")
print()

# This is reusable logic — let's make it a function.
def find_most_common(counts_dict):
    """Returns (key, count) for the entry with the highest value."""
    top_key = None
    top_val = 0
    for key, val in counts_dict.items():
        if val > top_val:
            top_val = val
            top_key = key
    return top_key, top_val

# Works on any counts dictionary — drinks, words, categories, anything.
print("Most common drink:", find_most_common(drink_counts))
print()


# ── Shortcut: max() with a key function ───────────────────────

# max(drink_counts) would compare keys alphabetically — not what we want.
# key=drink_counts.get tells max() to compare by values instead.
# It passes each key to drink_counts.get(), gets the count back,
# and returns whichever key had the highest count.
top = max(drink_counts, key=drink_counts.get)
print(f"Top drink (max): {top} ({drink_counts[top]} orders)")
print()

# ── Aggregations using .values() ─────────────────────────────

# .values() gives just the numbers — use built-in functions directly.
print("Values:", list(drink_counts.values()))
print("Total sold:", sum(drink_counts.values()))
print("Highest count:", max(drink_counts.values()))
print("Lowest count:", min(drink_counts.values()))
print("Unique drinks:", len(drink_counts))

average = sum(drink_counts.values()) / len(drink_counts)
print(f"Average per type: {average:.1f}")
print()


# ── pop(): remove AND get the value back ──────────────────────

# We saw del earlier — it deletes but returns nothing.
# pop() removes the key AND returns its value — useful when you
# need to know what was removed.

print("Before pop:", drink_counts)
removed = drink_counts.pop("Americano")
print(f"Popped 'Americano' — got back: {removed}")
print("After pop:", drink_counts)
print()

# pop() with a default avoids KeyError (same idea as get())
result = drink_counts.pop("Mocha", 0)
print(f"pop('Mocha', 0) — key missing, got back: {result}")
print("Dict unchanged:", drink_counts)
print()

# Summary of removal approaches:
# del dict[key]           → deletes, returns nothing, KeyError if missing
# dict.pop(key)           → deletes, returns value,   KeyError if missing
# dict.pop(key, default)  → deletes, returns value,   returns default if missing


# ── update(): merging dictionaries ────────────────────────────

# The afternoon shift tracked their sales separately.
afternoon = {"Latte": 3, "Flat White": 5, "Espresso": 2}

# update() OVERWRITES matching keys — it does NOT add.
test = drink_counts.copy()  # safe copy so we don't destroy our data
print("Morning:", test)
print("Afternoon:", afternoon)

test.update(afternoon) # Merges afternoon into test, overwriting any matching keys — NOT ADDING!
print("After update():", test)
# Latte was 4, afternoon had 3 → result is 3. Overwritten, not added!
# Flat White was new → added correctly. That part works fine.
print()

# To actually ADD values together, use the get() loop:
combined = drink_counts.copy()
for drink, count in afternoon.items():
    combined[drink] = combined.get(drink, 0) + count

print("Properly merged:", combined)
print()
# Rule of thumb:
#   update() = overwrite/add new keys
#   get() loop = accumulate values


# ── copy() vs assignment (aliasing trap) ──────────────────────

# Why do we keep writing .copy()? Because = doesn't create a new dict.
# It creates a second name pointing to the SAME object.
original = {"Latte": 4, "Espresso": 3}
alias = original          # same object, two names
backup = original.copy()  # genuinely separate dictionary

original["Latte"] = 99
print("original:", original)
print("alias:", alias)         # Also 99 — same object!
print("backup:", backup)       # Still 4 — independent copy
print()
# Use .copy() whenever you need to experiment without destroying the original.


# ── clear(): empty a dictionary completely ────────────────────

# Removes all key-value pairs. Dict still exists, just empty.
temp = {"x": 1, "y": 2, "z": 3}
print("Before clear:", temp)
temp.clear()
print("After clear:", temp)
# Useful for resetting counters at end of day, clearing caches, etc.
print()


# ── Practice: dict with list values ───────────────────────────

# Real-world data often maps keys to lists. This is good practice
# for combining dict access with list indexing and operations.

student_grades = {
    "Siobhan": [72, 85, 91, 68],
    "Aoife":   [88, 79, 95, 82],
    "Cian":    [65, 70, 58, 73],
}

# Access a student's grades, then index/slice the list
print("Aoife's grades:", student_grades["Aoife"])
print("Aoife's first:", student_grades["Aoife"][0])
print("Aoife's last two:", student_grades["Aoife"][-2:])
print()

# Average for one student
aoife = student_grades["Aoife"]
print(f"Aoife's average: {sum(aoife) / len(aoife):.1f}")

# Average for all students
print("\nAll averages:")
for name, grades in student_grades.items():
    avg = sum(grades) / len(grades)
    print(f"  {name}: {avg:.1f}")

# Highest average — same "best so far" pattern
best_student = None
best_avg = 0
for name, grades in student_grades.items():
    avg = sum(grades) / len(grades)
    if avg > best_avg:
        best_avg = avg
        best_student = name

print(f"\nTop student: {best_student} ({best_avg:.1f})")

# Adding a new grade to an existing student
student_grades["Cian"].append(80)
print(f"Cian after new grade: {student_grades['Cian']}")

# Adding a new student
student_grades["Roisin"] = [76, 88]
print(f"Added Roisin: {student_grades['Roisin']}")
print()


# ── Mini case: end-of-day sales report ────────────────────────

# Putting it all together: counting, revenue, formatted report.
daily_transactions = [
    "Latte", "Espresso", "Latte", "Cappuccino", "Espresso",
    "Latte", "Flat White", "Cappuccino", "Latte", "Espresso",
    "Flat White", "Flat White"
]

drink_prices = {
    "Latte": 3.80, "Espresso": 2.50, "Cappuccino": 3.50,
    "Flat White": 3.90, "Americano": 3.00,
}

# Step 1: Count sales (same get() pattern — just run it, you've seen this)
sales = {}
for item in daily_transactions:
    sales[item] = sales.get(item, 0) + 1
print("Sales:", sales)

# Step 2: Revenue per drink — two dicts working together
# Each entry is independent (count × price), so this works as a loop...
revenue = {}
for drink, qty in sales.items():
    revenue[drink] = qty * drink_prices.get(drink, 0)
print("Revenue:", revenue)

# ...or as a dictionary comprehension — same thing in one line:
revenue = {drink: qty * drink_prices.get(drink, 0) for drink, qty in sales.items()}
# Pattern: {new_key: new_value for key, value in dict.items()}
# Comprehensions work when each entry is calculated independently.
# They do NOT work for counting/accumulating (where you need get()).

# Step 3: Formatted report
print(f"\n{'Item':<18} {'Qty':>5} {'Revenue':>10}")
print("-" * 35)
for drink, qty in sales.items():
    rev = revenue[drink]
    print(f"{drink:<18} {qty:>5} {'€' + f'{rev:.2f}':>10}")

print("-" * 35)
total_units = sum(sales.values())
total_rev = sum(revenue.values())
print(f"{'Total':<18} {total_units:>5} {'€' + f'{total_rev:.2f}':>10}")

# Step 4: Best seller
top_drink = max(sales, key=sales.get)
print(f"\nBest seller: {top_drink} ({sales[top_drink]} units)")


# ── Methods covered so far ────────────────────────────────────
#
# Creating:     {}  or  dict()
# Accessing:    dict[key]  or  dict.get(key, default)
# Adding:       dict[new_key] = value
# Updating:     dict[key] = new_value
# Deleting:     del dict[key]           — no return, KeyError if missing
#               dict.pop(key)           — returns value, KeyError if missing
#               dict.pop(key, default)  — returns value, default if missing
#               dict.clear()            — empties the whole dict
# Copying:      dict.copy()             — independent shallow copy
# Merging:      dict.update(other)      — overwrites matching keys
# Looping:      dict.keys()             — just the keys
#               dict.values()           — just the values
#               dict.items()            — (key, value) tuples
# Checking:     key in dict             — True/False
# Aggregating:  sum/max/min/len on dict.values()
# Finding max:  max(dict, key=dict.get) — key with highest value