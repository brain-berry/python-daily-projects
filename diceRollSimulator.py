import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("🎲 Welcome to Dice Rolling Simulator!")

    while True:
        choice = input("\nRoll the dice? (yes/no): ").lower()

        if choice == "yes":
            dice1 = roll_dice()
            dice2 = roll_dice()

            print(f"\nYou rolled: {dice1} and {dice2}")
            print(f"Total: {dice1 + dice2}")

        elif choice == "no":
            print("\nThanks for playing! 👋")
            break

        else:
            print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    main()
