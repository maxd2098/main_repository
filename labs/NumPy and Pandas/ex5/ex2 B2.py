import requests
from bs4 import BeautifulSoup

url='https://en.wikipedia.org/wiki/Web_scraping'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

arr_link = []
for link in soup.find_all('a'):
    string = str(link.get('href'))
    if string.startswith('http'):
        arr_link.append(string)
print(*arr_link, sep='\n')
print(len(arr_link))

