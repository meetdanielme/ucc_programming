# =============================================================================
# SESSION 2 – CREATING CLASSES & OBJECTS
# Monday 9 March 2026 (demo) + Thursday 12 March 2026 (exercise)
# Slides 33–52
# Bank Domain
# =============================================================================


# =============================================================================
# PART A: The constructor — __init__
# =============================================================================
#
# NARRATIVE
# ---------
# In Session 1 our class had no constructor, so we had to set attributes
# manually after creating an object. That is clunky and error-prone.
#
# The constructor (slide 39) is a special method called __init__ that runs
# automatically the moment an object is created. Its job is to set the
# object's initial state — the values it starts with.
#
# We will build the BankAccount class in three steps, matching the slide
# progression (slides 42–44):
#   Step 1: __init__ with no parameters → set attributes manually afterwards
#   Step 2: __init__ with parameters    → pass values at creation time
#   Step 3: __init__ with default values → some parameters become optional
#
# Important: the self parameter in __init__ works exactly as in any other
# method — Python passes it automatically and it refers to the new object
# being constructed.
# =============================================================================

# ------------------------------------------------------------------
# Step 1: __init__ with no parameters (slide 42 pattern)
# ------------------------------------------------------------------

class BankAccount:
    def __init__(self): # constructor with no parameters other than self
        self.owner = ""
        self.balance = 0.0

a = BankAccount()
a.owner = "Aoife"
a.balance = 500.0
print(a.owner, a.balance)      # Aoife 500.0

# This works but it is inconvenient — we have to set every attribute
# separately after creating the object. Steps 2 and 3 fix this.


# ------------------------------------------------------------------
# Step 2: __init__ with parameters (slide 43 pattern)
# ------------------------------------------------------------------

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

a1 = BankAccount("Aoife", 500.0)
a2 = BankAccount("Brian", 1200.0)
print(a1.owner, a1.balance)    # Aoife 500.0
print(a2.owner, a2.balance)    # Brian 1200.0

# >>> PAUSE AND DISCUSS
# Two independent instances — depositing into a1 does not affect a2.
# This is the "many instances" concept from slide 51.


# ------------------------------------------------------------------
# Step 3: Default parameter values (slide 44 pattern)
# ------------------------------------------------------------------

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

a1 = BankAccount("Aoife", 500.0)   # balance provided
a2 = BankAccount("Brian")          # balance defaults to 0.0
print(a1.balance)    # 500.0
print(a2.balance)    # 0.0


# =============================================================================
# PART B: Methods — including a method calling another method
# =============================================================================
#
# NARRATIVE
# ---------
# Methods are functions defined inside a class (slides 45–47). They always
# take self as their first parameter, which gives them access to the object's
# attributes and other methods.
#
# A method can call another method on the same object using self.method_name()
# (slide 46). This avoids duplicating logic — if the logic needs to change,
# you only update it in one place.
#
# The __str__ method (shown in the Card example on slide 50) is called
# automatically by print(). It should return a string — not print one.
# This is a common mistake: returning vs printing inside __str__.
#
# Common misconception: forgetting the self parameter in a method definition.
# Python's error message for this (slide 48) is confusing — it says the method
# "takes 1 positional argument but 2 were given" because Python is counting
# self as an argument you forgot to declare.
# =============================================================================

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited €{amount:.2f}. New balance: €{self.balance:.2f}.")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrew €{amount:.2f}. New balance: €{self.balance:.2f}.")

    def get_balance_str(self):
        # Returns a formatted string — does not print.
        return f"€{self.balance:.2f}"

    def get_summary(self):
        # Calls get_balance_str() rather than duplicating the formatting.
        return f"Account holder: {self.owner} | Balance: {self.get_balance_str()}"

    def __str__(self):
        # Called automatically by print(obj). Must return a string.
        return f"BankAccount({self.owner}, {self.get_balance_str()})"


a = BankAccount("Aoife", 500.0)
print(a)                       # BankAccount(Aoife, €500.00)
a.deposit(200.0)               # Deposited €200.00. New balance: €700.00.
print(a.get_summary())         # Account holder: Aoife | Balance: €700.00
a.withdraw(50.0)               # Withdrew €50.00. New balance: €650.00.
print(a)                       # BankAccount(Aoife, €650.00)

# >>> PAUSE AND DISCUSS
# get_summary() calls get_balance_str() internally. If the balance format ever
# changes (e.g. we want to add a currency symbol or change decimal places),
# we update get_balance_str() once and get_summary() reflects the change.


# =============================================================================
# PART C: YOUR TASKS
# =============================================================================
# Implement the BankAccount class from scratch following the steps below.
# Do not copy the demo above — write your own version.
# Run your code after each task, then answer the poll question.
# -----------------------------------------------------------------------------

# TASK 1
# Define a BankAccount class with __init__(self, owner, balance=0.0).
# Create two instances with different owners and balances.
# Print the owner and balance of each directly (e.g. a1.owner).

# Write your code below:

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited €{amount:.2f}. New balance: €{self.balance:.2f}.")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrew €{amount:.2f}. New balance: €{self.balance:.2f}.")

    def get_balance_str(self):
        return f"€{self.balance:.2f}"
    
    def get_summary(self):
        return f"{self.owner} | Balance: {self.get_balance_str()}"
    
    def __str__(self):
        return f"BankAccount({self.owner}, {self.get_balance_str()})"
    
    def is_empty(self):
        return self.balance <= 0.0

a1 = BankAccount("Aoife", 300.0)
a2 = BankAccount("Brian", 500.0)
print(a1.owner, a1.balance)    # Aoife 300.0
print(a2.owner, a2.balance)    # Brian 500.0


# TASK 2
# Add a method deposit(self, amount) that increases balance by amount
# and prints: "Deposited €X.XX. New balance: €X.XX."
# Add a method withdraw(self, amount) that decreases balance by amount
# and prints: "Withdrew €X.XX. New balance: €X.XX."
#
# Test: create an account with €300.00, deposit €150.00, withdraw €80.00.
# Expected final balance: €370.00.

# Write your code below:

a = BankAccount("Aoife", 300.0)
a.deposit(150.0)              # Deposited €150.00. New balance: €450.00.
a.withdraw(80.0)              # Withdrew €80.00. New balance: €370.00.


# TASK 3
# Add a method get_balance_str(self) that returns the balance as a formatted
# Euro string, e.g. "€370.00".
# Add a method get_summary(self) that returns a string combining the owner's
# name and the result of get_balance_str(). get_summary must call
# get_balance_str() — do not duplicate the formatting logic.
# Example return value: "Aoife | Balance: €370.00"
#
# Print the summary for each of your two accounts.

# Write your code below:

print(a1.get_summary())        # Aoife | Balance: €300.00
print(a2.get_summary())        # Brian | Balance: €500.00


# TASK 4
# Add a __str__ method that returns a single formatted string describing
# the account. Example: "BankAccount(Aoife, €370.00)"
# Confirm that print(my_account) uses __str__ automatically.

# Write your code below:

print(a1)                       # BankAccount(Aoife, €300.00)
print(a2)                       # BankAccount(Brian, €500.00)

# TASK 5
# Create a list of three BankAccount instances with different owners
# and starting balances.
# Use a for loop to print each account and call get_summary() on it.

# Write your code below:

accounts = [
    BankAccount("Aoife", 300.0),
    BankAccount("Brian", 500.0),
    BankAccount("Cait", 1000.0)
]

for account in accounts:
    print(account)
    print(account.get_summary())


# TASK 6 (extension)
# Add a method is_empty(self) that returns True if balance is 0.0 or less,
# False otherwise.
# Loop through your list of accounts and print only those with a positive
# balance.

# Write your code below:
for account in accounts:
    if not account.is_empty():
        print(account)