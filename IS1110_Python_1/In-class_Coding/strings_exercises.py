# STRINGS - IN-CLASS PROGRAMMING EXAMPLES (PRACTICE VERSION)
# IS1110 Python Programming

# ============================================================
# STRING TYPE BASICS
# ============================================================

# A string is a sequence of characters enclosed in quotes
# Strings can use single or double quotes

# Create variable greeting with value 'Hello'
greeting = 'Hello'

# Create variable name with value "World"
name = "World"

# Print both greeting and name
print(greeting + name)

# Strings are objects that have methods and properties
# Create variable text with value 'Python'
text = 'Python'

# Print the type of text using type()
print(type(text))

# Strings are immutable - they cannot be changed after creation
# Any operation that modifies a string creates a new string


# ============================================================
# READING AND CONVERTING STRINGS
# ============================================================

# input() always returns a string, even if the user enters a number

# Get name from user with prompt 'Enter your name: '
name = input('Enter your name: ')

# Print 'Hello, ' concatenated with name
print('Hello, ' + name)

# Convert string to integer or float when needed
# Get age from user as string with prompt 'Enter your age: '
age = input('Enter your age: ')
age_str = age

# Convert age_str to integer and assign to age
age = int(age)

# Print 'Next year you will be' followed by age + 1
print("Next year you will be", age + 1)

# Convert numbers to strings for concatenation
# Create variable score with value 95
score = 95

# Create message variable: 'Your score is ' concatenated with str(score)
message = str(score)

# Print message
print("Your score is " + message)


# ============================================================
# INDEXING STRINGS
# ============================================================

# Each character in a string has a position (index) starting from 0
# Use square brackets [] to access individual characters

# Create variable word with value 'Python'
word = 'Python'

# Print word[0] (first character)
print(word[0])

# Print word[1] (second character)
print(word[1])

# Print word[5] (last character)
print(word[5])

# Negative indices count from the end
# Print word[-1] (last character)
print(word[-1])

# Print word[-2] (second to last)
print(word[-2])

# Index out of range causes an error
# print(word[10])  # IndexError


# ============================================================
# STRING LENGTH
# ============================================================

# len() returns the number of characters in a string

# Create variable word with value 'Python'
word = 'Python'

# Create variable length using len(word)
length = len(word)

# Print 'Length:' and length
print("Length:", length)

# Length is useful for accessing the last character
# Create variable last_index = len(word) - 1
last_index = len(word) - 1

# Print word[last_index]
print(word[last_index])

# Empty string has length 0
# Create variable empty with value ''
empty = ''

# Print len(empty)
print(len(empty))


# ============================================================
# LOOPING THROUGH STRINGS
# ============================================================

# Use a for loop to iterate through each character

# Create variable word with value 'Python'
word = 'Python'

# Loop through each letter in word and print letter
for letter in word:
    print(letter)


# Count specific characters in a string
# Create variable text with value 'banana'
text = 'banana'

# Initialise count = 0
count = 0

# Loop through each letter in text
# If letter equals 'n', increment count
for letter in text:
    if letter == 'n':
        count += 1


# Print 'Number of n:' and count
print("Number of n:", count)

# Loop using index with range(len())
# Create variable word with value 'Hello'
word = 'Hello'

# Loop using range(len(word)) with variable i
# Print i and word[i]
for i in range(len(word)):
    print(i, word[i])


# ============================================================
# SLICING STRINGS
# ============================================================

# Extract a substring using [start:end]
# Start is inclusive, end is exclusive

# Create variable text with value 'Hello World'
text = "Hello World"

# Print text[0:5]
print(text[0:5])

# Print text[6:11]
print(text[6:11])

# Omit start to begin from the beginning
# Print text[:5]
print(text[:5])

# Omit end to go to the end
# Print text[6:]
print(text[6:])

# Negative indices work in slicing
# Print text[-5:]
print(text[-5:])

# Extended slicing with step [start:end:step]
# Print text[::2] (every other character)
print(text[::2])

# Print text[::-1] (reverse string)
print(text[::-1])


# ============================================================
# CONCATENATING STRINGS
# ============================================================

# Use + operator to join strings together
# The + operator does not add spaces automatically
# You must add space characters manually if needed

# Create variable first with value 'Hello'
first = 'Hello'

# Create variable second with value 'World'
second = 'World'

# Create result by concatenating first + ' ' + second
result = first + " " + second

# Print result
print(result)

# Concatenate multiple strings
# Create greeting by concatenating 'Good' + ' ' + 'morning' + '!'
greeting = 'Good' + ' ' + 'morning' + '!'

# Print greeting
print(greeting)

# Cannot concatenate string and number directly
# text = 'Number: ' + 42  # TypeError
# Create text by concatenating 'Number: ' + str(42)
text = 'Number: ' + str(42)

# Print text
print(text)


# ============================================================
# REPEATING STRINGS
# ============================================================

# Use * operator to repeat a string

# Create variable line with value '=' * 20
line = '=' * 20

# Print line
print(line)

# Repeat words
# Create echo with value 'Hello ' * 3
echo = 'Hello ' * 3

# Print echo
print(echo)

# Useful for creating patterns
# Create border with value '-' * 30
border = '-' * 30

# Print border, then 'Title', then border again
print(border + '\n' + 'Title' + '\n' + border)



# Create a border that matches the length of a title
# Create title with value 'Python Programming'
title = 'Python Programming'

# Create dynamic_border with value '-' * len(title)
dynamic_border = '-' * len(title)

# Print dynamic_border, then title, then dynamic_border again
print(dynamic_border + '\n' + title + '\n' + dynamic_border)



# ============================================================
# STRING COMPARISONS
# ============================================================

# Compare strings using relational operators: <, >, ==, !=, <=, >=
# Comparison is based on ASCII values (alphabetical order)
# Python compares strings character by character from left to right

# Print result of 'apple' < 'banana'
print('apple' < 'banana')

# Print result of 'zebra' > 'aardvark'
print("zebra" > "aardvark")

# Print result of 'hello' == 'Hello'
print('hello' == 'Hello')

# When comparing character by character, if all characters match but one string ends first,
# the shorter string is considered less than the longer string
# Print result of 'Hell' < 'Hello'
print('Hell' < 'Hello')

# More comparison examples:
# Print result of '' < 'abc' (the empty string is less than any other string)
print('' < 'abc')

# Print result of 'abc' < 'abd' (different at index 2, i.e. 'c' < 'd')
print('abc' < 'abd')

# Print result of 'abc' < 'abcd' (equal up to 'abc' but 'abc' is shorter)
print('abc' < 'abcd')

# Uppercase letters come before lowercase in ASCII
# Print result of 'A' < 'a'
print('A' < 'a')

# Print result of 'Z' < 'a'
print('Z' < 'a')

# Numbers as strings compare lexicographically, not numerically
# Print result of '10' < '2'
print('10' < '2')


# ============================================================
# THE IN OPERATOR
# ============================================================

# Check if a substring exists within a string
# The in keyword is a logical operator that returns True or False
# The in expression can be used in an if statement

# Create variable text with value 'Hello World'
text = 'Hello World'

# Print result of 'World' in text
print('World' in text)

# Print result of 'Python' in text
print('Python' in text)

# Print result of 'lo W' in text
print('lo W' in text)

# Use 'not in' to check if substring is absent
# Print result of 'Python' not in text
print('Python' not in text)

# Case sensitive
# Print result of 'world' in text
print('world' in text)

# Using in with if statement
# Check if 'Hello' in text and print 'Found Hello in text'
if 'Hello' in text:
    print('Found Hello in text')


# ============================================================
# STRING METHODS: CASE CONVERSION
# ============================================================

# upper() converts all characters to uppercase
# lower() converts all characters to lowercase

# Create variable text with value 'Hello World'
text = 'Hello World'

# Print text.upper()
print(text.upper())

# Print text.lower()
print(text.lower())

# Original string is unchanged (strings are immutable)
# Print text
print(text)

# capitalize() makes first letter uppercase, rest lowercase
# Print 'hello world'.capitalize()
print('hello world'.capitalize())

# Print 'HELLO WORLD'.capitalize()
print('HELLO WORLD'.capitalize())

# title() capitalises first letter of each word
# Print 'hello world'.title()
print('hello world'.title())


# ============================================================
# STRING METHODS: SEARCHING
# ============================================================

# find() returns index of first occurrence, or -1 if not found

# Create variable text with value 'Hello World'
text = 'Hello World'

# Create variable pos using text.find('World')
pos = text.find('World')

# Print pos
print(pos)

# Assign pos = text.find('Python')
pos = text.find('Python')

# Print pos
print(pos)

# Find single character
# Assign pos = text.find('o')
pos = text.find('o')

# Print pos
print(pos)

# rfind() searches from the right (last occurrence)
# Assign pos = text.rfind('o')
pos = text.rfind('o')

# Print pos
print(pos)

# Can specify start and end positions
# Assign pos = text.find('o', 5) to search from index 5 onwards
pos = text.find('o', 5)

# Print pos
print(pos)


# ============================================================
# STRING METHODS: COUNTING
# ============================================================

# count() returns number of non-overlapping occurrences

# Create variable text with value 'banana'
text = 'banana'

# Print text.count('a')
print(text.count('a'))

# Print text.count('an')
print(text.count('an'))

# Print text.count('x')
print(text.count('x'))

# Assign text = 'Hello World'
text = 'Hello World'

# Print text.count('l')
print(text.count('l'))

# Print text.count('o')
print(text.count('o'))


# ============================================================
# STRING METHODS: REPLACING
# ============================================================

# replace() returns new string with replacements made

# Create variable text with value 'Hello World'
text = 'Hello World'

# Create new_text using text.replace('World', 'Python')
new_text = text.replace('World', 'Python')

# Print new_text
print(new_text)

# Print text (original unchanged)
print(text)

# Replace all occurrences
# Assign text = 'banana'
text = 'banana'

# Assign new_text = text.replace('a', 'o')
new_text = text.replace('a', 'o')

# Print new_text
print(new_text)

# Optional third argument limits number of replacements
# Assign text = 'banana'
text = 'banana'

# Assign new_text = text.replace('a', 'o', 2) to replace only first 2
new_text = text.replace('a', 'o',2)

# Print new_text
print(new_text)


# ============================================================
# STRING METHODS: WHITESPACE REMOVAL
# ============================================================

# strip() removes leading and trailing whitespace
# lstrip() removes leading whitespace only
# rstrip() removes trailing whitespace only

# Create variable text with value '   Hello World   '
text = '   Hello World   '

# Print '[' + text.strip() + ']'
print('[' + text.strip() + ']')

# Print '[' + text.lstrip() + ']'
print('[' + text.lstrip() + ']')

# Print '[' + text.rstrip() + ']'
print('[' + text.rstrip() + ']')

# Can remove specific characters instead of whitespace
# Assign text = '###Hello###'
text = '###Hello###'

# Print text.strip('#')
print(text.strip('#'))

# Useful for cleaning user input
# Get name from user and apply .strip() to clean it
name = input('Enter your name: ')
print(name.strip())


# ============================================================
# STRING METHODS: SPLITTING
# ============================================================

# split() breaks a string into a list of substrings
# By default, splits on whitespace

# Create variable text with value 'Hello World Python'
text = 'Hello World Python'

# Create variable words using text.split()
words = text.split()

# Print words
print(words)

# Specify delimiter
# Assign text = 'apple,banana,orange'
text = 'apple,banana,orange'

# Create variable fruits using text.split(',')
fruits = text.split(',')

# Print fruits
print(fruits)

# Can assign to multiple variables if you know the count
# Assign text = 'John Doe'
text = 'John Doe'

# Assign first_name, last_name = text.split()
first_name , last_name = text.split()

# Print first_name
print(first_name)

# Print last_name
print(last_name)

# Split on specific character
# Assign email = 'user@example.com'
email = 'user@example.com'

# Create variable parts using email.split('@')
parts = email.split('@')

# Print parts
print(parts)


# ============================================================
# COMBINING STRING OPERATIONS
# ============================================================

# Use multiple string operations together
# Methods can be chained - the result of one method becomes the input to the next

# Clean and process user input
# Create user_input with value '  HELLO world  '
user_input = '  HELLO world  '

# Create cleaned using user_input.strip().lower()
cleaned = user_input.strip().lower()

# Print cleaned
print(cleaned)

# Search case-insensitively
# Create text with value 'Hello World'
text = 'Hello World'

# Create search_term with value 'WORLD'
search_term = 'WORLD'

# Use if statement to check if search_term.lower() in text.lower()
# Print 'Found'
if search_term.lower() in text.lower():
    print('Found')


# Extract and modify parts of strings
# Create email with value 'John.Doe@Example.COM'
email = 'John.Doe@Example.COM'

# Create parts using email.split('@')
parts = email.split('@')

# Create username = parts[0].lower()
username = parts[0].lower()

# Create domain = parts[1].lower()
domain = parts[1].lower()

# Create clean_email by concatenating username + '@' + domain
clean_email = username + '@' + domain

# Print clean_email
print(clean_email)


# ============================================================
# PRACTICAL EXAMPLE: EMAIL VALIDATION
# ============================================================

# Check if string is a valid email format

# Get email from user, apply .strip().lower()
email = input('Enter your email address: ')
email = email.strip().lower()

# Check if '@' in email and '.' in email
# Create at_pos using email.find('@')
# Create dot_pos using email.rfind('.')
# Check if at_pos > 0 and dot_pos > at_pos + 1 and dot_pos < len(email) - 1
# Print 'Email format looks valid' or 'Invalid email format' as appropriate

if '@' in email and '.' in email:
    at_pos = email.find('@')
    dot_pos = email.rfind('.')
    if at_pos > 0 and dot_pos > at_pos + 1 and dot_pos < len(email) - 1:
        print('Email format looks valid')
    else:
        print('Invalid email format')