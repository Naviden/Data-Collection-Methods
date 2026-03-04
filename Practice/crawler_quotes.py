import requests
import json
import csv
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://quotes.toscrape.com"
data_directory = "../data/"
def crawl_quotes():
    all_quotes = []
    url = BASE_URL
    page = 1
    visited = set()

    while url and url not in visited:
        print(f"Crawling page {page}: {url}")
        visited.add(url)

        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            break

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract quotes from this page
        for quote_div in soup.select("div.quote"):
            text = quote_div.select_one("span.text").get_text(strip=True)
            author = quote_div.select_one("small.author").get_text(strip=True)
            tags = [t.get_text(strip=True) for t in quote_div.select("a.tag")]

            all_quotes.append({
                "page": page,
                "text": text,
                "author": author,
                "tags": ", ".join(tags),
            })

        # Follow "Next" button
        next_btn = soup.select_one("li.next > a")
        if next_btn:
            url = urljoin(BASE_URL, next_btn["href"])
            page += 1
            time.sleep(0.5)  # polite delay
        else:
            url = None  # no more pages

    print(f"\nDone. Crawled {page} pages, collected {len(all_quotes)} quotes.")
    return all_quotes


def save_json(data, filename="quotes.json"):
    filename = data_directory + filename
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved to {filename}")


def save_csv(data, filename="quotes.csv"):
    filename = data_directory + filename
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["page", "text", "author", "tags"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved to {filename}")


if __name__ == "__main__":
    quotes = crawl_quotes()
    save_json(quotes)
    save_csv(quotes)
