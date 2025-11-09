# LOOPS AND ITERATION - IN-CLASS PROGRAMMING EXAMPLES
# IS1110 Python Programming

# ============================================================
# INTRODUCTION: REPETITION
# ============================================================

# Besides selecting which statements to execute, a fundamental need in 
# a programme is repetition. We need to repeat a set of statements under 
# some conditions.

# With both selection (if/elif/else) and repetition (loops), we have the 
# two most necessary programming statements.

# Two types of loops in Python:
# - while statement: the more general repetition construct. It repeats a 
#   set of statements while some condition is True.
# - for statement: useful for iteration, moving through all the elements 
#   of a data structure, one at a time.


# ============================================================
# WHILE LOOPS (INDEFINITE LOOPS)
# ============================================================

# While loops repeat as long as a condition is True
# Called "indefinite" because we don't know how many times they'll run

# Create a variable n = 5 (this initialises the control (iteration) variable)
# Write a while loop that prints n, then decreases n by 1
# Loop while n > 0
# After the loop, print 'Blastoff'
n  = 5
while n > 0:
    print(n)
    n -= 1
else:
    print("Blastoff")

# While loop structure:
# 1. Initialise the control (iteration) variable before the loop (n = 5)
# 2. Test the condition (n > 0)
# 3. Modify the control (iteration) variable inside the loop (n = n - 1)


# ============================================================
# INFINITE LOOPS
# ============================================================

# A loop that never stops is called an infinite loop
# This happens when the condition never becomes False

# DANGER: This would run forever (don't run this!)
# n = 5
# while n > 0:
#     print(n)
#     # Forgot to modify n - infinite loop!


# ============================================================
# BREAK STATEMENT
# ============================================================

# break exits the loop immediately
# Useful when we find what we're looking for

# Create count = 0
# Write while True loop (infinite loop)
# Increment count by 1
# Print 'Count:' and count
# If count >= 3, print 'Breaking out' and break
# After loop, print 'Loop finished'

count = 0
while True:
    count += 1
    print(f"Count: {count}")
    if count >= 3:
        print("Breaking out")
        break
print("Loop finished")

# ============================================================
# CONTINUE STATEMENT
# ============================================================

# continue skips the rest of the current iteration
# The loop continues with the next iteration

# For loop from 1 to 5 (range(1, 6))
# If num == 3, use continue to skip
# Print 'Number:' and num

for num in range(1, 6):
    if num == 3:
        continue
    print(f"Number: {num}")

# ============================================================
# FOR LOOPS (DEFINITE LOOPS)
# ============================================================

# For loops repeat a specific number of times
# Called "definite" because we know how many times they'll run

# For loops have ITERATION VARIABLES that change each time through the loop
# The iteration variable is successively assigned each value in the sequence

# Create word = 'Hello'
# Loop through each letter in word (letter is the iteration variable)
# Print letter

word = 'Hello'
for letter in word:
    print(letter)

# Loop through range(5) (i is the iteration variable)
# Print 'Iteration:' and i
for i in range(5):
    print(f"Iteration: {i}")


# ============================================================
# RANGE FUNCTION
# ============================================================

# The range() function generates a sequence (an arithmetic progression) 
# of numbers

# Syntax:
# range(stop)
# range(start, stop)
# range(start, stop, step)

# range(stop) - from 0 to stop-1
# Loop through range(5) and print i
# Expected output: 0, 1, 2, 3, 4

for i in range(5):
    print(i)

# range(start, stop) - from start to stop-1
# Loop through range(2, 6) and print i
# Expected output: 2, 3, 4, 5

for i in range(2,6):
    print(i)

# range(start, stop, step) - from start to stop-1 with step
# Loop through range(0, 11, 2) and print i
# Expected output: 0, 2, 4, 6, 8, 10

for i in range(0,11,2):
    print(i)

# Counting backwards
# Loop through range(5, 0, -1) and print i
# Expected output: 5, 4, 3, 2, 1

for i in range(5,0,-1):
    print(i)

# ============================================================
# LOOP PATTERN: COUNTING
# ============================================================

# Count how many times something happens

# Initialise count = 0
# Print 'Before:' and count
# Create word = 'banana'
# Loop through each letter in word
# If letter == 'a', increment count and print count and letter
# After loop, print 'The letter a appears', count, 'times'

count = 0
print(f"Before: {count}")
word = "banana"
for letter in word:
    if letter == "a":
        count += 1
        print(count, letter)
print(f"The letter \'a\' appears {count} times.")

# ============================================================
# LOOP PATTERN: SUMMING (ACCUMULATOR)
# ============================================================

# Add up values using an accumulator variable

# Initialise total = 0
# Print 'Before:' and total
# Loop through range(1, 6) - numbers 1, 2, 3, 4, 5
# Add each num to total
# Print total and num
# After loop, print 'Sum:', total

total = 0
print(f"Before: {total}")
for num in range(1,6):
    total += num
    print(total, num)
print(f"Sum: {total}")

# Another example: Count letters in a word using range(len())
# Create word = 'Python'
# Initialise count = 0
# Loop through range(len(word)) - this gives indices 0, 1, 2, 3, 4, 5
# Increment count by 1
# Print count, i, and word[i]
# After loop, print 'Number of letters:', count

word = "Python"
count = 0
for i in range(len(word)):
    count += 1
    print(count, word[i])
print(f"Number of letters: {count}")

# ============================================================
# LOOP PATTERN: FINDING MAXIMUM
# ============================================================

# Find the largest value in a sequence

# Initialise largest = None
# Print 'Before:' and largest
# Loop through range(5, 46, 5) - numbers 5, 10, 15, ..., 45
# If largest is None, assign num to largest
# Elif num > largest, assign num to largest
# Print largest and num
# After loop, print 'Largest:', largest

largest = None
print(f"Before: {largest}")
for num in range(5, 46, 5):
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
        print(largest, num)
print(f"Largest: {largest}")

# ============================================================
# LOOP PATTERN: FINDING MINIMUM
# ============================================================

# Find the smallest value in a sequence

# COMMON MISTAKE: Using -1 as the initial value
# Initialise smallest = -1
# Print 'Before:' and smallest
# Loop through range(3, 40, 5) - numbers 3, 8, 13, ..., 38
# If num < smallest, assign num to smallest
# Print smallest and num
# After loop, print 'Smallest:', smallest
# Notice: This gives -1 (wrong!)

smallest = -1
print(f"Before: {smallest}")
for num in range(3, 40, 5):
    if num < smallest:
        smallest = num
        print(smallest, num)
print(f"Smallest: {smallest}")

# CORRECT APPROACH: Use None as the initial value
# Initialise smallest = None
# Print 'Before:' and smallest
# Loop through range(3, 40, 5) - numbers 3, 8, 13, ..., 38
# If smallest is None, assign num to smallest
# Elif num < smallest, assign num to smallest
# Print smallest and num
# After loop, print 'Smallest:', smallest
# This gives 3 (correct!)

smallest = None
print(f"Before: {smallest}")
for num in range(3, 40, 5):
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
        print(smallest, num)
print(f"Smallest: {smallest}")

# ============================================================
# LOOP PATTERN: CALCULATING AVERAGE
# ============================================================

# Combine counting and summing patterns

# Initialise count = 0 and total = 0
# Print 'Before:' count and total
# Loop through range(10, 51, 10) - numbers 10, 20, 30, 40, 50
# Increment count by 1
# Add num to total
# Print count, total, and num
# Calculate average = total / count
# Print 'After:' count, total, and average

count = 0
total = 0
print(f"After: {count} and {total}")
for num in range(10, 51, 10):
    count += 1
    total += num
    average = total / count
print(f"After: {count}, {total} and {average}")

# ============================================================
# THE NONE VALUE
# ============================================================

# None represents the absence of a value
# Useful for initialising variables before a loop

# Create value = None
# Print 'Value:' and value
# Print 'Type:' and type(value)

value = None
print(f"Value: {value}")
print(f"Type: {type(value)}")

# Check if value is None using if statement
# If so, print 'Value is None'

if value is None:
    print("Value is None")

# Assign value = 42
# Check if value is not None
# If so, print 'Value is not None:' and value

value = 42
if value is None:
    print(f"Value is not None, it's {value}")

# ============================================================
# IS AND IS NOT OPERATORS
# ============================================================

# 'is' tests if two variables refer to the same object
# 'is not' tests if two variables refer to different objects

# Create x = None
# Use if statement to check if x is None
# Print 'x is None'

x = None
if x is None:
    print("x is None")

# Assign x = 10
# Use if statement to check if x is not None
# Print 'x is not None'

x = 10
if x is not None:
    print(f"x is not None")

# Note: Use == for value comparison, use 'is' for identity comparison


# ============================================================
# COMBINING LOOPS WITH FUNCTIONS
# ============================================================

# Functions can contain loops

# Define function count_vowels(text)
# Initialise count = 0
# Loop through each letter in text
# If letter in 'aeiouAEIOU', increment count
# Return count

def count_vowels(text):
    count = 0
    for letter in text:
        if letter in "aeiouAEIOU":
            count += 1
    return count

# Call count_vowels('Hello World') and print result

print(count_vowels("Hello World"))


# Define calculate_sum(start, end) that returns sum of numbers from start to end
# Initialise total = 0
# Loop through range(start, end + 1)
# Add each number to total
# Return total

def calculate_sum(start, end):
    total = 0
    for num in (start, end + 1):
        total += num
    return total


# Define calculate_average(start, end)
# Call calculate_sum(start, end) to get total
# Calculate count = end - start + 1
# Return total / count

def calculate_average(start, end):
    total = calculate_sum(start, end)
    count = end - start + 1
    return total / count

# Call calculate_average(1, 10) and print result

print(calculate_average(1,10))

# ============================================================
# PRACTICAL EXAMPLE: INPUT VALIDATION
# ============================================================

# Use loops to keep asking until we get valid input

# Get a positive number from user
# while True:
# - Get input with message 'Enter a positive number: '
# - If input is 'quit', break
# - Use try/except to convert to int
# - If number > 0, print thank you message and break
# - Otherwise print error message
# - In except block, print invalid input message

while True:
    number = input("Enter a positive number: ")
    if number == "quit":
        break
    try:
        number = int(number)
        if number > 0:
            print("Thank you!")
            break
        else:
            print("Error")
    except ValueError:
        print("Invalid input")
