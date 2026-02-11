# =======================================================
# IS1111 Dictionaries Tutorial — Exercises
# =======================================================

# -------------------------------------------------------
# QUESTION 1 — Login tracker
# -------------------------------------------------------

logins = {}

# (a) Add:
logins["anna"] = 1 # anna logs in once

logins["ben"] = 2 # ben logs in twice

logins["cara"] = 1 # cara logs in once

# print the dictionary
print("Logins:", logins)

# (b) Ben logs in again
logins["ben"] = logins["ben"] + 1

# (c) Print how many logins anna has
print("Anna's logins:", logins["anna"])

# (d) Print 0 if david does not exist
print("David's logins:", logins.get("david", 0))

# (e) Check if any user has exactly 3 logins
print("Does anyone have exactly 3 logins?", 3 in logins.values())


# -------------------------------------------------------
# QUESTION 2 — Movie ratings counter
# -------------------------------------------------------

ratings = [
    "Inception", "Avatar", "Inception",
    "Matrix", "Avatar", "Inception",
    "Matrix", "Avatar"
]

# (a) Count how many ratings each movie has received

ratings_count = {}
for movie in ratings:
    ratings_count[movie] = ratings_count.get(movie, 0) + 1

# (b) Print each movie and its count
for movie, count in ratings_count.items():
    print(f"{movie}: {count}")

# (c) Print number of different movies
print("Number of different movies:", len(ratings_count))



# -------------------------------------------------------
# QUESTION 3 — Most popular drink
# -------------------------------------------------------

orders = "tea coffee tea juice coffee tea water coffee"

# (a) Count each drink

drink_counts = {}
for drink in orders.split():
    drink_counts[drink] = drink_counts.get(drink, 0) + 1

# (b) Find the most popular drink
top = max(drink_counts, key=drink_counts.get)
print(f"Top drink (max): {top} ({drink_counts[top]} orders)")

# (c) Print drinks ordered more than once
for drink, count in drink_counts.items():
    if count > 1:
        print(f"{drink}: {count}")

# -------------------------------------------------------
# QUESTION 4 — Mail log day counter
# -------------------------------------------------------

fname = input("Enter file name: ")

# Count how many emails were sent on each day
# Day is the 3rd word in lines starting with "From "
day_counts = {}

with open(fname) as file:
    for line in file:
        if line.startswith("From "):
            parts = line.split()
            day = parts[2]
            day_counts[day] = day_counts.get(day, 0) + 1

# Print the dictionary
print(day_counts)

# Print the busiest day
busiest_day = max(day_counts, key=day_counts.get)
print(f"Busiest day: {busiest_day} ({day_counts[busiest_day]} emails)")