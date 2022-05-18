from bs4 import BeautifulSoup

with open('table.html', 'r') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

summ = []
for tr in soup.find_all('tr'):
    for td in tr.find_all('td'):
        summ.append(int(td.text.strip(' ')))
print(sum(summ))
#print(tr, sep='\n\n')