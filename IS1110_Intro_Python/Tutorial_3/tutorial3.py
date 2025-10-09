# Task 1

sub_total = float(input("Subtotal:\n"))
tax_rate = float(input("Tax:\n"))

tax_amount = tax_rate / 100 * sub_total
total = sub_total + tax_amount

# Round numbers to 2 digits after the decimal

tax_amount = round(tax_amount, 2)
sub_total = round(sub_total, 2)
tax_rate = round(tax_rate, 2)
total = round(total, 2)

print("Subtotal: €" + str(sub_total) + " | Tax (" + str(tax_rate) + "%): €" + str(tax_amount) +  " | Total: €" + str(total))


# Task 2

seconds_total = int(input("Give me a number of seconds\n"))
hours = seconds_total // 3600
remainder = seconds_total % 3600
minutes = remainder // 60
seconds = remainder % 60
print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
print(hours, ":", minutes, ":", seconds)
# From ChatGPT: Format with leading zeros (2 digits each)
print(f"{hours:02}:{minutes:02}:{seconds:02}")


# Task 3

base = float(input("Provide the lenght of the triangle base in meters\n"))
height = float(input("Provide the lenght of the triangle height in meters\n"))
compute_area = 0.5 * base * height
print(compute_area, "meters squared")

# 	:.1f → formats the number to 1 decimal place (e.g. 12.345 → 12.3)
# 	Using f"" allows you to combine text, numbers, and units cleanly in one print statement.

print(f"Area of the triangle: {compute_area:.1f} meters²")

# Task 4

# Ask the user for two whole numbers, but read them as strings first.

first_number = input("Input the first number\n")
second_number = input("Input the second number\n")

# 1. Print their string concatenation (variable a + variable b).

print("Your numbers are:", first_number + second_number)

# 2. Then convert both to integers and

first_number = int(first_number)
second_number = int(second_number)

    # o Calculate sum

sum = first_number + second_number

    # o Multiply together

multiplication = first_number * second_number

    # o Find average as a loat with 1 decimal place.

average = (first_number + second_number) / 2
average = round(average, 1)

    # o Print results for sum, multiply and average

print("Sum:", sum)
print("Multiplication:", multiplication)
print("Average:", average)


# Task 5: Tip & split calculator

# Ask for the bill amount (float), tip percent (e.g., 12.5), and number of people (int).

bill_amount = float(input("What's the bill amount?\n"))
tip_percentage = float(input("How much you want to tip?\n"))
people_numb = int(input("How many people?\n"))

# Compute Compute tip, total, and amount per person.

tip = bill_amount * (tip_percentage / 100)
total = bill_amount + tip
per_person = total / people_numb

# Print in the following format: Tip: €X.XX | Total: € X.XX | Each: € X.XX

print("Tip: €", tip, "| Total: €", total, "| Each: €", per_person)