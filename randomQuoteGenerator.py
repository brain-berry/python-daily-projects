import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Do something today that your future self will thank you for.",
    "Dream big. Start small. Act now.",
    "The best way to predict the future is to create it.",
    "Great things never come from comfort zones.",
    "Your only limit is your mind.",
    "Push yourself, because no one else is going to do it for you.",
    "A hungry man, ia an angry man.",
    "Stay hungry. Stay foolish."
]

def typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()

def loading_animation():
    print(Fore.CYAN + "\nGenerating wisdom", end="")
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print("\n")

while True:
    loading_animation()

    quote = random.choice(quotes)

    print(Fore.YELLOW + Style.BRIGHT + "✨ RANDOM QUOTE ✨\n")
    typing_effect(Fore.GREEN + f'"{quote}"')

    print(Fore.MAGENTA + "\n" + "-"*50)

    again = input(Fore.CYAN + "\nGenerate another quote? (y/n): ").lower()
    if again != "y":
        print(Fore.RED + "\nStay inspired. Goodbye 👋")
        break
