print("🔄 PALINDROME CHECKER")
print("-" * 25)

text = input("Enter a word or sentence: ")

# Clean the text
cleaned = text.replace(" ", "").lower()

# Check palindrome
if cleaned == cleaned[::-1]:
    print("✅ It's a palindrome!")
else:
    print("❌ Not a palindrome.")
