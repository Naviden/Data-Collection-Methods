import requests
import json
import csv
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/"
data_directory = "../data/"
def scrape_hn():
    headers = {"User-Agent": "Mozilla/5.0"} #makes the request look like it comes from a normal web browser, reducing the chance of being blocked or served different content.
    response = requests.get(URL, headers=headers)
    response.raise_for_status() #It raises an exception if the HTTP request failed.

    soup = BeautifulSoup(response.text, "html.parser")
    stories = []

    # tr → table row element
	# .athing → CSS class used by Hacker News for each post row
    rows = soup.select("tr.athing")
    for row in rows:
        title_tag = row.select_one("span.titleline > a")
        if not title_tag:
            continue

        title = title_tag.text.strip()
        link = title_tag["href"]

        # Score and metadata are in the NEXT sibling row
        subrow = row.find_next_sibling("tr")
        score_tag = subrow.select_one("span.score") if subrow else None
        score = score_tag.text if score_tag else "N/A"

        stories.append({"rank": len(stories) + 1, "title": title, "score": score, "link": link})

    return stories

def save_json(stories, filename="hn_stories.json"):
    filename = data_directory + filename
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(stories, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(stories)} stories to {filename}")

def save_csv(stories, filename="hn_stories.csv"):
    filename = data_directory + filename
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["rank", "title", "score", "link"])
        writer.writeheader()
        writer.writerows(stories)
    print(f"Saved {len(stories)} stories to {filename}")

if __name__ == "__main__":
    stories = scrape_hn()
    for s in stories:
        print(f"{s['rank']:>2}. [{s['score']}] {s['title']}")
        print(f"    {s['link']}\n")
    save_json(stories)
    save_csv(stories)