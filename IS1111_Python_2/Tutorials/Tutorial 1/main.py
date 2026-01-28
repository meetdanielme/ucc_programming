import lists_functions

# 3.1. Write a Python programme to count the number of strings in a given list of strings using a for loop.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 4

strings = ['abc', 'xyz', 'aba', '1221']
print(lists_functions.count_strings(strings))

# 3.2. Write a Python programme to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(lists_functions.remove_elements(colors))

# 3.3. Write a Python programme to convert a list of characters into a string.

char_list = ['H', 'e', 'l', 'l', 'o']
print(lists_functions.list_to_string(char_list))

# 3.4. Write a Python programme to compute the difference between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['red', 'orange', 'white']
# Color2-Color1: ['black', 'yellow']

list1 = ["red", "orange", "green", "blue", "white"]
list2 = ["black", "yellow", "green", "blue"]
diff1, diff2 = lists_functions.list_difference(list1, list2)
print("Color1-Color2:", diff1)
print("Color2-Color1:", diff2)