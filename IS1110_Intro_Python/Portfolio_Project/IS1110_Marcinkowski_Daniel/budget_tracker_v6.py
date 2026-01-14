# budget_tracker_v6.py
# Author: Daniel Marcinkowski
# ID: 125701129
# Date: 2025-11-14
# Description: "Professional Budget Reports (Version 6.0)"
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
        print("You're overspending! Next week, you should cut your expenses by", euro(abs(money_left))) # the use of `abs` was suggested by ChatGPT
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
    """One interaction to add a week. Returns (this_income, this_expenses, rent, food, transport, entertainment)."""
    income, rent, food, transport, entertainment, rent_desc, food_desc, transport_desc, entertainment_desc = get_user_input()
    total_expenses, money_left = calculate_budget(income, rent, food, transport, entertainment)
    show_results(income, rent, food, transport, entertainment,
                 total_expenses, money_left,
                 rent_desc, food_desc, transport_desc, entertainment_desc,
                 week_number)
    return income, total_expenses, rent, food, transport, entertainment

def compute_averages(week_count, total_income, total_expenses):
    if week_count == 0:
        return 0.0, 0.0
    return total_income / week_count, total_expenses / week_count

def print_summary_report(week_count, total_income, total_expenses, total_rent, total_food, total_transport, total_entertainment):
    if week_count == 0:
        print("No data to summarise yet.")
        return

    avg_income, avg_expenses = compute_averages(week_count, total_income, total_expenses)
    avg_rent = total_rent / week_count
    avg_food = total_food / week_count
    avg_transport = total_transport / week_count
    avg_entertainment = total_entertainment / week_count

    if avg_income > 0:
        rent_percent = (avg_rent / avg_income) * 100
        food_percent = (avg_food / avg_income) * 100
        transport_percent = (avg_transport / avg_income) * 100
        entertainment_percent = (avg_entertainment / avg_income) * 100
        exp_percent = (avg_expenses / avg_income) * 100
        avg_remaining = avg_income - avg_expenses
        remaining_percent = (avg_remaining / avg_income) * 100
    else:
        rent_percent = food_percent = transport_percent = entertainment_percent = exp_percent = remaining_percent = 0.0
        avg_remaining = 0.0

    print_box_header("BUDGET SUMMARY REPORT")

    print(f"\nTotal Weeks Tracked: {week_count}")
    print("─" * 41)
    print(f"{'Category':<15}{'Average':>12}{'% of Income':>14}")
    print("─" * 41)
    print(f"{'Income':<15}{euro(avg_income):>12}{100.0:>14.1f}%")
    print(f"{'Rent':<15}{euro(avg_rent):>12}{rent_percent:>14.1f}%")
    print(f"{'Groceries':<15}{euro(avg_food):>12}{food_percent:>14.1f}%")
    print(f"{'Transport':<15}{euro(avg_transport):>12}{transport_percent:>14.1f}%")
    print(f"{'Entertainment':<15}{euro(avg_entertainment):>12}{entertainment_percent:>14.1f}%")
    print("─" * 41)
    print(f"{'Total Expenses':<15}{euro(avg_expenses):>12}{exp_percent:>14.1f}%")
    print(f"{'Remaining':<15}{euro(avg_remaining):>12}{remaining_percent:>14.1f}%")
    print("─" * 41)

    if avg_remaining < 0:
        print("Status: ⚠ Overspending - Review your budget.")
    elif avg_remaining < 0.05 * avg_income:
        print("Status: △ Tight Budget - Try to save a bit more.")
    else:
        print("Status: ✓ Balanced Budget - You're on track!")

def main():
    """main programme function"""
    week_count = 0
    total_income = 0.0
    total_expenses = 0.0
    total_rent = 0.0
    total_food = 0.0
    total_transport = 0.0
    total_entertainment = 0.0

    while True:
        choice = get_menu_choice()

        if choice == 1:
            # Add This Week’s Budget
            week_count += 1
            this_income, this_expenses, this_rent, this_food, this_transport, this_entertainment = add_week_flow(week_count)

            total_income += this_income
            total_expenses += this_expenses
            total_rent += this_rent
            total_food += this_food
            total_transport += this_transport
            total_entertainment += this_entertainment

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
            print_summary_report(week_count, total_income, total_expenses,
                                 total_rent, total_food, total_transport, total_entertainment)
            input("\n(Press Enter to return to the menu)")

        elif choice == 3:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()