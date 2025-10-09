# Exercise 1: Warmup – Numbers vs Strings

print(42) # 42 — int
print('42') # 42 — str
print('4' + '2') # 42
print(4 + 2) # 6
print(type('42')) # str — correct: <class 'str'>
print(type(42)) # int — correct: <class 'int'>


# Exercise 2: Variables & Assignment

name = "Daniel"
age = "28"
pi = "3.14159"
print("Hello, my name is", name + ", I am", age, "years old, and pi is about", pi)


# Exercise 3: Operators Practice

print(7 // 3) # 2
print(7 % 3) # 1
print(2 ** 5) # 32


# Exercise 4: Full Name Concatenation

name = input("What is your first name?\n")
surname = input("What is your last name?\n")
print("Hello, your full name is", name, surname + ".")


# Exercise 5: Gross Pay Calculator

rate = float(input("What's your hourly rate? (in €)\n"))
hours = float(input("How many hours have you worked?\n"))
print("You will earn", rate * hours, "€.")


# Exercise 6: Celsius to Fahrenheit

temp_c = float(input("Provide temperature in Celsius\n"))
freedom_temp = (temp_c * 9/5) + 32
print(temp_c, "°C equals", freedom_temp, "in freedom units.")

# Exercise 7: Even or Odd?

even_odd = int(input("Input a number to check if it's even or odd\n"))
even_odd = even_odd % 2
if even_odd == 0:
    print("It's even!")
else:
    print("It's odd (the number, not you)")


# Exercise 8: Challenge – Time Converter

user_minutes = int(input("Give me a number of minutes — I will convert it into hours\n"))
hours = user_minutes // 60
minutes = user_minutes % 60
print(user_minutes, "minutes equal", hours, "hour(s) and", minutes, "minute(s).")