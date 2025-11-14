# OUTPUT FORMATTING - IN-CLASS PROGRAMMING EXAMPLES (PRACTICE VERSION)
# IS1110 Python Programming

# ============================================================
# PRINT ARGUMENTS - BASIC OUTPUT
# ============================================================

# print() can take multiple arguments separated by commas
# By default, print separates them with a space
print('Hello', 'World')
print('Name:', 'Alice', 'Age:', 25)

# sep parameter changes the separator between arguments
# TODO: Print 'Cork', 'Ireland', 'Europe' separated by ' | '


# TODO: Print '2025', '11', '12' separated by '-'


# end parameter changes what's printed at the end (default is newline)
print('Loading', end='...')
print('Done')

# Combining multiple print features
# TODO: Print 'Item', 'Quantity', 'Price' separated by ' | ' with double newline at end



# ============================================================
# ESCAPE SEQUENCES - SPECIAL CHARACTERS IN STRINGS
# ============================================================

# \n creates a new line
print('First line\nSecond line\nThird line')

# \t creates a horizontal tab
# TODO: Print 'Name:', then a tab, then 'Alice'


# TODO: Print 'Age:', then a tab, then 25


# TODO: Print 'City:', then a tab, then 'Cork'


# \\ prints a backslash character
# TODO: Print 'File path: C:\Users\Documents\file.txt' using \\


# \' prints a single quote inside a single-quoted string
# TODO: Print "It's a lovely day" using \'


# \" prints a double quote inside a double-quoted string
# TODO: Print 'She said "Hello" to me' using \"


# Combining escape sequences
# TODO: Print 'Line 1', newline, tab, 'Indented line 2', newline, 2 tabs, 'Double indented line 3'



# ============================================================
# STRING METHODS FOR ALIGNMENT
# ============================================================

# ljust(n) left-justifies a string in n characters
# TODO: Print 'Left' left-justified in 10 characters


# TODO: Print 'Text' left-justified in 15 characters


# rjust(n) right-justifies a string in n characters
# TODO: Print 'Right' right-justified in 10 characters


# TODO: Print 'Text' right-justified in 15 characters


# center(n) centres a string in n characters
# TODO: Print 'Centre' centred in 10 characters


# TODO: Print 'Text' centred in 15 characters


# Practical example: creating a simple table using string methods
# Ruler to visualise column positions
print('0123456789012345678901234567')
# TODO: Print 'Rank' left-justified(5), 'Player' left-justified(20), 'HR' right-justified(3), no separator


# TODO: Print '1' centred(5), 'Barry Bonds' left-justified(20), '762' right-justified(3), no separator


# TODO: Print '2' centred(5), 'Hank Aaron' left-justified(20), '755' right-justified(3), no separator


# TODO: Print '3' centred(5), 'Babe Ruth' left-justified(20), '714' right-justified(3), no separator



# ============================================================
# FORMAT METHOD - BASIC USAGE
# ============================================================

# format() replaces {} placeholders within a string with arguments
# Replacement happens in order
print('Hello, {}!'.format('Alice'))
print('I am {} years old'.format(25))

# TODO: Print 'Price: €19.99' using format()


# Multiple placeholders
# TODO: Print '5 + 3 = 8' using format() with three placeholders


# TODO: Print 'Name: Bob, Age: 30, City: Dublin' using format()


# Position indices allow reordering or reuse
# TODO: Print 'Hello World' using {0} and {1}


# TODO: Print 'World Hello' using {1} and {0}


# TODO: Print 'Echo Echo Echo' using {0} three times


# Mixing text and format placeholders
# TODO: Print 'The capital of Ireland is Dublin' using format()



# ============================================================
# F-STRINGS - BASIC USAGE (SIMPLER ALTERNATIVE)
# ============================================================

# f-strings provide a simpler syntax for formatting
# Put f before the opening quote and use {} for variables directly
name = 'Alice'
age = 25
print(f'Hello, {name}!')

# TODO: Print 'Alice is 25 years old' using f-string


# f-strings can include expressions inside {}
# TODO: Print '5 + 3 = 8' using f-string with expression


# TODO: Print '25 + 10 = 35' using f-string with age variable and expression


# Multiple variables in f-strings
city = 'Cork'
country = 'Ireland'
# TODO: Print 'Alice lives in Cork, Ireland' using f-string


# Comparison: format() vs f-string for basic use
# Using format():
print('Name: {}, Age: {}'.format(name, age))
# TODO: Print the same using f-string




# ============================================================
# FORMAT METHOD - STRUCTURE AND COMPONENTS
# ============================================================

# The curly bracket can include formatting commands
# Types are the kind of thing to substitute, numbers indicate total spaces

# Each bracket looks like: {:align width .precision descriptor}
# - align is optional (default left for strings, right for numbers)
# - width is how many spaces (default just enough)
# - .precision is for floating point rounding (default no rounding)
# - descriptor is the expected type (error if the argument is the wrong type)

# Common type descriptors:
# s - string
# d - decimal integer
# f - floating-point decimal
# e - floating-point exponential
# % - floating-point as percent

# Alignment options:
# < - left align
# > - right align
# ^ - centre

# Examples showing the structure:
# TODO: Print 'Hello' using {:s} format (string type)


# TODO: Print 42 using {:d} format (decimal integer type)


# TODO: Print 3.14159 using {:f} format (floating-point type)


# TODO: Print 'Hello' in a width of 10 spaces using {:10s}


# TODO: Print 3.14159 with width 10, 2 decimal places using {:10.2f}




# ============================================================
# FORMAT METHOD - ALIGNMENT AND WIDTH
# ============================================================

# Field width specifies minimum space for output
# Default alignment: strings left, numbers right
print('{:10}'.format('Left'))
print('{:10}'.format(123))

# < forces left alignment
# TODO: Print 'Left' left-aligned in 10 spaces using format()


# TODO: Print 123 left-aligned in 10 spaces using format()


# > forces right alignment
# TODO: Print 'Right' right-aligned in 10 spaces using format()


# TODO: Print 123 right-aligned in 10 spaces using format()


# ^ centres the output
# TODO: Print 'Centre' centred in 10 spaces using format()


# TODO: Print 123 centred in 10 spaces using format()


# Practical example: creating aligned columns with format()
# Ruler to visualise column positions
print('0123456789012345678901234567')
# TODO: Print 'Product' left-aligned in 15 spaces, 'Price' right-aligned in 10 spaces


# TODO: Print 'Coffee' left-aligned in 15 spaces, '€3.50' right-aligned in 10 spaces


# TODO: Print 'Tea' left-aligned in 15 spaces, '€2.80' right-aligned in 10 spaces



# ============================================================
# F-STRINGS - ALIGNMENT AND WIDTH
# ============================================================

# f-strings use the same format specifiers after a colon
# TODO: Print 'Left' left-aligned in 10 spaces using f-string


# TODO: Print 123 left-aligned in 10 spaces using f-string


# Right alignment in f-strings
# TODO: Print 'Right' right-aligned in 10 spaces using f-string


# TODO: Print 123 right-aligned in 10 spaces using f-string


# Centre alignment in f-strings
# TODO: Print 'Centre' centred in 10 spaces using f-string


# TODO: Print 123 centred in 10 spaces using f-string


# Same table example using f-strings
product1 = 'Coffee'
price1 = '€3.50'
product2 = 'Tea'
price2 = '€2.80'
# Ruler to visualise column positions
print('0123456789012345678901234567')
# TODO: Print 'Product' left-aligned in 15, 'Price' right-aligned in 10 using f-string


# TODO: Print product1 left-aligned in 15, price1 right-aligned in 10 using f-string


# TODO: Print product2 left-aligned in 15, price2 right-aligned in 10 using f-string



# ============================================================
# FORMAT METHOD - PRECISION AND TYPE DESCRIPTORS
# ============================================================

# .2f formats a float with 2 decimal places
price = 19.9
# TODO: Print 'Price: €19.90' using .2f format


# Different precision values
pi = 3.14159265359
# TODO: Print 'Pi to 2 decimal places: 3.14' using .2f


# TODO: Print 'Pi to 4 decimal places: 3.1416' using .4f


# d formats integers (decimal)
# TODO: Print 'Quantity: 42' using :d format


# s formats strings
# TODO: Print 'Name: Alice' using :s format


# Combining width and precision
# TODO: Print 123.456 with width 10 and 2 decimal places


# TODO: Print 9.9 with width 10 and 2 decimal places


# Combining alignment, width, and precision
# TODO: Print 123.456 left-aligned, width 10, 2 decimal places


# TODO: Print 123.456 right-aligned, width 10, 2 decimal places


# TODO: Print 123.456 centred, width 10, 2 decimal places


# Thousands separator using comma
large_number = 1234567
# TODO: Print large_number with thousands separators


# TODO: Print 12345.678 with thousands separators and 2 decimal places


# Combining thousands separator with width and alignment
# TODO: Print 1234567 with thousands separators, width 15


# TODO: Print 12345.678 right-aligned, width 15, thousands separators, 2 decimals


# Percentage formatting
decimal_value = 0.235
# TODO: Print decimal_value as percentage with 2 decimal places


# TODO: Print 0.5 as percentage with 1 decimal place


# Combining percentage with width
# TODO: Print 0.235 as percentage, width 10, 2 decimal places


# TODO: Print 0.5 as percentage, right-aligned, width 10, 1 decimal place



# ============================================================
# F-STRINGS - PRECISION AND TYPE DESCRIPTORS
# ============================================================

# f-strings with precision
price = 19.99
# TODO: Print 'Price: €19.99' using f-string with .2f


pi = 3.14159265359
# TODO: Print 'Pi to 2 decimal places: 3.14' using f-string


# TODO: Print 'Pi to 4 decimal places: 3.1416' using f-string


# f-strings with thousands separator
large_number = 1234567
# TODO: Print large_number with thousands separators using f-string


# TODO: Print 12345.678 with thousands separators and 2 decimals using f-string


# f-strings with percentage
decimal_value = 0.235
# TODO: Print decimal_value as percentage with 2 decimals using f-string


# TODO: Print 0.5 as percentage with 1 decimal using f-string


# f-strings combining alignment, width, precision, and special formatting
value = 12345.678
# TODO: Print value right-aligned, width 15, thousands separators, 2 decimals


percentage = 0.235
# TODO: Print percentage right-aligned, width 10, as percentage with 2 decimals



# ============================================================
# PRACTICAL EXAMPLES - COMBINING TECHNIQUES
# ============================================================

# Example 1: Product list with prices using format()
print('\n=== Product List (using format()) ===')
# TODO: Print headers 'Item' and 'Price' using format()


print('-' * 30)
# TODO: Print 'Laptop' and €899.99 using format()


# TODO: Print 'Mouse' and €15.50 using format()


# TODO: Print 'Keyboard' and €45.00 using format()


# Example 1: Same product list using f-strings
print('\n=== Product List (using f-strings) ===')
# TODO: Print headers 'Item' and 'Price' using f-string


print('-' * 30)
# TODO: Print 'Laptop' and €899.99 using f-string


# TODO: Print 'Mouse' and €15.50 using f-string


# TODO: Print 'Keyboard' and €45.00 using f-string


# Example 2: Student results table with format()
print('\n=== Student Results ===')
# TODO: Print headers 'Name', 'Mark', 'Grade' with proper alignment


print('-' * 35)
# TODO: Print 'Alice', 85, 'First' with proper alignment


# TODO: Print 'Bob', 67, 'Second' with proper alignment


# TODO: Print 'Charlie', 52, 'Pass' with proper alignment


# Example 3: Financial report with f-strings and calculations
income = 850.00
rent = 650.00
groceries = 80.00
utilities = 75.00
total = rent + groceries + utilities
remaining = income - total

print('\n=== Monthly Budget ===')
# TODO: Print 'Income' and value using f-string with € and 2 decimals


# TODO: Print 'Rent' and value using f-string with € and 2 decimals


# TODO: Print 'Groceries' and value using f-string with € and 2 decimals


# TODO: Print 'Utilities' and value using f-string with € and 2 decimals


print('-' * 28)
# TODO: Print 'Total Expenses' and total using f-string with € and 2 decimals


# TODO: Print 'Remaining' and remaining using f-string with € and 2 decimals


# Example 4: Sales report with percentages and thousands separator
product = 'Premium Laptop'
units_sold = 1234
unit_price = 1299.99
revenue = units_sold * unit_price
target_revenue = 2000000
percentage_of_target = revenue / target_revenue

print('\n=== Sales Report ===')
# TODO: Print 'Product:' and product name using f-string


# TODO: Print 'Units Sold:' and units with thousands separator


# TODO: Print 'Unit Price:' and price with € and 2 decimals


# TODO: Print 'Total Revenue:' with €, thousands separator, and 2 decimals


# TODO: Print 'Target:' with €, thousands separator, and 2 decimals


# TODO: Print 'Achievement:' as percentage with 1 decimal place


# Example 5: Comparison table showing format() vs f-strings
print('\n=== Comparing format() and f-strings ===')
item = 'Coffee'
quantity = 3
price_per_unit = 3.50
total_price = quantity * price_per_unit

print('Using format():')
# TODO: Print item, quantity, and total using format()


print('Using f-string:')
# TODO: Print item, quantity, and total using f-string

