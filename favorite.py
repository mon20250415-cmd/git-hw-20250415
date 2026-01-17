"""
Jordan Pizza Picker 🍕
A tiny script that recommends a pizza place based on style + budget.

Run:
    python pizza_picker.py
"""

pizza_places = [
    {"name": "Pizza Hut",     "style": "classic",  "price": 8},
    {"name": "Domino's",      "style": "classic",  "price": 7},
    {"name": "Oliva Pizza",   "style": "italian",  "price": 12},
    {"name": "The Big Slice", "style": "newyork",  "price": 9},
]

print("🍕 Jordan Pizza Picker")
style = input("Style? (classic / italian / newyork): ").strip().lower()
budget = float(input("Max budget in JD? ").strip())

best = None

for p in pizza_places:
    if p["style"] == style and p["price"] <= budget:
        # pick the closest-to-budget option (highest price under budget)
        if best is None or p["price"] > best["price"]:
            best = p

if best:
    print(f"🍕 Order from: {best['name']} (~{best['price']} JD)")
else:
    print("😔 No match. Try higher budget or different style.")
