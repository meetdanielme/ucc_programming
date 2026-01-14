# Write a short program that keeps asking the user to enter numbers, one at a time.
# When the user types "done", your program should stop asking and then print out:
# * how many numbers were entered
# * the total (sum) of all the numbers
# * and the average (total ÷ count)
# Hints:
# * Think about what needs to repeat — that’s what your while loop will do.
# * Create two variables before the loop starts:
# o one to keep track of how many numbers you’ve seen (count)
# o one to add them all up (total)
# * Inside the loop, use input() to ask the user for a number.
# * If the user types "done", use a break statement to stop the loop.
# * Otherwise, convert the input into a number (use float()), then update your count and
# total each time.
# * After the loop finishes, print your results in a friendly message.

count = 0 # keep track of how many numbers you’ve seen
total = 0 # sum all the numbers

while True:
    number = input("Enter a number or type \'done\' to stop the program\n")
    if number == "done":
        break
    else:
        number = float(number)
        total += number
        count += 1

print("The sum is", total)
print("The count is", count)