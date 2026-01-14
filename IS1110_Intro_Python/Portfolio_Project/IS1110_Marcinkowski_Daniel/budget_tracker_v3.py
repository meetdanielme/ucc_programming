# budget_tracker_v3.py
# Author: Daniel Marcinkowski
# ID: 125701129
# Date: 2025-10-19
# Description: "Modular Budget System (Version 3.0)"
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
    """Validates input and returns positive float"""
    try:
        value = float(input(prompt))
        if value < 0:
            print("Please enter a number that is 0 or greater.")
            return 0.0
        return value
    except:
        print("Invalid input! Please enter a number.")
        return 0.0

def get_user_input():
    """gets all budget input from user with validation"""
    income = get_positive_float("What's your weekly income? (in €)\n")
    rent = get_positive_float("How much you spend on rent weekly? (in €)\n")
    food = get_positive_float("How much you spend on food weekly? (in €)\n")
    transport = get_positive_float("How much you spend on transport weekly? (in €)\n")
    entertainment = get_positive_float("How much you spend on entertainment weekly? (in €)\n")
    return income, rent, food, transport, entertainment

def calculate_budget(income, rent, food, transport, entertainment):
    """calculates total expenses and money remaining"""
    total_expenses = rent + food + transport + entertainment
    money_left = income - total_expenses
    return total_expenses, money_left

def analyse_status(money_left):
    """determines budget status and provides recommendations"""
    if money_left == 0:
        print("You don't have any money left!")
    elif money_left < 0:
        money_left = money_left * -1
        print("You're overspending! Next week, you should cut your expenses by", money_left)
    elif money_left > 50:
        print("Good job saving! You saved", money_left, "€")
    else:
        print("You should probably save a bit more next week.")

def show_results(income, rent, food, transport, entertainment, total_expenses, money_left):
    """displays formatted budget report"""
    print("\n===OVERVIEW===\n")
    print("Weekly Income:", income, "€")
    print("Total Expenses:", total_expenses, "€")
    print("Money Left:", money_left, "€")
    print("\n===SPEND===\n")
    print(f"Rent:", rent, "€")
    print("Food:", food, "€")
    print("Transport:", transport, "€")
    print("Entertainment:", entertainment, "€")
    print("\n===TIPS===\n")
    analyse_status(money_left)

def main():
    """main programme function"""
    income, rent, food, transport, entertainment = get_user_input()
    total_expenses, money_left = calculate_budget(income, rent, food, transport, entertainment)
    show_results(income, rent, food, transport, entertainment, total_expenses, money_left)

main()