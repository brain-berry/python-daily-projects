import json
from datetime import datetime
import os

FILENAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks yet.")
        return

    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['task']}")
        print(f"   Priority: {task['priority']} | Created: {task['time']}")

tasks = load_tasks()

print("🔥 ADVANCED TO-DO LIST")
print("-" * 30)

while True:
    print("\nOptions:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks(tasks)

    elif choice == "2":
        text = input("Enter task: ")
        priority = input("Priority (High/Medium/Low): ").capitalize()

        new_task = {
            "task": text,
            "done": False,
            "priority": priority,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        tasks.append(new_task)
        save_tasks(tasks)
        print("✅ Task added!")

    elif choice == "3":
        show_tasks(tasks)
        try:
            num = int(input("Enter task number: "))
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print("🎉 Task marked as completed!")
        except:
            print("❌ Invalid number.")

    elif choice == "4":
        show_tasks(tasks)
        try:
            num = int(input("Enter task number to delete: "))
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑 Removed: {removed['task']}")
        except:
            print("❌ Invalid number.")

    elif choice == "5":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice.")
