import random
import time

print(" RANDOM NAME PICKER ")
print ("-" * 25)

items = input ("Enter names/items separated by commas:\n")

items_list = [item.strip() for item  in items.split(",")]

print ("\nChoosing", end = "")

for i in range (5):
  print(".", end = "", flush = True)
  time.sleep(0.5)

winner = random.choice(items_list)

print (f"\n\n Selected: {winner}")
