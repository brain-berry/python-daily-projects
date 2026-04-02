import random
import time

# ──────────────────────────────────────────────
#  RANDOM NAME PICKER
# ──────────────────────────────────────────────

print("\n" + "=" * 30)
print("  RANDOM NAME PICKER")
print("=" * 30)

items = input("\nEnter names/items separated by commas:\n").strip()

# Handle empty input
if not items:
    print("\n  No items entered. Nothing to pick from.")
else:
    # Clean up the list and remove empty entries
    items_list = [item.strip() for item in items.split(",") if item.strip()]

    if len(items_list) < 2:
        print("\n  Please enter at least 2 items to pick from.")
    else:
        # Show the entries
        print(f"\n  Entries ({len(items_list)}):")
        for i, item in enumerate(items_list, 1):
            print(f"    {i}. {item}")

        # Dramatic selection animation
        print("\n  Choosing", end="")
        for i in range(5):
            print(".", end="", flush=True)
            time.sleep(0.5)

        winner = random.choice(items_list)

        print(f"\n\n  Selected: {winner}")
