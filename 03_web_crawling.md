# Web Crawling

Web crawling is the automated exploration of webpages by following links
between them.

Unlike scraping, which extracts data from specific pages, crawling
focuses on discovering large numbers of pages.

In practice, crawlers often collect pages and then scraping extracts
information from them.

## Basic Crawling Process

1.  Start with seed URLs
2.  Download the page
3.  Extract links
4.  Add links to a queue
5.  Visit new pages

Example structure:

    Seed page
       ↓
    Extract links
       ↓
    Visit new pages
       ↓
    Repeat

## The Web as a Graph

The web can be represented as a graph:

-   pages = nodes
-   links = edges

Crawlers navigate this graph automatically.

## Crawl Depth

Crawlers often limit how deep they explore.

Example:

Depth 0 → starting page\
Depth 1 → pages linked from start\
Depth 2 → links from those pages

This prevents infinite crawling.

## Simple Python Example

``` python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

links = [link.get("href") for link in soup.find_all("a")]

print(links)
```

A crawler would repeat this process for each discovered link.

## Crawling Frameworks

Large crawlers use specialised tools.

Examples:

Scrapy -- https://scrapy.org\
Apache Nutch -- https://nutch.apache.org

These frameworks manage:

-   request scheduling
-   link queues
-   duplicate detection
-   data storage

## Real Applications

Web crawling is used for:

-   search engines
-   building research datasets
-   monitoring large websites
-   market intelligence

## Responsible Crawling

Responsible crawlers:

-   respect robots.txt
-   limit request frequency
-   avoid revisiting pages unnecessarily

## Summary

Web crawling allows automated exploration of large websites and is often
combined with scraping to collect large datasets.
