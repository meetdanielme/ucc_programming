# class6_dictionaries_live.py
# Dictionaries — Counting, Methods & Aggregations


# ── Muddiest point from the quiz ──────────────────────────────

# Q3 used print(fruit, end=" ") — a few of you weren't sure about that.
# By default, print() adds a newline at the end: \n
# The end= parameter lets you change what goes at the end instead.

# Normal behaviour:
print("Hello")
print("World")
# Output:
# Hello
# World

# With end=" " — stays on the same line, separated by a space
print("Hello", end=" ")
print("World")
# Output: Hello World

# Useful when you want to build up a line piece by piece in a loop
flavours = ["Vanilla", "Chocolate", "Strawberry"]
for f in flavours:
    print(f, end=" | ")
print()  # blank print to move to the next line after the loop

# Another common one: end="" — no space, no newline, nothing
for f in flavours:
    print(f, end="")
print()
# Output: VanillaChocolateStrawberry  (all mashed together)

# So in Q3 when we wrote:
#   for fruit, price in prices.items():
#       if price > 1.00:
#           print(fruit, end=" ")
# It prints each matching fruit on the SAME line with a space between them.
print()


# ── Quick del refresher (another quiz sticking point) ─────────

demo = {"a": 1, "b": 2, "c": 3}
print("Before del:", demo, "| len:", len(demo))
del demo["b"]
print("After del:", demo, "| len:", len(demo))
# Key takeaway: del permanently removes the pair AND changes the length.
# There's no return value — it just deletes.
print()

# .items() gives you tuples — each pair is (key, value)
# That's why type() showed <class 'tuple'> in Q2
for pair in demo.items():
    print("pair:", pair, "| type:", type(pair))

# And we can UNPACK those tuples into two variables:
for key, value in demo.items():
    print(f"  key={key}, value={value}")
print()


# ── Counting pattern: the if/else way first ───────────────────

# Scenario: a coffee shop logs every drink sold as a simple list.
# They want to know how many of each drink sold today.

orders = ["Latte", "Espresso", "Latte", "Cappuccino", "Espresso",
          "Latte", "Americano", "Cappuccino", "Latte", "Espresso"]

# The verbose approach: check if the drink is already in the dict

drink_counts = {}

for drink in orders:
    if drink in drink_counts:
        drink_counts[drink] = drink_counts[drink] + 1
    else:
        drink_counts[drink] = 1

print("Counting (if/else):", drink_counts)

# This works perfectly. But it's 4 lines inside the loop every time.
# We can do the same thing in 1 line with get()...


# ── Counting pattern: the get() shortcut ──────────────────────

drink_counts_v2 = {}

for drink in orders:
    drink_counts_v2[drink] = drink_counts_v2.get(drink, 0) + 1

print("Counting (get()):", drink_counts_v2)

# Let's trace through this step by step:
# Iteration 1 — drink = "Latte"
#   drink_counts_v2.get("Latte", 0) → key not found → returns 0
#   0 + 1 = 1
#   drink_counts_v2 = {"Latte": 1}

# Iteration 2 — drink = "Espresso"
#   drink_counts_v2.get("Espresso", 0) → not found → 0
#   0 + 1 = 1
#   drink_counts_v2 = {"Latte": 1, "Espresso": 1}

# Iteration 3 — drink = "Latte"
#   drink_counts_v2.get("Latte", 0) → found! → returns 1
#   1 + 1 = 2
#   drink_counts_v2 = {"Latte": 2, "Espresso": 1}

# That one line replaces the entire if/else block.
print()


# ── Counting words in text ────────────────────────────────────

# A manager got a customer review and wants to see which words
# come up most often. We need to split the text into words first.

review = "the food was great and the service was great and fast"

words = review.split()
print("Split result:", words)
print("Number of words:", len(words))

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print("Word counts:", word_counts)

# What if the review had mixed case?
review_messy = "The food was Great and the Service was great AND fast"

words_messy = review_messy.split()
counts_messy = {}
for word in words_messy:
    counts_messy[word] = counts_messy.get(word, 0) + 1

print("\nWith mixed case:", counts_messy)
# "The" and "the" are separate keys! "Great" and "great" too!

# Fix: convert to lowercase before counting
counts_clean = {}
for word in words_messy:
    lower_word = word.lower()
    counts_clean[lower_word] = counts_clean.get(lower_word, 0) + 1

print("Case-insensitive:", counts_clean)
# Now "the" has 2, "great" has 2, "and" has 2 — much better
print()


# ── Finding the most common item ──────────────────────────────

# We have our counts — now how do we find the winner?
# Pattern: track "best so far" as you loop through .items()

print("Drink counts to search:", drink_counts)

best_drink = None
best_count = 0

for drink, count in drink_counts.items():
    print(f"  Checking {drink}: {count} — best so far: {best_count}")
    if count > best_count:
        best_count = count
        best_drink = drink
        print(f"    → New best! {best_drink} with {best_count}")

print(f"\nMost popular drink: {best_drink} ({best_count} orders)")
print()

# This pattern works on ANY counts dictionary.
# Let's turn it into a reusable function so we don't rewrite it.

def find_most_common(counts_dict):
    """Returns (key, count) for the entry with the highest value."""
    top_key = None
    top_val = 0
    for key, val in counts_dict.items():
        if val > top_val:
            top_val = val
            top_key = key
    return top_key, top_val

# Test it on different dictionaries:
print("Most common drink:", find_most_common(drink_counts))
print("Most common word:", find_most_common(counts_clean))

# Notice: the function doesn't care what the keys ARE — drinks,
# words, departments. It just finds whatever has the highest count.
print()


# ── Aggregations using .values() ─────────────────────────────

# .values() gives us just the numbers — no keys, just the counts.
# We can use Python's built-in functions on them directly.

print("Drink counts dict:", drink_counts)
print("Just the values:", list(drink_counts.values()))
print()

# Total drinks sold today
print("Total drinks sold:", sum(drink_counts.values()))

# Highest count for any single drink
print("Highest single count:", max(drink_counts.values()))

# Lowest count
print("Lowest single count:", min(drink_counts.values()))

# Number of unique drinks (that's just the number of keys)
print("Unique drinks:", len(drink_counts))

# Average drinks per type
total = sum(drink_counts.values())
unique = len(drink_counts)
average = total / unique
print(f"Average per drink type: {average:.1f}")
print()

# Same approach works on word counts
print("Total words counted:", sum(counts_clean.values()))
print("Unique words:", len(counts_clean))
print()


# ── pop(): remove AND get the value back ──────────────────────

# We already know del. But del just deletes — nothing comes back.

example = {"a": 10, "b": 20, "c": 30}
del example["a"]
# We can't capture what "a" was. It's just gone.
print("After del:", example)

# pop() removes the key AND returns its value — useful!
removed_value = example.pop("b")
print(f"Popped 'b' — got back: {removed_value}")
print("After pop:", example)
print()

# Real scenario: the coffee shop discontinues Americano
print("Before discontinuing:", drink_counts)

discontinued_count = drink_counts.pop("Americano")
print(f"Removed 'Americano' (had {discontinued_count} orders today)")
print("After discontinuing:", drink_counts)
print()

# What if we try to pop a key that doesn't exist?
# drink_counts.pop("Mocha")  # → KeyError! Just like del.

# But pop() accepts a DEFAULT (second argument) — same idea as get()
result = drink_counts.pop("Mocha", 0)
print(f"Tried to pop 'Mocha' — got back: {result}")
print("Dict unchanged:", drink_counts)

# Compare the three approaches:
# del dict["key"]           → deletes, returns nothing, KeyError if missing
# dict.pop("key")           → deletes, returns value, KeyError if missing
# dict.pop("key", default)  → deletes, returns value, returns default if missing
print()


# ── update(): merging one dictionary into another ─────────────

# The afternoon shift tracked their sales separately:
afternoon_orders = {"Latte": 3, "Flat White": 5, "Espresso": 2}

# You might think update() would ADD the counts together...
test = drink_counts.copy()  # (we'll explain copy in a sec)
print("Morning counts:", test)
print("Afternoon counts:", afternoon_orders)

test.update(afternoon_orders)
print("After update():", test)
# Look at Latte — morning had 4, afternoon had 3... result is 3!
# update() OVERWRITES matching keys. It doesn't add.
# It's like doing dict[key] = new_value for every key in the other dict.
print()

# Flat White was added because it was new — that part worked.
# But for existing keys, it replaced instead of adding. Bad for counting!

# The correct way to MERGE counts: loop with get()
print("Let's merge properly this time...")

combined = drink_counts.copy()
print("Starting with morning:", combined)

for drink, count in afternoon_orders.items():
    combined[drink] = combined.get(drink, 0) + count
    # First iteration: "Latte" → combined.get("Latte", 0) returns 4 → 4 + 3 = 7
    # "Flat White" → combined.get("Flat White", 0) returns 0 → 0 + 5 = 5

print("Properly merged:", combined)
print()

# Key lesson: update() is for overwriting/adding new keys.
# For ADDING VALUES together, you need the get() loop.


# ── copy() vs assignment (aliasing trap) ──────────────────────

# Why do we keep writing .copy() above? Because of this:

original = {"Latte": 4, "Espresso": 3}
alias = original              # this does NOT create a new dictionary
backup = original.copy()      # this DOES create a new dictionary

print("original:", original)
print("alias:", alias)
print("backup:", backup)
print()

# Now change the original:
original["Latte"] = 99

print("After changing original['Latte'] to 99:")
print("original:", original)
print("alias:", alias)         # ALSO shows 99 — same object!
print("backup:", backup)       # Still shows 4 — independent copy
print()

# Why? Because alias = original means "alias points to the SAME dict."
# It's two names for one object. Like a shortcut on your desktop —
# deleting the shortcut doesn't delete the file, but editing through
# the shortcut edits the actual file.

# .copy() creates a genuinely separate dictionary.
# When you need to experiment without destroying the original, use .copy()


# ── clear(): empty a dictionary completely ────────────────────

temp = {"x": 1, "y": 2, "z": 3}
print("Before clear:", temp, "| len:", len(temp))
temp.clear()
print("After clear:", temp, "| len:", len(temp))
# Useful for resetting at the end of a day, clearing a cache, etc.
print()


# ── Mini case: putting it all together ────────────────────────

# The shop manager wants an end-of-day report.
# They have: a list of transactions and a price dictionary.

daily_transactions = [
    "Latte", "Espresso", "Latte", "Cappuccino", "Espresso",
    "Latte", "Flat White", "Cappuccino", "Latte", "Espresso",
    "Flat White", "Flat White"
]

drink_prices = {
    "Latte": 3.80,
    "Espresso": 2.50,
    "Cappuccino": 3.50,
    "Flat White": 3.90,
    "Americano": 3.00,
}

# Step 1: Count sales
sales = {}
for item in daily_transactions:
    sales[item] = sales.get(item, 0) + 1

print("Sales counts:", sales)

# Step 2: Calculate revenue per drink (count × unit price)
# This needs TWO dictionaries working together
revenue = {}
for drink, qty in sales.items():
    unit_price = drink_prices.get(drink, 0)
    revenue[drink] = qty * unit_price

print("Revenue per drink:", revenue)

# Step 3: The manager wants to merge in the online orders too
online = {"Latte": 2, "Mocha": 4, "Espresso": 1}

all_sales = sales.copy()
for drink, count in online.items():
    all_sales[drink] = all_sales.get(drink, 0) + count

print("Combined (in-store + online):", all_sales)

# Step 4: Discontinue Mocha (pop it out safely)
removed = all_sales.pop("Mocha", 0)
print(f"Removed Mocha ({removed} units)")

# Step 5: Recalculate revenue on combined and print a report
combined_revenue = {}
for drink, qty in all_sales.items():
    combined_revenue[drink] = qty * drink_prices.get(drink, 0)

# Formatted report
print(f"\n{'Item':<18} {'Qty':>5} {'Revenue':>10}")
print("-" * 35)
for drink, qty in all_sales.items():
    rev = combined_revenue[drink]
    print(f"{drink:<18} {qty:>5} {'€' + f'{rev:.2f}':>10}")

print("-" * 35)
total_units = sum(all_sales.values())
total_rev = sum(combined_revenue.values())
print(f"{'Total':<18} {total_units:>5} {'€' + f'{total_rev:.2f}':>10}")

# Step 6: Who's the star?
top_drink, top_qty = find_most_common(all_sales)
print(f"\nBest seller: {top_drink} ({top_qty} units)")

# Note how we reused find_most_common() from earlier — functions pay off.
# Also notice how "Mocha" shows €0.00 if it's not in the price dict.
# get(drink, 0) handles that gracefully instead of crashing.