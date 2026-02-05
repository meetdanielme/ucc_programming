# Demonstrate error with string index assignment
# " "
friends = [ 'Joseph', 'Glenn', 'Sally' ]

friends[0] = "g"

print(friends)

# Reversing Lists

orders = [10, 20, 30, 40, 50, 60]

# How do I get the first two items? [10, 20]

orders_slice = orders[:2]
print(orders_slice)

# How do I get [40, 50, 60]?

orders_slice = orders[3:]
print(orders_slice)

# How do I reverse it? - [start:stop:step]

orders_slice = orders[::-1]
print(orders_slice)

# Did the original List Change?
## No.

# In-place vs out-of-place .reverse() / sort() reverse = True / sorted

a = [1, 2, 3]
b = a.copy()

print(b)

# Whats a list of lists?

list_of_lists = [[10, 20, 30], [40, 50, 60]]

# How do I get the first three items? [10, 20, 30]

slice_of_lists = list_of_lists[0]
print(slice_of_lists)

# How do I get [40, 50, 60]?

slice_of_lists = list_of_lists[1]
print(slice_of_lists)

# How do I get the first two items? [10, 20]

slice_of_lists = list_of_lists[0][:2]
print(slice_of_lists)

# How do I reverse it? - [start:stop:step] e.g. (60, 50, 40)

slice_of_lists = list_of_lists[1][::-1]
print(slice_of_lists)


# Mutating a list (in-place/out-of-place: pop, append, remove

numbers = [10, 20, 30, 40]

# Add 50 to the end of the list using append

numbers.append(50)

# how to fix? map(function, iterables)

# numbers = map(int, numbers)

# Remove the last item using pop and store it in a variable

numbers.pop()

# Remove the value 20 from the list using remove

numbers.remove(20)

# Add 60 and 70 to the list (one at a time)

numbers.append(60)
numbers.append(70)

# Remove the item at index 1 using pop

numbers.pop(1)

# Remove the value 40 from the list
numbers.remove(40)

# What does the list look like now?
print(numbers)

# What value was returned by the last pop?
print(numbers.pop())