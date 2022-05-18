import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/New_York_City'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table_s = soup.find('table', class_='wikitable sortable')
table_all = table_s.find_all('tr')
new_yourk = open('new_yourk.csv', 'w')
for trt in table_all:
    if trt.find_all('th'):
        #print('::::::::::::::::::::::::::::::::')
        trt = trt.find_all('th')
        for th in trt:
            if th==trt[-1]:
                print(th.text.strip(), file=new_yourk)
            else:
                print(th.text.strip(), end=';', file=new_yourk)
    else:
        #print('********************************')
        trt = trt.find_all('td')
        for td in trt:
            if td==trt[-1]:
                print(td.text.strip(), file=new_yourk)
            else:
                print(td.text.strip(), end=';', file=new_yourk)
    #print('\n', file=new_yourk)
    
#, file=new_yourk
new_yourk.close()
    
















