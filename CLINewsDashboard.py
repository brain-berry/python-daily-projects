import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

BASE_URL = "https://www.bbc.com/news"

def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print("❌ Error fetching page:", e)
        return None

def parse_headlines(html):
    soup = BeautifulSoup(html, "html.parser")
    headlines = []

    for h in soup.find_all("h3"):
        text = h.get_text(strip=True)
        if text and text not in headlines:
            headlines.append(text)

    return headlines

def display_headlines(headlines):
    print("\n📰 Latest Headlines:\n")
    for i, headline in enumerate(headlines[:10], start=1):
        print(f"{i}. {headline}")

def search_headlines(headlines, keyword):
    results = [h for h in headlines if keyword.lower() in h.lower()]
    return results

def save_txt(headlines):
    filename = "headlines.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for i, headline in enumerate(headlines, start=1):
            f.write(f"{i}. {headline}\n")
    print(f"✅ Saved to {filename}")

def save_csv(headlines):
    filename = "headlines.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Index", "Headline", "Timestamp"])
        for i, headline in enumerate(headlines, start=1):
            writer.writerow([i, headline, datetime.now()])
    print(f"✅ Saved to {filename}")

def choose_category():
    print("\nChoose Category:")
    print("1. General News")
    print("2. Technology")
    print("3. Business")

    choice = input("Enter choice: ")

    if choice == "1":
        return BASE_URL
    elif choice == "2":
        return BASE_URL + "/technology"
    elif choice == "3":
        return BASE_URL + "/business"
    else:
        print("Invalid choice. Defaulting to General.")
        return BASE_URL

def main():
    print("🧠 MINI NEWS DASHBOARD 🧠")

    url = choose_category()
    html = fetch_page(url)

    if not html:
        return

    headlines = parse_headlines(html)

    while True:
        print("\n--- MENU ---")
        print("1. View Headlines")
        print("2. Search Headlines")
        print("3. Save as TXT")
        print("4. Save as CSV")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            display_headlines(headlines)

        elif choice == "2":
            keyword = input("Enter keyword: ")
            results = search_headlines(headlines, keyword)

            if results:
                print("\n🔍 Results:\n")
                for i, r in enumerate(results, 1):
                    print(f"{i}. {r}")
            else:
                print("No matches found.")

        elif choice == "3":
            save_txt(headlines)

        elif choice == "4":
            save_csv(headlines)

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
