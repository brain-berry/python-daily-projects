import json
import os
from datetime import datetime

FILENAME = "notes.json"

def load_notes():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return json.load(file)

def save_notes(notes):
    with open(FILENAME, "w") as file:
        json.dump(notes, file, indent=4)

def add_note(notes):
    text = input("Enter note: ")
    tags = input("Enter tags (comma-separated): ").lower().split(",")

    note = {
        "text": text,
        "tags": [t.strip() for t in tags],
        "time": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    notes.append(note)
    save_notes(notes)
    print(" Note saved!")

def view_notes(notes):
    if not notes:
        print("📭 No notes yet.")
        return

    for i, note in enumerate(notes, 1):
        print(f"\n{i}. {note['text']}")
        print(f"   🏷 Tags: {', '.join(note['tags'])}")
        print(f"   ⏱ {note['time']}")

def search_notes(notes):
    query = input("Search keyword or tag: ").lower()

    found = []

    for note in notes:
        if query in note["text"].lower() or query in note["tags"]:
            found.append(note)

    if not found:
        print(" No matching notes.")
        return

    print("\n Results:")
    for note in found:
        print(f"\n {note['text']}")
        print(f"🏷 {', '.join(note['tags'])}")
        print(f"⏱ {note['time']}")

# --- Main App ---
notes = load_notes()

print(" SMART NOTES APP")
print("-" * 30)

while True:
    print("\nOptions:")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Notes")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_note(notes)

    elif choice == "2":
        view_notes(notes)

    elif choice == "3":
        search_notes(notes)

    elif choice == "4":
        print(" Goodbye!")
        break

    else:
        print(" Invalid option")