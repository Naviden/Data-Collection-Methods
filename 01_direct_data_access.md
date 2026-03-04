# Direct Data Access

Direct data access refers to situations where data is already available
in a structured format and can be downloaded or queried without the need
for automated extraction techniques such as scraping or crawling. This
is usually the simplest and most reliable way to obtain data for
analysis.

Many organisations publish datasets specifically intended for research,
analysis, or public transparency. These datasets are often provided in
formats that can be easily processed by common data analysis tools such
as Python, R, Excel, or SQL databases.

Because the data is already structured, the main task is simply
retrieving it and loading it into an analysis environment.

## Common Formats

Datasets distributed through direct access are typically provided in
standard formats.

### CSV (Comma-Separated Values)

CSV files are one of the most common formats for tabular data. Each row
represents an observation, and each column represents a variable.

Example structure:

    city,population,year
    Milan,1370000,2023
    Rome,2870000,2023
    Turin,870000,2023

CSV files can be easily loaded using most data analysis tools.

Python example:

``` python
import pandas as pd

df = pd.read_csv("population.csv")
print(df.head())
```

### Excel Files

Many organisations distribute datasets in Excel format (`.xlsx`). These
files may contain multiple sheets and formatted tables.

Python example:

``` python
import pandas as pd

df = pd.read_excel("dataset.xlsx")
print(df.head())
```

### JSON

Some datasets are provided in JSON format, particularly when the data
originates from web services.

Example:

    {
      "city": "Milan",
      "population": 1370000
    }

Python example:

``` python
import pandas as pd

df = pd.read_json("data.json")
```

### Database Dumps

Sometimes data is distributed as a database export, such as:

-   SQL dumps
-   SQLite databases
-   compressed database files

These allow users to recreate the original database locally.

Example with SQLite:

``` python
import sqlite3
import pandas as pd

conn = sqlite3.connect("database.db")
df = pd.read_sql("SELECT * FROM cities", conn)
```

## Common Sources of Directly Accessible Data

A large amount of useful data is publicly available through open data
portals, research repositories, and specialised platforms.

### Open Government Data

Many governments publish datasets covering topics such as population,
transportation, health, and economics.

Examples:

-   https://data.gov\
-   https://data.europa.eu\
-   https://dati.gov.it
-   [https://dati.lombardia.it/](https://dati.lombardia.it/)
-   [https://www.istat.it/dati/open-data/](https://www.istat.it/dati/open-data/)

These portals often allow datasets to be downloaded directly in formats
such as CSV or Excel.

### Research Data Repositories

Academic institutions and research projects frequently share datasets to
promote reproducibility and collaboration.

These platforms host datasets associated with scientific publications
and research projects.

### Machine Learning and Data Science Platforms

Some platforms host datasets specifically designed for analysis, machine
learning experiments, or competitions.

Examples:

-   https://www.kaggle.com/datasets\
-   https://huggingface.co/datasets\
-   https://archive.ics.uci.edu

These datasets often come with documentation and example code.

### Institutional and Organisational Data

Many organisations publish datasets through their websites, including:

-   statistical agencies
-   financial institutions
-   international organisations

Examples:

-   https://data.worldbank.org\
-   https://www.oecd.org/statistics/\
-   https://ec.europa.eu/eurostat

These sources provide large collections of structured datasets covering
economic, demographic, and social indicators.

## Advantages of Direct Data Access

Direct data access has several advantages compared to other data
gathering methods:

-   the data is already structured
-   minimal preprocessing is required
-   data retrieval is straightforward
-   datasets are often well documented
-   collection methods are stable and reliable

Because of these advantages, direct access should usually be the first
option when searching for data.

## Limitations

Despite its simplicity, direct access has some limitations:

-   datasets may not contain the exact variables required
-   data may not be updated frequently
-   some datasets require registration or access permissions
-   large datasets may require significant storage or processing
    resources

When direct datasets are not available, other techniques such as APIs,
web scraping, or web crawling may be necessary.

## Example Workflow

A typical workflow using direct data access might look like this:

1.  Identify a dataset from an open data portal.
2.  Download the dataset in CSV or Excel format.
3.  Load the dataset into Python using pandas.
4.  Inspect and clean the data.
5.  Perform analysis or build models.

Example:

``` python
import pandas as pd

url = "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"

df = pd.read_csv(url)

print(df.head())
print(df.describe())
```

## Summary

Direct data access is the most straightforward way to obtain data. When
structured datasets are available through open portals or repositories,
they provide a reliable starting point for data analysis projects.

For this reason, analysts typically begin by searching for existing
datasets before considering more complex techniques such as APIs,
scraping, or crawling.
