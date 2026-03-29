import os

print("🔍 FILE SEARCH TOOL")
print("-" * 30)

folder = input("Enter folder path to search: ")
keyword = input("Enter file name keyword: ").lower()

matches = []

print("\nSearching...\n")

for root, dirs, files in os.walk(folder):
    for file in files:
        if keyword in file.lower():
            full_path = os.path.join(root, file)
            matches.append(full_path)

if matches:
    print(f"Found {len(matches)} file(s):\n")
    for match in matches:
        print("📄", match)
else:
    print(" No matching files found.")