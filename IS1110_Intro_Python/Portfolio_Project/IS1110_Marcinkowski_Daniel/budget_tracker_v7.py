# budget_tracker_v7.py
# Author: Daniel Marcinkowski
# ID: 125701129
# Date: 2025-11-20
# Description: "Complete Budget System (Version 7.0)"
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

# python
from datetime import date

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
    return f"€{x:,.2f}"

def analyse_status(money_left):
    """determines budget status and provides recommendations"""
    if money_left == 0:
        print("You don't have any money left.")
    elif money_left < 0:
        print("You're overspending! Next week, you should cut your expenses by", euro(abs(money_left)))
    elif money_left > 50:
        print("Good job saving! You saved", euro(money_left))
    else:
        print("You should probably save a bit more next week.")

def print_box_header(title):
    """Print a simple boxed header with today's date."""
    width = 40
    today = date.today()
    print("\n" + "╔" + "═" * width + "╗")
    print(f"║{title:^{width}}║")
    print(f"║{'Date: ' + str(today):^{width}}║")
    print("╚" + "═" * width + "╝")

def show_results(income, rent, food, transport, entertainment, total_expenses, money_left,
                 rent_desc="", food_desc="", transport_desc="", entertainment_desc="", week_number=None):
    """displays formatted budget report"""
    if week_number is not None:
        print_box_header(f"Week {week_number} Budget Report")
    else:
        print_box_header("Budget Overview")

    print("\nSummary")
    print("-" * 45)
    print(f"{'Weekly Income':<20}{euro(income):>15}")
    print(f"{'Total Expenses':<20}{euro(total_expenses):>15}")
    print(f"{'Money Left':<20}{euro(money_left):>15}")

    print("\nDetails by Category")
    print("-" * 70)
    print(f"{'Category':<15}{'Amount':>15}{'Description':>40}")
    print("-" * 70)
    print(f"{'Rent':<15}{euro(rent):>15}{rent_desc:>40}")
    print(f"{'Groceries':<15}{euro(food):>15}{food_desc:>40}")
    print(f"{'Transport':<15}{euro(transport):>15}{transport_desc:>40}")
    print(f"{'Entertainment':<15}{euro(entertainment):>15}{entertainment_desc:>40}")
    print("-" * 70)

    print("\nStatus")
    print("-" * 45)
    analyse_status(money_left)

def compute_average(values):
    return sum(values) / len(values) if values else 0.0

def show_all_weeks_summary(weekly_incomes, weekly_expenses):
    if not weekly_incomes:
        print("No weeks recorded yet.")
        return
    print_box_header("All Weeks Summary")
    print(f"{'Week':<6}{'Income':>12}{'Expenses':>12}{'Balance':>12}")
    print("-" * 42)
    for idx, (inc, exp) in enumerate(zip(weekly_incomes, weekly_expenses), start=1):
        print(f"{idx:<6}{euro(inc):>12}{euro(exp):>12}{euro(inc - exp):>12}")

def identify_best_worst_weeks(weekly_expenses):
    max_expense = max(weekly_expenses)
    min_expense = min(weekly_expenses)
    worst_week = weekly_expenses.index(max_expense) + 1
    best_week = weekly_expenses.index(min_expense) + 1
    return best_week, min_expense, worst_week, max_expense

def show_best_worst_weeks(weekly_expenses):
    if not weekly_expenses:
        print("No weeks recorded yet.")
        return
    best_week, min_expense, worst_week, max_expense = identify_best_worst_weeks(weekly_expenses)
    print_box_header("Best & Worst Weeks")
    print(f"Best (lowest spending): Week {best_week} with expenses of {euro(min_expense)}")
    print(f"Worst (highest spending): Week {worst_week} with expenses of {euro(max_expense)}")

def print_complete_report(weekly_incomes, weekly_expenses, weekly_rent, weekly_food, weekly_transport, weekly_entertainment):
    if not weekly_incomes:
        print("No weeks recorded yet.")
        return

    total_income = sum(weekly_incomes)
    total_expenses = sum(weekly_expenses)
    avg_income = compute_average(weekly_incomes)
    avg_expenses = compute_average(weekly_expenses)
    best_week, min_expense, worst_week, max_expense = identify_best_worst_weeks(weekly_expenses)

    print_box_header("Complete Budget Report")
    header = f"{'Week':<6}{'Income':>12}{'Expenses':>12}{'Balance':>12}{'Rent':>12}{'Food':>12}{'Transport':>12}{'Ent.':>12}"
    print(header)
    print("-" * len(header))
    for idx in range(len(weekly_incomes)):
        income = weekly_incomes[idx]
        expense = weekly_expenses[idx]
        balance = income - expense
        print(f"{idx + 1:<6}{euro(income):>12}{euro(expense):>12}{euro(balance):>12}"
              f"{euro(weekly_rent[idx]):>12}{euro(weekly_food[idx]):>12}"
              f"{euro(weekly_transport[idx]):>12}{euro(weekly_entertainment[idx]):>12}")
    print("-" * len(header))
    print(f"{'Totals':<6}{euro(total_income):>12}{euro(total_expenses):>12}{euro(total_income - total_expenses):>12}")
    print(f"{'Averages':<6}{euro(avg_income):>12}{euro(avg_expenses):>12}{euro(avg_income - avg_expenses):>12}")
    print(f"\nBest Week: Week {best_week} ({euro(min_expense)} in expenses)")
    print(f"Worst Week: Week {worst_week} ({euro(max_expense)} in expenses)")

def get_menu_choice():
    """Show menu and return 1-5"""
    while True:
        print("\n=== MENU ===")
        print("1) Add This Week's Budget")
        print("2) Show All Weeks Summary")
        print("3) Find Best/Worst Week")
        print("4) Show Complete Report")
        print("5) Exit")
        choice = input("Choose 1-5: ")
        if choice in ("1", "2", "3", "4", "5"):
            return int(choice)
        print("Please enter a number between 1 and 5.")

def add_week_flow(week_number):
    """One interaction to add a week."""
    income, rent, food, transport, entertainment, rent_desc, food_desc, transport_desc, entertainment_desc = get_user_input()
    total_expenses, money_left = calculate_budget(income, rent, food, transport, entertainment)
    show_results(income, rent, food, transport, entertainment,
                 total_expenses, money_left,
                 rent_desc, food_desc, transport_desc, entertainment_desc,
                 week_number)
    return income, total_expenses, rent, food, transport, entertainment

def print_welcome():
    """Display welcome text and usage instructions."""
    print_box_header("Welcome to the Budget Management System")
    print(
        "Track weekly income and expenses, compare weeks, and review your best and worst spending.\n"
        "Use the menu to add data, view summaries, and generate reports. Invalid numbers are rejected."
    )

def main():
    """main programme function"""
    print_welcome()
    week_count = 0
    weekly_incomes = []
    weekly_expenses = []
    weekly_rent = []
    weekly_food = []
    weekly_transport = []
    weekly_entertainment = []

    while True:
        choice = get_menu_choice()

        if choice == 1:
            week_count += 1
            this_income, this_expenses, this_rent, this_food, this_transport, this_entertainment = add_week_flow(week_count)

            weekly_incomes.append(this_income)
            weekly_expenses.append(this_expenses)
            weekly_rent.append(this_rent)
            weekly_food.append(this_food)
            weekly_transport.append(this_transport)
            weekly_entertainment.append(this_entertainment)

            avg_inc = compute_average(weekly_incomes)
            avg_exp = compute_average(weekly_expenses)

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
            show_all_weeks_summary(weekly_incomes, weekly_expenses)
            input("\n(Press Enter to return to the menu)")

        elif choice == 3:
            show_best_worst_weeks(weekly_expenses)
            input("\n(Press Enter to return to the menu)")

        elif choice == 4:
            print_complete_report(weekly_incomes, weekly_expenses, weekly_rent, weekly_food, weekly_transport, weekly_entertainment)
            input("\n(Press Enter to return to the menu)")

        elif choice == 5:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
