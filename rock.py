import random

choices = [ "rock", "paper", "scissors"]
player_score = 0
computer_score = 0

print("ROCK, PAPER, SCISSORS")
print("-" * 30)

while True:
  player = input("\nChoose rock, paper, or scissors (or 'q' to quit): ").lower()

  if player == 'q':
    print("\nFinal Score")
    print(f"You: {player_score} | Computer: {computer_score}")
    print("Thanks for playing!")
    break

  if player not in choicea:
  print("Invalid choice. Try again.")
  continue

  computer = random.choice (choices)

  print(f"Computer chose: {computer}")

  if player == computer:
    print("It's a tie! ")

  elif (
    (player == "rock" and computer == "scissors") or
    (player == "paper" and computer == "rock") or
    (player == "scissors" and computer == "paper") 
  ):
    print("You win!")
    player_score += 1

  else:
    print("Computer Wins! ")
    computer_score += 1

  print(f"Score => You: {player_score} | Computer: {computer_score}")

