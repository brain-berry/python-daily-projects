import os

FILENAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return file.read().splitlines()

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks yet.")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

tasks = load_tasks()

print("📝 TO-DO LIST")
print("-" * 25)

while True:
    print("\nOptions:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks(tasks)

    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        save_tasks(tasks)
        print("✅ Task added!")

    elif choice == "3":
        show_tasks(tasks)
        try:
            num = int(input("Enter task number to delete: "))
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑 Removed: {removed}")
        except:
            print("❌ Invalid number.")

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice.")