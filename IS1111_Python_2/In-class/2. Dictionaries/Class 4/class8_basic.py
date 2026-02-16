# ══════════════════════════════════════════════════════════════
# EXERCISE: DATETIME, TRANSACTION LOGGING & DICT COMPREHENSION
# Fill in the blanks to complete each section.
# Theme: Gym check-in tracking system
# ══════════════════════════════════════════════════════════════


# ──────────────────────────────────────────────────────────────
# SECTION 1: THE DATETIME MODULE
# ──────────────────────────────────────────────────────────────

# 1) Import the datetime class from the datetime module.
from datetime import datetime

# 2) Get the current date and time.
right_now = datetime.now()
print("Current time:", right_now)

# 3) Convert the datetime to a string for STORAGE using isoformat.
time_string = right_now.isoformat()
print("As string:", time_string)
print("Type:", type(time_string))

# 4) Convert a stored ISO string BACK to a datetime object,
#    then format it for DISPLAY using strftime.
stored = "2026-02-10T09:45:30.123456"
parsed = datetime.fromisoformat(stored)
display = parsed.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", display)


# ──────────────────────────────────────────────────────────────
# SECTION 2: BUILDING AN EVENT DICTIONARY
# ──────────────────────────────────────────────────────────────

# 5) Create a check-in event dict with a timestamp.
#    The timestamp should be stored as a STRING (for saving later).
checkin = {
    "type": "checkin",
    "member_name": "Alice",
    "station": "Treadmill",
    "timestamp": datetime.now().isoformat()
}
print("\nCheck-in:", checkin)


# ──────────────────────────────────────────────────────────────
# SECTION 3: THE LOGGING FUNCTION
# ──────────────────────────────────────────────────────────────

# 6) Complete the log_checkin function that builds the event
#    dict and appends it to the log list.
activity_log = []

def log_checkin(log, member_name, station):
    entry = {
        "type": "checkin",
        "member_name": member_name,
        "station": station,
        "timestamp": datetime.now().isoformat()
    }
    log.append(entry)

# 7) Log five check-ins.
log_checkin(activity_log, "Alice", "Treadmill")
log_checkin(activity_log, "Bob", "Weights")
log_checkin(activity_log, "Alice", "Rowing")
log_checkin(activity_log, "Cara", "Treadmill")
log_checkin(activity_log, "Dave", "Cycling")

print(f"Total check-ins: {len(activity_log)}")


# ──────────────────────────────────────────────────────────────
# SECTION 4: VIEWING THE LOG
# ──────────────────────────────────────────────────────────────

# 8) Get the last 3 check-ins using list slicing.
recent = activity_log[-3:]

# 9) Display them newest-first, printing the timestamp directly.
print(f"\n{'Time':<22} {'Member':<12} {'Station':<12}")
print("=" * 46)

for entry in reversed(recent):
    print(f"{entry['timestamp']:<22} {entry['member_name']:<12} {entry['station']:<12}")


# ──────────────────────────────────────────────────────────────
# SECTION 5: SIGNED FORMATTING & DICT COMPREHENSION
# ──────────────────────────────────────────────────────────────

# 10) Use :+d to always show the sign (+ or -) on each number.
changes = [3, -1, 5, -2]
print("\nCapacity changes:")
for c in changes:
    print(f"  Change: {c:+d}")

# 11) Dict comprehension: create a dict that doubles each value.
#     Keys should be "slot_0", "slot_1", etc.
doubled = {f"slot_{i}": c * 2 for i, c in enumerate(changes)}
print("Doubled:", doubled)