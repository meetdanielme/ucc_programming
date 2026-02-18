# =======================================================
# IS1111 Dictionaries Tutorial 5 — Exercises
# Dicts (List/Dict conversions) — More Advanced
# =======================================================

# Daniel Marcinkowski
# 125701129

# -------------------------------------------------------
# QUESTION 1 — Nested dictionaries
# -------------------------------------------------------
employees = {
    "E001": {"name": "Sarah", "dept": "Sales", "salary": 45000},
    "E002": {"name": "Cian", "dept": "IT", "salary": 52000},
    "E003": {"name": "Aoife", "dept": "Sales", "salary": 48000},
    "E004": {"name": "Ben", "dept": "IT", "salary": 47000},
}

# (a) Print the name of employee "E002"
# (b) Increase Ben’s salary by 3000, then print Ben’s updated salary
# (c) If an employee ID does not exist, print "Employee not found" instead of crashing
#     Test using "E999"
# (d) Write a function get_salary(employees, emp_id)
#     - return the salary if the employee exists
#     - return None if the employee does not exist
#     Test with "E001" and "E999"

# 1a
print(employees["E002"]["name"])

# 1b
employees["E004"]["salary"] += 3000
print(employees["E004"]["salary"])

# 1c
if "E999" in employees:
    print(employees["E999"]["name"])
else:
    print("Employee not found")

# 1d
def get_salary(employees, emp_id):
    if emp_id in employees:
        return employees[emp_id]["salary"]
    else:
        return None
    
print(get_salary(employees, "E001"))  # should print 45000
print(get_salary(employees, "E999"))  # should print None


# -------------------------------------------------------
# QUESTION 2 — Grouping & aggregation
# -------------------------------------------------------
# Using employees above:
# (a) Create a dictionary dept_summary:
#     key = department name
#     value = {"count": number_of_employees, "total_salary": total_salary}
# (b) Print each department and its total salary
# (c) Print the department with the highest total salary

# 2a
dept_summary = {}
for emp in employees.values():
    dept = emp["dept"]
    salary = emp["salary"]
    if dept not in dept_summary:
        dept_summary[dept] = {"count": 0, "total_salary": 0}
    dept_summary[dept]["count"] += 1
    dept_summary[dept]["total_salary"] += salary

# 2b
for dept, summary in dept_summary.items():
    print(f"{dept}: Total Salary = {summary['total_salary']}")

# 2c - without lambda
highest_dept = None
highest_salary = 0

for dept, summary in dept_summary.items():
    if summary["total_salary"] > highest_salary:
        highest_salary = summary["total_salary"]
        highest_dept = dept

print(f"Department with highest total salary: {highest_dept} (Total Salary = {highest_salary})")

# -------------------------------------------------------
# QUESTION 3 — Dict ↔ list conversions
# -------------------------------------------------------
scores = {
    "Alice": 88,
    "Brian": 75,
    "Ciara": 92,
    "David": 75,
}

# (a) Convert scores into a list of tuples using .items(), then print it
# (b) Sort the students by score (highest first), then print the sorted result
#     NOTE: You may build a list of (score, name) tuples to make sorting easier
# (c) Create a new dictionary where:
#     value is "Pass" if score >= 80, otherwise "Fail"
#     Print the new dictionary

# 3a
scores_list = list(scores.items())
print(scores_list)

# 3b
scores_tuples = [(score, name) for name, score in scores.items()]
scores_tuples.sort(reverse=True)  # sort by score (first element of tuple)
print(scores_tuples)

# 3c
new_scores = {name: ("Pass" if score >= 80 else "Fail") for name, score in scores.items()}
print(new_scores)

# -------------------------------------------------------
# QUESTION 4 — ID generation + adding records
# -------------------------------------------------------
transactions = {
    "T001": {"amount": 250.0, "type": "deposit"},
    "T002": {"amount": 100.0, "type": "withdrawal"},
    "T003": {"amount": 400.0, "type": "deposit"},
}

# (a) Write a function generate_transaction_id(transactions)
#     - find the highest transaction number
#     - return the next ID (e.g. "T004")
# (b) Use your function to add a new transaction:
#     amount: 150.0
#     type: "deposit"
#     Print the updated transactions dictionary

# 4a

def generate_transaction_id(transactions):
    max_id = 0
    for tid in transactions.keys():
        num = int(tid[1:])
        if num > max_id:
            max_id = num
    return f"T{max_id + 1:03d}"

# 4b

new_tid = generate_transaction_id(transactions)
transactions[new_tid] = {"amount": 150.0, "type": "deposit"}
print(transactions)
