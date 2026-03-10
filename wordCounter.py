from collections import Counter

print("📊 Fancy Word Counter")
print("-" * 30)

text = input("\nEnter your text:\n")

# Word count
words = text.split()
word_count = len(words)

# Character count (excluding spaces)
char_count = len(text.replace(" ", ""))

# Sentence count
sentences = text.count(".") + text.count("!") + text.count("?")

# Most common words
word_freq = Counter(words)
common_words = word_freq.most_common(3)

print("\n📈 TEXT ANALYSIS")
print("-" * 30)
print(f"Total Words: {word_count}")
print(f"Total Characters (no spaces): {char_count}")
print(f"Total Sentences: {sentences}")

print("\n🔥 Most Common Words:")
for word, count in common_words:
    print(f"{word} → {count} times")