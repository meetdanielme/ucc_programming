# ══════════════════════════════════════════════════════════════════
# EXERCISE B: PERSISTENT STUDENT RECORDS
# Client: "BrightPath Tutorial Centre"
#
# Background:
# BrightPath is a small tutorial centre near campus that runs
# weekly maths and English sessions. The owner, Dara, currently
# tracks student attendance and test scores on sticky notes,
# which he keeps losing. He needs a system that SAVES data
# between sessions so he doesn't start from scratch every Monday.
#
# He also wants to export a CSV summary he can email to parents,
# and a formatted text report to pin on the office wall.
#
# Build the functions below to give BrightPath persistent
# file storage.
# ══════════════════════════════════════════════════════════════════

import json
import csv
from datetime import datetime

# Sample data (nested dict — same structure as A3 inventory)
students = {
    "T001": {"name": "Siobhan", "subject": "Maths",   "scores": [72, 85, 91], "sessions": 12},
    "T002": {"name": "Cian",    "subject": "Maths",   "scores": [65, 70, 58], "sessions": 8},
    "T003": {"name": "Aoife",   "subject": "English", "scores": [88, 79, 95], "sessions": 15},
    "T004": {"name": "Ben",     "subject": "English", "scores": [55, 60, 52], "sessions": 6},
}


# TASK 1: save_students(students, filename)
# ------------------------------------------
# Save the students dictionary to a JSON file.
# Use indent=2 for readability.
# Wrap in try/except to handle IOError.
# Print confirmation: "Saved X students to <filename>"
# Print error message if saving fails.
#
# Expected: Creates a readable JSON file on disk.

def save_students(students, filename):
    try:
        with open(filename, "w") as f:
            json.dump(students, f, indent=2)
        print(f"Saved {len(students)} students to {filename}")
    except IOError as e:
        print(f"Error saving students to {filename}: {e}")


# TASK 2: load_students(filename)
# --------------------------------
# Load student records from a JSON file.
# Handle TWO errors:
#   - FileNotFoundError → print note, return empty dict {}
#   - json.JSONDecodeError → print error, return empty dict {}
# On success, print "Loaded X students from <filename>"
# Return the loaded dictionary.
#
# Expected:
#   load_students("students.json")  → loads data, returns dict
#   load_students("missing.json")   → prints note, returns {}
#   load_students("bad.json")       → prints error, returns {}

def load_students(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        print(f"Loaded {len(data)} students from {filename}")
        return data
    except FileNotFoundError:
        print(f"Note: {filename} not found. Starting fresh.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {filename}: {e}")
        return {}


# TASK 3: export_student_csv(students, filename)
# ------------------------------------------------
# Export student data to CSV for emailing to parents.
# Include header row: ID, Name, Subject, Average, Sessions
# Calculate average from scores list (1 decimal place).
# Remember: use newline="" to prevent blank rows.
#
# Expected CSV:
#   ID,Name,Subject,Average,Sessions
#   T001,Siobhan,Maths,82.7,12
#   T002,Cian,Maths,64.3,8
#   ...

def export_student_csv(students, filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Subject", "Average", "Sessions"])
        for student_id, info in students.items():
            avg_score = sum(info["scores"]) / len(info["scores"])
            writer.writerow([student_id, info["name"], info["subject"], f"{avg_score:.1f}", info["sessions"]])


# TASK 4: generate_report(students, filename)
# ---------------------------------------------
# Generate a formatted text report Dara can print out.
# Include:
#   - Header with centre name and current date/time
#   - Table of all students (ID, Name, Subject, Avg, Sessions)
#   - Footer with total students and overall average
# Use datetime.now().strftime("%Y-%m-%d %H:%M") for timestamp.
# Use f-strings for column alignment.
#
# Expected output in file:
#   ============================================================
#            BRIGHTPATH TUTORIAL CENTRE — PROGRESS REPORT
#            Generated: 2026-02-12 14:30
#   ============================================================
#
#   ID     Name            Subject     Avg    Sessions
#   ============================================================
#   T001   Siobhan         Maths       82.7   12
#   T002   Cian            Maths       64.3   8
#   ...
#   ============================================================
#   Total Students: 4
#   Overall Average: 73.5
#   ============================================================

def generate_report(students, filename):
    with open(filename, "w") as f:
        f.write("=" * 60 + "\n")
        f.write("            BRIGHTPATH TUTORIAL CENTRE — PROGRESS REPORT\n")
        f.write(f"            Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write("=" * 60 + "\n\n")

        f.write("ID     Name            Subject     Avg    Sessions\n")
        f.write("=" * 60 + "\n")

        total_students = len(students)
        total_score = 0
        for student_id, info in students.items():
            avg_score = sum(info["scores"]) / len(info["scores"])
            total_score += avg_score
            f.write(f"{student_id:<6} {info['name']:<15} {info['subject']:<11} {avg_score:<6.1f} {info['sessions']}\n")

        f.write("=" * 60 + "\n")
        overall_avg = total_score / total_students if total_students > 0 else 0
        f.write(f"Total Students: {total_students}\n")
        f.write(f"Overall Average: {overall_avg:.1f}\n")
        f.write("=" * 60 + "\n")


# ── Test your functions ──────────────────────────────────────────
print("=" * 50)
print("  BRIGHTPATH TUTORIAL CENTRE — FILE SYSTEM TEST")
print("=" * 50)

# Test save
print("\n--- Task 1: Save ---")
save_students(students, "students.json")

# Test load (valid file)
print("\n--- Task 2: Load (valid) ---")
loaded = load_students("students.json")
print(f"Siobhan's scores: {loaded['T001']['scores']}")

# Test load (missing file)
print("\n--- Task 2: Load (missing) ---")
empty = load_students("nonexistent.json")
print(f"Result: {empty}")

# Test load (corrupted file)
print("\n--- Task 2: Load (corrupted) ---")
with open("bad.json", "w") as f:
    f.write("NOT VALID JSON {{{")
corrupt = load_students("bad.json")
print(f"Result: {corrupt}")

# Test CSV export
print("\n--- Task 3: CSV Export ---")
export_student_csv(students, "students.csv")
print("Verifying CSV:")
with open("students.csv", "r") as f:
    for row in f:
        print(f"  {row.rstrip()}")

# Test report
print("\n--- Task 4: Text Report ---")
generate_report(students, "progress_report.txt")
print("Report contents:")
with open("progress_report.txt", "r") as f:
    print(f.read())


# REFLECTION:
# 1. Why do we handle BOTH FileNotFoundError and JSONDecodeError
#    in load_students() instead of just one?
# 2. Why do we use indent=2 in json.dump() instead of leaving
#    it out?
# 3. What would happen if you forgot newline="" when writing CSV
#    on Windows?