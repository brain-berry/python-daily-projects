import random
import os

# ──────────────────────────────────────────────
#  CONSTANTS
# ──────────────────────────────────────────────
CHOICES    = ("rock", "paper", "scissors")
EMOJIS     = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
# Each choice maps to what it beats
WINS_AGAINST = {
    "rock":     "scissors",
    "paper":    "rock",
    "scissors": "paper",
}


# ──────────────────────────────────────────────
#  GAME LOGIC
# ──────────────────────────────────────────────
def get_player_choice():
    """Prompt until the player enters a valid choice or 'q'."""
    while True:
        choice = input("\n  Choose rock (r), paper (p), scissors (s), or 'q' to quit: ").strip().lower()

        # Allow single-letter shortcuts
        shortcuts = {"r": "rock", "p": "paper", "s": "scissors"}
        if choice in shortcuts:
            return shortcuts[choice]
        if choice in CHOICES:
            return choice
        if choice == "q":
            return None

        print("  ❌ Invalid choice. Try again.")


def determine_winner(player, computer):
    """Return 'player', 'computer', or 'tie'."""
    if player == computer:
        return "tie"
    if WINS_AGAINST[player] == computer:
        return "player"
    return "computer"


def display_result(player, computer, result):
    """Print the round outcome with emojis."""
    print(f"\n  You: {EMOJIS[player]}  {player.upper()}")
    print(f"  CPU: {EMOJIS[computer]}  {computer.upper()}")
    print("  ─────────────────")

    if result == "tie":
        print("  🤝 It's a tie!")
    elif result == "player":
        print(f"  🎉 You win! {player.title()} beats {computer}.")
    else:
        print(f"  💻 Computer wins! {computer.title()} beats {player}.")


def display_scoreboard(player_score, computer_score, ties, round_num):
    """Print the current scoreboard."""
    print(f"\n  ┌─────────── Round {round_num} ───────────┐")
    print(f"  │  You: {player_score}  │  CPU: {computer_score}  │  Ties: {ties}  │")
    print(f"  └──────────────────────────────┘")


def display_final_summary(player_score, computer_score, ties, total_rounds):
    """Print a game-over summary."""
    print("\n  ╔══════════════════════════════╗")
    print("  ║        GAME OVER             ║")
    print("  ╠══════════════════════════════╣")
    print(f"  ║  Rounds played : {total_rounds:<11}║")
    print(f"  ║  Your wins     : {player_score:<11}║")
    print(f"  ║  CPU wins      : {computer_score:<11}║")
    print(f"  ║  Ties          : {ties:<11}║")
    print("  ╠══════════════════════════════╣")

    if player_score > computer_score:
        print("  ║  🏆 YOU ARE THE CHAMPION!    ║")
    elif computer_score > player_score:
        print("  ║  🤖 Computer takes the win!  ║")
    else:
        print("  ║  🤝 It's a draw overall!     ║")

    print("  ╚══════════════════════════════╝")
    print("\n  Thanks for playing!\n")


# ──────────────────────────────────────────────
#  MAIN GAME LOOP
# ──────────────────────────────────────────────
def main():
    player_score   = 0
    computer_score = 0
    ties           = 0
    round_num      = 0

    print("\n  ╔══════════════════════════════╗")
    print("  ║   ROCK, PAPER, SCISSORS 🎮   ║")
    print("  ╚══════════════════════════════╝")

    while True:
        player_choice = get_player_choice()

        # Player wants to quit
        if player_choice is None:
            display_final_summary(player_score, computer_score, ties, round_num)
            break

        computer_choice = random.choice(CHOICES)
        round_num += 1

        result = determine_winner(player_choice, computer_choice)

        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
        else:
            ties += 1

        display_result(player_choice, computer_choice, result)
        display_scoreboard(player_score, computer_score, ties, round_num)


if __name__ == "__main__":
    main()
