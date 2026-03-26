# EXPENSE TRACKER
# Practice: file I/O, data structures, user input, functions

import os

# ──────────────────────────────────────────────
#  DATA STORAGE
# ──────────────────────────────────────────────
expenses = []


# ──────────────────────────────────────────────
#  FILE FUNCTIONS
# ──────────────────────────────────────────────
def save_expenses(filename="expenses.txt"):
    """Save all expenses to a text file."""
    try:
        with open(filename, "w") as file:
            for expense in expenses:
                line = f"{expense['amount']},{expense['category']},{expense['description']}\n"
                file.write(line)
        print(f"\n  Expenses saved to {filename}.")
    except Exception:
        print("\n  Error saving expenses.")


def load_expenses(filename="expenses.txt"):
    """Load expenses from a text file into the list."""
    if not os.path.exists(filename):
        print("  No existing expense file found. Starting fresh.\n")
        return

    try:
        with open(filename, "r") as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split(",", 2)
                    expense = {
                        "amount":      float(parts[0]),
                        "category":    parts[1],
                        "description": parts[2],
                    }
                    expenses.append(expense)
        print(f"  Loaded {len(expenses)} expense(s) from {filename}.\n")
    except Exception:
        print("  Error loading expenses.\n")


# ──────────────────────────────────────────────
#  EXPENSE FUNCTIONS
# ──────────────────────────────────────────────
def add_expense():
    """Collect expense details from the user and store them."""
    print("\n--- Add New Expense ---")

    try:
        amount = float(input("  Enter amount spent: $"))
        if amount <= 0:
            print("  Amount must be positive.")
            return
    except ValueError:
        print("  Invalid amount. Please enter a number.")
        return

    category    = input("  Enter category (food, transport, etc.): ").strip().lower()
    description = input("  Enter description: ").strip()

    if not category or not description:
        print("  Category and description cannot be empty.")
        return

    expense = {
        "amount":      amount,
        "category":    category,
        "description": description,
    }

    expenses.append(expense)
    print(f"\n  Added: ${amount:.2f} for '{description}' [{category}]")


def view_expenses():
    """Display all expenses and a total."""
    if not expenses:
        print("\n  No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    total = 0

    for i, expense in enumerate(expenses, 1):
        print(f"  {i}. ${expense['amount']:.2f} | {expense['category']} | {expense['description']}")
        total += expense["amount"]

    print(f"\n  Total spent: ${total:.2f}")


def view_by_category():
    """Show spending totals grouped by category."""
    if not expenses:
        print("\n  No expenses recorded yet.")
        return

    categories = {}

    for expense in expenses:
        cat    = expense["category"]
        amount = expense["amount"]

        if cat not in categories:
            categories[cat] = 0
        categories[cat] += amount

    print("\n--- Expenses by Category ---")
    for category, total in categories.items():
        print(f"  {category.title()}: ${total:.2f}")


def search_expense():
    """Search expenses by category name."""
    if not expenses:
        print("\n  No expenses to search.")
        return

    query   = input("  Enter category to search: ").strip().lower()
    results = [e for e in expenses if e["category"] == query]

    if results:
        print(f"\n--- Results for '{query}' ---")
        total = 0
        for i, expense in enumerate(results, 1):
            print(f"  {i}. ${expense['amount']:.2f} | {expense['description']}")
            total += expense["amount"]
        print(f"\n  Subtotal: ${total:.2f}")
    else:
        print(f"  No expenses found in '{query}'.")


# ──────────────────────────────────────────────
#  MAIN MENU
# ──────────────────────────────────────────────
def main():
    print("\n" + "=" * 35)
    print("  SIMPLE EXPENSE TRACKER")
    print("=" * 35)

    load_expenses()

    while True:
        print("\n  1. Add expense")
        print("  2. View all expenses")
        print("  3. View by category")
        print("  4. Search by category")
        print("  5. Save and exit")
        print("  6. Exit without saving")

        choice = input("\n  Enter your choice (1-6): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_by_category()
        elif choice == "4":
            search_expense()
        elif choice == "5":
            save_expenses()
            print("\n  Goodbye!\n")
            break
        elif choice == "6":
            print("\n  Goodbye! (Changes not saved)\n")
            break
        else:
            print("  Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
