#imports
import requests
from bs4 import BeautifulSoup

# get the user supplied query
query = input("Enter a search query: ")

# get the search results page
url = 'https://www.google.com/search?q=' + query
response = requests.get(url)
# parse the response with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
# get all search results
results = soup.find_all('div', {'class': 'g'})

# print the top 10 results
print("Top 10 results for " + query + ":")
for result in results[:10]:
    # get the title of the search result
    title = result.find('h3')
    if title:
        print(title.text)
