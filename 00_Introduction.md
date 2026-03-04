# Introduction to Data Gathering Techniques

Data gathering is the first step of any data analysis, machine learning, or artificial intelligence workflow. Before analysing data, building models, or producing visualisations, we must first obtain the data itself. In practice, data scientists rarely start with perfectly prepared datasets. Instead, they often need to identify relevant sources, retrieve data from different systems, and transform it into a usable format.

Modern data ecosystems provide multiple ways to access information. Some data sources offer structured datasets that can be downloaded directly, while others require programmatic access through interfaces or automated extraction from web pages. Understanding the different modes of data collection helps analysts choose the most appropriate technique depending on the data source, scale, and level of automation required.

This module introduces the main approaches used to collect data in real-world projects. The goal is to provide a conceptual understanding of the most common data acquisition methods and illustrate how they can be used in practice.

The techniques covered include:

- Direct access to structured datasets
- Accessing data through APIs
- Web scraping
- Web crawling

Each method represents a different level of automation and complexity. In many practical projects, several of these techniques are combined within the same data pipeline.

## Direct Data Access

In many cases, data is already available in a structured format. Governments, research institutions, and organisations often publish datasets that can be downloaded directly as files such as CSV, Excel, or database exports.

This approach is usually the simplest and most reliable way to obtain data. Since the data is already structured, it can be loaded directly into analytical tools such as Python, R, or database systems.

Typical examples include:

- Open government data portals
- Institutional datasets
- Research data repositories
- Public datasets distributed through platforms such as Kaggle

Direct data access is often the starting point for many data science projects because it requires minimal processing before analysis.

## APIs (Application Programming Interfaces)

When data needs to be accessed dynamically or updated frequently, organisations often provide APIs. An API is a programmatic interface that allows software applications to request data from a server.

Most modern APIs follow a REST architecture, where clients send requests to specific endpoints and receive structured responses, typically in JSON format.

APIs are widely used to provide controlled and structured access to data sources such as:

- Weather services
- Social media platforms
- Financial data providers
- Public transportation systems
- Government data services

Compared to manual downloads, APIs allow automated data retrieval and integration into software applications or analytical pipelines.

## Web Scraping

Not all information on the web is provided through APIs or downloadable datasets. Many websites display valuable data directly within web pages, designed primarily for human users rather than automated systems.

Web scraping refers to the process of automatically extracting information from web pages by analysing their underlying HTML structure. A typical scraping workflow involves downloading the webpage, parsing the HTML content, and extracting the relevant elements such as text, tables, or links.

Common use cases for web scraping include:

- Collecting product information from e-commerce websites
- Extracting news articles or headlines
- Gathering job postings
- Monitoring prices or availability of products

While scraping can be a powerful technique, it also introduces challenges. Website structures may change frequently, and many websites implement mechanisms to prevent automated data collection.

## Web Crawling

Web crawling is closely related to scraping but focuses on discovering and navigating large numbers of pages automatically. Instead of extracting data from a single page, a crawler systematically explores links between pages to collect information from entire websites.

A typical crawler starts from one or more initial pages (called seed URLs), identifies links within those pages, and follows them to discover additional content. This process allows the crawler to map and retrieve large portions of a website.

Web crawling is commonly used in scenarios such as:

- Search engine indexing
- Large-scale website analysis
- Building datasets from many interconnected pages

In practice, crawling is often combined with scraping: the crawler discovers pages, and the scraper extracts the relevant data from each page.

## Choosing the Appropriate Data Gathering Method

Different data sources require different acquisition strategies. In general:

- Direct downloads are the simplest when structured datasets are available.
- APIs provide reliable and scalable programmatic access.
- Web scraping is useful when data is embedded in web pages without an API.
- Web crawling is necessary when data is distributed across many interconnected pages.

Understanding these approaches allows analysts to design effective data collection pipelines tailored to the structure and accessibility of the data source.

## Responsible Data Collection

When gathering data, it is important to follow responsible practices. This includes respecting website terms of service, following rate limits, and considering privacy and legal constraints.

Responsible data collection ensures that automated systems do not overload servers, violate usage policies, or compromise sensitive information.

In the following sections, each data gathering technique will be explored in more detail, including practical examples and simple coding demonstrations.