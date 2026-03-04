# (b)
# Create employee_utils.py
# It should contain ONLY functions (no prints, no running code):
#
# Write:
#     get_salary(employees, emp_id)
#         - return salary if employee exists
#         - return None otherwise
#
def get_salary(employees, emp_id):
    employee = employees.get(emp_id)
    if employee:
        return employee["salary"]
    return None

# Write:
#     increase_salary(employees, emp_id, amount)
#         - increase salary if employee exists
#         - return True if updated
#         - return False otherwise

def increase_salary(employees, emp_id, amount):
    employee = employees.get(emp_id)
    if employee:
        employee["salary"] += amount
        return True
    return False