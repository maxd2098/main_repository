from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Jupiter'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find_all('table', class_='wikitable')
jup = open('jup.csv', 'w', encoding="utf-8")
for tab in table:
    if tab.find('a', href="/wiki/Moon"):
        table = tab

arr_str = []
tr_all = table.find_all('tr')
for tr in tr_all:
    tr = tr.find_all(['th', 'td'])
    for tdh in tr:
        print(tdh.text.strip(' ').strip('\n'), end=';', file = jup)
        
    print('\n', file = jup)
        
        
jup.close()

#, file = jup