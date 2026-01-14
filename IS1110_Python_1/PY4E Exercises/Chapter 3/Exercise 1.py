hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
if hours >40:
    pay = hours * rate * 1.5
else:
    pay = hours * rate
print("Gross salary:", pay)