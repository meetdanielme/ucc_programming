# budget_tracker_v2.py
# Author: Daniel Marcinkowski
# ID: 125701129
# Date: 2025-10-11
# Description: "A simple CLI-based budget tracker."

# Prompting user for input — their weekly income and expenses in various categories.

## Input validation — no negative numbers, only numeric values 

try:
    income = float(input("What's your weekly income? (in €)\n"))
except:
    print("Invalid input! Please enter a number.")
    income = 0.0
try:
    rent = float(input("How much you spend on **rent** weekly? (in €)\n"))
except:
    print("Invalid input! Please enter a number.")
    rent = 0.0
try:
    groceries = float(input("How much you spend on **groceries** weekly? (in €)\n"))
except:
    print("Invalid input! Please enter a number.")
    groceries = 0.0
try:
    transport = float(input("How much you spend on **transport** weekly? (in €)\n"))
except:
    print("Invalid input! Please enter a number.")
    transport = 0.0
try:
    entertainment = float(input("How much you spend on **entertainment** weekly? (in €)\n"))
except:
    print("Invalid input! Please enter a number.")
    entertainment = 0.0

# Processing the inputs from the user to calculate their total weekly expenses and how much money they will have left.

total_expenses = rent + groceries + transport + entertainment
money_left = income - total_expenses

# Printing the results showing income vs expenses

print("\n===OVERVIEW===\n")
print("Weekly Income:", income, "€")
print("Total Expenses:", total_expenses, "€")
print("Money Left:", money_left, "€")

# Determine budget status (surplus/deficit/balanced)

print("\n===TIPS===\n")
if money_left == 0:
    print("You don't have any money left!")
elif money_left < 0:
    money_left = money_left * -1
    print("You're overspending! Cut your expenses by", money_left, "€ next week." )
elif money_left > 50:
    print("Good job saving! You saved", money_left, "€")
else:
    print("You should probably save a bit more next week.")
