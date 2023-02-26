#import libraries
import requests
from bs4 import BeautifulSoup

query = input("Please enter your query: ")
url = "https://www.google.com/search?q="+query

#search results
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    #scrape top 10 results
    results = soup.find_all('div', attrs={'class': 'r'})
    for result in results[:10]:
        link = result.find('a')
        print(link.get('href'))
