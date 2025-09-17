import requests
import pandas as pd 
from bs4 import BeautifulSoup

page = 1
data = []

while True:
    url=  f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    if response.status_code != 200:
        break
    
    soup = BeautifulSoup(response.text,"html.parser")
    quotes = soup.find_all("div", class_='quote')

    if not quotes:
        break
    for q in quotes:
        text = q.find('span',class_='text').text
        author = q.find('small',class_='author').text
        tags = [tag.text for tag in q.find_all('a', class_='tag')]
        data.append({"Quotes": text,"Author" : author, "tags": tags})

    page += 1
    
df = pd.DataFrame(data)
df.to_csv("quotes.csv", index=False)

    
print(f"Scraped: {len(data)} Quotes")
print("CSV file saved as 'quotes.csv'")