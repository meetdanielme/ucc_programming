# Write a function:
#     count_drinks(drinks)
# It should:
#     - return a dictionary
#     - key = drink name
#     - value = how many times it appears

def count_drinks(drinks):
    drink_counts = {}
    for drink in drinks:
        if drink in drink_counts:
            drink_counts[drink] += 1
        else:
            drink_counts[drink] = 1
    return drink_counts