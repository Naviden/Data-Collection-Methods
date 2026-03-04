# Web Scraping

Web scraping is the automated extraction of information from web pages.
Many websites contain useful data but do not provide APIs or
downloadable datasets.

Scraping allows analysts to retrieve information directly from the HTML
of a webpage.

## Structure of Web Pages

Web pages are written in **HTML**.

Example:

    <html>
      <body>
        <h1>News Title</h1>
        <p>This is the article text.</p>
      </body>
    </html>

The hierarchical structure of a webpage is called the **DOM (Document
Object Model)**.

Scraping tools analyse this structure to locate elements.

## Basic Scraping Workflow

1.  Download the webpage
2.  Parse the HTML
3.  Identify relevant elements
4.  Extract the data
5.  Store the results

## Example in Python

Using `requests` and `BeautifulSoup`:

``` python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("h1")

for t in titles:
    print(t.text)
```

## Extracting Links

``` python
links = soup.find_all("a")

for link in links:
    print(link.get("href"))
```

## Common Applications

Web scraping is used for:

-   collecting product information
-   gathering news articles
-   extracting job listings
-   monitoring prices
-   collecting datasets from websites

## Challenges

Common difficulties include:

-   changing webpage structures
-   JavaScript-generated content
-   anti-scraping protections

Scripts may need regular updates.

## Legal and Ethical Considerations

Responsible scraping includes:

-   respecting terms of service
-   following robots.txt
-   limiting request frequency

Example robots file:

    https://example.com/robots.txt

## Summary

Web scraping allows analysts to collect information directly from web
pages when APIs or datasets are not available.
