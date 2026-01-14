# IS1110 Tutorial 6 – Loops Advanced & String Formatting
# Generated from IS1110_tutorial_8_exercises.docx on 2025-11-12
#
# Overview
# This tutorial builds your understanding of loops (for/while) and introduces simple string manipulation.
#
# Instructions
# • Each task below is described in comments.
# • Write your solution immediately under the relevant task heading.
# • Keep tasks separated by the provided separators so it's easy to run/debug one at a time.
# • You can comment out other tasks while testing.

# ============================================================================
# 1) Sum of Even Numbers
# Task: Ask the user for a positive integer n. Use a loop to calculate the sum
#       of all even numbers between 1 and n.
# Example:
#   Enter a number: 10
#   Sum of even numbers: 30
# ----------------------------------------------------------------------------
# Your code for Task 1 below:

num = int(input("Enter a positive number: "))
sum = 0
for i in range(1, num):
    if i % 2 == 0:
        sum += i
print("Sum of even numbers:", sum)

# ============================================================================
# 2) Multiplication Table Generator
# Task: Ask the user for a number and print its multiplication table (1–10)
#       using a for loop.
# Example:
#   Enter a number: 5
#   5 x 1 = 5
#   5 x 2 = 10
#   ...
# ----------------------------------------------------------------------------
# Your code for Task 2 below:

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# ============================================================================
# 3) Divisible Numbers Finder
# Task: Ask the user for a number n. Print all numbers between 1 and 100 that
#       are divisible by n.
# Example:
#   Enter a number: 15
#   Numbers divisible by 15 between 1 and 100:
#   15
#   30
#   45
#   60
#   75
#   90
# ----------------------------------------------------------------------------
# Your code for Task 3 below:

n = int(input("Enter a number: "))
for i in range(1, 101):
    if i % n == 0:
        print(i)


# ============================================================================
# 4) Find the Largest Number
# Task: Keep asking the user for numbers until they type "done". Then print the
#       largest number entered.
# Hint: Use a while True loop with break.
# Example:
#   Enter a number: 10
#   Enter a number: 25
#   Enter a number: 8
#   Enter a number: done
#   The largest number is 25.
# ----------------------------------------------------------------------------
# Your code for Task 4 below:

largest = None
while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    try:
        num = float(number)
        if largest is None or num > largest:
            largest = num
    except ValueError:
        print("Invalid input. Please enter a number or 'done' to finish.")


# ============================================================================
# 5) Count Vowels in a Word (Fill in the Blanks)
# Task: Ask for a word and count how many vowels (a, e, i, o, u) it contains.
# Given scaffold (complete the blanks or write your own version):
#   word = input("Enter a word: ")
#   count = 0
#   for ____ in ____:
#       if ____ in "aeiou":
#           count = count + 1
#   print("Number of vowels:", ____)
# ----------------------------------------------------------------------------
# Your code for Task 5 below:

word = input("Enter a word: ")
count = 0
for letter in word:
    if letter in "aeiou":
        count = count + 1
print("Number of vowels:", count)


# ============================================================================
# 6) Character Counter (Fill in the Blanks)
# Task: Ask the user for a word and a letter, then count how many times that
#       letter appears in the word.
# Given scaffold (complete the blanks or write your own version):
#   word = input("Enter a word: ")
#   letter = input("Enter a letter: ")
#   count = 0
#   for ____ in ____:
#       if ____ == ____:
#           count = count + 1
#   print("The letter", ____, "appears", ____, "times.")
# Example:
#   Enter a word: banana
#   Enter a letter: a
#   The letter a appears 3 times.
# ----------------------------------------------------------------------------
# Your code for Task 6 below:


word = input("Enter a word: ")
letter = input("Enter a letter: ")
count = 0
for char in word:
    if char == letter:
        count = count + 1
print("The letter", letter, "appears", count, "times.")

# ============================================================================
# 7) Fill-in-the-Blank: String Formatting
# Task: Fill in the missing code so the formatted string prints correctly.
# Given scaffold:
#   name = "____"
#   age = ____
#   print(f"My name is {____} and I am {____} years old.")
# Expected Output:
#   My name is John and I am 21 years old.
# ----------------------------------------------------------------------------
# Your code for Task 7 below:

name = "John"
age = 21
print(f"My name is {name} and I am {age} years old.")


# ============================================================================
# 8) Sentence Formatter (Bonus – Fill in the Blanks)
# Task: Ask the user for their name and hobby, then print:
#       Hello <name>, your favorite hobby is <hobby>.
# Given scaffold:
#   name = input("Enter your name: ")
#   hobby = input("Enter your hobby: ")
#   print(f"Hello {____}, your favorite hobby is {____}.")
# ----------------------------------------------------------------------------
# Your code for Task 8 below:

name = input("Enter your name: ")
hobby = input("Enter your hobby: ")
print(f"Hello {name}, your favorite hobby is {hobby}.")

# =============================== End of File ================================
