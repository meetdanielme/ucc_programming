# budget_tracker_v5.py
# Author: Daniel Marcinkowski
# ID: 125701129
# Date: 2025-11-14
# Description: "Improved Budget Categories (Version 5.0)"
# ---------------------------------------------------------------------
# REFERENCES & ACKNOWLEDGEMENT OF AI USE
# ---------------------------------------------------------------------
# This code was developed as part of the IS1110 Introduction to Programming for BIS 1
# module at University College Cork (2025–2026), using PyCharm IDE.
#
# Reference materials consulted:
# - Seppälä, S. (2025). IS1110 Lecture Slides: Introduction to Computers, Programming & Python.
# - Hunt, J. (2020). *A Beginner’s Guide to Python 3 Programming.* Springer Nature Switzerland AG.
# - Severance, C. (2016). *Python for Everybody: Exploring Data in Python 3.* PY4E.
# - Smithsonian Institution (2018). *Best Practices for File Naming and Organizing.*
# - Python Software Foundation (2024). *Python 3.12 Documentation.*
#
# ---------------------------------------------------------------------
# AI TOOL USAGE STATEMENT
# ---------------------------------------------------------------------
# I acknowledge the use of ChatGPT (GPT-5, OpenAI, https://chat.openai.com)
# and PyCharm’s built-in code completion features for minor guidance during the
# development of this project.
#
# Purpose of AI assistance:
# - To receive step-by-step guidance on implementing input validation and conditional logic.
# - To clarify Python syntax and structure while writing modular functions.
# - To debug and improve readability of code comments and docstrings.
#
# Example Prompts Used:
# - “Add input validation using try and except to handle non-numeric or negative values.”
# - “How should I structure my budget calculator into reusable functions?”
# - “Explain how to return multiple values from a Python function.”
#
# Evaluation & Adaptation:
# The AI’s output was critically reviewed and edited for correctness, simplicity,
# and compliance with IS1110 assessment requirements. Only explanatory and syntactic
# guidance was used — no full code segments were copied verbatim.
#
# ---------------------------------------------------------------------
# Citation Style References:
# University of Arkansas Libraries. (2024). *Citing Programming Code.*
# https://libguides.uark.edu/friendly.php?s=CSCE/CitingCode
#
# Massachusetts Institute of Technology. (2024). *Academic Integrity at MIT: Writing Code.*
# https://integrity.mit.edu/handbook/writing-code
# ---------------------------------------------------------------------

def get_positive_float(prompt):
    """Validates input and returns positive float — keep asking until the value entered is >= 0"""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a number that is 0 or greater.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a number like 123.45")

def get_user_input():
    """gets all budget input from user with validation"""
    income = get_positive_float("What's your weekly income? (in €)\n")
    rent = get_positive_float("How much you spend on rent weekly? (in €)\n")
    rent_desc = input("Rent description (optional): ").strip().title()
    food = get_positive_float("How much you spend on food weekly? (in €)\n")
    food_desc = input("Food description (optional): ").strip().title()
    transport = get_positive_float("How much you spend on transport weekly? (in €)\n")
    transport_desc = input("Transport description (optional): ").strip().title()
    entertainment = get_positive_float("How much you spend on entertainment weekly? (in €)\n")
    entertainment_desc = input("Entertainment description (optional): ").strip().title()
    return income, rent, food, transport, entertainment, rent_desc, food_desc, transport_desc, entertainment_desc

def calculate_budget(income, rent, food, transport, entertainment):
    """calculates total expenses and money remaining"""
    total_expenses = rent + food + transport + entertainment
    money_left = income - total_expenses
    return total_expenses, money_left

def euro(x):
    """Format numbers as Euro currency with two decimals — suggested by ChatGPT"""
    return f"€{x:.2f}"

def analyse_status(money_left):
    """determines budget status and provides recommendations"""
    if money_left == 0:
        print("You don't have any money left.")
    elif money_left < 0:
        print("You're overspending! Next week, you should cut your expenses by", euro(abs(money_left))) # the use of `abs` was suggested by ChatGPT
    elif money_left > 50:
        print("Good job saving! You saved", euro(money_left))
    else:
        print("You should probably save a bit more next week.")

def show_results(income, rent, food, transport, entertainment, total_expenses, money_left,
                 rent_desc="", food_desc="", transport_desc="", entertainment_desc="", week_number=None):
    """displays formatted budget report"""
    if week_number is not None:
        print(f"\n=== Week {week_number} Budget Details ===\n")
    else:
        print("\n=== OVERVIEW ===\n")
    print("Weekly Income:", euro(income))
    print("Total Expenses:", euro(total_expenses))
    print("Money Left:", euro(money_left))
    print("\n=== SPEND ===\n")
    print(f"Rent: {euro(rent)} - {rent_desc}")
    print(f"Groceries: {euro(food)} - {food_desc}")
    print(f"Transport: {euro(transport)} - {transport_desc}")
    print(f"Entertainment: {euro(entertainment)} - {entertainment_desc}")
    print("\n=== TIPS ===\n")
    analyse_status(money_left)

def get_menu_choice():
    """Show menu and return 1, 2, or 3"""
    while True:
        print("\n=== MENU ===")
        print("1) Add This Week's Budget")
        print("2) Show Overall Summary")
        print("3) Exit")
        choice = input("Choose 1-3: ") #
        if choice in ("1", "2", "3"):
            return int(choice)
        print("Please enter 1, 2, or 3.")

def add_week_flow(week_number):
    """One interaction to add a week. Returns (this_income, this_expenses)."""
    income, rent, food, transport, entertainment, rent_desc, food_desc, transport_desc, entertainment_desc = get_user_input()
    total_expenses, money_left = calculate_budget(income, rent, food, transport, entertainment)
    show_results(income, rent, food, transport, entertainment,
                 total_expenses, money_left,
                 rent_desc, food_desc, transport_desc, entertainment_desc,
                 week_number)
    return income, total_expenses

def compute_averages(week_count, total_income, total_expenses):
    if week_count == 0:
        return 0.0, 0.0
    return total_income / week_count, total_expenses / week_count

def main():
    """main programme function"""
    week_count = 0
    total_income = 0.0
    total_expenses = 0.0

    while True:
        choice = get_menu_choice()

        if choice == 1:
            # Add This Week’s Budget
            week_count += 1
            this_income, this_expenses = add_week_flow(week_count)

            total_income += this_income
            total_expenses += this_expenses

            avg_inc, avg_exp = compute_averages(week_count, total_income, total_expenses)

            print(f"\n=== Week {week_count} Added ===")
            print(f"This week's income: {euro(this_income)}")
            print(f"This week's expenses: {euro(this_expenses)}")
            print(f"Average weekly income so far: {euro(avg_inc)}")
            print(f"Average weekly expenses so far: {euro(avg_exp)}")

            inc_cmp = "↑ above" if this_income > avg_inc else ("↓ below" if this_income < avg_inc else "＝ equal to")
            exp_cmp = "↑ above" if this_expenses > avg_exp else ("↓ below" if this_expenses < avg_exp else "＝ equal to")
            print(f"(Income this week is {inc_cmp} the average.)")
            print(f"(Expenses this week are {exp_cmp} the average.)")

        elif choice == 2:
            # Show Overall Summary
            avg_inc, avg_exp = compute_averages(week_count, total_income, total_expenses)
            print("\n=== OVERALL SUMMARY ===")
            print(f"Weeks entered: {week_count}")
            print(f"Total income: {euro(total_income)}")
            print(f"Total expenses: {euro(total_expenses)}")
            print(f"Average weekly income: {euro(avg_inc)}")
            print(f"Average weekly expenses: {euro(avg_exp)}")
            input("\n(Press Enter to return to the menu)")

        elif choice == 3:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()