import json
import os
from datetime import datetime

FILENAME = "items.json"

def load_items():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return json.load(file)

def save_items(items):
    with open(FILENAME, "w") as file:
        json.dump(items, file, indent=4)

def add_item(items, item_type):
    name = input("Item name: ")
    description = input("Description: ")
    location = input("Location: ")

    item = {
        "name": name,
        "description": description,
        "location": location,
        "type": item_type,
        "status": "available",
        "claimed_by": None,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    items.append(item)
    save_items(items)
    print(f"✅ {item_type.capitalize()} item reported!")

def view_items(items):
    if not items:
        print("📭 No items yet.")
        return

    for i, item in enumerate(items, 1):
        print(f"\n{i}. {item['name']} ({item['type']})")
        print(f"   📍 {item['location']}")
        print(f"   📝 {item['description']}")
        print(f"   📊 Status: {item['status']}")

        if item["claimed_by"]:
            print(f"   👤 Claimed by: {item['claimed_by']}")

def claim_item(items):
    view_items(items)

    try:
        num = int(input("\nEnter item number to claim: "))
        item = items[num - 1]

        if item["status"] == "claimed":
            print("❌ This item is already claimed.")
            return

        name = input("Enter your name: ")

        item["status"] = "claimed"
        item["claimed_by"] = name

        save_items(items)
        print("🎉 Item successfully claimed!")

    except:
        print("❌ Invalid selection.")

def search_items(items):
    keyword = input("Search keyword: ").lower()

    results = [
        item for item in items
        if keyword in item["name"].lower()
        or keyword in item["description"].lower()
        or keyword in item["location"].lower()
    ]

    if not results:
        print("❌ No matching items.")
        return

    print("\n🔍 Results:")
    for item in results:
        print(f"\n📦 {item['name']} ({item['type']})")
        print(f"📍 {item['location']}")
        print(f"📝 {item['description']}")
        print(f"📊 Status: {item['status']}")

# --- Main ---
items = load_items()

print("📦 LOST & FOUND SYSTEM (WITH CLAIMS)")
print("-" * 40)

while True:
    print("\nOptions:")
    print("1. Report Lost Item")
    print("2. Report Found Item")
    print("3. View Items")
    print("4. Search Items")
    print("5. Claim Item")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_item(items, "lost")

    elif choice == "2":
        add_item(items, "found")

    elif choice == "3":
        view_items(items)

    elif choice == "4":
        search_items(items)

    elif choice == "5":
        claim_item(items)

    elif choice == "6":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid option")