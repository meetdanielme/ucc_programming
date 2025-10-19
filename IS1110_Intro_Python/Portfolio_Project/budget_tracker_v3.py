# budget_tracker_v3.py
# Author: Daniel Marcinkowski
# ID: 125701129
# Date: 2025-10-19
# Description: "Modular Budget System (Version 3.0)"

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