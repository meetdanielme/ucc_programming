# ══════════════════════════════════════════════════════════════
# EXERCISE A: DATABASE OPERATIONS PRACTICE — SOLUTIONS
# Client: "CoastalBrew Coffee Roasters"
# ══════════════════════════════════════════════════════════════

import json
import csv


# ── Section 1: CREATE — Save to JSON database ───────────────

beans = {
    "B001": {"name": "Ethiopian Yirgacheffe", "origin": "Ethiopia", "price": 14.50, "stock_kg": 25},
    "B002": {"name": "Colombian Supremo",     "origin": "Colombia", "price": 12.00, "stock_kg": 40},
    "B003": {"name": "Kenyan AA",             "origin": "Kenya",    "price": 16.00, "stock_kg": 15},
}

with open("beans.json", "w") as f:
    json.dump(beans, f, indent=2)

print("Database created with", len(beans), "records")


# ── Section 2: READ — Load with error handling ──────────────

try:
    with open("beans.json", "r") as f:
        loaded = json.load(f)
    print(f"Loaded {len(loaded)} records")
except FileNotFoundError:
    print("File not found — starting empty")
    loaded = {}


# ── Section 3: UPDATE — Modify a record and persist ─────────

loaded["B001"]["price"] = 15.50

with open("beans.json", "w") as f:
    json.dump(loaded, f, indent=2)

print("Price updated and saved")


# ── Section 4: DELETE — Remove a record and persist ──────────

del loaded["B003"]

with open("beans.json", "w") as f:
    json.dump(loaded, f, indent=2)

print(f"Record deleted. Remaining: {len(loaded)}")


# ── Section 5: EXPORT — CSV flat-file for customers ─────────

with open("beans_catalogue.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name", "Origin", "Price per kg"])
    for bid, bean in loaded.items():
        writer.writerow([bid, bean["name"], bean["origin"],
                        f"{bean['price']:.2f}"])

print("Exported to CSV")
