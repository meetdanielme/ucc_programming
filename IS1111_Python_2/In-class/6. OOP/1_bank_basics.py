# =============================================================================
# SESSION 1 – OOP BASICS: Objects, Classes & Instances
# Thursday 5 March 2026 | Slides 1–32
# Bank Domain
# =============================================================================


# =============================================================================
# PART A: Everything in Python is an object
# =============================================================================
#
# NARRATIVE
# ---------
# The slides describe OOP as a way of thinking about programs as collections
# of cooperating objects rather than lists of instructions. But here is the
# key point for Python specifically (slide 9): you have been using objects
# all along.
#
# Every value in Python — a string, an integer, a list — is an object. It has
# a type (what kind of thing it is) and a set of methods (what it can do).
# Two functions let us inspect any object at runtime:
#
#   type(obj)  → tells us which class the object belongs to
#   dir(obj)   → lists all the attributes and methods available on it
#
# Run the code below and look at the output carefully.
# For dir(), ignore entries that start with __ — those are used internally
# by Python (slide 30). Focus on the plain names at the end of the list.
# You will recognise most of them.
# =============================================================================

owner = "Aoife"
balance = 500.0
transactions = [100.0, -50.0, 200.0]

print("--- type() ---")
print(type(owner))         # <class 'str'>
print(type(balance))       # <class 'float'>
print(type(transactions))  # <class 'list'>

print("\n--- dir() on a string ---")
print(dir(owner))
# upper, lower, replace... — the str methods you already use every day.
# They belong to the str CLASS. Every string is an INSTANCE of str.

print("\n--- dir() on a list ---")
print(dir(transactions))
# append, remove, sort... — the list methods you already use.
# Every list is an INSTANCE of list.

# >>> PAUSE AND DISCUSS
# When you write transactions.append(300.0), you are calling the append METHOD
# on a list OBJECT. That is OOP. The question is simply: can we define
# our own classes, with our own attributes and methods? Yes — that is what
# the rest of this topic is about.


# =============================================================================
# PART B: Defining a class and creating instances
# =============================================================================
#
# NARRATIVE
# ---------
# A class is a template (slides 12, 15 — the cookie cutter analogy).
# From one template you can create as many objects (instances) as you like.
# Each instance is independent: changing one does not affect the others.
#
# The simplest possible class has just a class-level attribute and a method.
# No constructor yet — we will add that in Session 2.
#
# Syntax (slide 23):
#   class ClassName:
#       indented list of methods and attributes
#
# Methods are defined like functions but always take self as their first
# parameter (slide 24). self refers to the specific instance the method
# is being called on — it is how the method knows which object's data to use.
#
# Common misconception: students sometimes think self needs to be passed
# explicitly when calling a method. It does not — Python passes it
# automatically. If you define def describe(self) and call account.describe(),
# Python handles self = account behind the scenes.
# =============================================================================

class BankAccount:
    status = "active"      # class-level attribute: shared by all instances initially

    def freeze(self):
        self.status = "frozen"
        print("Account frozen.")

    def describe(self):
        print(f"This account is {self.status}.")


# Creating instances from the class (slide 35 syntax pattern)
account_1 = BankAccount()
account_2 = BankAccount()

print("\n--- Two independent instances ---")
account_1.describe()        # This account is active.
account_2.describe()        # This account is active.

account_1.freeze()          # Only account_1 is affected
account_1.describe()        # This account is frozen.
account_2.describe()        # This account is active.  ← unchanged

# >>> PAUSE AND DISCUSS
# account_1 and account_2 were made from the same template, but they are
# independent. This is the cookie cutter analogy from slide 15: the cutter
# (class) is unchanged no matter how many cookies (instances) you stamp out.

print("\n--- type() and dir() on our own class ---")
print(type(account_1))      # <class '__main__.BankAccount'>
print(type(account_2))      # <class '__main__.BankAccount'>
print("\ndir(account1):", [m for m in dir(account_1) if not m.startswith("__")])
# Shows: describe, freeze, status

# >>> PAUSE AND DISCUSS
# Just like str and list have their own dir() entries, so does our BankAccount.
# describe and freeze appear because we defined them.
# This confirms that user-defined classes behave exactly like built-in ones.


# =============================================================================
# PART C: YOUR TASKS
# =============================================================================
# Work through the tasks below. Run your code after each one.
# Answer the poll question before moving to the next task.
# -----------------------------------------------------------------------------

# TASK 1
# Use type() and dir() to inspect the following objects.
# For each, identify two methods from dir() that you have used before.
#
name = "Murphy's General Store"
amount = 1250.50
history = {"name": "Aoife", "balance": 500.0}
#
# Write your code below:

print(type(name))
print(type(amount))
print(type(history))
print("\ndir(name):", [m for m in dir(name) if not m.startswith("__")]) # upper, lower, replace... — the str methods you already use every day.
print("\ndir(amount):", [m for m in dir(amount) if not m.startswith("__")]) # is_integer, as_integer_ratio... — the float methods you have used before.
print("\ndir(history):", [m for m in dir(history) if not m.startswith("__")]) # keys, values... — the dict methods you have used before.

# TASK 2
# Define a class called Wallet with:
#   - A class-level attribute: currency = "EUR"
#   - A method describe(self) that prints: "This wallet holds X currency."
#     where X is replaced with the value of currency.
#   - A method open(self) that prints: "Opening wallet."
#
# Then:
#   - Create two Wallet instances called wallet1 and wallet2.
#   - Call describe() and open() on both.
#   - Use type() to confirm both are instances of Wallet.
#   - Use dir() to list the methods of wallet1 (filter out dunder methods).
#
# Write your code below:

class Wallet:
    currency = "EUR"

    def describe(self):
        print(f"This wallet holds {self.currency} currency.")

    def open(self):
        print("Opening wallet.")

wallet1 = Wallet()
wallet2 = Wallet()

wallet1.describe()
wallet2.describe()
wallet1.open()
wallet2.open()

print(type(wallet1))
print(type(wallet2))
print("\ndir(wallet1):", [m for m in dir(wallet1) if not m.startswith("__")])

# TASK 3
# Add a class-level attribute is_locked = False to your Wallet class.
# Add a method lock(self) that sets is_locked to True
# and prints: "Wallet locked."
# Add a method unlock(self) that sets is_locked to False
# and prints: "Wallet unlocked."
#
# Create two wallets. Lock one. Confirm the other is still unlocked.
#
# Write your code below:

class Wallet:
    currency = "EUR"
    is_locked = False

    def describe(self):
        print(f"This wallet holds {self.currency} currency.")

    def open(self):
        print("Opening wallet.")

    def lock(self):
        self.is_locked = True
        print("Wallet locked.")

    def unlock(self):
        self.is_locked = False
        print("Wallet unlocked.")

wallet1 = Wallet()
wallet2 = Wallet()
wallet1.lock()
print(f"wallet1 is_locked: {wallet1.is_locked}")  # True
print(f"wallet2 is_locked: {wallet2.is_locked}")  # False


# TASK 4 (extension)
# Create an instance of your Wallet class.
# Then assign a new attribute directly on that instance:
#   my_wallet.owner = "Alex"
# Print my_wallet.owner.
# Now try printing wallet_1.owner (a different instance that has no owner set).
# What happens? Why?
#
# Write your code and explain the result in a comment:

my_wallet = Wallet()
my_wallet.owner = "Alex"
print(my_wallet.owner)  # Alex
# print(wallet1.owner)    # AttributeError: 'Wallet' object has no attribute 'owner'
# Explanation: When we assign my_wallet.owner = "Alex", we are creating a new attribute called owner on the my_wallet instance. This does not affect wallet1 or any other instance of Wallet, which do not have an owner attribute defined. Therefore, when we try to access wallet1.owner, we get an AttributeError because that attribute does not exist for wallet1. Each instance can have its own attributes that are independent of other instances.