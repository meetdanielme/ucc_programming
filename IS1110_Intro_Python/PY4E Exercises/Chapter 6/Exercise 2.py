# Exercise 2: Write another program that prompts for a list of numbers as above and
# at the end prints out both the maximum and minimum of the numbers instead of the average.

smallest = None
largest  = None

while True:
    line = input('Enter a number: ')
    if line == 'done':
        break
    try:
        num = int(line)
    except:
        print('Invalid input')
        continue
    if smallest is None or num < smallest:
        smallest = num
    if largest is None or num > largest:
        largest = num

if smallest is None:
    print('No valid numbers were entered.')
else:
    print('Minimum:', smallest, 'Maximum:', largest)