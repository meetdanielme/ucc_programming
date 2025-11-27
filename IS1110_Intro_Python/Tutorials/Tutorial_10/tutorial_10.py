

# IS1110 Tutorial 10 - Revision
# This file contains scaffolding for all tasks from the Tutorial 10 PDF.
# Write your own solutions under each heading.

# --------------------------------------------------
# 1) Variables, Input, and Basic Equations
# --------------------------------------------------
# a) Ask the user for the price of an item and how many they wish to buy.
#    Calculate and print the total cost.
#
# b) Apply a 5% discount to the total, then print the discounted amount.

# --- Q1(a) ---
# 1. Ask the user for the price of an item.
# 2. Ask how many they wish to buy.
# 3. Calculate the total cost.
# 4. Print the total cost.

price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity you wish to buy: "))
total_cost = price * quantity
print(f"Total cost: {total_cost}")

# --- Q1(b) ---
# 1. Calculate a 5% discount.
# 2. Print the discounted amount.

discounted_amount = total_cost * 0.95
print(f"Discounted amount (after 5% discount): {discounted_amount}")

# --------------------------------------------------
# 2) Conditionals
# --------------------------------------------------
# a) Ask the user for their age.
#    Print whether they are:
#       "child" if age < 13
#       "teenager" if 13-17
#       "adult" if 18+
#
# b) If the age is below 0 or above 120, print "Invalid age" and stop the question.
#
# c) If the age is valid, also print the year they were born.

# --- Q2 ---
# 1. Ask the user for their age.
# 2. Handle invalid ages (< 0 or > 120).
# 3. For valid ages:
#    - print whether they are child / teenager / adult.
#    - calculate and print their year of birth.

age = int(input("Enter your age: "))
if age < 0 or age > 120:
    print("Invalid age")
else:
    if age < 13:
        print("child")
    elif 13 <= age <= 17:
        print("teenager")
    else:
        print("adult")
    current_year = 2025  # You can update this to the current year
    birth_year = current_year - age
    print(f"You were born in {birth_year}.")

# --------------------------------------------------
# 3) Strings & Text Processing
# --------------------------------------------------
# a) Ask the user to enter a sentence.
#    Count how many spaces it contains and print the result.
#
# b) Replace each space in the sentence with an underscore ("_") and display the new sentence.

# --- Q3(a) ---
# 1. Ask the user to enter a sentence.
# 2. Count how many spaces (' ') are in the sentence.
# 3. Print the number of spaces.

sentence = input("Enter a sentence: ")
space_count = sentence.count(' ')
print(f"The number of spaces in the sentence: {space_count}")

# --- Q3(b) ---
# 1. Take the same sentence.
# 2. Replace each space with an underscore.
# 3. Print the updated sentence.

updated_sentence = sentence.replace(' ', '_')
print(f"Updated sentence: {updated_sentence}")

# --------------------------------------------------
# 4) Loops
# --------------------------------------------------
# a) Ask the user for a number n.
#    Use a loop to print all odd numbers from 1 to n (inclusive).
#
# b) Use a loop to repeatedly ask the user for numbers until they type "stop".
#    Add all the entered numbers together and print the total.

# --- Q4(a) ---
# 1. Ask the user for a number n.
# 2. Use a loop to print all odd numbers from 1 to n.

n = int(input("Enter a number n: "))
print(f"Odd numbers from 1 to {n}:")
for i in range(1, n + 1, 2):
    print(i)

# --- Q4(b) ---
# 1. Repeatedly ask the user to enter a number (or "stop" to finish).
# 2. Keep a running total of the numbers entered.
# 3. When the user types "stop", print the total.

total = 0
while True:
    user_input = input("Enter a number (or type 'stop' to finish): ")
    if user_input.lower() == "stop":
        break
    try:
        number = float(user_input)
        total = total + number
    except ValueError:
        print("Invalid input. Please enter a number or 'stop'.")

# --------------------------------------------------
# 5) Lists and f-strings
# --------------------------------------------------
# a) Ask the user for:
#       - their favourite hobby
#       - how many years they have been doing it
#
# b) Use an f-string to print:
#       "You have enjoyed <hobby> for <years> years."
#
# c) Then print a second line where the hobby is shown in UPPERCASE.

# --- Q5 ---
# 1. Ask for the user's favourite hobby.
# 2. Ask how many years they have been doing it.
# 3. Print the sentence using an f-string.
# 4. Print the hobby again, but in uppercase.

hobby = input("Enter your favourite hobby: ")
years = int(input("How many years have you been doing it? "))
print(f"You have enjoyed {hobby} for {years} years.")
print(hobby.upper())

# --------------------------------------------------
# 6) Functions
# --------------------------------------------------
# a) Define a function square(n) that returns the square of a number.
#    Example: square(4) should return 16.
#
# b) Define a function that returns:
#       - "short"  if the word length is 3 or fewer characters
#       - "medium" if 4-6 characters
#       - "long"   if 7 or more characters
#
# c) Define a function that:
#       1. Calculates the subtotal (price * quantity)
#       2. Adds tax, where tax_rate is a percentage
#       3. Returns the final amount
#    Then call the function and print the result to 2 decimal places.

# --- Q6(a) ---

def square(n):
    return n * n

# --- Q6(b) ---
# based on the word's length.

def word_length_category(word):
    length = len(word)
    if length <= 3:
        return "short"
    elif 4 <= length <= 6:
        return "medium"
    else:
        return "long"

# --- Q6(c) ---
# 1. Define a function that takes price, quantity, and tax_rate.
# 2. Inside the function, calculate subtotal, then add tax.
# 3. Return the final amount.
# 4. Call the function and print the result rounded to 2 decimal places.

def calculate_final_amount(price, quantity, tax_rate):
    subtotal = price * quantity
    tax_amount = subtotal * (tax_rate / 100)
    final_amount = subtotal + tax_amount
    return final_amount

# When you are finished, you can test each section by running this file
# and working through each question one by one.