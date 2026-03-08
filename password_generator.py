import random
import string

try:
    import pyperclip
    clipboard_available = True  

except:
    clipboard_available = False  
    print("pyperclip module not found. Clipboard functionality will be disabled.")
    
def password_strength (password):
    score = 0
    
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if len(password) >= 12:
        score += 1
        
    if score <= 2:
        print("Weak password. Consider adding more character types and increasing the length.")
    elif score == 3 or score == 4:
        print("Moderate password. Consider adding more character types and increasing the length for better security.")
    else:
        return "Strong password! Good job!"    

print ("Wanted to generate a strong password? Let's do it!")

length = int(input("Enter the desired password length: "))
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
count = int(input("How many passwords to generate? "))

characters = string.ascii_letters

if use_numbers:
    characters += string.digits
    
if use_symbols:
    characters += string.punctuation
    
print("\nGenerated Passwords: \n")

for i in range(count):
    password = ''.join(random.choice(characters) for _ in range(length))
    strength = password_strength(password)
    
    print(f"{i + 1}.{password} | Strength: {strength}")
    
    if clipboard_available:
        pyperclip.copy(password)
        
if clipboard_available:
    print("\nLast password copied to clipboard")
else:
    print('\nInstall pyperclip to enable clipboard functionality: pip install pyperclip')