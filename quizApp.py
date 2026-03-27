import threading
import time
from colorama import Fore, Style, init

init(autoreset=True)

questions = [
    {
        "question": "What is the capital of Ghana?",
        "options": ["A. Kumasi", "B. Accra", "C. Tamale", "D. Cape Coast"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. Java", "C. JavaScript", "D. All of the above"],
        "answer": "D"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Computer Personal Unit", "C. Central Program Utility", "D. None"],
        "answer": "A"
    }
]

score = 0
time_limit = 10

def countdown():
    for i in range(time_limit, 0, -1):
        print(Fore.YELLOW + f"⏱ Time left: {i}s ", end="\r")
        time.sleep(1)

def timed_input(prompt):
    answer = [None]

    def get_input():
        answer[0] = input(Fore.CYAN + prompt)

    input_thread = threading.Thread(target=get_input)
    timer_thread = threading.Thread(target=countdown)

    input_thread.start()
    timer_thread.start()

    input_thread.join(time_limit)

    if input_thread.is_alive():
        return None

    return answer[0]

print(Fore.MAGENTA + Style.BRIGHT + "🧠 QUIZ GAME (Timed & Flashy)")
print("-" * 40)

for q in questions:
    print("\n" + Fore.WHITE + Style.BRIGHT + q["question"])

    for option in q["options"]:
        print(Fore.BLUE + option)

    answer = timed_input("Your answer (A/B/C/D): ")

    if answer is None:
        print(Fore.RED + "\n⏰ Time's up!")
        continue

    answer = answer.upper()

    if answer == q["answer"]:
        print(Fore.GREEN + "✅ Correct!")
        score += 1
    else:
        print(Fore.RED + f"❌ Wrong! Correct answer: {q['answer']}")

print("\n" + Fore.MAGENTA + "🎯 FINAL SCORE")
print("-" * 20)
print(Fore.CYAN + f"You got {score} out of {len(questions)}")

if score == len(questions):
    print(Fore.GREEN + "🔥 Perfect! Genius level!")
elif score >= 2:
    print(Fore.YELLOW + "👏 Nice work!")
else:
    print(Fore.RED + "😅 Keep practicing!")