import random
import time

# ASCII dice faces
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘",
    ),
}

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def print_dice(dice):
    dice_faces = [DICE_ART[d] for d in dice]

    for line in range(5):
        for die in dice_faces:
            print(die[line], end="  ")
        print()

def main():
    print("🎲 Welcome to Advanced Dice Simulator 🎲")

    while True:
        try:
            num_dice = int(input("\nHow many dice do you want to roll? (1 or 2): "))
            if num_dice not in [1, 2]:
                print("Please choose 1 or 2.")
                continue
        except ValueError:
            print("Enter a valid number.")
            continue

        choice = input("Roll the dice? (yes/no): ").lower()

        if choice == "yes":
            print("\nRolling", end="")
            for _ in range(3):
                print(".", end="", flush=True)
                time.sleep(0.5)
            print("\n")

            dice = roll_dice(num_dice)
            print_dice(dice)

            print(f"\nYou rolled: {dice}")
            print(f"Total: {sum(dice)}")

        elif choice == "no":
            print("\nGoodbye! 👋")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
