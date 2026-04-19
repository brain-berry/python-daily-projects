import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error fetching page:", e)
        return None

def parse_headlines(html):
    soup = BeautifulSoup(html, "html.parser")

    headlines = []
    
    # BBC headlines (can change if site structure changes)
    for h in soup.find_all("h3"):
        text = h.get_text(strip=True)
        if text and text not in headlines:
            headlines.append(text)

    return headlines

def save_to_file(headlines, filename="headlines.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for i, headline in enumerate(headlines, start=1):
            f.write(f"{i}. {headline}\n")

def main():
    print("🌐 Fetching headlines...\n")

    html = fetch_page(URL)
    if not html:
        return

    headlines = parse_headlines(html)

    if not headlines:
        print("No headlines found.")
        return

    for i, headline in enumerate(headlines[:10], start=1):
        print(f"{i}. {headline}")

    save_to_file(headlines)

    print("\n✅ Headlines saved to 'headlines.txt'")

if __name__ == "__main__":
    main()
