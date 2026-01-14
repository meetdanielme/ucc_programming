# 1) Number Range Checker
# Ask the user to enter two numbers — a start and an end value.
# •	If both numbers are between 1 and 100 and start < end, print “Valid range.”
# •	If start >= end, print “Invalid range order.”
# •	If any of the numbers are outside 1–100, print “Numbers out of range.”

start = int(input("Enter the start number\n"))
end = int(input("Enter the end number\n"))

if 1 < start < 100 and 1 < end < 100 and start < end:
    print("Valid range")
elif start >= end:
    print("Invalid range")
else:
    print("Numbers out of range")

# 2) Positive Ratio Guard
# Ask the user for two numbers, x and y.
# •	If both x and y are positive and y is not zero, print the result of x / y.
# •	If y is zero, print that you can’t divide by 0.
# •	Otherwise, print an appropriate message (e.g., "Invalid input for division").
# Hint: Use logical operators.

x = int(input("Enter the x number\n"))
y = int(input("Enter the y number\n"))

if x >= 0 and y > 0:
    print(x / y)
elif y == 0:
    print("You can't divide by zero")
else:
    print("Invalid input for division")

# 3) Discount Calculator
# Ask the user for the total amount of their shopping.
# •	If the total is €100 or more, apply a 20% discount.
# •	If it’s between €50 and €99, apply a 10% discount.
# •	Otherwise, print no discount applies.
# Then display the final price.

total = int(input("Enter the total amount spent\n"))

if total >= 100:
    total = total * 1.2
elif 50 <= total <= 99:
    total = total * 1.1
else:
    print("No discounts apply")
print(f"Your total is {total}")

# 4) Pizza Price Calculator
# Ask the user which pizza size they want: small, medium, or large.
# Then ask if they want extra cheese (yes/no).
# •	Small: €8
# •	Medium: €10
# •	Large: €12
# •	Extra cheese adds €1.50
# Print the final price.

size = input("Which pizza do you want: small, medium, or large?\n")
cheese = input("Do you want extra cheese??\n")

if size == "small":
    pizza_price = 8
elif size == "medium":
    pizza_price = 10
else:
    pizza_price = 12

if cheese == "cheese":
    pizza_price = pizza_price + 1.5

print(f"Your pizza price is {pizza_price}")

# 5) Login System
# Create a simple login system.
# •	Create variables: username = "admin" and password = "1234".
# •	Ask the user to enter a username and password.
# •	If both match, print "Login successful!"
# •	Otherwise, print "Incorrect username or password."
# Hint: Use nested if statements.

username = "admin"
password = "1234"

entered_username = input("Enter username\n")
entered_password = input("Enter password\n")

if entered_username == username:
    if entered_password == password:
        print("Login successful!")
    else:
        print("Incorrect username or password.")
else:
    print("Incorrect username or password.")

# 6) Battery Health Monitor
# Ask the user for the battery percentage (0–100) and whether the charger is plugged in (yes/no).
# Rules:
# •	Below 10 → “Battery critically low!”
# •	10–20 and not charging → “Low battery — please connect your charger!”
# •	10–20 and charging → “Charging... please wait.”
# •	20–80 → “Battery level normal.”
# •	Above 80 → “Battery high.”
# •	If charging and above 95 → “Unplug charger to preserve battery health.”

try:
    battery = int(input("Enter battery percentage (0-100)\n"))
except ValueError:
    print("Invalid battery percentage. Please enter a number between 0 and 100.")
else:
    charging_input = input("Is the charger plugged in? (yes/no)\n").strip().lower()
    charging = charging_input == "yes"

    if charging and battery > 95:
        print("Unplug charger to preserve battery health.")
    elif battery < 10:
        print("Battery critically low!")
    elif 10 <= battery <= 20 and not charging:
        print("Low battery — please connect your charger!")
    elif 10 <= battery <= 20 and charging:
        print("Charging... please wait.")
    elif 20 < battery <= 80:
        print("Battery level normal.")
    else:  # battery > 80 and not caught by >95 charging case
        print("Battery high.")

# 7) Weather Clothing Advisor
# Ask the user for the temperature in Celsius and whether it is raining (yes/no).
# Then, using if, elif, and else, suggest what to wear.
# Rules:
# •	If the temperature is below 10 → print “Wear a coat.”
# •	If the temperature is between 10 and 20 → print “Wear a jacket.”
# •	If the temperature is 20 or higher → print “T-shirt weather!”
# •	If it’s raining, also print “Don’t forget an umbrella!”

try:
    temp_c = float(input("Enter the temperature in °C\n"))
except ValueError:
    print("Invalid temperature. Please enter a number.")
else:
    raining_input = input("Is it raining? (yes/no)\n").strip().lower()
    is_raining = raining_input == "yes"

    if temp_c < 10:
        print("Wear a coat.")
    elif 10 <= temp_c < 20:
        print("Wear a jacket.")
    else:
        print("T-shirt weather!")

    if is_raining:
        print("Don't forget an umbrella!")
