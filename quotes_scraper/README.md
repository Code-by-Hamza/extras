# Quotes Scraper

This is a simple Python script that scrapes quotes from [quotes.toscrape.com](https://quotes.toscrape.com/) and saves them into a CSV file.

## Features
- Scrapes all quotes, authors, and tags from the website
- Saves the data to `quotes.csv`
- Prints the total number of quotes scraped

## Requirements
- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [pandas](https://pypi.org/project/pandas/)

Install dependencies with:
```
pip install requests beautifulsoup4 pandas
```

## Usage
Run the script:
```
python scraper.py
```

After running, you will find a `quotes.csv` file with all the scraped quotes.
