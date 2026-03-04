# =======================================================
# IS1111 Packages & Modules Tutorial — Exercises
# Dictionaries + Imports + __name__ Guard
# =======================================================

# -------------------------------------------------------
# QUESTION 1 — Dictionary Counter in a Module
# -------------------------------------------------------

drinks = ["Latte", "Americano", "Latte", "Espresso", "Latte", "Americano"]

# (a)
# Create a file called drink_counter.py
# Write a function:
#     count_drinks(drinks)
# It should:
#     - return a dictionary
#     - key = drink name
#     - value = how many times it appears

# (b)
# In THIS file, import ONLY the function using:
#     from drink_counter import count_drinks
# Call the function using the drinks list above.
# Print the returned dictionary.

## from drink_counter import count_drinks

## result = count_drinks(drinks)
## print(result)

# (c)
# Comment out the previous import.
# Import the whole module instead using:
#     import drink_counter
# Call the function using dot notation.
# Print the result again.

import drink_counter
result = drink_counter.count_drinks(drinks)
print(result)


# -------------------------------------------------------
# QUESTION 2 — Module with Dictionary + Top-Level Code
# -------------------------------------------------------

# (a)
# Create a file called user_logins.py
# Inside it, create this dictionary:
#     logins = {"Katie": 1, "Ben": 2, "Ciara": 1}

# (b)
# Still inside user_logins.py,
# add this TOP-LEVEL print statement:
#     print("Loading user_logins...")

# (c)
# Inside user_logins.py, write a function:
#     add_login(logins, username)
# It should:
#     - increase the count if username exists
#     - otherwise create it with value 1

# (d)
# In THIS file, import user_logins.
import user_logins

# (e)
# Call:
#     add_login(logins, "Ben")
#     add_login(logins, "David")

user_logins.add_login(user_logins.logins, "Ben")
user_logins.add_login(user_logins.logins, "David")

# (f)
# Print the updated logins dictionary.
# Run this file and observe what prints during import.

print(user_logins.logins)


# -------------------------------------------------------
# QUESTION 3 — __name__ Guard + Safe Lookup
# -------------------------------------------------------

# (a)
# Inside user_logins.py, write a function:
#     get_login_count(logins, username)
# It should:
#     - return the login count if the user exists
#     - return 0 if the user does not exist

# (b)
# Inside user_logins.py, add a test block:

#     if __name__ == "__main__":
#         # test your functions here

# In the test block:
#     - print Katie’s login count
#     - print David’s login count
#     - call add_login(logins, "Katie")
#     - print the updated dictionary

# (c)
# Run:
#     - user_logins.py directly
#     - this file
# Observe the difference in output.



# -------------------------------------------------------
# QUESTION 4 — Nested Dictionary + Separation of Concerns
# -------------------------------------------------------

# (a)
# Create employee_data.py
# It should ONLY contain this dictionary (no prints, no functions):

employees = {
    "E001": {"name": "Sarah", "dept": "Sales", "salary": 45000},
    "E002": {"name": "Cian", "dept": "IT", "salary": 52000},
    "E003": {"name": "Aoife", "dept": "Sales", "salary": 48000},
    "E004": {"name": "Ben", "dept": "IT", "salary": 47000},
}

# (b)
# Create employee_utils.py
# It should contain ONLY functions (no prints, no running code):
#
# Write:
#     get_salary(employees, emp_id)
#         - return salary if employee exists
#         - return None otherwise
#
# Write:
#     increase_salary(employees, emp_id, amount)
#         - increase salary if employee exists
#         - return True if updated
#         - return False otherwise

# (c)
# In THIS file, import:
#     - employees from employee_data
#     - both functions from employee_utils

from employee_data import employees
from employee_utils import get_salary, increase_salary

# (d)
# Print the salary for "E002".
print(get_salary(employees, "E002"))

# (e)
# Print the salary for "E999".
# It should not crash.
print(get_salary(employees, "E999"))

# (f)
# Increase Ben’s salary by 3000.
increase_salary(employees, "E004", 3000)

# (g)
# Print Ben’s updated salary.
print(get_salary(employees, "E004"))
