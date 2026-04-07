import random

# ──────────────────────────────────────────────
#  NUMBER GUESSER GAME
# ──────────────────────────────────────────────

print("\n" + "=" * 40)
print("  NUMBER GUESSER GAME")
print("=" * 40)

# Generate random number between 1 and 100
number = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("\nI'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it!\n")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        attempts += 1

        # Validate range
        if guess < 1 or guess > 100:
            print("  Please enter a number between 1 and 100.\n")
            attempts -= 1  # Don't count invalid input
            continue

        # Check if the guess is correct
        if guess < number:
            print("  Too low! Try again.\n")
        elif guess > number:
            print("  Too high! Try again.\n")
        else:
            print(f"\n  Congratulations! You guessed it in {attempts} attempt(s)!")
            break

    except ValueError:
        print("  Invalid input. Please enter a whole number.\n")
        attempts -= 1  # Don't count invalid input

else:
    # Loop finished without a correct guess
    print(f"\n  Game Over! The number was {number}.")
    print(f"  You used all {max_attempts} attempts.\n")
