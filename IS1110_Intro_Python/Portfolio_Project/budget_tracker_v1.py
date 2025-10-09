# budget_tracker_v1.py
# Author: Daniel Marcinkowski
# ID: 125701129
# Date: 2025-10-06
# Description: "A simple CLI-based budget tracker."

# Prompting user for input — their weekly income and expenses in various categories.

income = float(input("What's your weekly income? (in €)\n"))
rent = float(input("How much you spend on **rent** weekly? (in €)\n"))
groceries = float(input("How much you spend on **groceries** weekly? (in €)\n"))
transport = float(input("How much you spend on **transport** weekly? (in €)\n"))
entertainment = float(input("How much you spend on **entertainment** weekly? (in €)\n"))

# Processing the inputs from the user to calculate their total weekly expenses and how much money they will have left.

total_expenses = rent + groceries + transport + entertainment
money_left = income - total_expenses

# Printing the results showing income vs expenses

print("Weekly Income:", income, "€")
print("Total Expenses:", total_expenses, "€")
print("Money Left:", money_left, "€")
