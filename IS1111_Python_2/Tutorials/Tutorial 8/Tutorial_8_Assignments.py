# =============================================================================
# IS1111 | Tutorial – Object-Oriented Programming
# Sessions 1 & 2: Objects, Classes, and Instances
# Duration: approximately 2 hours (self-directed)
# Domain: Flix Cinema
# =============================================================================
#
# HOW TO USE THIS FILE
# --------------------
# Work through each part in order. Every part builds on the one before it.
# Do not skip ahead.
#
# At each CHECKPOINT, compare your output to the expected output shown.
# If your output does not match, fix the issue before continuing — later
# parts depend on earlier ones working correctly.
#
# The EXTENSION tasks at the end are for students who finish early.
# They are not required, but they are good practice.
#
# You do not need any imports for this tutorial.
# =============================================================================


# =============================================================================
# PART 1 – YOUR FIRST CLASS  (~20 minutes)
# =============================================================================
#
# We are going to build a first simple class together.
# A CinemaScreen object represents one of the screens in the cinema.
# -----------------------------------------------------------------------------

# TASK 1.1 – A class with class-level attributes and two methods
#
# Define a class called CinemaScreen with:
#   - A class-level attribute: is_available = True
#   - A class-level attribute: format = "2D"
#   - A method show_status(self) that prints:
#       "Screen | Format: X | Available: Y"
#       where X is format and Y is is_available
#   - A method book(self) that sets is_available to False
#       and prints: "Screen booked."
#
# Then:
#   - Create two CinemaScreen instances: screen1 and screen2
#   - Call show_status() on both
#   - Call book() on screen1
#   - Call show_status() on both again
#   - Print type(screen1) and type(screen2)
#   - Print dir(screen1), filtering out dunder entries
#
# ✔ CHECKPOINT – Expected output:
# Screen | Format: 2D | Available: True
# Screen | Format: 2D | Available: True
# Screen booked.
# Screen | Format: 2D | Available: False
# Screen | Format: 2D | Available: True
# <class '__main__.CinemaScreen'>
# <class '__main__.CinemaScreen'>
# ['book', 'format', 'is_available', 'show_status']

# Write your code below:

class CinemaScreen:
    is_available = True
    format = "2D"

    def show_status(self):
        print(f"Screen | Format: {self.format} | Available: {self.is_available}")

    def book(self):
        self.is_available = False
        print("Screen booked.")

screen1 = CinemaScreen()
screen2 = CinemaScreen()
screen1.show_status()    # Screen | Format: 2D | Available: True
screen2.show_status()    # Screen | Format: 2D | Available: True
screen1.book()           # Screen booked.
screen1.show_status()    # Screen | Format: 2D | Available: False
screen2.show_status()    # Screen | Format: 2D | Available: True
print(type(screen1))     # <class '__main__.CinemaScreen'>
print(type(screen2))     # <class '__main__.CinemaScreen'>
print([attr for attr in dir(screen1) if not attr.startswith("__")])


# =============================================================================
# PART 2 – THE CONSTRUCTOR  (~30 minutes)
# =============================================================================
#
# In Part 1 every CinemaScreen started with the same default values and we had
# no way to give each object its own data at creation time. The constructor
# solves this. We will practise the three steps of building a constructor
# using two different classes before introducing Film.
# -----------------------------------------------------------------------------

# TASK 2.1 – Constructor with no parameters (class: CinemaScreen)
#
# Rewrite CinemaScreen so it has a constructor with no parameters
# (apart from self). Inside the constructor, set the following attributes:
#       self.screen_number = 0
#       self.capacity = 0
#       self.format = "2D"
#       self.is_available = True
#
# Create one instance. Then set its attributes manually afterwards:
#   screen1.screen_number = 3
#   screen1.capacity = 120
#   screen1.format = "IMAX"
#
# Print each attribute directly.
#
# ✔ CHECKPOINT – Expected output:
# 3
# 120
# IMAX
# True

# Write your code below:

class CinemaScreen:
    def __init__(self):
        self.screen_number = 0
        self.capacity = 0
        self.format = "2D"
        self.is_available = True

screen1 = CinemaScreen()
screen1.screen_number = 3
screen1.capacity = 120
screen1.format = "IMAX"
print(screen1.screen_number)  # 3
print(screen1.capacity)       # 120
print(screen1.format)         # IMAX
print(screen1.is_available)   # True


# TASK 2.2 – Constructor with parameters (class: Customer)
#
# Define a NEW class called Customer whose constructor takes name and
# loyalty_points as parameters. Set those as instance attributes, and also
# set is_member to True for every new Customer.
#
# Create two instances — one for Alex with 150 points, one for Max with 0 —
# and print the name and loyalty_points of each directly.
#
# Then confirm the two instances are independent: add 50 points to
# Alex's loyalty_points and print both values again.
#
# ✔ CHECKPOINT – Expected output:
# Alex 150
# Max 0
# 200
# 0

# Write your code below:

class Customer:
    def __init__(self, name, loyalty_points):
        self.name = name
        self.loyalty_points = loyalty_points
        self.is_member = True

customer1 = Customer("Alex", 150)
customer2 = Customer("Max", 0)
print(customer1.name, customer1.loyalty_points)  # Alex 150
print(customer2.name, customer2.loyalty_points)  # Max 0
customer1.loyalty_points += 50
print(customer1.loyalty_points)  # 200
print(customer2.loyalty_points)  # 0


# TASK 2.3 – Constructor with a default parameter value (class: Film)
#
# Define a NEW class called Film. Its constructor should take title, duration,
# rating, and ticket_price — where ticket_price defaults to 12.50.
# Every Film also starts with is_showing set to True.
#
# Create three instances using the data below and print the title and
# formatted ticket_price of each using an f-string.
#
#   "The Lighthouse" | 109 min | rated 16  | €14.00
#   "Paddington"     | 95 min  | rated G   | (use the default price)
#   "Dune: Part Two" | 166 min | rated 12A | (use the default price)
#
# ✔ CHECKPOINT – Expected output:
# The Lighthouse: €14.00
# Paddington: €12.50
# Dune: Part Two: €12.50

# Write your code below:

class Film:
    num_films = 0

    def __init__(self, title, duration, rating, ticket_price=12.50):
        Film.num_films += 1
        self.title = title
        self.duration = duration
        self.rating = rating
        self.ticket_price = ticket_price
        self.is_showing = True

    def cancel(self):
        self.is_showing = False
        print(f"{self.title} has been cancelled.")

    def reopen(self):
        self.is_showing = True
        print(f"{self.title} is showing again.")

    def get_duration_str(self):
        return f"{self.duration} min"
    
    def get_price_str(self):
        return f"€{self.ticket_price:.2f}"
    
    def get_summary(self):
        return f"{self.title} ({self.get_duration_str()}) | Rating: {self.rating} | Ticket: {self.get_price_str()}"
    
    def apply_discount(self, percent):
        discount_amount = self.ticket_price * (percent / 100)
        new_price = self.ticket_price - discount_amount
        if new_price < 0:
            self.ticket_price = 0.0
        else:
            self.ticket_price = new_price
        print(f"Discount applied. New price: {self.get_price_str()}")

    def __str__(self):
        return self.get_summary()
    
    def is_family_friendly(self):
        return self.rating in ["G", "PG"]
    
    def apply_student_discount(self):
        if self.ticket_price > 10.00:
            self.apply_discount(15)
        else:
            print(f"No discount available for {self.title}.")

film1 = Film("The Lighthouse", 109, "16", 14.00)
film2 = Film("Paddington", 95, "G")
film3 = Film("Dune: Part Two", 166, "12A")
print(f"{film1.title}: €{film1.ticket_price:.2f}")  # The Lighthouse: €14.00
print(f"{film2.title}: €{film2.ticket_price:.2f}")  # Paddington: €12.50
print(f"{film3.title}: €{film3.ticket_price:.2f}")  # Dune: Part Two: €12.50


# =============================================================================
# PART 3 – ADDING METHODS TO FILM  (~30 minutes)
# =============================================================================
#
# Keep the Film class from Task 2.3 and add methods to it step by step.
# After each task, add the new method(s) to the same class definition and
# re-run your tests.
# -----------------------------------------------------------------------------

# TASK 3.1 – cancel() and reopen()
#
# Add to your Film class:
#   - cancel(self): sets is_showing to False,
#       prints "X has been cancelled." where X is the title
#   - reopen(self): sets is_showing to True,
#       prints "X is showing again." where X is the title
#
# Create a Dune: Part Two instance. Print is_showing, cancel the film,
# print is_showing again, reopen it, then print is_showing one final time.
#
# ✔ CHECKPOINT – Expected output:
# True
# Dune: Part Two has been cancelled.
# False
# Dune: Part Two is showing again.
# True

# Write your code below:

print(film3.is_showing)  # True
film3.cancel()           # Dune: Part Two has been cancelled.
print(film3.is_showing)  # False
film3.reopen()           # Dune: Part Two is showing again.
print(film3.is_showing)  # True


# TASK 3.2 – get_duration_str() and get_price_str()
#
# Add two methods that return formatted strings (do not print inside them):
#   - get_duration_str(self): returns the duration as "X min"
#       e.g. "109 min"
#   - get_price_str(self): returns the ticket price formatted as "€X.XX"
#       e.g. "€14.00"
#
# Create an instance using the data below and print the result of each method.
#
#   "The Lighthouse" | 109 min | rated 16 | €14.00
#
# ✔ CHECKPOINT – Expected output:
# 109 min
# €14.00

# Write your code below:

lighthouse = Film("The Lighthouse", 109, "16", 14.00)
print(lighthouse.get_duration_str())  # 109 min
print(lighthouse.get_price_str())     # €14.00


# TASK 3.3 – get_summary() calling get_duration_str() and get_price_str()
#
# Add a method get_summary(self) that returns a single formatted string.
# It MUST call get_duration_str() and get_price_str() internally —
# do not duplicate the formatting logic.
#
# Format: "TITLE (DURATION) | Rating: RATING | Ticket: PRICE"
#
# Test using the two instances below and print the result of calling
# get_summary() on each.
#
#   "The Lighthouse" | 109 min | rated 16 | €14.00
#   "Paddington"     | 95 min  | rated G  | (use the default price)
#
# ✔ CHECKPOINT – Expected output:
# The Lighthouse (109 min) | Rating: 16 | Ticket: €14.00
# Paddington (95 min) | Rating: G | Ticket: €12.50

# Write your code below:

print(film1.get_summary())  # The Lighthouse (109 min) | Rating: 16 | Ticket: €14.00
print(film2.get_summary())  # Paddington (95 min) | Rating: G | Ticket: €12.50


# TASK 3.4 – apply_discount(percent)
#
# Add a method apply_discount(self, percent) that:
#   - Reduces ticket_price by the given percentage
#   - Prints: "Discount applied. New price: €X.XX"
#   - Does NOT allow the price to go below €0.00
#     (if it would, set it to 0.0 and then print)
#
# Create an instance using the data below. Apply a 10% discount and print
# the price. Then apply a 100% discount and print the price again.
#
#   "Dune: Part Two" | 166 min | rated 12A | €14.00
#
# ✔ CHECKPOINT – Expected output:
# Discount applied. New price: €12.60
# €12.60
# Discount applied. New price: €0.00
# €0.00

# Write your code below:

film3 = Film("Dune: Part Two", 166, "12A", 14.00)
film3.apply_discount(10)  # Discount applied. New price: €12.60
print(film3.get_price_str())  # €12.60
film3.apply_discount(100)  # Discount applied. New price: €0.00
print(film3.get_price_str())  # €0.00


# =============================================================================
# PART 4 – __str__ AND LISTS OF OBJECTS  (~20 minutes)
# =============================================================================

# TASK 4.1 – Adding __str__
#
# Add a __str__ method to your Film class that returns the same string as
# get_summary(). __str__ must CALL get_summary() — do not duplicate the logic.
#
# Test:
#   film = Film("The Lighthouse", 109, "16", 14.00)
#   print(film)      # __str__ is called automatically by print()
#
# ✔ CHECKPOINT – Expected output:
# The Lighthouse (109 min) | Rating: 16 | Ticket: €14.00

# Write your code below:

film = Film("The Lighthouse", 109, "16", 14.00)
print(film)  # The Lighthouse (109 min) | Rating: 16 | Ticket: €14.00


# TASK 4.2 – A list of Film objects
#
# Create a list called programme containing four Film instances
# using the data below:
#
#   "The Lighthouse" | 109 min | rated 16  | €14.00
#   "Paddington"     | 95 min  | rated G   | (use the default price)
#   "Dune: Part Two" | 166 min | rated 12A | (use the default price)
#   "Jaws"           | 124 min | rated PG  | €11.00
#
# Use a for loop to print each film (this will call __str__ automatically).
# Then use a second loop to print the summary of each using get_summary().
# Both loops should produce identical output.
#
# ✔ CHECKPOINT – Expected output (both loops):
# The Lighthouse (109 min) | Rating: 16 | Ticket: €14.00
# Paddington (95 min) | Rating: G | Ticket: €12.50
# Dune: Part Two (166 min) | Rating: 12A | Ticket: €12.50
# Jaws (124 min) | Rating: PG | Ticket: €11.00

# Write your code below:

programme = [
    Film("The Lighthouse", 109, "16", 14.00),
    Film("Paddington", 95, "G"),
    Film("Dune: Part Two", 166, "12A"),
    Film("Jaws", 124, "PG", 11.00)
]

for film in programme:
    print(film)  # __str__ is called automatically

for film in programme:
    print(film.get_summary())  # get_summary() is called explicitly


# TASK 4.3 – Filtering a list
#
# Using your programme list from Task 4.2:
#   (a) Print "--- All showing ---" then loop and print all showing films.
#   (b) Call cancel() on the Dune: Part Two instance.
#   (c) Print "--- Still showing ---" then loop and print only showing films.
#
# ✔ CHECKPOINT – Expected output:
# --- All showing ---
# The Lighthouse (109 min) | Rating: 16 | Ticket: €14.00
# Paddington (95 min) | Rating: G | Ticket: €12.50
# Dune: Part Two (166 min) | Rating: 12A | Ticket: €12.50
# Jaws (124 min) | Rating: PG | Ticket: €11.00
# Dune: Part Two has been cancelled.
# --- Still showing ---
# The Lighthouse (109 min) | Rating: 16 | Ticket: €14.00
# Paddington (95 min) | Rating: G | Ticket: €12.50
# Jaws (124 min) | Rating: PG | Ticket: €11.00

# Write your code below:

print("--- All showing ---")
for film in programme:
    if film.is_showing:
        print(film)
programme[2].cancel()  # Dune: Part Two has been cancelled.
print("--- Still showing ---")
for film in programme:
    if film.is_showing:
        print(film)

# =============================================================================
# PART 5 – REFACTORING: FROM A DICTIONARY AND FUNCTIONS TO A CLASS (~15 minutes)
# =============================================================================
#
# The code below uses a dictionary and standalone functions to manage a
# cinema booking. Study it carefully, then complete the tasks.
# -----------------------------------------------------------------------------

booking = {
    "customer": "Alex",
    "film": "Paddington",
    "seats": 2,
    "total": 25.00,
    "confirmed": False
}

def confirm_booking(booking):
    booking["confirmed"] = True
    return f"Booking confirmed for {booking['customer']}."

def cancel_booking(booking):
    booking["confirmed"] = False
    return f"Booking cancelled for {booking['customer']}."

def display_booking(booking):
    status = "Confirmed" if booking["confirmed"] else "Pending"
    print(f"{booking['customer']} | {booking['film']} | "
          f"{booking['seats']} seat(s) | €{booking['total']:.2f} | {status}")

# TASK 5.1 – Refactor the code above into a Booking class.
#
# Your class should include a constructor and all three methods.
# The constructor takes customer, film, seats, and total as parameters.
# confirmed should always start as False.

# Write your code below:

class Booking:
    def __init__(self, customer, film, seats, total):
        self.customer = customer
        self.film = film
        self.seats = seats
        self.total = total
        self.confirmed = False

    def confirm_booking(self):
        self.confirmed = True
        return f"Booking confirmed for {self.customer}."

    def cancel_booking(self):
        self.confirmed = False
        return f"Booking cancelled for {self.customer}."

    def display_booking(self):
        status = "Confirmed" if self.confirmed else "Pending"
        print(f"{self.customer} | {self.film} | "
              f"{self.seats} seat(s) | €{self.total:.2f} | {status}")


# TASK 5.2 – Create a Booking instance using the same data as the dictionary
# above. Call display_booking(), then confirm_booking(), then
# display_booking() again to confirm the status changed.
#
# ✔ CHECKPOINT – Expected output:
# Alex | Paddington | 2 seat(s) | €25.00 | Pending
# Booking confirmed for Alex.
# Alex | Paddington | 2 seat(s) | €25.00 | Confirmed

# Write your code below:

booking1 = Booking("Alex", "Paddington", 2, 25.00)
booking1.display_booking()          # Alex | Paddington | 2 seat(s) | €25.00 | Pending
print(booking1.confirm_booking())   # Booking confirmed for Alex.
booking1.display_booking()          # Alex | Paddington | 2 seat(s) | €25.00 | Confirmed


# =============================================================================
# PART 6 – BRINGING IT TOGETHER  (~15 minutes)
# =============================================================================
#
# Write standalone functions that work with a list of Film objects.
# These functions live OUTSIDE the class.
# Use the programme list you built in Task 4.2.
# -----------------------------------------------------------------------------

# TASK 6.1
# Write a function print_programme(films) that:
#   - Prints the header: "=== Flix Cinema — Today's Programme ==="
#   - Loops through the list and prints each film that is currently showing
#   - Prints a footer: "X film(s) showing today." where X is the count
#     of showing films (not the total list length)
#
# Before testing, cancel Dune: Part Two in your programme list.
#
# ✔ CHECKPOINT – Expected output:
# === Flix Cinema — Today's Programme ===
# The Lighthouse (109 min) | Rating: 16 | Ticket: €14.00
# Paddington (95 min) | Rating: G | Ticket: €12.50
# Jaws (124 min) | Rating: PG | Ticket: €11.00
# 3 film(s) showing today.

# Write your code below:

def print_programme(films):
    print("=== Flix Cinema — Today's Programme ===")
    count = 0
    for film in films:
        if film.is_showing:
            print(film)
            count += 1
    print(f"{count} film(s) showing today.")

programme[2].cancel()  # Dune: Part Two has been cancelled.
print_programme(programme)


# TASK 6.2
# Write a function cheapest_ticket(films) that:
#   - Returns the Film object with the lowest ticket_price
#   - Only considers films where is_showing is True
#   - Returns None if no films are showing
#
# Print the cheapest film using an f-string.
#
# ✔ CHECKPOINT – Expected output:
# Cheapest showing: Jaws (124 min) | Rating: PG | Ticket: €11.00
#
# Note how the Film object embedded in the f-string produces the full
# summary without you calling get_summary() explicitly. Python calls
# __str__ automatically whenever an object appears inside an f-string
# or is passed to print().

# Write your code below:

def cheapest_ticket(films):
    cheapest = None
    for film in films:
        if film.is_showing:
            if cheapest is None or film.ticket_price < cheapest.ticket_price:
                cheapest = film
    return cheapest

print(f"Cheapest showing: {cheapest_ticket(programme)}")  # Cheapest showing: Jaws (124 min) | Rating: PG | Ticket: €11.00


# =============================================================================
# PART 7 – EXTENSION TASKS  (if you finish early)
# =============================================================================
# No expected output is provided — test your own logic.
# -----------------------------------------------------------------------------

# TASK 7.1
# Write a function total_runtime(films) that returns the total duration
# in minutes of all SHOWING films.
# Convert the total to hours and minutes and print:
# "Total runtime: X hr Y min"

# Write your code below:

def total_runtime(films):
    total_minutes = 0
    for film in films:
        if film.is_showing:
            total_minutes += film.duration
    hours = total_minutes // 60
    minutes = total_minutes % 60
    print(f"Total runtime: {hours} hr {minutes} min")


# TASK 7.2
# Add a method is_family_friendly(self) to Film that returns True if
# the rating is "G" or "PG", False otherwise.
# Write a function family_films(films) that returns a list of Film objects
# that are both showing and family friendly.
# Print the titles of the results.

# Write your code below:

def family_films(films):
    family_friendly = []
    for film in films:
        if film.is_showing and film.is_family_friendly():
            family_friendly.append(film)
    return family_friendly

family_films_list = family_films(programme)
for film in family_films_list:
    print(film.title)


# TASK 7.3
# Add a method apply_student_discount(self) to Film that applies a fixed
# 15% discount only if ticket_price is above €10.00.
# If the price is already €10.00 or below, print:
#   "No discount available for X." (where X is the title)
# Otherwise apply the discount using apply_discount() and print the new price.
# Test on all four films in your programme list.

# Write your code below:

for film in programme:
    film.apply_student_discount()


# TASK 7.4 (challenge)
# Add a class-level attribute num_films = 0 to Film.
# Increment it inside the constructor each time a new Film is created.
# After creating your four-film programme, print Film.num_films.
# Then try: print(film1.num_films).
# Are they the same? Explain in a comment why, and describe how they could
# become different.
#
# Note: class attributes are accessed and modified using the class name
# (e.g. Film.num_films), not self. Using self inside the constructor would
# create a separate instance attribute on that object rather than updating
# the shared class-level one.

# Write your code below:

print(Film.num_films)
print(film1.num_films)

# Both print statements will output the same value because num_films is a class-level attribute shared by all instances of the Film class. It counts the total number of Film instances created. 