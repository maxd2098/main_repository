from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Vladivostok'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', class_='wikitable mw-collapsible')
vlad = open('vlad.csv', 'w', encoding="utf-8")
for tr in table.find_all('tr'):
    for tdh in tr.find_all(['td', 'th']):
        
        print((tdh.text.strip(' ').strip('\n')).strip('\n'), end = ';', file=vlad)
    print('\n', file=vlad)
#print(table)
vlad.close()