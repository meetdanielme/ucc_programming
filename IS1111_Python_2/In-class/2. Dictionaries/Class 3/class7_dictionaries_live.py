# class7_dictionaries_live.py
# Class 7: Nested Dicts, Search Patterns & Key Extraction (Dict class 3 of 4)

print("\nCLASS 7: NESTED DICTS, SEARCH & ID GENERATION\n")

# ══════════════════════════════════════════════════════════════
# SECTION 1: NESTED DICTIONARIES
# ══════════════════════════════════════════════════════════════
# So far our dict values have been strings, numbers, or lists.
# Values can also be dicts — that gives us two levels of lookup:
#   outer key → finds a record
#   inner key → finds a field within that record

print("=" * 55)
print("SECTION 1: NESTED DICTIONARIES")
print("=" * 55)

employees = {
    "E001": {"name": "Sarah",  "dept": "Sales",  "salary": 45000},
    "E002": {"name": "Cian",   "dept": "IT",     "salary": 52000},
    "E003": {"name": "Aoife",  "dept": "Sales",  "salary": 48000},
    "E004": {"name": "Ben",    "dept": "IT",     "salary": 47000},
    "E005": {"name": "Roisin", "dept": "HR",     "salary": 44000},
}

# ── Two-bracket access ────────────────────────────────────────
# First bracket gets the inner dict, second gets the field.
print("Nested access:")
print("  employees['E001']           →", employees["E001"])
print("  employees['E001']['name']   →", employees["E001"]["name"])
print("  employees['E001']['salary'] →", employees["E001"]["salary"])

# Same thing split into two steps (helpful for understanding):
record = employees["E001"]
print("  Step-by-step:", record["name"])
print()

# ── What goes wrong ───────────────────────────────────────────
# Missing outer key → KeyError.  Missing inner key → KeyError.
# (Uncomment briefly to show tracebacks, then re-comment)
# print(employees["E999"])                  # KeyError: 'E999'
# print(employees["E001"]["email"])         # KeyError: 'email'

# ── Safe chained get() ────────────────────────────────────────
# .get(key, default) returns default instead of crashing.
# For nested: chain two get() calls with {} as the outer default.
# Why {}?
#   employees.get("E999")       → None     → None.get("salary") → CRASH
#   employees.get("E999", {})   → {}       → {}.get("salary")   → None ✓
print("Safe chained get():")
print("  E001 salary:", employees.get("E001", {}).get("salary"))    # 45000
print("  E999 salary:", employees.get("E999", {}).get("salary"))    # None
print("  E001 email: ", employees.get("E001", {}).get("email"))     # None
print()

# ── Check before access ──────────────────────────────────────
# When you want a clear message rather than just None.
emp_id, field = "E003", "email"
if emp_id in employees:
    if field in employees[emp_id]:
        print(f"  {emp_id} {field}: {employees[emp_id][field]}")
    else:
        print(f"  {emp_id} has no '{field}' on file.")
print()

# ── Modifying nested values ───────────────────────────────────
# Inner dict is mutable — update or add fields directly.
print("Modify nested:")
employees["E002"]["salary"] = 55000                     # update existing
employees["E002"]["email"] = "cian@company.ie"          # add new field
print("  Updated E002:", employees["E002"])
del employees["E002"]["email"]                          # clean up
print()

# ── Looping through nested dicts ──────────────────────────────
print(f"  {'ID':<6} {'Name':<10} {'Dept':<8} {'Salary':<10}")
print("  " + "-" * 34)
for eid, emp in employees.items():
    print(f"  {eid:<6} {emp['name']:<10} {emp['dept']:<8} €{emp['salary']:,}")
print()


# ══════════════════════════════════════════════════════════════
# SECTION 2: GROUPING & AGGREGATING
# ══════════════════════════════════════════════════════════════
# Goal: count employees per dept AND sum their salaries.
#
# The pattern (CA):
#   1. Start with empty summary dict
#   2. Loop through data
#   3. If this group key is NEW → create entry with zeros
#   4. Accumulate (add to count, add to total)

print("=" * 55)
print("SECTION 2: GROUPING & AGGREGATING")
print("=" * 55)

dept_summary = {}

for emp in employees.values():
    dept = emp["dept"]
    if dept not in dept_summary:
        dept_summary[dept] = {"count": 0, "total_salary": 0.0}     # CREATE
    dept_summary[dept]["count"] += 1                                # ACCUMULATE
    dept_summary[dept]["total_salary"] += emp["salary"]             # ACCUMULATE

# Trace what happened on each iteration:
# Sarah  → "Sales" not in {} → create → count=1, total=45000
# Cian   → "IT"    not in {} → create → count=1, total=55000
# Aoife  → "Sales" already in → count=2, total=93000
# Ben    → "IT"    already in → count=2, total=102000
# Roisin → "HR"    not in    → create → count=1, total=44000

print("Raw summary:", dept_summary)
print()

# ── Display as formatted report ───────────────────────────────
print(f"  {'Department':<15} {'Count':<10} {'Total Salary':<15}")
print("  " + "=" * 40)
grand_count, grand_total = 0, 0.0
for dept, data in sorted(dept_summary.items()):
    print(f"  {dept:<15} {data['count']:<10} €{data['total_salary']:,.2f}")
    grand_count += data["count"]
    grand_total += data["total_salary"]
print("  " + "=" * 40)
print(f"  {'Total':<15} {grand_count:<10} €{grand_total:,.2f}")
print()

# ── Wrap it as a function (CA) ───────
def department_report(employees_dict):
    """Group employees by dept, show count and total salary."""
    if not employees_dict:
        print("No employees.")
        return {}

    summary = {}
    for emp in employees_dict.values():
        dept = emp["dept"]
        if dept not in summary:
            summary[dept] = {"count": 0, "total_salary": 0.0}
        summary[dept]["count"] += 1
        summary[dept]["total_salary"] += emp["salary"]

    print(f"\n  {'Department':<15} {'Count':<10} {'Total Salary':<15}")
    print("  " + "=" * 40)
    t_count, t_salary = 0, 0.0
    for dept, data in sorted(summary.items()):
        print(f"  {dept:<15} {data['count']:<10} €{data['total_salary']:,.2f}")
        t_count += data["count"]
        t_salary += data["total_salary"]
    print("  " + "=" * 40)
    print(f"  {'Total':<15} {t_count:<10} €{t_salary:,.2f}")
    return summary

print("As a function:")
result = department_report(employees)
print("Returned:", result)
print()

# CA: generate_category_report() — same pattern but group by
# product["category"], accumulate count + value (price × quantity).


# ══════════════════════════════════════════════════════════════
# SECTION 3: SEARCH PATTERNS
# ══════════════════════════════════════════════════════════════
# Two types of search, both case-insensitive:
#   PARTIAL: does the term appear INSIDE the value?  → "in"
#   EXACT:   does the term EQUAL the value?          → "=="

print("=" * 55)
print("SECTION 3: SEARCH PATTERNS")
print("=" * 55)

# ── .lower() for case-insensitive comparison ──────────────────
print("Case-insensitive basics:")
print("  'Sarah'.lower()          →", "Sarah".lower())
print("  'sarah' == 'Sarah'       →", "sarah" == "Sarah")          # False
print("  'sarah' == 'Sarah'.lower()→", "sarah" == "Sarah".lower()) # True
print()

# ── Two uses of "in" — don't confuse them! ────────────────────
# Use 1 (from Class 1): key in dict → checks if KEY exists
# Use 2 (new today):    substr in string → checks if SUBSTRING exists
print("Two uses of 'in':")
print("  'E001' in employees      →", "E001" in employees)         # key in dict
print("  'sar' in 'sarah'         →", "sar" in "sarah")            # substr in string
print()

# ── Partial match: "in" for substrings ────────────────────────
print("Partial match (substring):")
print("  'sar' in 'Sarah'.lower() →", "sar" in "Sarah".lower())    # True
print("  'xyz' in 'Sarah'.lower() →", "xyz" in "Sarah".lower())    # False
print()

# ── Exact match: "==" for full string ─────────────────────────
# "sal" won't match "Sales" — the whole string must match.
print("Exact match (full string):")
print("  'sales' == 'Sales'.lower() →", "sales" == "Sales".lower()) # True
print("  'sal'   == 'Sales'.lower() →", "sal" == "Sales".lower())   # False
print()

# ── Collecting matches ────────────────────────────────────────
# Start with empty list, append a (key, value) tuple for each match.
matches = []
for eid, emp in employees.items():
    if "oi" in emp["name"].lower():
        matches.append((eid, emp))
print(f"Partial name 'oi' → {len(matches)} match(es):")
for eid, emp in matches:
    print(f"  {eid}: {emp['name']}")
print()

# ── Search function with both match types ─────────────────────
def search_employees(employees_dict):
    """Search by name (partial) or department (exact), case-insensitive."""
    print("\n--- Search Employees ---")
    search_type = input("  Search by (N)ame or (D)epartment? ").strip().lower()
    while search_type not in ['n', 'd']:
        search_type = input("  Enter 'N' or 'D': ").strip().lower()

    matches = []
    if search_type == 'n':
        term = input("  Enter name (or part): ").strip()
        for eid, emp in employees_dict.items():
            if term.lower() in emp["name"].lower():             # PARTIAL
                matches.append((eid, emp))
    else:
        term = input("  Enter department: ").strip()
        for eid, emp in employees_dict.items():
            if emp["dept"].lower() == term.lower():             # EXACT
                matches.append((eid, emp))

    if not matches:
        print("  No results found.")
        return
    print(f"\n  {'ID':<6} {'Name':<10} {'Dept':<8} {'Salary':<10}")
    print("  " + "=" * 34)
    for eid, emp in matches:
        print(f"  {eid:<6} {emp['name']:<10} {emp['dept']:<8} €{emp['salary']:,}")
    print(f"  Found {len(matches)} employee(s)")

# Uncomment for live interactive demo:
# search_employees(employees)

# Quick tests showing the key distinction:
print("Exact dept 'it' (matches IT):", end=" ")
for eid, emp in employees.items():
    if emp["dept"].lower() == "it":
        print(emp["name"], end="  ")
print()

print("Exact dept 'i'  (no match):  ", end=" ")
count = sum(1 for e in employees.values() if e["dept"].lower() == "i")
print(f"{count} match(es) — exact means the WHOLE string must match")
print()
# CA: search_products() — name partial, category exact. Same structure.


# ══════════════════════════════════════════════════════════════
# SECTION 4: KEY EXTRACTION & ID GENERATION
# ══════════════════════════════════════════════════════════════
# Keys like "E001" encode a number. We extract it, find the max,
# add 1, and format back with zero-padding.

print("=" * 55)
print("SECTION 4: KEY EXTRACTION & ID GENERATION")
print("=" * 55)

# ── String slicing to extract the number ──────────────────────
print("Key extraction:")
for key in ["E001", "E015", "P003", "P042"]:
    print(f"  '{key}'  → key[1:] = '{key[1:]}'  → int() = {int(key[1:])}")
print()

# ── f-string zero-padding :03d ────────────────────────────────
# :03d = integer (d), minimum 3 chars wide (3), pad with zeros (0)
print("Zero-padding :03d")
for n in [1, 7, 42, 100]:
    print(f"  n={n:<4} → f'E{{n:03d}}' → 'E{n:03d}'")
print()

# ── Best-so-far applied to key numbers ────────────────────────
print("Finding max key number (trace):")
max_num = 0
for eid in employees:
    num = int(eid[1:])
    old = max_num
    if num > max_num:
        max_num = num
    print(f"  key='{eid}' → num={num}  max was {old} → now {max_num}")
print(f"  → Next ID: E{max_num + 1:03d}")
print()

# ── The function ──────────────────────────────────────────────
def generate_employee_id(employees_dict):
    """Generate next unique ID (E001, E002, etc.) — finds max + 1."""
    if not employees_dict:
        return "E001"
    max_num = 0
    for eid in employees_dict:
        num = int(eid[1:])
        if num > max_num:
            max_num = num
    return f"E{max_num + 1:03d}"

# Tests — the gap case matters: finds MAX, not count
print("ID generation tests:")
print(f"  Empty         → '{generate_employee_id({})}'")             # E001
print(f"  E001, E002    → '{generate_employee_id({'E001':{}, 'E002':{}})}'")  # E003
print(f"  E001, E003    → '{generate_employee_id({'E001':{}, 'E003':{}})}'")  # E004 (gap!)
print(f"  Our employees → '{generate_employee_id(employees)}'")      # E006
print()

# Use it to add a new employee
new_id = generate_employee_id(employees)
employees[new_id] = {"name": "Declan", "dept": "HR", "salary": 43000}
print(f"Added: {new_id} → {employees[new_id]}")
print(f"Next after that: {generate_employee_id(employees)}")
print()
# CA: generate_product_id() — same logic, "P" prefix, inventory keys.


# ══════════════════════════════════════════════════════════════
# CLASS 3 SUMMARY
# ══════════════════════════════════════════════════════════════
#
# ── New syntax & patterns covered today ───────────────────────
#
# NESTED ACCESS
#   dict[k1][k2]                    Two-level access
#   dict.get(k1, {}).get(k2)        Safe chained (no crash)
#   dict[k1][k2] = val              Modify nested value
#   del dict[k1][k2]                Delete a nested field
#   if k2 in dict[k1]              Check if inner key exists
#
# SEARCH (case-insensitive)
#   term.lower() in val.lower()     Partial match (substring)
#   term.lower() == val.lower()     Exact match (full string)
#   matches = []  →  .append()      Collect results in a list
#
# KEY EXTRACTION & ID GENERATION
#   int(key[1:])                    Extract number from key
#   f"P{n:03d}"                     Zero-padded ID (P001)
#   if not dict: return "P001"      Handle empty dict
#
# GROUPING PATTERN
#   if key not in summary:
#       summary[key] = {"count": 0, "value": 0.0}
#   summary[key]["count"] += 1
#   summary[key]["value"] += amount
#
#
# ── All dict methods & syntax covered so far (classes 1–3) ───
#
#   Syntax / Method                 First Seen
#   ──────────────────────────────  ──────────
#   {} and dict()                   Class 1
#   dict[key] / dict[key] = value   Class 1
#   del dict[key]                   Class 1
#   key in dict / key not in dict   Class 1
#   .get(key, default)              Class 1
#   .keys() / .values() / .items()  Class 1
#   hash()                          Class 1
#   len() / sorted()                Class 1
#   .pop(key) / .pop(key, default)  Class 2
#   .update(other_dict)             Class 2
#   .copy()                         Class 2
#   .clear()                        Class 2
#   max(dict, key=dict.get)         Class 2
#   sum/max/min on .values()        Class 2
#   dict[k1][k2] (nested access)    Class 3
#   .get(k1,{}).get(k2) (safe)      Class 3
#   term.lower() in val.lower()     Class 3
#   int(key[1:]) (key extraction)   Class 3
#   f"P{n:03d}" (zero-padding)      Class 3
#   grouping pattern (if not in)    Class 3
# ══════════════════════════════════════════════════════════════