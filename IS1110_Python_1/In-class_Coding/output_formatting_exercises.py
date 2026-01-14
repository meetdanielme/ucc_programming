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
# Print 'Cork', 'Ireland', 'Europe' separated by ' | '
print("Cork", "Ireland", "Europe", sep=" | ")

# Print '2025', '11', '12' separated by '-'
print("2025", "11", "12", sep="-")

# end parameter changes what's printed at the end (default is newline)
print('Loading', end='...')
print('Done')

# Combining multiple print features
# Print 'Item', 'Quantity', 'Price' separated by ' | ' with double newline at end
print("Item", "Quantity", "Price", sep=" | ", end="\n\n")


# ============================================================
# ESCAPE SEQUENCES - SPECIAL CHARACTERS IN STRINGS
# ============================================================

# \n creates a new line
print('First line\nSecond line\nThird line')

# \t creates a horizontal tab
# Print 'Name:', then a tab, then 'Alice'
print("Name:\tAlice")

# Print 'Age:', then a tab, then 25
print("Age:\t25")

# Print 'City:', then a tab, then 'Cork'
print("City:\tCork")

# \\ prints a backslash character
# Print 'File path: C:\Users\Documents\file.txt' using \\
print("File path: C:\\Users\\Documents\\file.txt")

# \' prints a single quote inside a single-quoted string
# Print "It's a lovely day" using \'
print('It\'s a lovely day')

# \" prints a double quote inside a double-quoted string
# Print 'She said "Hello" to me' using \"
print("She said \"Hello\" to me")

# Combining escape sequences
# Print 'Line 1', newline, tab, 'Indented line 2', newline, 2 tabs, 'Double indented line 3'
print('Line 1\n\tIndented line 2\n\t\tDouble indented line 3')


# ============================================================
# STRING METHODS FOR ALIGNMENT
# ============================================================

# ljust(n) left-justifies a string in n characters
# Print 'Left' left-justified in 10 characters
print('Left'.ljust(10))

# Print 'Text' left-justified in 15 characters
print('Text'.ljust(15))

# rjust(n) right-justifies a string in n characters
# Print 'Right' right-justified in 10 characters
print('Right'.rjust(10))

# Print 'Text' right-justified in 15 characters
print('Text'.rjust(15))

# center(n) centres a string in n characters
# Print 'Centre' centred in 10 characters
print('Centre'.center(10))

# Print 'Text' centred in 15 characters
print('Text'.center(15))

# Practical example: creating a simple table using string methods
# Ruler to visualise column positions
print('0123456789012345678901234567')
# Print 'Rank' left-justified(5), 'Player' left-justified(20), 'HR' right-justified(3), no separator
print('Rank'.ljust(5) + 'Player'.ljust(20) + 'HR'.rjust(3))

# Print '1' centred(5), 'Barry Bonds' left-justified(20), '762' right-justified(3), no separator
print('1'.center(5) + 'Barry Bonds'.ljust(20) + '762'.rjust(3))

# Print '2' centred(5), 'Hank Aaron' left-justified(20), '755' right-justified(3), no separator
print('2'.center(5) + 'Hank Aaron'.ljust(20) + '755'.rjust(3))

# Print '3' centred(5), 'Babe Ruth' left-justified(20), '714' right-justified(3), no separator
print('3'.center(5) + 'Babe Ruth'.ljust(20) + '714'.rjust(3))


# ============================================================
# FORMAT METHOD - BASIC USAGE
# ============================================================

# format() replaces {} placeholders within a string with arguments
# Replacement happens in order
print('Hello, {}!'.format('Alice'))
print('I am {} years old'.format(25))

# Print 'Price: €19.99' using format()
print('Price: €{}'.format(19.99))

# Multiple placeholders
# Print '5 + 3 = 8' using format() with three placeholders
print('{} + {} = {}'.format(5, 3, 8))

# Print 'Name: Bob, Age: 30, City: Dublin' using format()
print('Name: {}, Age: {}, City: {}'.format('Bob', 30, 'Dublin'))

# Position indices allow reordering or reuse
# Print 'Hello World' using {0} and {1}
print('{0} {1}'.format('Hello', 'World'))

# Print 'World Hello' using {1} and {0}
print('{1} {0}'.format('Hello', 'World'))

# Print 'Echo Echo Echo' using {0} three times
print('{0} {0} {0}'.format('Echo'))

# Mixing text and format placeholders
# Print 'The capital of Ireland is Dublin' using format()
print('The capital of Ireland is {}'.format('Dublin'))


# ============================================================
# F-STRINGS - BASIC USAGE (SIMPLER ALTERNATIVE)
# ============================================================

# f-strings provide a simpler syntax for formatting
# Put f before the opening quote and use {} for variables directly
name = 'Alice'
age = 25
print(f'Hello, {name}!')

# Print 'Alice is 25 years old' using f-string
print(f'{name} is {age} years old')

# f-strings can include expressions inside {}
# Print '5 + 3 = 8' using f-string with expression
print(f'5 + 3 = {5 + 3}')

# Print '25 + 10 = 35' using f-string with age variable and expression
print(f'{age} + 10 = {age + 10}')

# Multiple variables in f-strings
city = 'Cork'
country = 'Ireland'
# Print 'Alice lives in Cork, Ireland' using f-string
print(f'{name} lives in {city}, {country}')

# Comparison: format() vs f-string for basic use
# Using format():
print('Name: {}, Age: {}'.format(name, age))
# Print the same using f-string
print(f'Name: {name}, Age: {age}')



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
# Print 'Hello' using {:s} format (string type)
print('{:s}'.format('Hello'))

# Print 42 using {:d} format (decimal integer type)
print('{:d}'.format(42))

# Print 3.14159 using {:f} format (floating-point type)
print('{:f}'.format(3.14159))

# Print 'Hello' in a width of 10 spaces using {:10s}
print("{:10s}".format('Hello'))

# Print 3.14159 with width 10, 2 decimal places using {:10.2f}
print("{:10.2f}".format(3.14159))



# ============================================================
# FORMAT METHOD - ALIGNMENT AND WIDTH
# ============================================================

# Field width specifies minimum space for output
# Default alignment: strings left, numbers right
print('{:10}'.format('Left'))
print('{:10}'.format(123))

# < forces left alignment
# Print 'Left' left-aligned in 10 spaces using format()
print('{:<10}'.format('Left'))

# Print 123 left-aligned in 10 spaces using format()
print('{:<10}'.format(123))

# > forces right alignment
# Print 'Right' right-aligned in 10 spaces using format()
print('{:>10}'.format('Right'))

# Print 123 right-aligned in 10 spaces using format()
print('{:>10}'.format(123))

# ^ centres the output
# Print 'Centre' centred in 10 spaces using format()
print('{:^10}'.format('Centre'))

# Print 123 centred in 10 spaces using format()
print('{:^10}'.format('123'))

# Practical example: creating aligned columns with format()
# Ruler to visualise column positions
print('0123456789012345678901234567')
# Print 'Product' left-aligned in 15 spaces, 'Price' right-aligned in 10 spaces
print('{:<15}{:>10}'.format('Product', 'Price'))

# Print 'Coffee' left-aligned in 15 spaces, '€3.50' right-aligned in 10 spaces
print('{:<15}{:>10}'.format('Coffee', '€3.50'))

# Print 'Tea' left-aligned in 15 spaces, '€2.80' right-aligned in 10 spaces
print('{:<15}{:>10}'.format('Tea', '€2.80'))


# ============================================================
# F-STRINGS - ALIGNMENT AND WIDTH
# ============================================================

# f-strings use the same format specifiers after a colon
# Print 'Left' left-aligned in 10 spaces using f-string
print(f'{"Left":<10}')

# Print 123 left-aligned in 10 spaces using f-string
print(f'{"Right":<10}')

# Right alignment in f-strings
# Print 'Right' right-aligned in 10 spaces using f-string
print(f'{"Right":>10}')

# Print 123 right-aligned in 10 spaces using f-string
print(f'{"123":>10}')

# Centre alignment in f-strings
# Print 'Centre' centred in 10 spaces using f-string
print(f'{"Centre":^10}')

# Print 123 centred in 10 spaces using f-string
print(f'{"123":^10}')

# Same table example using f-strings
product1 = 'Coffee'
price1 = '€3.50'
product2 = 'Tea'
price2 = '€2.80'
# Ruler to visualise column positions
print('0123456789012345678901234567')
# Print 'Product' left-aligned in 15, 'Price' right-aligned in 10 using f-string
print(f'{"Product":<15}{"Price":>10}')

# Print product1 left-aligned in 15, price1 right-aligned in 10 using f-string
print(f'{product1:<15}{price1:>10}')

# Print product2 left-aligned in 15, price2 right-aligned in 10 using f-string
print(f'{product2:<15}{price2:>10}')


# ============================================================
# FORMAT METHOD - PRECISION AND TYPE DESCRIPTORS
# ============================================================

# .2f formats a float with 2 decimal places
price = 19.9
# Print 'Price: €19.90' using .2f format
print('Price: €{:.2f}'.format(price))

# Different precision values
pi = 3.14159265359
# Print 'Pi to 2 decimal places: 3.14' using .2f
print('Pi to 2 decimal places: {:.2f}'.format(pi))

# Print 'Pi to 4 decimal places: 3.1416' using .4f
print('Pi to 4 decimal places: {:.4f}'.format(pi))

# d formats integers (decimal)
# Print 'Quantity: 42' using :d format
print('Quantity: {:d}'.format(42))

# s formats strings
# Print 'Name: Alice' using :s format
print('Name: {:s}'.format('Alice'))

# Combining width and precision
# Print 123.456 with width 10 and 2 decimal places
print('{:10.2f}'.format(123.456))

# Print 9.9 with width 10 and 2 decimal places
print('{:10.2f}'.format(9.9))

# Combining alignment, width, and precision
# Print 123.456 left-aligned, width 10, 2 decimal places
print('{:<10.2f}'.format(123.456))

# Print 123.456 right-aligned, width 10, 2 decimal places
print('{:>10.2f}'.format(123.456))

# Print 123.456 centred, width 10, 2 decimal places
print('{:^10.2f}'.format(123.456))

# Thousands separator using comma
large_number = 1234567
# Print large_number with thousands separators
print('{:,}'.format(large_number))

# Print 12345.678 with thousands separators and 2 decimal places
print('{:,.2f}'.format(12345.678))

# Combining thousands separator with width and alignment
# Print 1234567 with thousands separators, width 15
print('{:15,}'.format(1234567))

# Print 12345.678 right-aligned, width 15, thousands separators, 2 decimals
print('{:>15,.2f}'.format(12345.678))

# Percentage formatting
decimal_value = 0.235
# Print decimal_value as percentage with 2 decimal places
print('{:.2%}'.format(decimal_value))

# Print 0.5 as percentage with 1 decimal place
print('{:.1%}'.format(0.5))

# Combining percentage with width
# Print 0.235 as percentage, width 10, 2 decimal places
print('{:10.2%}'.format(0.235))

# Print 0.5 as percentage, right-aligned, width 10, 1 decimal place
print('{:>10.1%}'.format(0.5))


# ============================================================
# F-STRINGS - PRECISION AND TYPE DESCRIPTORS
# ============================================================

# f-strings with precision
price = 19.99
# Print 'Price: €19.99' using f-string with .2f
print(f'Price: €{price:.2f}')

pi = 3.14159265359
# Print 'Pi to 2 decimal places: 3.14' using f-string
print(f'Pi to 2 decimal places: {pi:.2f}')

# Print 'Pi to 4 decimal places: 3.1416' using f-string
print(f'Pi to 4 decimal places: {pi:.4f}')

# f-strings with thousands separator
large_number = 1234567
# Print large_number with thousands separators using f-string
print(f"{large_number:,}")

# Print 12345.678 with thousands separators and 2 decimals using f-string
print(f"{12345.678:,.2f}")

# f-strings with percentage
decimal_value = 0.235
# Print decimal_value as percentage with 2 decimals using f-string
print(f"{decimal_value:.2%}")

# Print 0.5 as percentage with 1 decimal using f-string
print(f"{0.5:.1%}")

# f-strings combining alignment, width, precision, and special formatting
value = 12345.678
# Print value right-aligned, width 15, thousands separators, 2 decimals
print(f"{value:>15,.2f}")

percentage = 0.235
# Print percentage right-aligned, width 10, as percentage with 2 decimals
print(f"{percentage:>10.2%}")


# ============================================================
# PRACTICAL EXAMPLES - COMBINING TECHNIQUES
# ============================================================

# Example 1: Product list with prices using format()
print('\n=== Product List (using format()) ===')
# Print headers 'Item' and 'Price' using format()
print('{:<15}{:>10}'.format('Item', 'Price'))

print('-' * 30)
# Print 'Laptop' and €899.99 using format()
print('{:<15}{:>10}'.format('Laptop', '€899.99'))

# Print 'Mouse' and €15.50 using format()
print('{:<15}{:>10}'.format('Mouse', '€15.50'))

# Print 'Keyboard' and €45.00 using format()
print('{:<15}{:>10}'.format('Keyboard', '€45.00'))

# Example 1: Same product list using f-strings
print('\n=== Product List (using f-strings) ===')
# Print headers 'Item' and 'Price' using f-string
print('{:<15}{:>10}'.format('Item', 'Price'))

print('-' * 30)
# Print 'Laptop' and €899.99 using f-string
print('{:<15}{:>10}'.format('Laptop', '€899.99'))

# Print 'Mouse' and €15.50 using f-string
print('{:<15}{:>10}'.format('Mouse', '€15.50'))

# Print 'Keyboard' and €45.00 using f-string
print('{:<15}{:>10}'.format('Keyboard', '€45.00'))

# Example 2: Student results table with format()
print('\n=== Student Results ===')
# Print headers 'Name', 'Mark', 'Grade' with proper alignment
print('{:<10}{:>6}{:>10}'.format('Name', 'Mark', 'Grade'))

print('-' * 35)
# Print 'Alice', 85, 'First' with proper alignment
print('{:<10}{:>6}{:>10}'.format('Alice', 85, 'First'))

# Print 'Bob', 67, 'Second' with proper alignment
print('{:<10}{:>6}{:>10}'.format('Bob', 67, 'Second'))

# Print 'Charlie', 52, 'Pass' with proper alignment
print('{:<10}{:>6}{:>10}'.format('Charlie', 52, 'Pass'))

# Example 3: Financial report with f-strings and calculations
income = 850.00
rent = 650.00
groceries = 80.00
utilities = 75.00
total = rent + groceries + utilities
remaining = income - total

print('\n=== Monthly Budget ===')
# Print 'Income' and value using f-string with € and 2 decimals
print(f'Income: €{income:.2f}')

# Print 'Rent' and value using f-string with € and 2 decimals
print(f'Rent: €{rent:.2f}')

# Print 'Groceries' and value using f-string with € and 2 decimals
print(f'Groceries: €{groceries:.2f}')

# Print 'Utilities' and value using f-string with € and 2 decimals
print(f'Utilities: €{utilities:.2f}')

print('-' * 28)
# Print 'Total Expenses' and total using f-string with € and 2 decimals
print(f'Total Expenses: €{total:.2f}')

# Print 'Remaining' and remaining using f-string with € and 2 decimals
print(f'Remaining: €{remaining:.2f}')

# Example 4: Sales report with percentages and thousands separator
product = 'Premium Laptop'
units_sold = 1234
unit_price = 1299.99
revenue = units_sold * unit_price
target_revenue = 2000000
percentage_of_target = revenue / target_revenue

print('\n=== Sales Report ===')
# Print 'Product:' and product name using f-string
print(f'Product: {product}')

# Print 'Units Sold:' and units with thousands separator
print(f'Units Sold: {units_sold:,}')

# Print 'Unit Price:' and price with € and 2 decimals
print(f'Unit Price: {price:.2f}')

# Print 'Total Revenue:' with €, thousands separator, and 2 decimals
print(f'Total Revenue: €{revenue:,.2f}')

# Print 'Target:' with €, thousands separator, and 2 decimals
print(f'Target: €{target_revenue:,.2f}')

# Print 'Achievement:' as percentage with 1 decimal place
print(f'Achievement: {percentage_of_target:.1%}')

# Example 5: Comparison table showing format() vs f-strings
print('\n=== Comparing format() and f-strings ===')
item = 'Coffee'
quantity = 3
price_per_unit = 3.50
total_price = quantity * price_per_unit

print('Using format():')
# Print item, quantity, and total using format()
print('Item: {}, Quantity: {}, Total: {:.2f}'.format(item, quantity, total_price))

print('Using f-string:')
# Print item, quantity, and total using f-string
print(f'Item: {item}, Quantity: {quantity}, Total: {total_price:.2f}')
