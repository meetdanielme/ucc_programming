# class9_files_live.py
# Class 9: Files — Reading, Writing, JSON & CSV

import json
import csv

print("\nCLASS 9: FILES\n")

# ══════════════════════════════════════════════════════════════
# SECTION 1: WRITING TEXT FILES
# ══════════════════════════════════════════════════════════════
# Until now every programme LOSES its data when it ends.
# Variables live in RAM — files live on disk (secondary storage).

print("=" * 55)
print("SECTION 1: WRITING TEXT FILES")
print("=" * 55)

# open(filename, mode) returns a FILE HANDLE (a connection)
# Mode "w" = write.  Creates the file, or OVERWRITES if exists.

# Method 1: manual open / close  (risky — easy to forget close)
f = open("sample_data/demo.txt", "w")
f.write("Line 1: Hello from Python\n")
f.write("Line 2: Files store data on disk\n")
f.close()
print("Wrote 2 lines (manual open/close)")

# File Paths Quick overview:
# Problem: \n is interpreted as a newline, \t as a tab
path = "C:\new_folder\test.txt"    # Broken!
# 1. Double backslash — escapes the backslash
path = "C:\\new_folder\\test.txt"

# 2. Raw string — r prefix tells Python to ignore escapes
path = r"C:\new_folder\test.txt"

# 3. Forward slashes — Python accepts these on Windows too
path = "C:/new_folder/test.txt"
# On Mac/Linux this never comes up because paths use forward slashes (/home/user/file.txt), which aren't escape characters.

# Method 2: with statement — PREFERRED.  Auto-closes the file.
with open("demo.txt", "w") as f:
    f.write("Line 1: Hello from Python\n")
    f.write("Line 2: Files store data on disk\n")
    f.write("Line 3: with statement is safer\n")
print("Wrote 3 lines (with statement)")
# File is closed here automatically — even if an error occurs

# ⚠️ "w" OVERWRITES — the original 2-line version is gone!

# write() does NOT add newlines — you must include \n yourself
with open("concat.txt", "w") as f:
    f.write("Hello")
    f.write("World")
# File contains: HelloWorld   (no space, no newline, one line)

# Append mode "a" — adds to the END, keeps existing content
with open("demo.txt", "a") as f:
    f.write("Line 4: Appended with 'a' mode\n")
print("Appended 1 line")
print()

# writelines() writes a LIST of strings (but still does NOT add \n for you)
lines = [
    "Line A: written with writelines()\n",
    "Line B: each item must include its own newline\n",
]

with open("multi.txt", "w") as f:
    f.writelines(lines)

print("Wrote multiple lines using writelines()")

# ══════════════════════════════════════════════════════════════
# SECTION 2: READING TEXT FILES
# ══════════════════════════════════════════════════════════════

print("=" * 55)
print("SECTION 2: READING TEXT FILES")
print("=" * 55)

with open("demo.txt", "r") as f:
    f.write("Hello")
# io.UnsupportedOperation: not writable

# The file handle is NOT the data — it's a connection
fhand = open("demo.txt", "r")          # "r" = read (the default)
print("File handle:", fhand)
fhand.close()
print()

# ── for loop (line by line) — MOST COMMON ─────────────────────
# Double-spacing problem: each line has \n AND print() adds one
print("Raw (double-spaced):")
with open("demo.txt") as f:
    for line in f:
        print(line)

# Fix: rstrip() removes trailing whitespace including \n
print("Fixed with rstrip():")
with open("demo.txt") as f:
    for line in f:
        print(line.rstrip())
print()

# ── The \n character ──────────────────────────────────────────
# \n LOOKS like two characters but is ONE (a newline)
print("Newline is 1 character:")
print(f"  len('X\\nY') = {len('X\nY')}")          # 3
print(f"  repr('Hello\\n') = {repr('Hello\n')}")
print()

# ── .read() — entire file as ONE string ───────────────────────
with open("demo.txt") as f:
    contents = f.read()
print(f".read():  type={type(contents).__name__}  len={len(contents)}")
print(f"  First 40 chars: {repr(contents[:40])}")
print()

# ── .readlines() — list of lines ─────────────────────────────
with open("demo.txt") as f:
    lines = f.readlines()
print(f".readlines():  type={type(lines).__name__}  count={len(lines)}")
print(f"  lines[0] raw:      {repr(lines[0])}")
print(f"  lines[0].rstrip(): {lines[0].rstrip()}")
print()

# ── .readline() — one line per call ──────────────────────────
with open("demo.txt") as f:
    first = f.readline()
    second = f.readline()
print(f".readline(): {first.rstrip()}  |  {second.rstrip()}")
print()

# When to use which:
#   for line in f     → process line by line (most common, memory efficient)
#   f.read()          → entire file as one string
#   f.readlines()     → list you can index/slice
#   f.readline()      → one line at a time


# ══════════════════════════════════════════════════════════════
# SECTION 3: SEARCHING IN FILES
# ══════════════════════════════════════════════════════════════

print("=" * 55)
print("SECTION 3: SEARCHING IN FILES")
print("=" * 55)

# Create a sample file to search through
with open("emails.txt", "w") as f:
    f.write("From: sarah@ucc.ie\n")
    f.write("Subject: Meeting tomorrow\n")
    f.write("Date: 2026-02-12\n")
    f.write("From: cian@ucc.ie\n")
    f.write("Subject: RE: Meeting\n")

# startswith() — match prefix
print("Lines starting with 'From:':")
with open("emails.txt") as f:
    for line in f:
        line = line.rstrip()
        if line.startswith("From:"):
            print(f"  {line}")

# "in" — substring anywhere in line
print("\nLines containing 'ucc':")
with open("emails.txt") as f:
    for line in f:
        line = line.rstrip()
        if "ucc" in line:
            print(f"  {line}")
print()


# ══════════════════════════════════════════════════════════════
# SECTION 4: ERROR HANDLING
# ══════════════════════════════════════════════════════════════

print("=" * 55)
print("SECTION 4: ERROR HANDLING")
print("=" * 55)

# Opening a missing file → FileNotFoundError
# try/except catches it so the programme can continue

fname = "missing_file.txt"
try:
    with open(fname) as f:
        data = f.read()
    print(f"Loaded {len(data)} chars from {fname}")
except FileNotFoundError:
    print(f"'{fname}' not found — using empty data")
    data = ""

print(f"Programme continues. data = {repr(data)}")
print()
# This is EXACTLY the pattern A3 uses for load_inventory()


# ══════════════════════════════════════════════════════════════
# SECTION 5: JSON FILES  (import json)
# ══════════════════════════════════════════════════════════════
# JSON = JavaScript Object Notation
# Python dicts/lists ←→ JSON map directly.
# A3 saves/loads inventory and transactions this way.

print("=" * 55)
print("SECTION 5: JSON FILES")
print("=" * 55)

student_grades = {
    "S001": {"name": "Siobhan", "programme": "BIS", "grades": [72, 85, 91]},
    "S002": {"name": "Cian",    "programme": "CS",  "grades": [65, 70, 58]},
    "S003": {"name": "Aoife",   "programme": "BIS", "grades": [88, 79, 95]},
}

# ── json.dump(): dict → JSON file ────────────────────────────
with open("grades.json", "w") as f:
    json.dump(student_grades, f, indent=2)
print("Saved to grades.json (indent=2 makes it readable)")

# What JSON looks like as a string:
print(json.dumps(student_grades["S001"], indent=2))
print()

# ── json.load(): JSON file → dict ────────────────────────────
with open("grades.json", "r") as f:
    loaded = json.load(f)

print(f"Loaded: type={type(loaded).__name__}, {len(loaded)} students")
print(f"Siobhan's grades: {loaded['S001']['grades']}")
# It's a normal dict — everything you learned in dict classes works!
print()

# ── Error handling: two things can go wrong ───────────────────
#   1. File missing      → FileNotFoundError
#   2. File corrupted    → json.JSONDecodeError

# Create a corrupted file for testing
with open("bad.json", "w") as f:
    f.write("{ this is NOT valid JSON !!! }")

def load_json_safe(filename):
    """Load JSON; return empty dict if missing or corrupted."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"  Note: {filename} not found. Starting empty.")
        return {}
    except json.JSONDecodeError:
        print(f"  Error: {filename} corrupted. Starting empty.")
        return {}

print("Safe JSON loading:")
print(f"  Valid:     {len(load_json_safe('grades.json'))} records")
print(f"  Missing:   {len(load_json_safe('nope.json'))} records")
print(f"  Corrupted: {len(load_json_safe('bad.json'))} records")
print()

# ── Lists work too (A3 transactions = list of dicts) ─────────
transactions = [
    {"action": "added",   "student": "Siobhan", "grade": 72},
    {"action": "updated", "student": "Cian",    "grade": 70},
]
with open("log.json", "w") as f:
    json.dump(transactions, f, indent=2)

with open("log.json", "r") as f:
    loaded_log = json.load(f)
print(f"List from JSON: {type(loaded_log).__name__}, {len(loaded_log)} items")
print()


# ══════════════════════════════════════════════════════════════
# SECTION 6: CSV FILES  (import csv)
# ══════════════════════════════════════════════════════════════
# CSV = Comma-Separated Values — opens in Excel/Sheets.
# Great for exporting data to non-programmers (A3 export).

print("=" * 55)
print("SECTION 6: CSV FILES")
print("=" * 55)

# ── Writing CSV ───────────────────────────────────────────────
# newline="" prevents extra blank rows on Windows
with open("grades.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name", "Programme", "Average"])  # header
    for sid, s in student_grades.items():
        avg = sum(s["grades"]) / len(s["grades"])
        writer.writerow([sid, s["name"], s["programme"], f"{avg:.1f}"])
print("Exported to grades.csv — open in Excel!")

# ── Reading CSV back ─────────────────────────────────────────
print("\nCSV contents:")
with open("grades.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"  {row}")
# Every value comes back as a STRING
print()


# ══════════════════════════════════════════════════════════════
# SECTION 7: THE A3 PATTERN  (save → close → load → export)
# ══════════════════════════════════════════════════════════════

print("=" * 55)
print("SECTION 7: FULL SAVE → LOAD → EXPORT CYCLE")
print("=" * 55)

employees = {
    "E001": {"name": "Sarah",  "dept": "Sales", "salary": 45000},
    "E002": {"name": "Cian",   "dept": "IT",    "salary": 52000},
    "E003": {"name": "Aoife",  "dept": "Sales", "salary": 48000},
}

def save_records(data, filename):
    """Save dict to JSON (like A3's save_inventory)."""
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"  Saved {len(data)} records to {filename}")
    except IOError as e:
        print(f"  Error saving: {e}")

def load_records(filename):
    """Load dict from JSON (like A3's load_inventory)."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"  {filename} not found. Starting empty.")
        return {}
    except json.JSONDecodeError:
        print(f"  {filename} corrupted. Starting empty.")
        return {}

def export_to_csv(data, filename):
    """Export to CSV (like A3's export_inventory_to_csv)."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Dept", "Salary"])
        for eid, emp in data.items():
            writer.writerow([eid, emp["name"], emp["dept"], emp["salary"]])
    print(f"  Exported to {filename}")

# Full cycle
print("Session 1 — save:")
save_records(employees, "employees.json")

print("Session 2 — load (as if restarted):")
loaded_emps = load_records("employees.json")
print(f"  Sarah's salary: €{loaded_emps['E001']['salary']:,}")

print("Export for management:")
export_to_csv(loaded_emps, "employees.csv")
print()


# ══════════════════════════════════════════════════════════════
# FILES SUMMARY
# ══════════════════════════════════════════════════════════════
#
# Modes:  "r" read (default)  |  "w" write (ERASES)  |  "a" append
#
# Reading:
#   for line in f        Line by line (most common, memory efficient)
#   f.read()             Entire file as one string
#   f.readlines()        List of lines (can index/slice)
#   f.readline()         One line at a time
#   line.rstrip()        Remove trailing \n
#
# Writing:
#   f.write(string)      Write one string — no auto \n
#   f.writelines(list)   Write a list of strings — no auto \n either!
#   ⚠️ There is no writeline() — it does not exist
#
# Reading vs Writing methods:
#   read()      ↔  write()        One string
#   readlines() ↔  writelines()   List of strings
#   readline()  ↔  (no match)     One line at a time (read only)
#
# Best practice:
#   with open() as f:    Auto-closes file (even on error)
#   try/except           Handle FileNotFoundError
#
# File paths (Windows only):
#   "C:\\folder\\file.txt"         Double backslash
#   r"C:\folder\file.txt"          Raw string
#   "C:/folder/file.txt"           Forward slashes (works everywhere)
#
# JSON  (import json):
#   json.dump(data, f, indent=2)    Dict/list → JSON file
#   json.load(f)                    JSON file → dict/list
#   json.dumps(data)                Dict/list → JSON string
#   json.loads(string)              JSON string → dict/list
#   json.JSONDecodeError            Corrupted file error
#
# CSV  (import csv):
#   writer = csv.writer(f)          Create writer
#   writer.writerow([...])          Write one row
#   writer.writerows([[...], ...])  Write multiple rows
#   reader = csv.reader(f)          Create reader (rows as lists of strings)
#   newline="" in open()            Prevent blank rows (Windows)
#   ⚠️ All values from csv.reader come back as strings
# ══════════════════════════════════════════════════════════════