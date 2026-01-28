"""
# 2026-IS1111 Tutorial Assignment 2
#
# Your name: Daniel Marcinkowski
# Your student ID: 125701129
# 
# Semester 2

Topics covered:
- Lists
- Indexing & slicing
- List methods
- Basic list comprehensions
- Lists of lists (2D lists)
- Functions
- String formatting (f-strings)
"""


# ============================================================
# QUESTION 1 — Lists: indexing, slicing, copying
# ============================================================
"""
NOTE:
Slicing syntax is:
    list[start:end:step]
The 'step' controls how many positions Python jumps each time.
A step of 2 means “skip every second element”.

Given the list:

names = ["Aisha", "Sean", "Maya", "Omar", "Niamh", "Liam", "Zara", "Noah"]

(a) Print the last element using negative indexing.
(b) Print the last THREE names using slicing.
(c) Print the middle two names using slicing (should be ["Maya", "Omar"]).
(d) Print every second name starting from index 1 using slicing.
(e) Print the list reversed using slicing (do NOT use reverse()).
(f) Create a NEW list called names_copy that is a copy of names.
    Change names_copy[0] to "CHANGED".
    Print both lists to show they are different.
"""

# TODO: write your code for Question 1 below

names = ["Aisha", "Sean", "Maya", "Omar", "Niamh", "Liam", "Zara", "Noah"]

# (a)
print(names[-1])

# (b)
print(names[-3:])

# (c)
print(names[2:4])

# (d)
print(names[1::2])

# (e)
print(names[::-1])

# (f)
names_copy = names[:]  
names_copy[0] = "CHANGED"  
print("Original list:", names)  
print("Copied list:", names_copy)  


# ============================================================
# QUESTION 2 — List methods + cleaning data
# ============================================================
"""
You are given messy text data (duplicates, spaces, mixed case):

raw_items = ["  Milk", "bread ", "EGGS", "milk", " Coffee", "bread", "tea", "TEA  "]

Write a function clean_shopping_list(raw_items) that returns a NEW list that is:
- trimmed (no leading/trailing spaces)
- lowercase
- contains NO duplicates
- keeps the FIRST occurrence of each item (preserve order)

Example output:
["milk", "bread", "eggs", "coffee", "tea"]

Rules:
(a) You MUST use string methods like strip() and lower().
(b) You are NOT allowed to use set(...).
(c) You MUST NOT modify raw_items.
(d) Write one sentence (as a comment) explaining why set(...) is not suitable here.
"""

# TODO: write your function for Question 2 below

raw_items = ["  Milk", "bread ", "EGGS", "milk", " Coffee", "bread", "tea", "TEA  "]

def clean_shopping_list(raw_items):
    cleaned_items = []
    for item in raw_items:
        cleaned_item = item.strip().lower()
        if cleaned_item not in cleaned_items:
            cleaned_items.append(cleaned_item)
    return cleaned_items

# set() would remove duplicates easily but wouldn't preserve the order of first occurrence

# ============================================================
# QUESTION 3 — List comprehensions (basic, controlled)
# ============================================================
"""
Write the following functions using list comprehensions.
Keep them SIMPLE: one for-loop, optional if.

## List comprehension formula:
# [expression for item in list if condition]
# Read as: "do THIS for each item in the list, but only if the condition is true"
# Helpful to do normal way first, then convert to comprehension.


(a) square_numbers(nums)
    - nums is a list of integers
    - return a NEW list where each number is squared

Example:
square_numbers([2, 3, 4]) -> [4, 9, 16]

(b) long_words(words, min_length)
    - words is a list of strings
    - min_length is an integer
    - return a NEW list containing only the words
      whose length is STRICTLY greater than min_length

Example:
long_words(["hi", "hello", "bye", "amazing"], 3)
-> ["hello", "amazing"]

(c) shout_short_words(words, max_length)
    - words is a list of strings
    - return a NEW list of words
      where the word length is LESS THAN OR EQUAL TO max_length
    - convert the kept words to UPPERCASE

Example:
shout_short_words(["cat", "elephant", "dog", "mouse"], 3)
-> ["CAT", "DOG"]

(d) first_letters(words)
    - words is a list of strings
    - return a NEW list containing the first character of each word
    - assume every word has at least one character

Example:
first_letters(["cat", "dog", "mouse"]) -> ["c", "d", "m"]
"""

# TODO: write your functions for Question 3 below

# (a)
def square_numbers(nums):
    return [num ** 2 for num in nums]

print(square_numbers([2, 3, 4])) 

# (b)
def long_words(words, min_length):
    return [word for word in words if len(word) > min_length]

print(long_words(["hi", "hello", "bye", "amazing"], 3))

# (c)
def shout_short_words(words, max_length):
    return [word.upper() for word in words if len(word) <= max_length]

print(shout_short_words(["cat", "elephant", "dog", "mouse"], 3))

# (d)
def first_letters(words):
    return [word[0] for word in words]

print(first_letters(["cat", "dog", "mouse"]))

# ============================================================
# QUESTION 4 — Lists of lists + functions + string formatting
# ============================================================
"""
We have a 2D list of student records.
Each inner list is: [name, mark1, mark2, mark3]

records = [
    ["Aisha", 78, 82, 90],
    ["Sean", 65, 70, 68],
    ["Maya", 88, 91, 85],
    ["Omar", 55, 60, 58],
]

(a) Print Maya’s second mark using indexing.
(b) Change Omar’s first mark from 55 to 59.
(c) Add a new record: ["Niamh", 72, 74, 79].
(d) Print the updated records list.

(e) Write a function student_average(record)
    - record is ONE student list, e.g. ["Aisha", 78, 82, 90]
    - calculate and return the average of the marks
    - do NOT hard-code the number of marks

(f) Write a function top_student(records)
    - records is the full 2D list
    - return the NAME of the student with the highest average
    - if two students have the same average, return the first one

(g) Write a function format_report(records)
    - build and return ONE string that looks like this:

Student Report
--------------
Aisha: avg=83.33333333333333
Sean: avg=67.66666666666667
Maya: avg=88.0
Omar: avg=59.0
Niamh: avg=75.0

Rules:
- Use f-strings
- Build the output using a loop
- Do NOT worry about rounding or formatting decimal places
"""

# TODO: write your code and functions for Question 4 below

records = [
    ["Aisha", 78, 82, 90],
    ["Sean", 65, 70, 68],
    ["Maya", 88, 91, 85],
    ["Omar", 55, 60, 58],
]
# (a)
print(records[2][2])  

# (b)
records[3][1] = 59

# (c)
records.append(["Niamh", 72, 74, 79])

# (d)
print(records)

# (e)
def student_average(record):
    marks = record[1:]  
    average = sum(marks) / len(marks)  
    return average

# (f)
def top_student(records):
    top_name = ""
    top_avg = -1  
    for record in records:
        avg = student_average(record)
        if avg > top_avg:
            top_avg = avg
            top_name = record[0]
    return top_name

# (g)
def format_report(records):
    header = "Student Report"
    print(header + "\n" + "-" * len(header))
    for record in records:
        name = record[0]
        avg = student_average(record)
        print(f"{name}: avg={avg}")

format_report(records)