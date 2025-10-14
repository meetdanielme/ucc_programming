while True:
    try:
        hours = float(input("Enter hours: "))
        break
    except:
        print("Error, please enter numeric input")

while True:
    try:
        rate = float(input("Enter rate per hour: "))
        break
    except:
        print("Error, please enter numeric input")
# ^^^ Got help from ChatGPT
if hours > 40:
    pay = hours * rate * 1.5
else:
    pay = hours * rate

print("Gross salary:", pay)