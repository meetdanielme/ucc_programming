

# IS1110 Tutorial 9 – Advanced Strings & String Formatting
# Overview: This tutorial builds your understanding of strings & string formatting,
# and introduces more advanced string exercises.

# ---------------------------------------------------------
# Exercise 1 – Movie Night Sentence (warm up exercise)
# Goal:
#   Practise joining (concatenating) several strings into one message using user input.
# Task:
#   - Ask the user for their name, favourite movie, and favourite snack.
#   - Then print:
#       Hi <name>! Tonight you are watching <movie> with some <snack>.
# (Write your solution for Exercise 1 below.)

name = input("Enter your name: ")
movie = input("Enter your favourite movie: ")
snack = input("Enter your favourite snack: ")
print(f"Hi {name}! Tonight you are watching {movie} with some {snack}.")

# ---------------------------------------------------------
# Exercise 2 – Counting the Length of a String
# Goal:
#   Practise using a for loop to count how many characters are in a string.
#   (Spaces, punctuation, and numbers are all counted as characters.)
# Task:
#   1. Define a function called string_length that takes one argument, str1.
#   2. Inside the function, use a loop to count how many characters are in str1.
#   3. The function should return the final count.
#   4. Call the function with the following strings and print the results:
#        "Hello"
#        "Hello World!"
#        "Python 4 everyone"
# (Write your solution for Exercise 2 below.)

def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length("Hello"))
print(string_length("Hello World!"))
print(string_length("Python 4 everyone"))

# ---------------------------------------------------------
# Exercise 3 – Every Second Character from a String
# Goal:
#   Practise using range() and len() to loop over a string by index and build a new string.
# Task:
#   1. Define a function called odd_values_string that takes one argument, e.g. str3.
#   2. The function should create a new string made up of every second character,
#      starting with the first character.
#   3. Return this new string.
#   4. Test the function with:
#        "abcdef"
#        "python"
# (Write your solution for Exercise 3 below.)

def odd_values_string(str3):
    new_str = ""
    for i in range(0, len(str3), 2):
        new_str += str3[i]
    return new_str

odd_values_string("abcdef")
odd_values_string("python")

# ---------------------------------------------------------
# Exercise 4 – Adding "ing" or "ly" to a Word
# Goal:
#   Practise using string length and slicing to modify the end of a word.
# Task:
#   1. Define a function called add_string that takes one argument, str2.
#   2. If the length of str2 is 2 characters or less, return the string unchanged.
#   3. If the length is greater than 2:
#        a. If the string already ends with "ing", add "ly" to the end.
#        b. Otherwise, add "ing" to the end.
#   4. Print the result of calling the function with:
#        "ab"
#        "abc"
#        "string"
# (Write your solution for Exercise 4 below.)

def add_string(str2):
    if len(str2) <= 2:
        return str2
    elif str2.endswith("ing"):
        return str2 + "ly"
    else:
        return str2 + "ing"

add_string("ab")
add_string("abc")
add_string("string")

# ---------------------------------------------------------
# Exercise 5 – Looping Through a String with for and while
# Goal:
#   Show how to loop through each character in a string using both a for loop and a while loop.
# Task:
#   1. Ask the user to enter a word and store it in a variable.
#   2. Use a for loop to print each character of the word on its own line,
#      with a heading:
#        "Using for loop:"
#   3. Then, use a while loop to do the same thing.
#      - Start an index at 0.
#      - Keep looping while the index is less than the length of the string.
#      - Print the character at the current index and then increase the index by 1.
#   Expected output example (if the user enters "cat"):
#      Using for loop:
#      c
#      a
#      t
#      Using while loop:
#      c
#      a
#      t
# (Write your solution for Exercise 5 below.)

word = input("Enter a word: ")
print("Using for loop:")
for char in word:
    print(char)

# ---------------------------------------------------------
# String Formatting Exercises

# Exercise 6 – Escape Sequences \t
# Goal:
#   Show \t (tab) inside strings.
# Task:
#   Write a program that prints a tiny timetable like this (2 lines, with tabs):
#      Time\tSubject
#      9am\tMaths
#   (Your exact timetable text can vary, but use \t to separate columns.)
# (Write your solution for Exercise 6 below.)

print("Time\tSubject")
print("9am\tMaths")

# ---------------------------------------------------------
# Exercise 7 – Custom separator and line ending
# Goal:
#   Show how print() can change the separator and line ending.
# Task:
#   1. Ask the user for three favourite foods.
#   2. Print them on one line, separated by " | " (pipe and spaces).
#   3. Make sure the line ends with " THE END" instead of a normal newline.
#   Expected Output example:
#      Pizza | Pasta | Sushi THE END
# (Write your solution for Exercise 7 below.)

food1 = input("Enter your first favourite food: ")
food2 = input("Enter your second favourite food: ")
food3 = input("Enter your third favourite food: ")
print(food1, food2, food3, sep=" | ", end=" THE END\n

# ---------------------------------------------------------
# Exercise 8 – f-strings with a Calculation (fill in the blanks)
# Goal:
#   Practise using f-strings and formatting numbers to 2 decimal places.
# Task:
#   Complete the following code so that it:
#     - Asks the user for a product name and its price (as a number).
#     - Adds tax of 23% to the price.
#     - Prints the price with tax to 2 decimal places using an f-string.
#   Template:
#       product = _________("Enter the product name: ")
#       price = _______(input("Enter the price (before tax): "))
#       price_with_tax = ______ * 1.23
#       print(f"The price of {______} with tax is €{________:.2f}.")
#   Expected Output:
#       The price of <product> with tax is €<price_with_tax>.
# (Write your solution for Exercise 8 below.)

product = input("Enter the product name: ")
price = float(input("Enter the price (before tax): "))
price_with_tax = price * 1.23
print(f"The price of {product} with tax is €{price_with_tax:.2f}.")