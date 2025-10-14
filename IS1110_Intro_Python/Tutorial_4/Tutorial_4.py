# a. Grade Calculator

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("This score is invalid")
elif score >=90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# b. Weather Suggestion App

## Ask the user for the temperature in Celsius

temperature = int(input("Enter temperature in Celsius:\n"))

## Suggest what to wear

if temperature < 10:
    print("Wear a coat!")
elif temperature > 10 and temperature < 20:
    print("Take a jumper.")
else:
    print("T-shirt weather.")


# c. Cinema Tickets Price Calculator
# Ask for customer’s age and if they are a student.

age = int(input("How old are you?\n"))
student = (input("Are you a student (yes/no)?\n"))
ticket = 0

# Ticket prices are as follows:
#  If under 12, ticket price is €5
#  If 12 – 17, ticket price is €7
#  If 18+ and a student, ticket price is €8
#  If 18+ and not a student, ticket price is €12

if age < 12:
    ticket += 5
elif age >= 12 and age <= 17:
    ticket += 7
elif age >= 18 and student == "yes":
    ticket += 8
else:
    ticket += 12

print("Your ticket is: €", ticket)


# d. Store Discount Calculator

#  Ask user the total amount of purchase
#  Ask if they are a store member (yes/no)
#  Ask what day of the week it is

purchase = float(input("What's the total amount of purchase?\n"))
member = input("Are you a store member (yes/no)?\n")
day = input("What's the day of the week?\n")

#  Apply following discounts for the following rules:
# o Members on Wednesday: 20% discount
# o Members any other day: 10% discount
# o Non-members on Wednesday: 5% discount
# o Non-members any other day: no discount
#  Calculate and print total price after discount is applied
#  Round final price to 2 decimal places

if member == "yes" and day == "wednesday":
    purchase = purchase * 0.8
elif member == "yes":
    purchase = purchase * 0.9
elif member == "no" and day == "wednesday":
    purchase = purchase * 0.95

purchase = round(purchase, 2)
print("Your total after discount is: €", purchase)