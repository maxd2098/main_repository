from bs4 import BeautifulSoup

with open('table.html', 'r') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
tr = soup.find_all('tr')
summ = []
for td in tr:
    td = td.find_all('td')
    for num in td:
        summ.append(int(num.text.strip()))
        #print(num.text.strip(), end=' ')

print(sum(summ))