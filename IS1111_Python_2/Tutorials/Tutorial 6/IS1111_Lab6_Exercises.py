"""
IS1111 Lab 6 – Exercises
Dicts + Files (TXT/CSV/JSON) + CRUD
Student Name: Daniel Marcinkowski
Student Number: 125701129
"""

# =======================================================
# QUESTION 1 — Dict ↔ List conversions
# =======================================================

modules = ["IS1111", "IS1109", "IS1103", "IS1120"]

# (a) Create an empty dictionary called module_lengths.
# (b) Loop through modules and store:
#     key   = module code
#     value = length of the module code
# (c) Print the dictionary.
# (d) Convert the dictionary to a list of tuples using .items()
# (e) Create a list of tuples (length, code) and sort descending.

# 1a
module_lengths = {}

# 1b
for module in modules:
    module_lengths[module] = len(module)

# 1c
print(module_lengths)

# 1d
module_items = list(module_lengths.items())
print(module_items)

# 1e
length_code_tuples = []
for code, length in module_lengths.items():
    length_code_tuples.append((length, code))
length_code_tuples.sort(reverse=True)
print(length_code_tuples)

# =======================================================
# QUESTION 2 — TXT file + CRUD basics
# =======================================================

filename = "shopping.txt"

# (a) Ask the user to enter 3 shopping items and store them in a list.
# (b) Write the list to shopping.txt (one item per line).
# (c) Read the file and print the contents.
# (d) Ask for one extra item and append it to the file.
# (e) Ask for an item to remove. Remove it safely and rewrite the file.

# 2a
shopping_list = []
for i in range(3):
    item = input(f"Enter shopping item #{i+1}: ")
    shopping_list.append(item)

# 2b
with open(filename, "w") as file:
    for item in shopping_list:
        file.write(item + "\n")

# 2c
with open(filename, "r") as file:
    contents = file.read()
print("Shopping List:" + "\n" + contents)

# 2d
extra_item = input("Enter an extra shopping item to add: ")
with open(filename, "a") as file:
    file.write(extra_item + "\n")

# 2e
item_to_remove = input("Enter an item to remove: ")
with open(filename, "r") as file:
    items = file.readlines()

for i in range(len(items)):
    if items[i].strip() == item_to_remove:
        del items[i]
        break

# Rewrite the file with the updated items list
with open(filename, "w") as file:
    for item in items:
        file.write(item)

# =======================================================
# QUESTION 3 — CSV file + dictionary records
# =======================================================

products = {
    "P001": {"name": "Laptop", "price": 900},
    "P002": {"name": "Mouse", "price": 25},
    "P003": {"name": "Keyboard", "price": 45},
}

# (a) Write the products dictionary to products.csv with header: id,name,price
# (b) Read the file and rebuild a new dictionary called products_from_file.
# (c) Ask for a product ID and update the price.
# (d) Save the updated dictionary back to products.csv.

# 3a
import csv

with open("products.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id", "name", "price"])
    for product_id, details in products.items():
        writer.writerow([product_id, details["name"], details["price"]])

# 3b
products_from_file = {}
with open("products.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        products_from_file[row["id"]] = {"name": row["name"], "price": float(row["price"])}

# 3c
product_id_to_update = input("Enter product ID to update price: ")
if product_id_to_update in products_from_file:
    new_price = float(input("Enter new price: "))
    products_from_file[product_id_to_update]["price"] = new_price
else:
    print("Product ID not found.")

# 3d
with open("products.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id", "name", "price"])
    for product_id, details in products_from_file.items():
        writer.writerow([product_id, details["name"], details["price"]])

# =======================================================
# QUESTION 4 — JSON + FULL CRUD menu system
# =======================================================

# Build a simple student management system using JSON.

# Requirements:
# 1. Store students as a list of dictionaries.
# 2. Save to students.json.
# 3. Build a menu with:
#    1 View
#    2 Add
#    3 Update
#    4 Delete
#    5 Exit
# 4. Save the file after every change.

import json

students_file = "students.json"

def load_students():
    try:
        with open(students_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_students(students):
    with open(students_file, "w") as file:
        json.dump(students, file, indent=4)

def view_students(students):
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}")

def add_student(students):
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    students.append({"id": student_id, "name": name})
    save_students(students)
    print("Student added.")

def update_student(students):
    student_id = input("Enter student ID to update: ")
    for student in students:
        if student["id"] == student_id:
            new_name = input("Enter new name: ")
            student["name"] = new_name
            save_students(students)
            print("Student updated.")
            return
    print("Student ID not found.")

def delete_student(students):
    student_id = input("Enter student ID to delete: ")
    for i in range(len(students)):
        if students[i]["id"] == student_id:
            del students[i]
            save_students(students)
            print("Student deleted.")
            return
    print("Student ID not found.")

def main():
    students = load_students()
    
    while True:
        print("\nMenu:")
        print("1. View Students")
        print("2. Add Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            view_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()