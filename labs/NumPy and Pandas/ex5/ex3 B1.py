import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Moscow'
response = requests.get(url)
soup_m = BeautifulSoup(response.text, 'html.parser')

url = 'https://en.wikipedia.org/wiki/Beijing'
response = requests.get(url)
soup_b = BeautifulSoup(response.text, 'html.parser')

arr_m = set()
arr_b = set()
for link in soup_m.find_all('a'):
    string = str(link.get('href'))
    if not string.startswith('http') and not string.startswith('#') and string.find(':')==-1 and string!='None':
        arr_m.add(string)
for link in soup_b.find_all('a'):
    string = str(link.get('href'))
    if not string.startswith('http') and not string.startswith('#') and string.find(':')==-1 and string!='None':
        arr_b.add(string)
arr_m = list(arr_m)
arr_b = list(arr_b)
arr = arr_m+arr_b
arr.sort()
print(*arr, sep='\n')
print(len(arr))