## Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.

def chop(lst):
    del lst[0]
    del lst[-1]
    return None

## Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def middle(lst):
    return lst[1:-1]