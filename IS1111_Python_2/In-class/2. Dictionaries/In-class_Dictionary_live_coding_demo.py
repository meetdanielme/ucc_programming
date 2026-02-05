# class5_dictionaries_live.py
# Class 5: Dictionaries (first class)

print("\nCLASS 5: DICTIONARIES\n")

# Warm-up: three ways to store student records (ID, name, programme, GPA)
# Parallel lists:
#   + simple to start with
#   - fragile: sorting/deleting one list can break alignment
# Nested lists (2D list):
#   + keeps each record together as a row
#   - lookup by ID still needs a loop; fields are positional (rec[3] means GPA only if you remember)
# Dictionary:
#   + fast lookup by key (ID); clear intent
#   - keys must be unique (reusing a key overwrites)

# Parallel lists: store each "column" separately (keep index alignment!)
student_ids = [101, 102, 103]
names = ["Siobhan", "Aoife", "Cian"]   # intentionally not alphabetical
programmes = ["BIS", "BIS", "CS"]
gpas = [3.9, 3.6, 3.2]

target_id = 102

# Parallel lists: lookup means "find the index, then use it everywhere"
idx = student_ids.index(target_id)
print("Parallel lists lookup:", student_ids[idx], names[idx], programmes[idx], gpas[idx])
print()

# Parallel lists: show that it works while aligned
print("Parallel lists (aligned):")
for i in range(len(student_ids)):
    print(student_ids[i], names[i], programmes[i], gpas[i])
print()

# Parallel lists: sorting ONE list breaks alignment
names.sort()
print("After sorting names only (misaligned):")
for i in range(len(student_ids)):
    print(student_ids[i], names[i], programmes[i], gpas[i])

# Parallel lists: deleting from ONE list breaks alignment / lengths
removed_name = names.pop(0)
print("Removed:", removed_name)
print("Lengths:", len(student_ids), len(names), len(programmes), len(gpas))
print()

# Nested list (2D list): each row is a student record
students_nested = [
    [101, "Siobhan", "BIS", 3.9],
    [102, "Aoife", "BIS", 3.6],
    [103, "Cian", "CS", 3.2],
]

# Nested list: lookup by ID requires a loop
print("Nested list lookup (loop by ID):")
for rec in students_nested:
    if rec[0] == target_id:
        print(rec)
        break
print()

# Nested list: update requires find-first + positional index
print("Nested list update GPA (rec[3]):")
for rec in students_nested:
    if rec[0] == target_id:
        rec[3] = 3.7
        break
print(students_nested)
print()

# Nested list: sorting rows keeps records together (safer than sorting a single parallel list)
students_nested.sort()  # sorts by first element (ID)
print("Nested list after sorting rows (records stay together):")
print(students_nested)
print()


# Dictionary: step-by-step intro (start simple, then add complexity)

# Step 1: simplest dictionary: key -> single value
# key = student ID, value = name
student_name_by_id = {
    101: "Siobhan",
    102: "Aoife",
    103: "Cian",
}

print("Dictionary (simple) lookup:", target_id, "->", student_name_by_id[target_id])

# Update a value (overwrite)
student_name_by_id[target_id] = "Aoife Byrne"
print("After overwrite name:", student_name_by_id[target_id])

# Add / delete are direct by key
student_name_by_id[104] = "Ben"
del student_name_by_id[103]
print("After add/delete:", student_name_by_id)
print()


# Step 2: dictionary values can store MORE than one field (tuple values)
# Tuple values are immutable, so updates mean overwriting the whole tuple.
students_dict_tuples = {
    101: ("Siobhan", "BIS", 3.9),
    102: ("Aoife", "BIS", 3.6),
    103: ("Cian", "CS", 3.2),
}

print("Dictionary (tuple values) lookup:", target_id, students_dict_tuples[target_id])

name, programme, gpa = students_dict_tuples[target_id]
students_dict_tuples[target_id] = (name, programme, 3.7)  # overwrite tuple to update GPA
print("After tuple GPA update:", target_id, students_dict_tuples[target_id])
print()


# Step 3: dictionary values can also be LISTS (mutable), allowing in-place updates
students_dict_lists = {
    101: ["Siobhan", "BIS", 3.9],
    102: ["Aoife", "BIS", 3.6],
    103: ["Cian", "CS", 3.2],
}

print("Dictionary (list values) lookup:", target_id, students_dict_lists[target_id])

# Update GPA in-place (list is mutable)
students_dict_lists[target_id][2] = 3.7
print("After in-place list GPA update:", target_id, students_dict_lists[target_id])

# Add / delete still direct
del students_dict_lists[103]
students_dict_lists[104] = ["Ben", "BIS", 3.1]
print("After delete/add (list values):", students_dict_lists)
print()


# Creating dictionaries: {}, dict(), literals
empty_a = {}
empty_b = dict()
print("Empty dictionaries:", empty_a, empty_b)
print("Type check:", type(empty_a))
print()

countries = {"CA": "Canada", "US": "United States", "MX": "Mexico"}
numbers = {1: "One", 2: "Two", 3: "Three"}
movie = {"name": "The Holy Grail", "year": 1975, "price": 9.99}

print("Dictionary literals:")
print("countries:", countries)
print("numbers:", numbers)
print("movie:", movie)
print()



# Accessing, adding, modifying (dictionaries are mutable)
employee = {"name": "Sarah Murphy", "department": "Sales", "salary": 45000}
print("Employee record:", employee)

print("Access with []:", employee["department"])
employee["salary"] = 48000
employee["email"] = "sarah.murphy@company.ie"
print("After update/add:", employee)
print("len(employee):", len(employee))
print()


# KeyError: what happens when a key is missing?
# (Uncomment briefly during demo to show the traceback)
# print(employee["phone"])  # KeyError: 'phone'

# Avoid KeyError: check with 'in'
field = "phone"
if field in employee:
    print("Phone:", employee[field])
else:
    print("Phone not found (checked with 'in').")

# Avoid KeyError: use get() with a default
print("Safe access with get():")
print("phone:", employee.get("phone", "Not on file"))
print("department:", employee.get("department", "Not on file"))
print()


# Slide example: purse updates based on current value
purse = dict()
purse["money"] = 12
purse["candy"] = 3
purse["tissues"] = 75

print("Purse:", purse)
print("Candy:", purse["candy"])
purse["candy"] = purse["candy"] + 2
print("After candy update:", purse)
print()

# Terminology crossover:
# - Python: dictionary (dict)
# - Other languages: map / associative array
# - Common implementation name: hash map / hash table (because hashing supports fast lookup)
# - Data interchange: a JSON "object" is often loaded into a dict in Python

# Hashing (why dict lookup is fast, and why keys must be immutable)
# Dicts use hash(key) internally to decide where to store/find a value.
# Note: Python randomises hashing for strings between PROGRAM RUNS (security feature),
# so hash("email") may differ tomorrow. Within one run, it is consistent.

print("hash('email'):", hash("email"))
print("hash('email') again:", hash("email"))
print("hash(102):", hash(102))
print("hash(102) again:", hash(102))
print()


# Same key -> same value -> stable lookup
demo = {"email": "student@ucc.ie"}
print("Lookup by key:", demo["email"])

# Lists are mutable so they are not hashable -> cannot be dict keys
try:
    bad = {}
    bad[[1, 2, 3]] = "x"
except TypeError as e:
    print("List as key error:", e)

print()
# Keys must be immutable (strings, ints, tuples ok; lists not ok)
valid_key_types = {
    "dept": "Sales",
    10: "ten",
    (1, 2): "tuple key works"
}
print("Valid key types:", valid_key_types)

# (Uncomment to show the error)
# invalid_key_types = {[1, 2, 3]: "list key"}  # TypeError: unhashable type: 'list'
print()

# Values can be anything (we'll keep it simple: strings, numbers, lists)
profile = {"name": "Cian", "roles": ["student_rep", "club_member"], "active": True}
print("Values can be lists:", profile["roles"])
print()


print("Looping countries (keys -> values):")
for code in countries:
    print(code, "->", countries[code])
print()

print("countries.keys() as a list:", list(countries.keys()))
print("countries.values() as a list:", list(countries.values()))
print()

print("Looping with items() (key, value together):")
for code, country in countries.items():
    print(code, "->", country)
print()

# values(): show it as a list (ties to quiz wording)
print("countries.values() as a list:", list(countries.values()))
print()


# Counting pattern preview (more depth next class)
names_seen = ["csev", "cwen", "csev", "zqian", "cwen", "csev"]
counts = {}

print("Counting occurrences with get():")
for name in names_seen:
    counts[name] = counts.get(name, 0) + 1
print(counts)
print()


# Dictionary order note (slides may say “no order”)
# Python 3.7+ preserves insertion order. Still: dicts are used for key-based lookup, not positions.
# If you need a specific order, sort explicitly.

order_test = {}
order_test["first"] = 1
order_test["second"] = 2
order_test["third"] = 3
order_test["fourth"] = 4

print("Insertion order preserved (Python 3.7+):", order_test)

print("Loop order matches insertion:")
for k in order_test:
    print(k, order_test[k])
print()

print("Explicit order when needed (sorted keys):")
for k in sorted(order_test):
    print(k, order_test[k])
print()


# Business mini-example: menu lookup (dictionary beats list for item -> price)
menu = {
    "Cheeseburger": 5.99,
    "Grilled Chicken Sandwich": 7.49,
    "Caesar Salad": 4.99,
    "Veggie Wrap": 6.29,
    "Iced Coffee": 2.99,
    "Lemonade": 1.99,
    "Orange Juice": 3.49
}

# Menu functions: lookup, add, update, order total, display

# Lookup: return -1 if missing (easy to test)
def get_price(menu_dict, item_name):
    return menu_dict.get(item_name, -1)

# Add: don't overwrite if already present
def add_item(menu_dict, item_name, price):
    if item_name in menu_dict:
        print(f"'{item_name}' already exists (not overwriting).")
        return
    menu_dict[item_name] = price
    print(f"Added '{item_name}' at €{price:.2f}")

# Update: only update existing items
def update_price(menu_dict, item_name, new_price):
    if item_name not in menu_dict:
        print(f"Cannot update '{item_name}': not on the menu.")
        return
    old = menu_dict[item_name]
    menu_dict[item_name] = new_price
    print(f"Updated '{item_name}': €{old:.2f} -> €{new_price:.2f}")

# Total: order is a list; menu is a dict (integration)
def calculate_total(menu_dict, order_list):
    total = 0
    for item in order_list:
        price = menu_dict.get(item)
        if price is None:
            print(f"  Missing item: {item} (skipping)")
            continue
        total += price
    return total

# Display: loop keys and print formatted output
def display_menu(menu_dict):
    print("Menu:")
    for item in menu_dict:
        print(f"{item:.<28} €{menu_dict[item]:.2f}")
    print()

# Menu demo: lookups
print("Menu lookup examples:")

item = "Caesar Salad"
price = get_price(menu, item)
if price is None:
    print(item, "not found")
else:
    print(item + ":", price)

item = "Pizza"
price = get_price(menu, item)
if price is None:
    print(item, "not found")
else:
    print(item + ":", price)

print()

# Menu demo: adding items
print("Adding items:")
add_item(menu, "Espresso", 2.49)
add_item(menu, "Lemonade", 2.49)
print()

# Menu demo: updating prices
print("Updating prices:")
update_price(menu, "Lemonade", 2.29)
update_price(menu, "Pizza", 12.99)
print()

# Menu demo: calculating a total
order = ["Cheeseburger", "Caesar Salad", "Iced Coffee", "Espresso", "Pizza"]
print("Order:", order)
print("Total:", f"€{calculate_total(menu, order):.2f}")
print()

# Menu demo: formatted menu output
display_menu(menu)