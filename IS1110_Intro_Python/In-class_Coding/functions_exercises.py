# FUNCTIONS - IN-CLASS PROGRAMMING EXAMPLES (STUDENT VERSION)
# IS1110 Python Programming

# ============================================================
# FUNCTION DEFINITION AND UTILITY
# ============================================================

# Functions are reusable blocks of code that perform specific tasks
# Benefits: code reuse, modularity, easier testing and debugging
# Syntax: def function_name(parameters):

# Define a function called greet that prints 'Hello'

def greet():
    print("Hello")

# Call the greet function

greet() 

# ============================================================
# BUILT-IN FUNCTIONS
# ============================================================

# Python provides many built-in functions
# Examples: print(), max(), min(), type(), int(), float(), str()

# Print the maximum of 5, 9, and 3

print(max(5, 9, 3))


# Print the minimum of 5, 9, and 3

print(min(5, 9, 3))


# Type conversion functions
age_str = '25'

# Convert age_str to an integer and assign to age_int
def age_convert(age_str):
    age_int = int(age_str)
    return age_int
    

# Print the type of age_int

print(type(age_convert(age_str)))


# Convert the string '19.99' to a float and assign to price_float

nineteen = "19.99"

def price_convert():
    price_float = float(nineteen)
    return price_float


# ============================================================
# USER-DEFINED FUNCTIONS WITH PARAMETERS
# ============================================================

# Parameters are variables in the function definition
# Arguments are the actual values passed when calling the function

# Define a function called greet_person that takes one parameter (name)
# and prints 'Hello, ' followed by the name

def greet_person(name):
    print(f"Hello, {name}")


# Call greet_person with the argument 'Alice'

greet_person("Alice")

# ============================================================
# MULTIPLE PARAMETERS
# ============================================================

# Functions can have multiple parameters
# Arguments in the function call are matched to parameters by position

# Define a function called add_two_numbers that takes two parameters (a and b)
# Calculate the sum and return it 

def add_two_numbers(a, b):
    sum = a + b
    return sum


# Call add_two_numbers with arguments 3 and 5, assign result in sum_result
sum_result = add_two_numbers(3, 5)

# Print sum_result
print(sum_result)


# ============================================================
# RETURN VALUES (FRUITFUL FUNCTIONS)
# ============================================================

# Fruitful functions return a value using the return statement
# The return statement ends function execution

# Define a function called calculate_area that takes length and width
# Calculate and return the area (length * width)
def calculate_area(length, width):
    area = length * width
    return area

# Call calculate_area with 5 and 4, assign to room_area

room_area = calculate_area(5,4)

# Print 'Area:' followed by room_area
print(f"Area: {room_area}m2")


# Function with conditional returns
# Define a function called get_grade that takes a score parameter
# If score >= 70, return 'Pass', otherwise return 'Fail'
def get_grade(score):
    if score >= 70:
        return "Pass"
    else:
        return "Fall"

# Call get_grade with 75 and print the result
print(get_grade(75))

# ============================================================
# RETURNING MULTIPLE VALUES
# ============================================================

# Functions can return multiple values at once
# The values are returned as a tuple (a collection of values)

# Define calculate_rectangle_properties that takes length and width
# Calculate area = length * width
# Calculate perimeter = 2 * (length + width)
# Return both area and perimeter (separated by comma)

def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


# Method 1: Assign both values to a single variable (gets a tuple)
# Call calculate_rectangle_properties(5, 3) and assign to result
# Then print 'Result:' followed by result
result = calculate_rectangle_properties(5, 3)
print(f"Result: {result}")

# Method 2: Assign each value to a distinct variable in a single statement
# This is called "unpacking"
# Call calculate_rectangle_properties(5, 3) and assign to two variables:
# area, perimeter = calculate_rectangle_properties(5, 3)
calculate_rectangle_properties(5, 3)
area, perimeter = calculate_rectangle_properties(5, 3)


# Print 'Area:' followed by area
print(f"Area: {area}")

# Print 'Perimeter:' followed by perimeter
print(f"Perimeter: {perimeter}")

# Another example with three return values
# Define get_student_info that takes name, score, and attendance
# Call get_grade(score) to get the grade
# If attendance >= 80, set status = 'Good standing', otherwise status = 'Warning'
# Return name, grade, and status (three values)
def get_student_info(name, score, attendance):
    get_grade(score)
    if attendance >= 80:
        status = "Good standing"
    else:
        status = "Warning"
    return name, score, status

# Call get_student_info('Alice', 85, 90) and unpack into three variables:
# student_name, student_grade, student_status = ...

student_name, student_grade, student_status = get_student_info('Alice', 85, 90)

# Print student_name, '-', student_grade, '-', student_status
print(f"{student_name} - {student_grade} - {student_status}")

# ============================================================
# VOID (NON-FRUITFUL) FUNCTIONS
# ============================================================

# Void functions perform actions but don't return a value
# They implicitly return None

# Define a function called print_message that takes a message parameter
# and prints it (no return statement)
def print_message(message):
    print(message)

# Call print_message with 'This is a void function'
print_message("This is a void function")

# Call print_message again and assign the result in a variable
# Then print that variable to see that it's None
message_var = print_message("This is a void function")
print(message_var)

# ============================================================
# PASSING ARGUMENTS: BY POSITION
# ============================================================

# Arguments matched to parameters based on their position

# Define a function called calculate_pay with parameters wage and hours
# If hours <= 40, amount = wage * hours
# Otherwise, amount = (wage * 40) + (1.5 * wage * (hours - 40))
# Return the amount

def calculate_pay(wage, hours):
    if hours <= 40:
        amount = wage * hours
    else:
        amount = (wage * 40) + (1.5 * wage * (hours - 40))
    return amount


# Call calculate_pay with wage=24.50 and hours=45
# Print 'Earnings: €' followed by the result
print(f"Earnings: €{calculate_pay(wage=24.5, hours=45)}")


# ============================================================
# PASSING ARGUMENTS: BY KEYWORD/NAME
# ============================================================

# Arguments can be passed using parameter names
# Order doesn't matter when using keywords

# Define a function called describe_pet with parameters animal_type and pet_name
# Print 'I have a', animal_type, 'named', pet_name
def describe_pet(animal_type, pet_name):
    print(f'I have a {animal_type} named {pet_name}')

# Call describe_pet using positional arguments: 'dog' and 'Rex'
describe_pet(animal_type="dog",pet_name="Rex")

# Call describe_pet using keyword arguments: pet_name='Whiskers', animal_type='cat'
# Notice the order doesn't matter with keyword arguments
describe_pet(pet_name="Whiskers", animal_type="cat")

# ============================================================
# PASSING ARGUMENTS: DEFAULT VALUES
# ============================================================

# Parameters can have default values
# Parameters with defaults must come last in the definition

# Define a function called greet_with_title with parameters name and title
# Set title to have a default value of 'Mr'
# Print 'Hello,', title, name
def greet_with_title(name, title="Mr"):
    print(f"Hello {title} {name}")


# Call greet_with_title with just 'Smith' (uses default title)
greet_with_title("Smith")

# Call greet_with_title with 'Jones' and 'Dr' (overrides default)
greet_with_title("Jones", "Dr")

# More complex example
# Define calculate_total with parameters: price, quantity (default=1), discount (default=0)
# Calculate: subtotal = price * quantity, then total = subtotal - discount
# Return total
def calculate_total(price, quantity=1, discount=0):
    subtotal = price * quantity
    total = subtotal - discount
    return total


# Call calculate_total with just price=10
calculate_total(10)

# Call calculate_total with price=10 and quantity=3
calculate_total(10, 3)

# Call calculate_total with price=10, quantity=3, and discount=5
calculate_total(10, 3, 5)

# ============================================================
# SCOPE OF VARIABLES: LOCAL SCOPE
# ============================================================

# Variables created inside a function are local to that function
# They only exist within the function and cease to exist when function ends

# TODO: Define a function called calculate_tax with parameters amount and tax_rate
# Create a local variable tax = amount * tax_rate
# Return tax


# TODO: Call calculate_tax with 100 and 0.20, assign to result


# TODO: Print 'Tax: €' followed by result


# Try uncommenting this line to see the error:
# print(tax)  # This causes an error - tax doesn't exist outside the function


# ============================================================
# SCOPE OF VARIABLES: GLOBAL SCOPE
# ============================================================

# Variables created in the main body of code are global
# Global variables can be read inside functions

company_name = 'Tech Corp'  # Global variable

# Define a function called print_company that prints company_name
# Note: you can read global variables without any special syntax

def print_company():
    print(company_name)

# Call print_company

print_company()

# ============================================================
# VARIABLE SHADOWING (NOT RECOMMENDED)
# ============================================================

# A local variable can have the same name as a global variable
# This "shadows" the global variable inside the function
# This is confusing and should be avoided

tax = 0.0  # Global variable

# Define calc_tax with parameters amount and tax_rate
# Create a local variable called tax (same name as global!)
# Calculate tax = amount * tax_rate
# Print 'Tax (local): €' followed by the tax

def calc_tax(amount, tax_rate):
    tax = amount * tax_rate
    print(f'Tax (local): €{tax}')

# Call calc_tax with 100 and 0.20

calc_tax(100, 0.2)

# Print 'Tax (global): €' followed by the global tax variable
print(f'Tax (global): €{tax}')


# ============================================================
# MODIFYING GLOBAL VARIABLES
# ============================================================

# To modify a global variable inside a function, use the global keyword
# Generally not recommended - better to use return values

counter = 0  # Global variable

# Define increment_counter function
# Use 'global counter' to declare you're modifying the global variable
# Increment counter by 1

def increment_counter():
    global counter 
    counter += 1 

# Call increment_counter twice
increment_counter()
increment_counter()

# Print 'Counter:' followed by counter
print(f"Counter: {counter}")

# ============================================================
# LIBRARY MODULES
# ============================================================

# Python provides many standard library modules
# Import modules to use their functions

# Using the datetime module
# Import the datetime module
import datetime

# Create a variable today = datetime.date.today()
today = datetime.date.today()

# Print 'Today:' followed by today
print(f"Today: {today}")

# Using specific functions from a module
# Import date and timedelta from the datetime module
from datetime import date, timedelta

# Calculate yesterday = date.today() - timedelta(days=1)
yesterday = date.today() - timedelta(days=1)

# Print 'Yesterday:' followed by yesterday
print(f"Yesterday: {yesterday}")

# Using the random module
# Import the random module
import random

# Print a random integer between 1 and 10
print(random.randint(1, 10))

# ============================================================
# RETURN STATEMENTS INSIDE CONDITIONALS
# ============================================================

# Return statements immediately exit the function
# Understanding this flow is important for writing efficient code

# Example 1: Multiple return statements
# Define check_age_category that takes age as parameter
# If age < 13, return 'Child'
# Elif age < 20, return 'Teenager'
# Elif age < 65, return 'Adult'
# Else return 'Senior'

def check_age_category(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenage"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

# Test your function with ages: 10, 16, 30, 70
check_age_category(10)
check_age_category(16)
check_age_category(30)
check_age_category(70)

# Example 2: Early return for validation
# Define divide_numbers that takes parameters a and b
# If b == 0, print 'Error: Cannot divide by zero' and return None
# Otherwise, return a / b

def divide_numbers(a, b):
    if b == 0:
        print("Error: Cannot divide by zero")
        return None
    else:
        return a / b

# Test with divide_numbers(10, 2) and divide_numbers(10, 0)
divide_numbers(10, 2) 
divide_numbers(10, 0)

# Example 3: Guard clauses (early returns for edge cases)
# Define calculate_discount_price that takes price and discount_code
# If price <= 0, return 0 (guard clause)
# If discount_code == 'SAVE10', return price * 0.9
# Elif discount_code == 'SAVE20', return price * 0.8
# Elif discount_code == 'SAVE50', return price * 0.5
# Else return price (no discount)

def calculate_discount_price(price, discount_code):
    if price <= 0:
        return 0
    if discount_code == 'SAVE10':
        return price * 0.9
    elif discount_code == 'SAVE20':
        return price * 0.8
    elif discount_code == 'SAVE50':
        return price * 0.5
    else:
        return price

# Test with:
# calculate_discount_price(100, 'SAVE20')
# calculate_discount_price(-50, 'SAVE20')
# calculate_discount_price(100, 'INVALID')

calculate_discount_price(100, 'SAVE20')
calculate_discount_price(-50, 'SAVE20')
calculate_discount_price(100, 'INVALID')

# ============================================================
# TWO WAYS TO WRITE FUNCTIONS WITH CONDITIONALS
# ============================================================

# There are two common styles for writing functions with conditionals.
# Both are correct - let's look at when to use each.

# STYLE 1: Multiple returns (exit as soon as you know the answer)
# Define get_grade_style1 that takes score as parameter
# If score >= 90, return 'A'
# Elif score >= 80, return 'B'
# Elif score >= 70, return 'C'
# Else return 'F'

def get_grade_style1(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else: 
        return "F"


# STYLE 2: Single return (store answer in variable first)
# Define get_grade_style2 that takes score as parameter
# If score >= 90, set grade = 'A'
# Elif score >= 80, set grade = 'B'
# Elif score >= 70, set grade = 'C'
# Else set grade = 'F'
# Then return grade

def get_grade_style2(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else: 
        grade = "F"
    return grade


# Test both functions with score 85 - they should give the same result

get_grade_style1(85)
get_grade_style2(85)

# When to use STYLE 1 (Multiple returns):
# - Simple functions where each condition gives a direct answer
# - When you want to exit the function as soon as you know the result
# - Generally easier to read and understand for beginners
# - This is the more common modern style

# When to use STYLE 2 (Single return):
# - When you need to do something with the result before returning
# - When you need to perform actions after determining the value

# Example of when STYLE 2 is better:
# Define calculate_final_price that takes price and discount_code
# If discount_code == 'SAVE10', set final_price = price * 0.9
# Elif discount_code == 'SAVE20', set final_price = price * 0.8
# Else set final_price = price
# Then print 'Processing payment of €' followed by final_price
# Then return final_price

def calculate_final_price(price, discount_code):
    if discount_code == 'SAVE10':
        final_price = price * 0.9
    elif discount_code == 'SAVE20':
        final_price = price * 0.8
    else: 
        final_price = price
    print(f'Processing payment of € {final_price}')
    return final_price

# Test with calculate_final_price(100, 'SAVE20')

calculate_final_price(100, 'SAVE20')

# For this course, we recommend STYLE 1 (multiple returns) for simple
# conditional functions because it's more straightforward: 
# "if this condition, give this answer immediately"


# ============================================================
# REFACTORING EXERCISE: IMPROVING CODE WITH FUNCTIONS
# ============================================================

# Refactoring means restructuring existing code to improve its design
# without changing its behaviour. Functions are key to good refactoring.

# BEFORE: Code with repetition (not using functions)
print('=== Original Code (Before Refactoring) ===')

# Calculate and display results for Student 1
student1_name = 'Alice'
student1_score = 85
student1_attendance = 90

if student1_score >= 70 and student1_attendance >= 80:
    student1_result = 'Pass'
else:
    student1_result = 'Fail'

print(student1_name + ': Score=' + str(student1_score) + ', Attendance=' + str(student1_attendance) + '%, Result=' + student1_result)

# Calculate and display results for Student 2
student2_name = 'Bob'
student2_score = 65
student2_attendance = 75

if student2_score >= 70 and student2_attendance >= 80:
    student2_result = 'Pass'
else:
    student2_result = 'Fail'

print(student2_name + ': Score=' + str(student2_score) + ', Attendance=' + str(student2_attendance) + '%, Result=' + student2_result)

# Calculate and display results for Student 3
student3_name = 'Charlie'
student3_score = 78
student3_attendance = 85

if student3_score >= 70 and student3_attendance >= 80:
    student3_result = 'Pass'
else:
    student3_result = 'Fail'

print(student3_name + ': Score=' + str(student3_score) + ', Attendance=' + str(student3_attendance) + '%, Result=' + student3_result)

# Problems with this code:
# 1. Repetitive - same logic copied multiple times
# 2. Hard to maintain - if pass criteria change, must update in multiple places
# 3. Error-prone - easy to make mistakes when copying code
# 4. Not scalable - adding more students means more copying


# AFTER: Refactored code using functions
print('\n=== Refactored Code (After) ===')

# ANALYSIS TASK: Before writing the refactored code, answer these questions:
# 1. Look at the code above. Which parts are repeated for each student?
# 2. What information changes between students (the data)?
# 3. What stays the same (the logic)?
# 4. How many functions do you think we need? What should each function do?
#
# Discuss with a classmate or think through these questions before proceeding.

# Define determine_result that takes score and attendance
# If score >= 70 AND attendance >= 80, return 'Pass'
# Otherwise, return 'Fail'

def determine_result(score, attendance):
    if score >= 70 and attendance >= 80:
        return "Pass"
    else:
        return "Fail"

# Define display_student_info that takes name, score, and attendance
# Call determine_result to get the result
# Print: name + ': Score=' + str(score) + ', Attendance=' + str(attendance) + '%, Result=' + result

def display_student_info(name, score, attendance):
    determine_result(score, attendance)
    print(f"{name}: Score = {score}, Attendance = {attendance}%, Result = {result}")
    

# Now use your functions to process the three students:

display_student_info('Alice', 85, 90)
display_student_info('Bob', 65, 75)
display_student_info('Charlie', 78, 85)


# Benefits of refactored code:
# 1. DRY (Don't Repeat Yourself) - logic written once
# 2. Maintainable - change pass criteria in one place
# 3. Readable - function names explain what code does
# 4. Testable - can test determine_result independently
# 5. Scalable - easy to process any number of students


# ============================================================
# PRACTICAL EXAMPLE: COMBINING CONCEPTS
# ============================================================

# Real-world scenario combining multiple function concepts

# Define calculate_discount with parameters:
# - price
# - discount_percent (default=0)
# - is_member (default=False)
# 
# Calculate: price_after_discount = price * (1 - discount_percent / 100)
# If is_member is True, subtract 5 from price_after_discount
# If price_after_discount < 0, set it to 0
# Return price_after_discount

def calculate_discount(price, discount_percent=0, is_member=False):
    price_after_discount = price * (1 - discount_percent / 100)
    if is_member == True:
        price_after_discount -= 5
    if price_after_discount < 0:
        price_after_discount = 0
    return price_after_discount


# Test the function with these calls and print each result with '€' before it:

calculate_discount(50)
calculate_discount(50, 10)
calculate_discount(50, 10, True)
calculate_discount(50, discount_percent=20, is_member=True)
