import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

BASE_URL = "https://www.bbc.com/news"

def fetch_page(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        console.print(f"[red]Error:[/red] {e}")
        return None

def parse_headlines(html):
    soup = BeautifulSoup(html, "html.parser")
    headlines = []

    for h in soup.find_all("h3"):
        text = h.get_text(strip=True)
        if text and text not in headlines:
            headlines.append(text)

    return headlines

def show_headlines(headlines):
    table = Table(title="📰 Latest Headlines")

    table.add_column("No.", style="cyan")
    table.add_column("Headline", style="white")

    for i, headline in enumerate(headlines[:10], start=1):
        table.add_row(str(i), headline)

    console.print(table)

def search_headlines(headlines):
    keyword = Prompt.ask("Enter keyword")
    results = [h for h in headlines if keyword.lower() in h.lower()]

    if results:
        show_headlines(results)
    else:
        console.print("[yellow]No matches found.[/yellow]")

def save_csv(headlines):
    with open("headlines.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Headline", "Timestamp"])
        for h in headlines:
            writer.writerow([h, datetime.now()])
    console.print("[green]Saved to headlines.csv[/green]")

def choose_category():
    console.print(Panel("1. General\n2. Technology\n3. Business", title="Select Category"))

    choice = Prompt.ask("Enter choice")

    if choice == "1":
        return BASE_URL
    elif choice == "2":
        return BASE_URL + "/technology"
    elif choice == "3":
        return BASE_URL + "/business"
    else:
        console.print("[yellow]Defaulting to General[/yellow]")
        return BASE_URL

def main():
    console.print(Panel("🧠 MINI NEWS DASHBOARD", style="bold magenta"))

    url = choose_category()
    html = fetch_page(url)

    if not html:
        return

    headlines = parse_headlines(html)

    while True:
        console.print(Panel(
            "1. View Headlines\n"
            "2. Search\n"
            "3. Save CSV\n"
            "4. Exit",
            title="Menu",
            style="cyan"
        ))

        choice = Prompt.ask("Choose option")

        if choice == "1":
            show_headlines(headlines)
        elif choice == "2":
            search_headlines(headlines)
        elif choice == "3":
            save_csv(headlines)
        elif choice == "4":
            console.print("[bold red]Goodbye![/bold red]")
            break
        else:
            console.print("[red]Invalid choice[/red]")

if __name__ == "__main__":
    main()
