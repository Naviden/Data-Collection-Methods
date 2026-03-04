# Accessing Data Through APIs

An API (Application Programming Interface) allows software applications
to communicate with each other. In the context of data gathering, APIs
provide a structured and programmatic way to retrieve data from remote
systems.

Many organisations expose their data through APIs instead of
downloadable datasets. This approach allows users to retrieve data
dynamically and ensures that the information is always up to date.

## How APIs Work

Most modern APIs follow the REST architecture.

Typical interaction:

1.  A client sends a request to an endpoint (URL).
2.  The server processes the request.
3.  The server returns data, usually in JSON format.

Example JSON:

    {
      "city": "Milan",
      "temperature": 18,
      "humidity": 65
    }

## HTTP Methods

Common request types:

-   GET -- retrieve data
-   POST -- create data
-   PUT -- update data
-   DELETE -- remove data

For data collection, **GET** is the most common.

Example request:

    https://api.example.com/weather?city=Milan

## Using APIs in Python

Example using the `requests` library:

``` python
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=45.46&longitude=9.19&current_weather=true"

response = requests.get(url)

data = response.json()

print(data)
```

## Converting API Data to a DataFrame

``` python
import pandas as pd

weather = data["current_weather"]

df = pd.DataFrame([weather])

print(df)
```

## Authentication

Some APIs require authentication.

Common methods:

-   API keys
-   OAuth tokens

Example:

    https://api.example.com/data?apikey=YOUR_KEY

## Rate Limits

APIs often restrict how many requests can be made within a period
(e.g. 100 requests per minute).

Always respect these limits.

## Example Public APIs

Weather: https://open-meteo.com\
NASA: https://api.nasa.gov\
Public API directory: https://publicapis.dev

## Summary

APIs provide a reliable and structured way to retrieve data
programmatically. When available, they are usually the preferred method
for automated data collection.
