# CONDITIONALS - IN-CLASS PROGRAMMING EXAMPLES (STUDENT VERSION)
# IS1110 Python Programming

# ============================================================
# BOOLEAN DATA TYPE
# ============================================================

# Boolean values: True and False (note the capitalisation)
# Data type: bool
# Boolean expressions evaluate to either True or False

x = 5
y = 10

# Assign True to a variable called is_active

is_active = True

# Assign False to a variable called is_complete

is_complete = False

# Print the type of is_active

print(is_active)

# Print the result of x < y

print(x < y)

# Print the result of x > y

print(x > y)

# Print the result of x == 5

print(x == 5)

# ============================================================
# RELATIONAL/COMPARISON OPERATORS
# ============================================================

# Comparison operators evaluate to True or False
# They look at variables but do not change them
# Available operators: < <= == >= > !=

x = 5

# Write if statements to check:
# 1. if x equals 5
# 2. if x is greater than 4
# 3. if x is greater than or equal to 5
# 4. if x is less than 6
# 5. if x is less than or equal to 5
# 6. if x is not equal to 6

if x == 5:
    print("Yes")
if x > 4:
    print("Yes")
if x >= 5:
    print("Yes")
if x < 6:
    print("Yes")
if x <= 5:
    print("Yes")
if x != 6:
    print("Yes")

# ============================================================
# BOOLEAN EXPRESSIONS AND LOGICAL OPERATORS
# ============================================================

# Logical operators: and, or, not
# and: true only if both conditions are true
# or: true if either or both conditions are true
# not: reverses the truth value

age = 25
has_licence = True

# Write a condition to check if someone can drive (age >= 18 AND has_licence)

if age >= 25 and has_licence == True:
    print("Yes")

# Write a condition to check if someone cannot drive (age < 18 OR does not have licence)

if age < 18 or has_licence == False:
    print("Yes")

temperature = 22
# Write a condition to check if temperature is pleasant (not too cold and not too hot)
# Pleasant means: NOT (temperature < 0 OR temperature > 30)

if temperature < 0 or temperature > 30:
    print("Yes")

# ============================================================
# SHORT-CIRCUIT EVALUATION
# ============================================================

# Python evaluates conditions from left to right and stops as soon as the result is known
# For 'and': if first condition is False, second is not checked
# For 'or': if first condition is True, second is not checked
# This is useful to prevent errors

number = 0
m = 10
n = 5

# Write a safe condition that checks if m == (n / number)
# Make sure to check if number is not zero first

if m == (n / number) and number != 0:
    print("Yes")
else:
    print("No")

# ============================================================
# ONE-WAY DECISIONS (if only)
# ============================================================

# Executes code block only if condition is True
# Otherwise, skips the indented block entirely

score = 85

# Write code that prints 'You passed the exam' and 'Well done' if score >= 70

if score >= 70:
    print("You passed the exam")
    print("Well done")
print('Programme continues')


# ============================================================
# TWO-WAY DECISIONS (if-else)
# ============================================================

# Executes one block if condition is True, another if False
# Exactly one of the two blocks will execute

x = 4

# Write an if-else statement that prints 'Bigger than 2' if x > 2,
# otherwise prints 'Not bigger than 2'

if x > 2:
    print("Bigger than 2")
else:
    print("Not bigger than 2")
print('All done')


# ============================================================
# MULTI-WAY DECISIONS (if-elif-else)
# ============================================================

# Tests multiple conditions in sequence
# Only the first True condition executes
# Once a condition is True, remaining conditions are skipped

grade = 65

# Write a multi-way decision structure to classify grades:
# >= 70: 'First Class'
# >= 60: 'Upper Second Class'
# >= 50: 'Lower Second Class'
# >= 40: 'Pass'
# else: 'Fail'

if grade >= 70:
    print('First Class')
elif grade >= 60:
    print('Upper Second Class')
elif grade >= 50:
    print('Lower Second Class')
elif grade >= 40:
    print('Pass')
else:
    print('Fail')

# ============================================================
# NESTED DECISIONS
# ============================================================

# if statements inside other if statements
# Inner condition only checked if outer condition is True

# Example 1: Basic nested if
x = 42

# Write nested if statements:
# If x > 1, print 'More than one'
#   Then if x < 100, print 'Less than 100'

if x > 2:
    print("More than one")
    if x < 100:
        print("Less than 100")
print('All done')


# Example 2: Nested if-else structures
age = 20
has_id = True

# Write nested if-else:
# If age >= 18, print 'Age requirement met'
#   Then if has_id is True, print 'Entry granted'
#   Otherwise, print 'Need ID for entry'
# If age < 18, print 'Too young for entry'

if age >= 18:
    print("Age requirement met")
    if has_id is True:
        print("Entry granted")
    else:
        print("Need ID for entry")
else:
    print("Too young for entry")

# Example 3: Real-world scenario - loan eligibility
income = 35000
credit_score = 720
employment_years = 3

# Write a three-level nested structure:
# If income >= 30000, print 'Income requirement met'
#   Then if credit_score >= 700, print 'Credit score acceptable'
#     Then if employment_years >= 2, print 'Loan approved'
#     Otherwise, print 'Need 2+ years employment'
#   Otherwise, print 'Credit score too low'
# Otherwise, print 'Income too low'

if income >= 30000:
    print("Income requirement met")
    if credit_score >= 700:
        print("Credit score acceptable")
        if employment_years >= 2:
            print("Loan approved")
        else:
            print("Need 2+ years employment")
    else :
        print("Credit score too low")
else:
    print("Income too low")

# Example 4: Nested vs logical operators comparison
# These two approaches can sometimes achieve the same result

score = 75
attendance = 85

# Using nested conditionals, check:
# If score >= 70
#   Then if attendance >= 80, print 'Pass with good attendance'

if score >= 70:
    if attendance >= 80:
        print("Pass with good attendance")

# Now rewrite the above using logical operators (and) instead

if score >= 70 and attendance >= 80:
        print("Pass with good attendance")

# Write nested conditionals with different messages at each level:
# If score >= 70, print 'Score is sufficient'
#   Then if attendance >= 80, print 'Attendance is also good'
#   Otherwise, print 'But attendance needs improvement'
# Otherwise, print 'Score is insufficient'

if score >= 70:
    print('Score is sufficient')
    if attendance >= 80:
        print('Attendance is also good')
    else:
        print('But attendance needs improvement')
else:
    print('Score is insufficient')

# When to use nested conditionals:
# 1. When you need to check a condition only if another is True
# 2. When you need different actions/messages at each decision level
# 3. When the inner condition is expensive to check (short-circuit benefit)

# When to use logical operators instead:
# 1. When both conditions must be True for a single action
# 2. When the logic is simple and both conditions are equally important
# 3. When it makes the code more readable


# ============================================================
# MEMBERSHIP OPERATORS (in / not in)
# ============================================================

# in: checks if an element exists in a sequence (string, list, tuple)
# not in: checks if an element does not exist in a sequence
# Returns True or False

# Using 'in' with strings
text = 'Hello World'

# Check if 'World' is in the text variable

print("World" in text)

# Check if 'x' is not in the text variable

print("x" not in text)

# Using 'in' with lists
fruits = ['apple', 'banana', 'orange']

# Check if 'banana' is in the fruits list

print("banana" in fruits)

# Check if 'grape' is not in the fruits list

print("grape" not in fruits)

# Using 'in' with conditionals for validation
user_input = input('Enter a vowel: ')

# Check if user_input is in the string 'aeiou'
# Print 'Valid vowel' if it is, otherwise print 'Not a vowel'

if user_input in "aeiou":
    print("Valid vowel")
else:
    print("Not a vowel")

# ============================================================
# METHODS THAT RETURN BOOLEAN VALUES
# ============================================================

# String methods that return True or False
# Useful for validation in conditionals

# isdigit(): checks if all characters are digits
text1 = '12345'
# Check if text1 contains all digits
print(text1.isdigit())

# isalpha(): checks if all characters are letters
text2 = 'Hello'
# Check if text2 contains all letters
print(text2.isalpha())

# isalnum(): checks if all characters are letters or digits
text3 = 'Hello123'
# Check if text3 is alphanumeric
print(text3.isalnum())

# islower(): checks if at least 1 alphabetic character and all alphabetic characters are lowercase
text4 = 'hello'
# Check if text4 is all lowercase
print(text4.islower())

# isupper(): checks if at least 1 alphabetic character and all alphabetic characters are uppercase
text5 = 'HELLO'
# Check if text5 is all uppercase
print(text5.isupper())

# isspace(): checks if string contains only whitespace
text6 = '   '
# Check if text6 contains only whitespace
print(text6.isspace())

# startswith(): checks if string starts with specified substring
filename = 'report.pdf'
# Check if filename starts with 'report'
print(filename.startswith('report'))

# endswith(): checks if string ends with specified substring
# Check if filename ends with '.pdf'
print(filename.endswith('.pdf'))

# isinstance(): checks if an item is of a particular data type
value = 42
# Check if value is an integer
print(isinstance(value, int))

# Check if filename is a string
print(isinstance(filename, str))


# ============================================================
# INDENTATION
# ============================================================

# Indentation is crucial in Python
# Increase indent after if/elif/else/for statements (after :)
# Maintain indent to show which lines belong to the block
# Reduce indent to end the block
# Blank lines and comments don't affect indentation

x = 10

# Write an if statement that checks if x > 5
# Inside the if block, print 'x is greater than 5'
# Then print 'Still inside the if block' (also indented)
# Outside the if block, print 'This always executes' (not indented)
# Test your code with different values of x (e.g., x = 3, x = 10) to see how indentation affects execution

if x > 5:
    print("x is greater than 5")
    print("Still inside the if block")
print("This always executes")

# ============================================================
# STRING COMPARISON
# ============================================================

# Strings compared based on ASCII values
# Digits (0-9) < Uppercase letters (A-Z) < Lowercase letters (a-z)

word1 = 'Apple'
word2 = 'apple'

# Compare word1 and word2 and print lexical order
if word1 < word2:
    print(f"'{word1}' comes before '{word2}'")
elif word1 > word2:
    print(f"'{word1}' comes after '{word2}'")
else:
    print(f"'{word1}' and '{word2}' are equal")

# Compare 'App' and 'Apple'
a, b = 'App', 'Apple'
if a < b:
    print(f"'{a}' comes before '{b}'")
elif a > b:
    print(f"'{a}' comes after '{b}'")
else:
    print(f"'{a}' and '{b}' are equal")

# ============================================================
# TRY/EXCEPT STRUCTURE
# ============================================================

# Wraps dangerous code that might cause errors
# If code in try block works, except block is skipped
# If code in try block fails, programme jumps to except block

# Example 1: Converting string to integer
astr = 'Hello Bob'

# Use try/except to convert astr to integer; if it fails, set istr to -1 and print the result
try:
    istr = int(astr)
except ValueError:
    istr = -1
print(istr)

astr = '123'

# Use try/except to convert astr to integer; if it fails, set istr to -1 and print the result
try:
    istr = int(astr)
except ValueError:
    istr = -1
print(istr)

# Example 2: User input validation
rawstr = input('Enter a number: ')

# Use try/except to convert rawstr to integer. If conversion fails, set ival to -1
try:
    ival = int(rawstr)
except ValueError:
    ival = -1

# Then check: if ival > 0 print 'Nice work', else print 'Not a number'
if ival > 0:
    print('Nice work')
else:
    print('Not a number')
