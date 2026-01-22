# Create a Python file called list_functions.py that contains the following functions:
# Then, create a file called main.py for testing that each function is working as expected. At the top of this file write: import list_functions. Call each function as normal.

# 3.1. Write a Python programme to count the number of strings in a given list of strings using a for loop.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 4

def count_strings(string_list):
    count = 0
    for string in string_list:
        count += 1
    return count

# 3.2. Write a Python programme to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

def remove_elements(input_list):
    return input_list[1:4]

# 3.3. Write a Python programme to convert a list of characters into a string.

def list_to_string(char_list):
    result = ''
    for char in char_list:
        result += char
    return result

# 3.4. Write a Python programme to compute the difference between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['red', 'orange', 'white']
# Color2-Color1: ['black', 'yellow']

def list_difference(list1, list2):
    diff1 = [item for item in list1 if item not in list2]
    diff2 = [item for item in list2 if item not in list1]
    return diff1, diff2