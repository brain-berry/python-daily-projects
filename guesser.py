import random

#Generate a random number between 1 and 100
number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guesser Game!")
print("I am thinking of a number between 1 and 100. Can you guess it?")

while True:
    #Get the user's guess
    guess = int(input("Enter your guess: "))
    attempts += 1

    #Check if the guess is correct
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} attempts!")
        break