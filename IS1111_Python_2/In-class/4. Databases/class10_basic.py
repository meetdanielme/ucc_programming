# ══════════════════════════════════════════════════════════════
# EXERCISE A: DATABASE OPERATIONS PRACTICE
# Client: "CoastalBrew Coffee Roasters"
#
# CoastalBrew is a Cork-based specialty coffee roastery that
# sources beans from around the world. They track their bean
# inventory digitally and need proper database operations —
# Create, Read, Update, Delete — with persistent JSON storage
# and CSV export for their wholesale customers.
#
# Fill in the blanks to build their database system.
# ══════════════════════════════════════════════════════════════

import ______
import ______


# ── Section 1: CREATE — Save to JSON database ───────────────

beans = {
    "B001": {"name": "Ethiopian Yirgacheffe", "origin": "Ethiopia", "price": 14.50, "stock_kg": 25},
    "B002": {"name": "Colombian Supremo",     "origin": "Colombia", "price": 12.00, "stock_kg": 40},
    "B003": {"name": "Kenyan AA",             "origin": "Kenya",    "price": 16.00, "stock_kg": 15},
}

with open("beans.json", ______) as f:
    json.______(beans, f, ______=2)

print("Database created with", len(beans), "records")


# ── Section 2: READ — Load with error handling ──────────────

______:
    with open("beans.json", "r") as f:
        loaded = json.______(f)
    print(f"Loaded {len(loaded)} records")
except ______:
    print("File not found — starting empty")
    loaded = ______


# ── Section 3: UPDATE — Modify a record and persist ─────────

# Ethiopian price increased to 15.50
loaded[______][______] = 15.50

with open("beans.json", ______) as f:
    json.dump(loaded, f, indent=2)

print("Price updated and saved")


# ── Section 4: DELETE — Remove a record and persist ──────────

______ loaded[______]

with open("beans.json", "w") as f:
    json.______(loaded, f, indent=2)

print(f"Record deleted. Remaining: {______(loaded)}")


# ── Section 5: EXPORT — CSV flat-file for customers ─────────

with open("beans_catalogue.csv", "w", ______="") as f:
    writer = csv.______(f)
    writer.______(["ID", "Name", "Origin", "Price per kg"])
    for bid, bean in loaded.______():
        writer.writerow([bid, bean["name"], bean["origin"],
                        f"{bean['price']:.2f}"])

print("Exported to CSV")
