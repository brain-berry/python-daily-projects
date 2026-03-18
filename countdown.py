import time

print("COUNTDOWN TIMER")
print ("-" * 25)

seconds = int(input("Enter the number of seconds: "))

while seconds:
    mins, secs = divmod(seconds, 60)
    timer = f"{mins:02d}:{secs:02d}"
    
    print(timer, end="\r")
    time.sleep(1)
    seconds -= 1

#print("Time's up!")
for i in range(3):
    print("Time's up!")
    time.sleep(0.5)
    
prompt = "Hey, what's up? "
user_input = input(prompt)
print("You said: " + user_input)