# =======================================================
# 2026-IS1111 Tutorial Assignment 1
# 
# Your name: 
# Your student ID:
# =======================================================


# =======================================================
# Exercise 1: Basics
# =======================================================

# 1.1. Define a list of fruits that contains the following values: "apple", "banana", "cherry".

fruits = ["apple", "banana", "cherry"]

# 1.2. Print the second item in the fruits list using list indexing.

print(fruits[1])

# 1.3. Change the value from "apple" to "kiwi"", in the fruits list using the index operator.

fruits[0] = "kiwi"

# 1.4. Use the append method to add "orange" to the fruits list.

fruits.append("orange")

# 1.5. Use the insert method to add "lemon" as the second item in the fruits list.

fruits.insert(1, "lemon")

# 1.6. Use the remove method to remove "banana" from the fruits list.

fruits.remove("banana")

# 1.7. Use negative indexing to print the last item in the list.

print(fruits[-1])

# 1.8. Append the following fruits: "orange", "kiwi", "melon", "mango", to the original list, then use a range of indexes (slicing) to print the third, fourth, and fifth items in the list.

fruits.extend(["orange", "kiwi", "melon", "mango"])
print(fruits[2:5])

# 1.9. Use the correct Python function to print the number of items in the list.

print(len(fruits))


# =======================================================
# Exercise 2: List processing
# =======================================================
# Create the following functions:

# 2.1. A Python function to sum all the items in a list of numbers.

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# 2.2. A Python function to multiply all the items in a list of numbers.

def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# 2.3. A Python function to get the largest number from a list of numbers.

def largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# 2.4. A Python function to get the smallest number from a list of numbers.

def smallest_number(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

# 2.5. A Python function to remove duplicates from a list.

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# 2.6. A Python function to check if a list is empty or not.

def is_list_empty(input_list):
    return len(input_list) == 0

# 2.7. A Python function to clone or copy a list.

def clone_list(input_list):
    return input_list[:]

# =======================================================
# Exercise 3: Lists and strings
# =======================================================
# Create a Python file called list_functions.py that contains the following functions:
# Then, create a file called main.py for testing that each function is working as expected. At the top of this file write: import list_functions. Call each function as normal.


# 3.1. Write a Python programme to count the number of strings in a given list of strings using a for loop.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 4


# 3.2. Write a Python programme to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']


# 3.3. Write a Python programme to convert a list of characters into a string.


# 3.4. Write a Python programme to compute the difference between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['red', 'orange', 'white']
# Color2-Color1: ['black', 'yellow']


# =======================================================
# Exercise 4
# =======================================================
# Write the code for the following pseudocode.
# Place your answers below the respective comment line.

# PSEUDOCODE:
# -----------
# Get user input for 5 grades as int.
grade1 = int(input("Enter grade 1: "))
grade2 = int(input("Enter grade 2: "))
grade3 = int(input("Enter grade 3: "))
grade4 = int(input("Enter grade 4: "))
grade5 = int(input("Enter grade 5: "))
# Append each grade to a list.
grades_list = []
grades_list.append(grade1)
grades_list.append(grade2)
grades_list.append(grade3)
grades_list.append(grade4)
grades_list.append(grade5)
# Sort the list of grades (in ascending order).
grades_list.sort()
# Remove the two first (lowest) values.
grades_list = grades_list[2:]

# Calcuate the range of the remaining three grades by subtracting the lowest from the highest remaining grades.
grade_range = grades_list[-1] - grades_list[0]

# Calculate the average of the remaining three grades by adding them and dividing by 3.
average_grade = sum(grades_list) / 3

# Display the calculated range and average on the console.
print("Range of grades:", grade_range)
print("Average grade:", average_grade)
